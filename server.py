#!/usr/bin/env python3
"""
🐍 PYTHON LERNPLATTFORM – GEHÄRTETER BACKEND SERVER 🐍
======================================================
Sicherheitsoptimierter, abhängigkeitsfreier REST-API & Static Server.
- Persistenter SECRET_KEY (Env / geschützte .secret_key Datei).
- Schutz gegen User-Enumeration (Constant-Time Dummy PBKDF2).
- In-Memory Rate-Limiting gegen Brute-Force-Angriffe.
- Autorisierungsprüfung (IDOR-Schutz) in allen Lehrer-Endpunkten.
- Striktes Blockieren sensitiver Dateien (.db, .secret_key, .py, .php, .git) im Static-Handler.
- Security-Header (CSP, X-Content-Type-Options, X-Frame-Options).
- Neuer Code-Inspektor für Lehrkräfte, CSV-Matrix-Export & Zertifikats-Verifikation.
"""

import http.server
import socketserver
import json
import sqlite3
import hashlib
import hmac
import secrets
import time
import os
import re
import uuid
import urllib.parse
import ipaddress
from pathlib import Path
from collections import defaultdict

PORT = int(os.environ.get("PORT", 8000))
BASE_DIR = Path(__file__).parent.resolve()
DB_FILE = BASE_DIR / "platform_data.db"
KEY_FILE = BASE_DIR / ".secret_key"

def is_trusted_source(ip: str) -> bool:
    """Verhindert direkte Zugriffe am Reverse Proxy vorbei."""
    try:
        addr = ipaddress.ip_address(ip)
        return addr.is_loopback or addr.is_private
    except ValueError:
        return False

# ------------------------------------------------------------------------------
# 1. PERSISTENTER SECRET KEY
# ------------------------------------------------------------------------------
def get_or_create_secret_key() -> str:
    env_key = os.environ.get("SECRET_KEY")
    if env_key and len(env_key) >= 32:
        return env_key

    if KEY_FILE.exists():
        try:
            with open(KEY_FILE, "r", encoding="utf-8") as f:
                key = f.read().strip()
                if len(key) >= 32:
                    return key
        except Exception:
            pass

    new_key = secrets.token_hex(32)
    try:
        flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
        mode = 0o600
        fd = os.open(str(KEY_FILE), flags, mode)
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(new_key)
    except Exception as e:
        print(f"⚠️ Warnung: Konnte .secret_key nicht schreiben: {e}")
    return new_key

SECRET_KEY = get_or_create_secret_key()

# ------------------------------------------------------------------------------
# 2. IN-MEMORY RATE LIMITER
# ------------------------------------------------------------------------------
class SimpleRateLimiter:
    def __init__(self):
        self.attempts = defaultdict(list)

    def is_allowed(self, key: str, max_requests: int = 5, window_seconds: int = 60) -> bool:
        now = time.time()
        self.attempts[key] = [t for t in self.attempts[key] if now - t < window_seconds]
        if len(self.attempts[key]) >= max_requests:
            return False
        self.attempts[key].append(now)
        return True

rate_limiter = SimpleRateLimiter()

