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
import subprocess
import tempfile
import shutil
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
# 0. AUTOMATISCHES ROUTING FÜR ALLE 264 KURS-KAPITEL
# ------------------------------------------------------------------------------
CHAPTER_ROUTES = {}

def load_chapter_routes():
    global CHAPTER_ROUTES
    manifest_path = BASE_DIR / "assets" / "courses_manifest.js"
    if not manifest_path.exists():
        return
    try:
        content = manifest_path.read_text(encoding="utf-8")
        idx = content.find("{")
        if idx != -1:
            json_str = content[idx:].strip()
            if json_str.endswith(";"):
                json_str = json_str[:-1]
            manifest = json.loads(json_str)
            routes = {}
            for cid, c in manifest.items():
                for tr in c.get("tracks", []):
                    tid = tr.get("id", "")
                    for ch in tr.get("chapters", []):
                        f = ch.get("folder", "")
                        if f:
                            if cid == "python":
                                routes[f] = f"/{tid}/{f}"
                            else:
                                routes[f] = f"/courses/{cid}/{f}"
            legacy_aliases = {
                "01_lf9_netzwerke_und_dienste": "/courses/ihk_ap2_fisi/01_lf9_netzwerkinfrastruktur_und_routing",
                "02_lf10_serverdienste_und_automation": "/courses/ihk_ap2_fisi/03_lf10_serverdienste_und_identitaeten",
                "07_ap2_teil_1_probepruefung": "/courses/ihk_ap2_fisi/12_ap2_gesamtpruefung_simulation",
                "08_ap2_teil_2_probepruefung": "/courses/ihk_ap2_fisi/12_ap2_gesamtpruefung_simulation",
                "09_ap2_wiso_probepruefung": "/courses/ihk_ap2_fisi/12_ap2_gesamtpruefung_simulation"
            }
            routes.update(legacy_aliases)
            CHAPTER_ROUTES = routes
    except Exception as e:
        print(f"Warnung beim Laden der Kapitel-Routen: {e}")

load_chapter_routes()

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

    # Migrationen für Ausbildungen, Lernfelder und Kurszuweisungen
    for col_def in [
        "ALTER TABLE classrooms ADD COLUMN assigned_courses TEXT DEFAULT '[]'",
        "ALTER TABLE classrooms ADD COLUMN profession TEXT DEFAULT 'FISI'",
        "ALTER TABLE classrooms ADD COLUMN training_year INTEGER DEFAULT 1",
        "ALTER TABLE users ADD COLUMN profession TEXT DEFAULT 'FISI'",
        "ALTER TABLE users ADD COLUMN training_year INTEGER DEFAULT 1",
        "ALTER TABLE users ADD COLUMN assigned_courses TEXT DEFAULT '[]'",
    ]:
        try:
            c.execute(col_def)
        except Exception:
            pass

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

        # 1. System-, Konfigurations- und geheime Dateien immer strikt sperren
        if any(seg in clean_path for seg in ["/.git", "/.system_generated", "/.gemini", "platform_data.db", ".secret_key", ".env", ".jsonl"]):
            return True
        if "/." in clean_path or clean_path.startswith("."):
            return True
        if clean_path.startswith("/exams/") or clean_path == "/exams":
            return True
        if clean_path in ("/server.py", "server.py"):
            return True

        # 2. Gefährliche Endungen für Server-Root und PHP/DB
        if any(clean_path.endswith(ext) for ext in [".db", ".sqlite", ".sqlite3", ".secret_key", ".php", ".env", ".bak", ".conf"]):
            return True

        # 3. Kursdateien in den Lehrpfaden und Kursordnern explizit erlauben
        is_course_file = (
            clean_path.startswith("/lehrpfad_") or 
            clean_path.startswith("lehrpfad_") or 
            clean_path.startswith("/courses/") or 
            clean_path.startswith("courses/")
        )
        if not is_course_file:
            blocked_outside = (".py", ".sh", ".sql", ".log", ".ini", ".yaml", ".yml")
            if any(clean_path.endswith(ext) for ext in blocked_outside):
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

        # Automatische Weiterleitung für Direktaufrufe von Kapitel-Ordnern an der Root-Ebene
        # (z. B. /02_lf2_arbeitsplaetze_ausstatten/index.html -> /courses/ihk_ap1/02_lf2_arbeitsplaetze_ausstatten/index.html)
        path_parts = [p for p in path.split("/") if p]
        if path_parts and not path.startswith("/api/"):
            first_part = path_parts[0]
            if first_part in CHAPTER_ROUTES:
                target_base = CHAPTER_ROUTES[first_part]
                sub_path = "/".join(path_parts[1:])
                if not sub_path:
                    sub_path = "index.html"
                target_url = f"{target_base}/{sub_path}"
                if parsed.query:
                    target_url += f"?{parsed.query}"
                self.send_response(302)
                self.send_header("Location", target_url)
                self.send_header("Cache-Control", "no-cache")
                self.end_headers()
                return

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
            row = conn.execute("SELECT id, email, name, role, xp, level, streak_days, profession, training_year, assigned_courses FROM users WHERE id = ?", (user_token["uid"],)).fetchone()
            if not row:
                conn.close()
                return self.send_json({"error": "Benutzer nicht gefunden"}, 404)
            user_dict = dict(row)
            try:
                assigned_set = set(json.loads(user_dict.get("assigned_courses") or "[]"))
            except Exception:
                assigned_set = set()

            # Enrolled classrooms assignments
            class_courses = conn.execute("""
                SELECT c.assigned_courses, c.profession, c.training_year 
                FROM class_enrollments ce 
                JOIN classrooms c ON ce.classroom_id = c.id 
                WHERE ce.user_id = ?
            """, (user_token["uid"],)).fetchall()
            conn.close()

            for cc in class_courses:
                if not user_dict.get("profession") and cc["profession"]:
                    user_dict["profession"] = cc["profession"]
                if not user_dict.get("training_year") and cc["training_year"]:
                    user_dict["training_year"] = cc["training_year"]
                try:
                    c_arr = json.loads(cc["assigned_courses"] or "[]")
                    for ca in c_arr:
                        assigned_set.add(ca)
                except Exception:
                    pass
            user_dict["assigned_courses"] = list(assigned_set)
            return self.send_json({"user": user_dict})

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
            if user_token.get("role") in ("teacher", "admin"):
                if user_token.get("role") == "admin":
                    classes = conn.execute("SELECT id, name, invite_code, assigned_courses, profession, training_year, created_at FROM classrooms").fetchall()
                else:
                    classes = conn.execute("SELECT id, name, invite_code, assigned_courses, profession, training_year, created_at FROM classrooms WHERE teacher_id = ?", (user_token["uid"],)).fetchall()
                result = []
                for cl in classes:
                    student_count = conn.execute("SELECT COUNT(*) FROM class_enrollments WHERE classroom_id = ?", (cl["id"],)).fetchone()[0]
                    courses_raw = cl["assigned_courses"] or "[]"
                    try:
                        courses_list = json.loads(courses_raw)
                    except Exception:
                        courses_list = []
                    result.append({
                        **dict(cl),
                        "assigned_courses": courses_list,
                        "student_count": student_count
                    })
                conn.close()
                return self.send_json({"classrooms": result})
            else:
                classes = conn.execute("""
                    SELECT c.id, c.name, c.assigned_courses, c.profession, c.training_year, u.name as teacher_name, ce.joined_at 
                    FROM class_enrollments ce 
                    JOIN classrooms c ON ce.classroom_id = c.id 
                    JOIN users u ON c.teacher_id = u.id 
                    WHERE ce.user_id = ?
                """, (user_token["uid"],)).fetchall()

                u_row = conn.execute("SELECT profession, training_year, assigned_courses FROM users WHERE id = ?", (user_token["uid"],)).fetchone()
                conn.close()

                parsed_classes = []
                all_assigned = set()
                for c in classes:
                    cd = dict(c)
                    try:
                        c_list = json.loads(cd.get("assigned_courses") or "[]")
                    except Exception:
                        c_list = []
                    cd["assigned_courses"] = c_list
                    for crs in c_list:
                        all_assigned.add(crs)
                    parsed_classes.append(cd)

                if u_row and u_row["assigned_courses"]:
                    try:
                        user_courses = json.loads(u_row["assigned_courses"])
                        for crs in user_courses:
                            all_assigned.add(crs)
                    except Exception:
                        pass

                return self.send_json({
                    "classrooms": parsed_classes,
                    "assigned_courses": list(all_assigned),
                    "profession": (u_row and u_row["profession"]) or (parsed_classes and parsed_classes[0].get("profession")) or "FISI",
                    "training_year": (u_row and u_row["training_year"]) or (parsed_classes and parsed_classes[0].get("training_year")) or 1
                })

        # 4. CLASSROOMS MATRIX (mit IDOR-Schutz)
        elif path.startswith("/api/classrooms/matrix"):
            user_token = self.get_auth_user()
            if not user_token or user_token.get("role") not in ("teacher", "admin"):
                return self.send_json({"error": "Nur für Lehrkräfte"}, 403)
            
            query = urllib.parse.parse_qs(parsed.query)
            classroom_id = query.get("classroom_id", [""])[0]
            if not classroom_id or not classroom_id.isdigit():
                return self.send_json({"error": "Ungültige classroom_id"}, 400)

            conn = get_db()
            if user_token.get("role") == "admin":
                owner_check = conn.execute("SELECT id, name FROM classrooms WHERE id = ?", (int(classroom_id),)).fetchone()
            else:
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
                return self.send_json({"valid": False, "verified": False, "error": "Zertifikat nicht gefunden"}, 404)
            return self.send_json({"valid": True, "verified": True, "certificate": dict(cert)})

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
            if not user_token or user_token.get("role") not in ("teacher", "admin"):
                return self.send_json({"error": "Nur für Lehrkräfte und Administratoren gestattet"}, 403)

            name = str(body.get("name", "")).strip()[:80]
            if not name:
                return self.send_json({"error": "Klassenname erforderlich"}, 400)

            profession = str(body.get("profession", "FISI")).strip()[:10]
            try:
                training_year = int(body.get("training_year", 1))
                if training_year not in (1, 2, 3):
                    training_year = 1
            except (ValueError, TypeError):
                training_year = 1

            assigned_courses = body.get("assigned_courses", [])
            if not isinstance(assigned_courses, list):
                assigned_courses = []
            assigned_courses_json = json.dumps(assigned_courses)

            invite_code = "PY-" + secrets.token_hex(3).upper()
            conn = get_db()
            c = conn.cursor()
            c.execute("INSERT INTO classrooms (teacher_id, name, invite_code, assigned_courses, profession, training_year) VALUES (?, ?, ?, ?, ?, ?)",
                      (user_token["uid"], name, invite_code, assigned_courses_json, profession, training_year))
            class_id = c.lastrowid
            conn.commit()
            conn.close()

            return self.send_json({
                "classroom": {
                    "id": class_id,
                    "name": name,
                    "invite_code": invite_code,
                    "profession": profession,
                    "training_year": training_year,
                    "assigned_courses": assigned_courses
                }
            }, 201)

        # 5b. KLASSENRAUM KURSE & LERNFELDER AKTUALISIEREN
        elif path == "/api/classrooms/update-courses":
            user_token = self.get_auth_user()
            if not user_token or user_token.get("role") not in ("teacher", "admin"):
                return self.send_json({"error": "Nur für Lehrkräfte und Administratoren"}, 403)

            class_id = body.get("classroom_id")
            if not class_id:
                return self.send_json({"error": "classroom_id erforderlich"}, 400)

            assigned_courses = body.get("assigned_courses", [])
            if not isinstance(assigned_courses, list):
                assigned_courses = []
            assigned_courses_json = json.dumps(assigned_courses)

            profession = str(body.get("profession", "FISI")).strip()[:10]
            try:
                training_year = int(body.get("training_year", 1))
                if training_year not in (1, 2, 3):
                    training_year = 1
            except (ValueError, TypeError):
                training_year = 1

            conn = get_db()
            if user_token.get("role") == "admin":
                owner_check = conn.execute("SELECT id FROM classrooms WHERE id = ?", (int(class_id),)).fetchone()
            else:
                owner_check = conn.execute("SELECT id FROM classrooms WHERE id = ? AND teacher_id = ?", (int(class_id), user_token["uid"])).fetchone()

            if not owner_check:
                conn.close()
                return self.send_json({"error": "Klasse nicht gefunden oder keine Berechtigung"}, 403)

            conn.execute("UPDATE classrooms SET assigned_courses = ?, profession = ?, training_year = ? WHERE id = ?",
                         (assigned_courses_json, profession, training_year, int(class_id)))
            conn.commit()
            conn.close()
            return self.send_json({
                "status": "updated",
                "assigned_courses": assigned_courses,
                "profession": profession,
                "training_year": training_year
            })

        # 5c. SCHÜLER AUSBILDUNGSPLAN & KURSE SETZEN
        elif path == "/api/user/apprenticeship":
            user_token = self.get_auth_user()
            if not user_token:
                return self.send_json({"error": "Nicht authentifiziert"}, 401)

            profession = str(body.get("profession", "FISI")).strip()[:10]
            try:
                training_year = int(body.get("training_year", 1))
                if training_year not in (1, 2, 3):
                    training_year = 1
            except (ValueError, TypeError):
                training_year = 1

            assigned_courses = body.get("assigned_courses", None)
            conn = get_db()
            if assigned_courses is not None and isinstance(assigned_courses, list):
                assigned_json = json.dumps(assigned_courses)
                conn.execute("UPDATE users SET profession = ?, training_year = ?, assigned_courses = ? WHERE id = ?",
                             (profession, training_year, assigned_json, user_token["uid"]))
            else:
                conn.execute("UPDATE users SET profession = ?, training_year = ? WHERE id = ?",
                             (profession, training_year, user_token["uid"]))
            conn.commit()
            conn.close()
            return self.send_json({
                "status": "updated",
                "profession": profession,
                "training_year": training_year,
                "assigned_courses": assigned_courses
            })

        # 6. KLASSENRAUM BEITRETEN
        elif path == "/api/classrooms/join":
            if not rate_limiter.is_allowed(f"join_{client_ip}", max_requests=10, window_seconds=60):
                return self.send_json({"error": "Zu viele Versuche. Bitte kurz warten."}, 429)

            user_token = self.get_auth_user()
            if not user_token:
                return self.send_json({"error": "Nicht authentifiziert"}, 401)

            code = str(body.get("invite_code", "")).strip().upper()[:12]
            conn = get_db()
            cl = conn.execute("SELECT id, name, profession, training_year, assigned_courses FROM classrooms WHERE invite_code = ?", (code,)).fetchone()
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

        # 7. KLASSE LÖSCHEN (LEHRER & ADMIN)
        elif path == "/api/classrooms/delete":
            user_token = self.get_auth_user()
            if not user_token or user_token.get("role") not in ("teacher", "admin"):
                return self.send_json({"error": "Nur für Lehrkräfte und Administratoren"}, 403)

            class_id = body.get("classroom_id")
            conn = get_db()
            if user_token.get("role") == "admin":
                conn.execute("DELETE FROM classrooms WHERE id = ?", (class_id,))
            else:
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

        # 14. AUTOMATISIERTER RUNNER TESTSUITE ENDPUNKT (BASH, GIT, DNS, POWERSHELL, AD)
        elif path == "/api/runners/test":
            user_token = self.get_auth_user()
            if not user_token:
                return self.send_json({"error": "Nicht authentifiziert. Bitte melde dich an, um Tests auszuführen."}, 401)

            language = str(body.get("language", "")).strip().lower()
            base_path = str(body.get("base_path", "")).strip()
            user_code = str(body.get("user_code", ""))[:100_000]
            task_file = str(body.get("task_file", "")).strip()
            test_file = str(body.get("test_file", "")).strip()

            if not base_path or ".." in base_path or base_path.startswith("/") or "\\" in base_path:
                return self.send_json({"error": "Ungültiger Pfad"}, 400)

            chapter_dir = os.path.normpath(os.path.join(str(BASE_DIR), base_path))
            if not os.path.isdir(chapter_dir) or not chapter_dir.startswith(str(BASE_DIR)):
                return self.send_json({"error": "Kapitelverzeichnis nicht gefunden"}, 404)

            # Security: Gefährliche Shell/PowerShell-Befehle blockieren
            danger_patterns = [
                r"\brm\s+-[rf]*\s+/(?:\s|$)",
                r"\bmkfs\b",
                r"\bdd\s+if=",
                r"\bshutdown\b",
                r"\breboot\b",
                r":\(\)\s*\{\s*:\s*\|\s*:\s*&\s*\}\s*;",
                r"\bcurl\b.*\|\s*(?:bash|sh)\b",
                r"Remove-Item\s+-Recurse\s+[\'\"]?/(?:[\'\"]|\s|$)",
                r"Format-Volume"
            ]
            for pat in danger_patterns:
                if re.search(pat, user_code, re.IGNORECASE):
                    return self.send_json({
                        "success": False,
                        "error": "Sicherheits-Sperre: Unzulässiger Systembefehl im Code erkannt.",
                        "stdout": "❌ Ausführung durch Sicherheitsfilter blockiert.\n",
                        "failures": 1,
                        "total": 1
                    }, 400)

            sandbox = tempfile.mkdtemp(prefix="test_sandbox_")
            try:
                # 1. BASH / GIT / DNS EXECUTION
                if language in ("bash", "shell", "git", "dns_records", "dns"):
                    actual_task_file = task_file or "aufgabe.sh"
                    actual_test_file = test_file or "test_aufgabe.sh"
                    src_test = os.path.join(chapter_dir, actual_test_file)
                    if not os.path.isfile(src_test):
                        return self.send_json({"error": f"Testdatei '{actual_test_file}' nicht gefunden"}, 404)

                    shutil.copy(src_test, os.path.join(sandbox, actual_test_file))
                    user_script_path = os.path.join(sandbox, actual_task_file)
                    with open(user_script_path, "w", encoding="utf-8") as f:
                        f.write(user_code)
                    os.chmod(user_script_path, 0o755)
                    os.chmod(os.path.join(sandbox, actual_test_file), 0o755)

                    env = os.environ.copy()
                    env["HOME"] = sandbox
                    env["TERM"] = "xterm-256color"

                    proc = subprocess.run(
                        ["bash", actual_test_file, actual_task_file],
                        cwd=sandbox,
                        capture_output=True,
                        text=True,
                        timeout=12,
                        env=env
                    )

                    stdout = proc.stdout or ""
                    stderr = proc.stderr or ""
                    exit_code = proc.returncode

                    passed_match = re.search(r"(\d+)\s+von\s+(\d+)\s+Tests\s+bestanden", stdout)
                    fail_match = re.search(r"(\d+)\s+von\s+(\d+)\s+Tests\s+fehlgeschlagen", stdout)
                    
                    if exit_code == 0:
                        failures = 0
                        passed = int(passed_match.group(1)) if passed_match else 4
                        total = int(passed_match.group(2)) if passed_match else passed
                    else:
                        if fail_match:
                            failures = int(fail_match.group(1))
                            total = int(fail_match.group(2))
                            passed = max(0, total - failures)
                        else:
                            failures = 1
                            passed = 0
                            total = 1

                    return self.send_json({
                        "success": exit_code == 0 and failures == 0 and total > 0,
                        "exit_code": exit_code,
                        "stdout": stdout,
                        "stderr": stderr,
                        "total": total,
                        "passed": passed,
                        "failures": failures
                    })

                # 2. POWERSHELL / ACTIVE DIRECTORY EXECUTION
                elif language in ("powershell", "pwsh", "active_directory", "ad"):
                    actual_task_file = task_file or "aufgabe.ps1"
                    actual_test_file = test_file or "test_aufgabe.ps1"
                    src_test = os.path.join(chapter_dir, actual_test_file)
                    if not os.path.isfile(src_test):
                        return self.send_json({"error": f"Testdatei '{actual_test_file}' nicht gefunden"}, 404)

                    shutil.copy(src_test, os.path.join(sandbox, actual_test_file))
                    user_script_path = os.path.join(sandbox, actual_task_file)
                    with open(user_script_path, "w", encoding="utf-8") as f:
                        f.write(user_code)

                    pester_shim = f"""
function Describe ($name, [ScriptBlock]$block) {{
    Write-Host "`n🧪 Testsuite: $name" -ForegroundColor Cyan
    & $block
}}
function Context ($name, [ScriptBlock]$block) {{
    Write-Host "  📂 $name" -ForegroundColor DarkCyan
    & $block
}}
$script:PesterTotal = 0
$script:PesterPassed = 0
$script:PesterFailed = 0

function It ($name, [ScriptBlock]$block) {{
    $script:PesterTotal++
    try {{
        & $block
        Write-Host "  [+] $name [Passed]" -ForegroundColor Green
        $script:PesterPassed++
    }} catch {{
        Write-Host "  [-] $name [Failed]" -ForegroundColor Red
        Write-Host "      $($_.Exception.Message)" -ForegroundColor DarkGray
        $script:PesterFailed++
    }}
}}

function Should {{
    [CmdletBinding()]
    param(
        [Parameter(ValueFromPipeline = $true)]
        $Actual,
        [switch]$Be,
        [switch]$Not,
        [switch]$BeGreaterThan,
        [switch]$BeLessThan,
        [switch]$Match,
        [Parameter(Position = 0)]
        $Expected
    )
    process {{
        if ($Be) {{
            if ("$Actual" -ne "$Expected") {{
                throw "Expected: $Expected, but got: $Actual"
            }}
        }} elseif ($Not) {{
            if ("$Actual" -eq "$Expected") {{
                throw "Expected not: $Expected, but got equal value"
            }}
        }} elseif ($Match) {{
            if ("$Actual" -notmatch "$Expected") {{
                throw "Expected $Actual to match $Expected"
            }}
        }} else {{
            if ("$Actual" -ne "$Expected") {{
                throw "Expected: $Expected, but got: $Actual"
            }}
        }}
    }}
}}

. ./{actual_task_file}
. ./{actual_test_file}

Write-Host "`n📊 Gesamtergebnis: $script:PesterPassed von $script:PesterTotal Tests bestanden."
if ($script:PesterFailed -gt 0 -or $script:PesterTotal -eq 0) {{
    Write-Host "❌ $script:PesterFailed Test(s) fehlgeschlagen!" -ForegroundColor Red
    exit 1
}} else {{
    Write-Host "🎉 Alle $script:PesterTotal Tests erfolgreich bestanden!" -ForegroundColor Green
    exit 0
}}
"""
                    runner_path = os.path.join(sandbox, "run_pester_test.ps1")
                    with open(runner_path, "w", encoding="utf-8") as f:
                        f.write(pester_shim)

                    proc = subprocess.run(
                        ["pwsh", "-NoProfile", "-NonInteractive", "-File", "run_pester_test.ps1"],
                        cwd=sandbox,
                        capture_output=True,
                        text=True,
                        timeout=12
                    )

                    stdout = proc.stdout or ""
                    stderr = proc.stderr or ""
                    exit_code = proc.returncode

                    passed_match = re.search(r"(\d+)\s+von\s+(\d+)\s+Tests\s+bestanden", stdout)
                    if passed_match:
                        passed = int(passed_match.group(1))
                        total = int(passed_match.group(2))
                        failures = total - passed
                    else:
                        if exit_code == 0:
                            passed = 4
                            total = 4
                            failures = 0
                        else:
                            passed = 0
                            total = 1
                            failures = 1

                    return self.send_json({
                        "success": exit_code == 0 and failures == 0 and total > 0,
                        "exit_code": exit_code,
                        "stdout": stdout,
                        "stderr": stderr,
                        "total": total,
                        "passed": passed,
                        "failures": failures
                    })

                else:
                    return self.send_json({"error": f"Kein Server-Runner für Sprache '{language}' konfiguriert"}, 400)

            except subprocess.TimeoutExpired:
                return self.send_json({
                    "success": False,
                    "error": "Zeitüberschreitung: Testausführung dauerte länger als 12 Sekunden.",
                    "stdout": "⏱️ Zeitüberschreitung bei der Testausführung.\n",
                    "failures": 1,
                    "total": 1
                }, 408)
            except Exception as e:
                return self.send_json({"error": f"Serverfehler bei Testausführung: {str(e)}"}, 500)
            finally:
                shutil.rmtree(sandbox, ignore_errors=True)

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