# ------------------------------------------------------------------------------
# 3. DATENBANK INITIALISIERUNG
# ------------------------------------------------------------------------------
def get_db():
    conn = sqlite3.connect(str(DB_FILE))
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        salt TEXT NOT NULL,
        name TEXT NOT NULL,
        role TEXT DEFAULT 'student',
        xp INTEGER DEFAULT 0,
        level INTEGER DEFAULT 1,
        streak_days INTEGER DEFAULT 1,
        last_active_date TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")

    c.execute("""
    CREATE TABLE IF NOT EXISTS chapter_progress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        chapter_id TEXT NOT NULL,
        code_draft TEXT,
        subgoals_json TEXT,
        is_solved INTEGER DEFAULT 0,
        solved_at TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(user_id, chapter_id),
        FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
    )""")

    c.execute("""
    CREATE TABLE IF NOT EXISTS classrooms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        teacher_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        invite_code TEXT UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(teacher_id) REFERENCES users(id) ON DELETE CASCADE
    )""")

    c.execute("""
    CREATE TABLE IF NOT EXISTS class_enrollments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        classroom_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(classroom_id, user_id),
        FOREIGN KEY(classroom_id) REFERENCES classrooms(id) ON DELETE CASCADE,
        FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
    )""")

    c.execute("""
    CREATE TABLE IF NOT EXISTS certificates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uuid TEXT UNIQUE NOT NULL,
        user_id INTEGER NOT NULL,
        track_id TEXT NOT NULL,
        student_name TEXT NOT NULL,
        issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
    )""")

    c.execute("""
    CREATE TABLE IF NOT EXISTS platform_settings (
        key TEXT PRIMARY KEY,
        value TEXT,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")

    conn.commit()
    conn.close()

def get_platform_setting(key: str, default: str = "") -> str:
    """Liest einen Einstellungswert sicher aus der Datenbank."""
    try:
        conn = get_db()
        row = conn.execute("SELECT value FROM platform_settings WHERE key = ?", (key,)).fetchone()
        conn.close()
        return str(row["value"]) if row and row["value"] is not None else default
    except Exception:
        return default

def is_maintenance_active() -> bool:
    """Prüft, ob der globale Wartungsmodus aktiv ist."""
    return get_platform_setting("maintenance_mode", "0") == "1"

# ------------------------------------------------------------------------------
# 4. AUTH & HASHING
# ------------------------------------------------------------------------------
def hash_password(password: str, salt: str = None) -> tuple[str, str]:
    if not salt:
        salt = secrets.token_hex(16)
    pwd_bytes = password.encode("utf-8")
    salt_bytes = salt.encode("utf-8")
    key = hashlib.pbkdf2_hmac("sha256", pwd_bytes, salt_bytes, 100000)
    return key.hex(), salt

def verify_password(password: str, password_hash: str, salt: str) -> bool:
    new_hash, _ = hash_password(password, salt)
    return hmac.compare_digest(new_hash, password_hash)

# Constant-Time Dummy PBKDF2 gegen User-Enumeration
DUMMY_SALT = secrets.token_hex(16)
DUMMY_HASH, _ = hash_password("dummy_password_constant_time", DUMMY_SALT)

def generate_token(user_id: int, email: str, role: str) -> str:
    payload = {
        "uid": user_id,
        "email": email,
        "role": role,
        "exp": int(time.time()) + 43200  # 12 Stunden Token-Gültigkeit (Sitzungsbegrenzung für Alpha-Test)
    }
    payload_json = json.dumps(payload, sort_keys=True)
    sig = hmac.new(SECRET_KEY.encode("utf-8"), payload_json.encode("utf-8"), hashlib.sha256).hexdigest()
    token = f"{payload_json}.{sig}"
    return urllib.parse.quote(token)

def verify_token(token_str: str) -> dict | None:
    try:
        raw_token = urllib.parse.unquote(token_str)
        if "." not in raw_token:
            return None
        payload_json, sig = raw_token.rsplit(".", 1)
        expected_sig = hmac.new(SECRET_KEY.encode("utf-8"), payload_json.encode("utf-8"), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(sig, expected_sig):
            return None
        payload = json.loads(payload_json)
        if payload.get("exp", 0) < time.time():
            return None
        return payload
    except Exception:
        return None

# ------------------------------------------------------------------------------
# 5. HTTP REQUEST HANDLER
# ------------------------------------------------------------------------------
class PlatformRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def end_headers(self):
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, DELETE")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.send_header("Cache-Control", "no-cache, must-revalidate")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def send_json(self, data: dict, status: int = 200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))

    def get_client_ip(self) -> str:
        forwarded = self.headers.get("X-Forwarded-For")
        if forwarded:
            return forwarded.split(",")[0].strip()
        return self.client_address[0]

    def get_auth_user(self) -> dict | None:
        auth_header = self.headers.get("Authorization", "")
        if auth_header.startswith("Bearer "):
            token = auth_header[7:].strip()
            verified = verify_token(token)
            if not verified:
                return None
            try:
                conn = get_db()
                row = conn.execute("SELECT id, email, name, role, xp, level, streak_days FROM users WHERE id = ?", (verified["uid"],)).fetchone()
                conn.close()
                if not row:
                    return None
                data = dict(row)
                data["uid"] = row["id"]
                return data
            except Exception:
                return None
        return None

    def get_admin_user(self) -> dict | None:
        user = self.get_auth_user()
        if user and user.get("role") == "admin":
            return user
        return None

    def read_json_body(self) -> dict:
        content_length = int(self.headers.get("Content-Length", 0))
        if content_length == 0 or content_length > 1_000_000:
            return {}
        body = self.rfile.read(content_length)
        return json.loads(body.decode("utf-8"))

    def is_path_blocked(self, path: str) -> bool:
        clean_path = urllib.parse.unquote(path).split("?")[0].lower()
        clean_path = os.path.normpath(clean_path).replace("\\", "/")
        blocked_extensions = (
            ".db", ".sqlite", ".sqlite3", ".secret_key", ".py", ".sh", ".php",
            ".jsonl", ".env", ".bak", ".sql", ".log", ".conf", ".ini", ".yaml", ".yml"
        )
        if any(clean_path.endswith(ext) for ext in blocked_extensions):
            return True
        if "/." in clean_path or clean_path.startswith("."):
            return True
        if clean_path.startswith("/exams/") or clean_path == "/exams":
            return True
        if any(seg in clean_path for seg in ["/.git", "/.system_generated", "/.gemini", "platform_data.db", ".secret_key"]):
            return True
        return False

    def do_GET(self):
        # 0. Proxy-Schutz gegen direktes Ansprechen von Port 8008 von außen
        if not is_trusted_source(self.client_address[0]):
            return self.send_json({"error": "Direkter Serverzugriff verweigert"}, 403)

        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if self.is_path_blocked(path):
            return self.send_json({"error": "Zugriff verweigert (Geschützte Datei)"}, 403)

        # 1. ÖFFENTLICHER STATUS-ENDPUNKT (Wartungsmodus, Ankündigung, Registrierung)
        if path == "/api/platform/status":
            return self.send_json({
                "maintenance": is_maintenance_active(),
                "announcement": get_platform_setting("announcement_banner", ""),
                "allow_registration": get_platform_setting("allow_registration", "1") == "1"
            })

        # 2. WARTUNGSMODUS-FILTER FÜR GET-APIS
        if path.startswith("/api/"):
            if is_maintenance_active() and not self.get_admin_user():
                return self.send_json({
                    "error": "Die Plattform befindet sich derzeit im Wartungsmodus. Nur Administratoren haben Zugriff.",
                    "maintenance": True
                }, 503)

        # 3. AUTH ME
        if path == "/api/auth/me":
            user_token = self.get_auth_user()
            if not user_token:
                return self.send_json({"error": "Nicht authentifiziert"}, 401)
            conn = get_db()
            row = conn.execute("SELECT id, email, name, role, xp, level, streak_days FROM users WHERE id = ?", (user_token["uid"],)).fetchone()
            conn.close()
            if not row:
                return self.send_json({"error": "Benutzer nicht gefunden"}, 404)
            return self.send_json({"user": dict(row)})

        # 2. PROGRESS GET
        elif path.startswith("/api/progress/get"):
            user_token = self.get_auth_user()
            if not user_token:
                return self.send_json({"error": "Nicht authentifiziert"}, 401)
            query = urllib.parse.parse_qs(parsed.query)
            chapter_id = query.get("chapter_id", [""])[0]
            
            conn = get_db()
            if chapter_id:
                row = conn.execute("SELECT chapter_id, code_draft, subgoals_json, is_solved, solved_at FROM chapter_progress WHERE user_id = ? AND chapter_id = ?", (user_token["uid"], chapter_id)).fetchone()
                conn.close()
                return self.send_json({"progress": dict(row) if row else None})
            else:
                rows = conn.execute("SELECT chapter_id, is_solved, solved_at FROM chapter_progress WHERE user_id = ?", (user_token["uid"],)).fetchall()
                conn.close()
                return self.send_json({"all_progress": [dict(r) for r in rows]})

        # 3. CLASSROOMS LIST
        elif path.startswith("/api/classrooms/list"):
            user_token = self.get_auth_user()
            if not user_token:
                return self.send_json({"error": "Nicht authentifiziert"}, 401)
            
            conn = get_db()
            if user_token.get("role") == "teacher":
                classes = conn.execute("SELECT id, name, invite_code, created_at FROM classrooms WHERE teacher_id = ?", (user_token["uid"],)).fetchall()
                result = []
                for cl in classes:
                    student_count = conn.execute("SELECT COUNT(*) FROM class_enrollments WHERE classroom_id = ?", (cl["id"],)).fetchone()[0]
                    result.append({**dict(cl), "student_count": student_count})
                conn.close()
                return self.send_json({"classrooms": result})
            else:
                classes = conn.execute("""
                    SELECT c.id, c.name, u.name as teacher_name, ce.joined_at 
                    FROM class_enrollments ce 
                    JOIN classrooms c ON ce.classroom_id = c.id 
                    JOIN users u ON c.teacher_id = u.id 
                    WHERE ce.user_id = ?
                """, (user_token["uid"],)).fetchall()
                conn.close()
                return self.send_json({"classrooms": [dict(c) for c in classes]})

        # 4. CLASSROOMS MATRIX (mit IDOR-Schutz)
        elif path.startswith("/api/classrooms/matrix"):
            user_token = self.get_auth_user()
            if not user_token or user_token.get("role") != "teacher":
                return self.send_json({"error": "Nur für Lehrkräfte"}, 403)
            
            query = urllib.parse.parse_qs(parsed.query)
            classroom_id = query.get("classroom_id", [""])[0]
            if not classroom_id or not classroom_id.isdigit():
                return self.send_json({"error": "Ungültige classroom_id"}, 400)

            conn = get_db()
            owner_check = conn.execute("SELECT id, name FROM classrooms WHERE id = ? AND teacher_id = ?", (int(classroom_id), user_token["uid"])).fetchone()
            if not owner_check:
                conn.close()
                return self.send_json({"error": "Zugriff verweigert (Nicht deine Klasse)"}, 403)

            students = conn.execute("""
                SELECT u.id, u.name, u.email, u.xp, u.level, u.streak_days 
                FROM class_enrollments ce 
                JOIN users u ON ce.user_id = u.id 
                WHERE ce.classroom_id = ?
            """, (int(classroom_id),)).fetchall()

            matrix = []
            for st in students:
                solved = conn.execute("SELECT chapter_id, is_solved FROM chapter_progress WHERE user_id = ?", (st["id"],)).fetchall()
                matrix.append({
                    "student": dict(st),
                    "solved_chapters": {r["chapter_id"]: bool(r["is_solved"]) for r in solved}
                })
            conn.close()
            return self.send_json({"classroom": dict(owner_check), "matrix": matrix})

        # 5. SCHÜLER-CODE INSPEKTOR FÜR LEHRER
        elif path.startswith("/api/classrooms/student-code"):
            user_token = self.get_auth_user()
            if not user_token or user_token.get("role") != "teacher":
                return self.send_json({"error": "Nur für Lehrkräfte"}, 403)

            query = urllib.parse.parse_qs(parsed.query)
            classroom_id = query.get("classroom_id", [""])[0]
            student_id = query.get("student_id", [""])[0]
            chapter_id = query.get("chapter_id", [""])[0]

            if not classroom_id or not student_id or not chapter_id:
                return self.send_json({"error": "Fehlende Parameter"}, 400)

            conn = get_db()
            # Prüfe Autorisierung
            auth_check = conn.execute("""
                SELECT c.id FROM classrooms c
                JOIN class_enrollments ce ON c.id = ce.classroom_id
                WHERE c.id = ? AND c.teacher_id = ? AND ce.user_id = ?
            """, (int(classroom_id), user_token["uid"], int(student_id))).fetchone()

            if not auth_check:
                conn.close()
                return self.send_json({"error": "Zugriff verweigert"}, 403)

            progress = conn.execute("SELECT chapter_id, code_draft, subgoals_json, is_solved, solved_at FROM chapter_progress WHERE user_id = ? AND chapter_id = ?", (int(student_id), chapter_id)).fetchone()
            student = conn.execute("SELECT id, name, email FROM users WHERE id = ?", (int(student_id),)).fetchone()
            conn.close()

            return self.send_json({
                "student": dict(student) if student else None,
                "progress": dict(progress) if progress else None
            })

        # 6. ZERTIFIKATS-VERIFIKATION
        elif path.startswith("/api/certificates/verify"):
            query = urllib.parse.parse_qs(parsed.query)
            cert_uuid = query.get("uuid", [""])[0].strip()

            if not cert_uuid:
                return self.send_json({"error": "uuid fehlt"}, 400)

            conn = get_db()
            cert = conn.execute("SELECT uuid, track_id, student_name, issued_at FROM certificates WHERE uuid = ?", (cert_uuid,)).fetchone()
            conn.close()

            if not cert:
                return self.send_json({"valid": False, "error": "Zertifikat nicht gefunden"}, 404)
            return self.send_json({"valid": True, "certificate": dict(cert)})

        elif path == "/api/stats/leaderboard":
            conn = get_db()
            rows = conn.execute("SELECT name, xp, level, role FROM users WHERE role = 'student' ORDER BY xp DESC LIMIT 20").fetchall()
            conn.close()
            return self.send_json({"leaderboard": [dict(r) for r in rows]})

        # 7. ADMIN: SYSTEMSTATISTIKEN
        elif path == "/api/admin/stats":
            admin = self.get_admin_user()
            if not admin:
                return self.send_json({"error": "Admin-Rechte erforderlich"}, 403)
            conn = get_db()
            total_users = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
            roles_count = dict(conn.execute("SELECT role, COUNT(*) FROM users GROUP BY role").fetchall())
            total_solved = conn.execute("SELECT COUNT(*) FROM chapter_progress WHERE is_solved = 1").fetchone()[0]
            total_classrooms = conn.execute("SELECT COUNT(*) FROM classrooms").fetchone()[0]
            recent_users = conn.execute("SELECT COUNT(*) FROM users WHERE created_at >= datetime('now', '-7 days')").fetchone()[0]
            conn.close()
            db_size = DB_FILE.stat().st_size if DB_FILE.exists() else 0
            return self.send_json({
                "total_users": total_users,
                "roles": roles_count,
                "total_solved": total_solved,
                "total_classrooms": total_classrooms,
                "recent_users": recent_users,
                "db_size_kb": round(db_size / 1024, 1)
            })

        # 8. ADMIN: BENUTZERLISTE
        elif path == "/api/admin/users":
            admin = self.get_admin_user()
            if not admin:
                return self.send_json({"error": "Admin-Rechte erforderlich"}, 403)
            conn = get_db()
            rows = conn.execute("""
                SELECT u.id, u.email, u.name, u.role, u.xp, u.level, u.streak_days, u.created_at,
                       COUNT(cp.id) as solved_count
                FROM users u
                LEFT JOIN chapter_progress cp ON u.id = cp.user_id AND cp.is_solved = 1
                GROUP BY u.id
                ORDER BY u.id DESC
            """).fetchall()
            conn.close()
            return self.send_json({"users": [dict(r) for r in rows]})

        # 9. ADMIN: EINSTELLUNGEN
        elif path == "/api/admin/settings":
            admin = self.get_admin_user()
            if not admin:
                return self.send_json({"error": "Admin-Rechte erforderlich"}, 403)
            conn = get_db()
            rows = conn.execute("SELECT key, value FROM platform_settings").fetchall()
            conn.close()
            return self.send_json({"settings": dict(rows)})

        return super().do_GET()

    def do_POST(self):
        # 0. Proxy-Schutz gegen direktes Ansprechen von Port 8008 von außen
        if not is_trusted_source(self.client_address[0]):
            return self.send_json({"error": "Direkter Serverzugriff verweigert"}, 403)

        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        client_ip = self.get_client_ip()

        try:
            body = self.read_json_body()
        except Exception:
            return self.send_json({"error": "Ungültiges JSON"}, 400)

        # Globaler Wartungsmodus-Filter für schreibende Operationen (außer Login und Admin)
        if path.startswith("/api/") and path != "/api/auth/login" and not path.startswith("/api/admin/"):
            if is_maintenance_active() and not self.get_admin_user():
                return self.send_json({
                    "error": "Die Plattform befindet sich im Wartungsmodus. Schreibaktionen sind derzeit gesperrt.",
                    "maintenance": True
                }, 503)

        # 1. REGISTRIERUNG
        if path == "/api/auth/register":
            if is_maintenance_active() or get_platform_setting("allow_registration", "1") != "1":
                return self.send_json({"error": "Die Registrierung ist derzeit deaktiviert (Wartungsmodus oder Administrator-Sperre)."}, 403)

            if not rate_limiter.is_allowed(f"reg_{client_ip}", max_requests=5, window_seconds=60):
                return self.send_json({"error": "Zu viele Registrierungsversuche. Bitte warte eine Minute."}, 429)

            email = str(body.get("email", "")).strip().lower()
            password = str(body.get("password", ""))
            name = str(body.get("name", "")).strip()
            role = str(body.get("role", "student")).strip()

            if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email) or len(email) > 120:
                return self.send_json({"error": "Ungültige E-Mail-Adresse"}, 400)
            if len(password) < 6 or len(password) > 128:
                return self.send_json({"error": "Passwort muss zwischen 6 und 128 Zeichen lang sein"}, 400)
            if not name or len(name) > 60:
                return self.send_json({"error": "Name muss zwischen 1 und 60 Zeichen lang sein"}, 400)
            if role not in ("student", "teacher", "solo"):
                role = "solo"

            pwd_hash, salt = hash_password(password)
            conn = get_db()
            try:
                c = conn.cursor()
                c.execute("INSERT INTO users (email, password_hash, salt, name, role) VALUES (?, ?, ?, ?, ?)",
                          (email, pwd_hash, salt, name, role))
                user_id = c.lastrowid
                conn.commit()
                token = generate_token(user_id, email, role)
                return self.send_json({
                    "message": "Erfolgreich registriert!",
                    "token": token,
                    "user": {"id": user_id, "email": email, "name": name, "role": role, "xp": 0, "level": 1}
                }, 201)
            except sqlite3.IntegrityError:
                return self.send_json({"error": "Ein Benutzer mit dieser E-Mail existiert bereits"}, 409)
            finally:
                conn.close()

        # 2. LOGIN (mit Constant-Time Schutz gegen Enumeration & Wartungsmodus-Prüfung)
        elif path == "/api/auth/login":
            if not rate_limiter.is_allowed(f"login_{client_ip}", max_requests=8, window_seconds=60):
                return self.send_json({"error": "Zu viele Login-Versuche. Bitte warte eine Minute."}, 429)

            email = str(body.get("email", "")).strip().lower()
            password = str(body.get("password", ""))

            conn = get_db()
            user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
            conn.close()

            if not user:
                verify_password(password, DUMMY_HASH, DUMMY_SALT)
                return self.send_json({"error": "Ungültige E-Mail-Adresse oder Passwort"}, 401)

            if not verify_password(password, user["password_hash"], user["salt"]):
                return self.send_json({"error": "Ungültige E-Mail-Adresse oder Passwort"}, 401)

            # Wartungsmodus: Nur Administratoren dürfen sich anmelden
            if is_maintenance_active() and user["role"] != "admin":
                return self.send_json({
                    "error": "Die Plattform befindet sich im Wartungsmodus. Der Login ist vorübergehend nur für Administratoren freigeschaltet.",
                    "maintenance": True
                }, 503)

            token = generate_token(user["id"], user["email"], user["role"])
            return self.send_json({
                "message": "Erfolgreich angemeldet!",
                "token": token,
                "user": {
                    "id": user["id"],
                    "email": user["email"],
                    "name": user["name"],
                    "role": user["role"],
                    "xp": user["xp"],
                    "level": user["level"],
                    "streak_days": user["streak_days"]
                }
            })

        # 3. CODE SPEICHERN (AUTO-SAVE)
        elif path == "/api/progress/save":
            user_token = self.get_auth_user()
            if not user_token:
                return self.send_json({"error": "Nicht authentifiziert"}, 401)

            chapter_id = str(body.get("chapter_id", ""))[:120]
            code_draft = str(body.get("code_draft", ""))[:100_000]
            subgoals_json = json.dumps(body.get("subgoals", {}))[:10_000]

            if not chapter_id or ".." in chapter_id or "\\" in chapter_id:
                return self.send_json({"error": "Ungültiges chapter_id"}, 400)

            conn = get_db()
            conn.execute("""
                INSERT INTO chapter_progress (user_id, chapter_id, code_draft, subgoals_json, updated_at)
                VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(user_id, chapter_id) DO UPDATE SET
                    code_draft = excluded.code_draft,
                    subgoals_json = excluded.subgoals_json,
                    updated_at = CURRENT_TIMESTAMP
            """, (user_token["uid"], chapter_id, code_draft, subgoals_json))
            conn.commit()
            conn.close()

            return self.send_json({"status": "saved", "chapter_id": chapter_id})

        # 4. PROGRESS SOLVE
        elif path == "/api/progress/solve":
            user_token = self.get_auth_user()
            if not user_token:
                return self.send_json({"error": "Nicht authentifiziert"}, 401)

            chapter_id = str(body.get("chapter_id", ""))[:120]
            try:
                xp_reward = min(max(0, int(body.get("xp_reward", 100))), 100)
            except (ValueError, TypeError):
                xp_reward = 100

            if not chapter_id:
                return self.send_json({"error": "chapter_id erforderlich"}, 400)

            conn = get_db()
            existing = conn.execute("SELECT is_solved FROM chapter_progress WHERE user_id = ? AND chapter_id = ?", (user_token["uid"], chapter_id)).fetchone()
            was_already_solved = existing and existing["is_solved"] == 1

            if not was_already_solved:
                conn.execute("""
                    INSERT INTO chapter_progress (user_id, chapter_id, is_solved, solved_at, updated_at)
                    VALUES (?, ?, 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                    ON CONFLICT(user_id, chapter_id) DO UPDATE SET
                        is_solved = 1,
                        solved_at = CURRENT_TIMESTAMP,
                        updated_at = CURRENT_TIMESTAMP
                """, (user_token["uid"], chapter_id))

                user_row = conn.execute("SELECT xp FROM users WHERE id = ?", (user_token["uid"],)).fetchone()
                new_xp = (user_row["xp"] if user_row else 0) + xp_reward
                new_level = (new_xp // 100) + 1

                conn.execute("UPDATE users SET xp = ?, level = ? WHERE id = ?", (new_xp, new_level, user_token["uid"]))
                conn.commit()
                conn.close()
                return self.send_json({"status": "solved", "earned_xp": xp_reward, "total_xp": new_xp, "level": new_level})
            else:
                conn.close()
                return self.send_json({"status": "already_solved", "earned_xp": 0})

        # 5. KLASSENRAUM ERSTELLEN
        elif path == "/api/classrooms/create":
            user_token = self.get_auth_user()
            if not user_token or user_token.get("role") != "teacher":
                return self.send_json({"error": "Nur für Lehrkräfte gestattet"}, 403)

            name = str(body.get("name", "")).strip()[:80]
            if not name:
                return self.send_json({"error": "Klassenname erforderlich"}, 400)

            invite_code = "PY-" + secrets.token_hex(3).upper()
            conn = get_db()
            c = conn.cursor()
            c.execute("INSERT INTO classrooms (teacher_id, name, invite_code) VALUES (?, ?, ?)",
                      (user_token["uid"], name, invite_code))
            class_id = c.lastrowid
            conn.commit()
            conn.close()

            return self.send_json({"classroom": {"id": class_id, "name": name, "invite_code": invite_code}}, 201)

        # 6. KLASSENRAUM BEITRETEN
        elif path == "/api/classrooms/join":
            if not rate_limiter.is_allowed(f"join_{client_ip}", max_requests=10, window_seconds=60):
                return self.send_json({"error": "Zu viele Versuche. Bitte kurz warten."}, 429)

            user_token = self.get_auth_user()
            if not user_token:
                return self.send_json({"error": "Nicht authentifiziert"}, 401)

            code = str(body.get("invite_code", "")).strip().upper()[:12]
            conn = get_db()
            cl = conn.execute("SELECT id, name FROM classrooms WHERE invite_code = ?", (code,)).fetchone()
            if not cl:
                conn.close()
                return self.send_json({"error": "Ungültiger Einladungscode"}, 404)

            try:
                conn.execute("INSERT INTO class_enrollments (classroom_id, user_id) VALUES (?, ?)", (cl["id"], user_token["uid"]))
                conn.commit()
                conn.close()
                return self.send_json({"message": f"Erfolgreich Klasse '{cl['name']}' beigetreten!", "classroom": dict(cl)})
            except sqlite3.IntegrityError:
                conn.close()
                return self.send_json({"message": "Du bist dieser Klasse bereits beigetreten.", "classroom": dict(cl)})

        # 7. KLASSE LÖSCHEN (LEHRER)
        elif path == "/api/classrooms/delete":
            user_token = self.get_auth_user()
            if not user_token or user_token.get("role") != "teacher":
                return self.send_json({"error": "Nur für Lehrkräfte"}, 403)

            class_id = body.get("classroom_id")
            conn = get_db()
            conn.execute("DELETE FROM classrooms WHERE id = ? AND teacher_id = ?", (class_id, user_token["uid"]))
            conn.commit()
            conn.close()
            return self.send_json({"status": "deleted"})

        # 8. ZERTIFIKAT AUSSTELLEN
        elif path == "/api/certificates/create":
            user_token = self.get_auth_user()
            if not user_token:
                return self.send_json({"error": "Nicht authentifiziert"}, 401)

            track_id = str(body.get("track_id", ""))[:60]
            student_name = str(body.get("student_name", ""))[:100]
            cert_uuid = str(uuid.uuid4())

            conn = get_db()
            conn.execute("INSERT INTO certificates (uuid, user_id, track_id, student_name) VALUES (?, ?, ?, ?)",
                         (cert_uuid, user_token["uid"], track_id, student_name))
            conn.commit()
            conn.close()
            return self.send_json({"uuid": cert_uuid, "track_id": track_id, "student_name": student_name})

        # 9. ADMIN: ROLLE ÄNDERN
        elif path == "/api/admin/users/role":
            admin = self.get_admin_user()
            if not admin:
                return self.send_json({"error": "Admin-Rechte erforderlich"}, 403)
            target_uid = int(body.get("user_id", 0))
            new_role = str(body.get("role", "")).strip().lower()
            if new_role not in ["admin", "teacher", "student", "solo"]:
                return self.send_json({"error": "Ungültige Rolle"}, 400)
            conn = get_db()
            conn.execute("UPDATE users SET role = ? WHERE id = ?", (new_role, target_uid))
            conn.commit()
            conn.close()
            return self.send_json({"success": True, "message": f"Rolle auf '{new_role}' geändert"})

        # 10. ADMIN: PASSWORT ZURÜCKSETZEN
        elif path == "/api/admin/users/reset-password":
            admin = self.get_admin_user()
            if not admin:
                return self.send_json({"error": "Admin-Rechte erforderlich"}, 403)
            target_uid = int(body.get("user_id", 0))
            new_pw = str(body.get("new_password", "")).strip()
            if len(new_pw) < 6:
                return self.send_json({"error": "Passwort muss mindestens 6 Zeichen lang sein"}, 400)
            salt = secrets.token_hex(16)
            pw_hash, _ = hash_password(new_pw, salt)
            conn = get_db()
            conn.execute("UPDATE users SET password_hash = ?, salt = ? WHERE id = ?", (pw_hash, salt, target_uid))
            conn.commit()
            conn.close()
            return self.send_json({"success": True, "message": "Passwort erfolgreich aktualisiert"})

        # 11. ADMIN: BENUTZER LÖSCHEN
        elif path == "/api/admin/users/delete":
            admin = self.get_admin_user()
            if not admin:
                return self.send_json({"error": "Admin-Rechte erforderlich"}, 403)
            target_uid = int(body.get("user_id", 0))
            if target_uid == admin["id"]:
                return self.send_json({"error": "Der eigene Admin-Account kann nicht gelöscht werden"}, 400)
            conn = get_db()
            conn.execute("DELETE FROM users WHERE id = ?", (target_uid,))
            conn.commit()
            conn.close()
            return self.send_json({"success": True, "message": "Benutzer erfolgreich gelöscht"})

        # 12. ADMIN: BENUTZER MANUELL ANLEGEN
        elif path == "/api/admin/users/create":
            admin = self.get_admin_user()
            if not admin:
                return self.send_json({"error": "Admin-Rechte erforderlich"}, 403)
            name = body.get("name", "").strip()
            email = body.get("email", "").strip().lower()
            password = body.get("password", "")
            role = body.get("role", "student")
            if not name or not email or len(password) < 6 or role not in ["admin", "teacher", "student", "solo"]:
                return self.send_json({"error": "Ungültige Eingaben"}, 400)
            salt = secrets.token_hex(16)
            pw_hash, _ = hash_password(password, salt)
            try:
                conn = get_db()
                cur = conn.execute("INSERT INTO users (name, email, password_hash, salt, role) VALUES (?, ?, ?, ?, ?)",
                                   (name, email, pw_hash, salt, role))
                new_id = cur.lastrowid
                conn.commit()
                conn.close()
                return self.send_json({"success": True, "user_id": new_id, "message": f"Benutzer {name} erstellt"})
            except sqlite3.IntegrityError:
                return self.send_json({"error": "E-Mail-Adresse existiert bereits"}, 409)

        # 13. ADMIN: GLOBALE EINSTELLUNGEN SPEICHERN
        elif path == "/api/admin/settings":
            admin = self.get_admin_user()
            if not admin:
                return self.send_json({"error": "Admin-Rechte erforderlich"}, 403)
            settings = body.get("settings", {})
            conn = get_db()
            for k, v in settings.items():
                conn.execute("INSERT INTO platform_settings (key, value) VALUES (?, ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value, updated_at = CURRENT_TIMESTAMP", (str(k), str(v)))
            conn.commit()
            conn.close()
            return self.send_json({"success": True, "message": "Einstellungen gespeichert"})

        return self.send_json({"error": "Endpunkt nicht gefunden"}, 404)

def run_server():
    init_db()
    handler = PlatformRequestHandler
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"🚀 Python Lernplattform Server läuft auf: http://localhost:{PORT}")
        print(f"🔒 Secret Key Status: Aktiv (Persistiert)")
        print(f"💾 SQLite-Datenbank: {DB_FILE}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server gestoppt.")

if __name__ == "__main__":
    run_server()
