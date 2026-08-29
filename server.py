#!/usr/bin/env python3
"""
🐍 PYTHON LERNPLATTFORM – BACKEND SERVER 🐍
===========================================
Leichtgewichtiger, abhängigkeitsfreier REST-API & Static Server für die Online-Lernplattform.
- Läuft auf jedem Linux-Server / Webspace mit Standard-Python 3.
- SQLite-Datenbank (User-Accounts, Code-Drafts, XP, Klassen & Lehrer-Dashboard).
- PBKDF2-HMAC-SHA256 Passwort-Verschlüsselung & signierte Session-Tokens.
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
import urllib.parse
from pathlib import Path

PORT = int(os.environ.get("PORT", 8000))
BASE_DIR = Path(__file__).parent.resolve()
DB_FILE = BASE_DIR / "platform_data.db"
SECRET_KEY = secrets.token_hex(32)

# ==============================================================================
# DATENBANK INITIALISIERUNG
# ==============================================================================

def get_db():
    conn = sqlite3.connect(str(DB_FILE))
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    
    # 1. Benutzer-Tabelle
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

    # 2. Kapitel-Fortschritt & Code-Drafts
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

    # 3. Klassenräume (Lehrer-Feature)
    c.execute("""
    CREATE TABLE IF NOT EXISTS classrooms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        teacher_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        invite_code TEXT UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(teacher_id) REFERENCES users(id) ON DELETE CASCADE
    )""")

    # 4. Klassen-Mitgliedschaften
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

    # 5. Freigeschaltete Trophäen
    c.execute("""
    CREATE TABLE IF NOT EXISTS achievements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        trophy_id TEXT NOT NULL,
        unlocked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(user_id, trophy_id),
        FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
    )""")

    conn.commit()
    conn.close()

# ==============================================================================
# AUTHENTIFIZIERUNG & HASHING
# ==============================================================================

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

def generate_token(user_id: int, email: str, role: str) -> str:
    payload = {
        "uid": user_id,
        "email": email,
        "role": role,
        "exp": int(time.time()) + (86400 * 30) # 30 Tage gültig
    }
    payload_json = json.dumps(payload)
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

# ==============================================================================
# HTTP REQUEST HANDLER
# ==============================================================================

class PlatformRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def end_headers(self):
        # CORS & Cache-Header für moderne Web-Apps
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
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

    def get_auth_user(self) -> dict | None:
        auth_header = self.headers.get("Authorization", "")
        if auth_header.startswith("Bearer "):
            token = auth_header[7:].strip()
            return verify_token(token)
        return None

    def read_json_body(self) -> dict:
        content_length = int(self.headers.get("Content-Length", 0))
        if content_length == 0:
            return {}
        body = self.rfile.read(content_length)
        return json.loads(body.decode("utf-8"))

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        # --- API ROUTES ---
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

        elif path.startswith("/api/classrooms/matrix"):
            user_token = self.get_auth_user()
            if not user_token or user_token.get("role") != "teacher":
                return self.send_json({"error": "Nur für Lehrkräfte"}, 403)
            
            query = urllib.parse.parse_qs(parsed.query)
            classroom_id = query.get("classroom_id", [""])[0]
            if not classroom_id:
                return self.send_json({"error": "classroom_id fehlt"}, 400)

            conn = get_db()
            students = conn.execute("""
                SELECT u.id, u.name, u.email, u.xp, u.level, u.streak_days 
                FROM class_enrollments ce 
                JOIN users u ON ce.user_id = u.id 
                WHERE ce.classroom_id = ?
            """, (classroom_id,)).fetchall()

            matrix = []
            for st in students:
                solved = conn.execute("SELECT chapter_id, is_solved FROM chapter_progress WHERE user_id = ?", (st["id"],)).fetchall()
                matrix.append({
                    "student": dict(st),
                    "solved_chapters": {r["chapter_id"]: bool(r["is_solved"]) for r in solved}
                })
            conn.close()
            return self.send_json({"matrix": matrix})

        elif path == "/api/stats/leaderboard":
            conn = get_db()
            rows = conn.execute("SELECT name, xp, level, role FROM users WHERE role = 'student' ORDER BY xp DESC LIMIT 20").fetchall()
            conn.close()
            return self.send_json({"leaderboard": [dict(r) for r in rows]})

        # --- STATISCHE DATEIEN ---
        return super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        try:
            body = self.read_json_body()
        except Exception:
            return self.send_json({"error": "Ungültiges JSON"}, 400)

        # 1. REGISTRIERUNG
        if path == "/api/auth/register":
            email = body.get("email", "").strip().lower()
            password = body.get("password", "")
            name = body.get("name", "").strip()
            role = body.get("role", "student")

            if not email or not password or not name:
                return self.send_json({"error": "Name, E-Mail und Passwort sind erforderlich"}, 400)
            if len(password) < 6:
                return self.send_json({"error": "Passwort muss mindestens 6 Zeichen lang sein"}, 400)

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

        # 2. LOGIN
        elif path == "/api/auth/login":
            email = body.get("email", "").strip().lower()
            password = body.get("password", "")

            conn = get_db()
            user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
            conn.close()

            if not user or not verify_password(password, user["password_hash"], user["salt"]):
                return self.send_json({"error": "Ungültige E-Mail-Adresse oder Passwort"}, 401)

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

            chapter_id = body.get("chapter_id", "")
            code_draft = body.get("code_draft", "")
            subgoals_json = json.dumps(body.get("subgoals", {}))

            if not chapter_id:
                return self.send_json({"error": "chapter_id erforderlich"}, 400)

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

        # 4. KAPITEL ALS GELÖST MARKIEREN & XP VERGEBEN
        elif path == "/api/progress/solve":
            user_token = self.get_auth_user()
            if not user_token:
                return self.send_json({"error": "Nicht authentifiziert"}, 401)

            chapter_id = body.get("chapter_id", "")
            xp_reward = int(body.get("xp_reward", 100))

            if not chapter_id:
                return self.send_json({"error": "chapter_id erforderlich"}, 400)

            conn = get_db()
            # Prüfe, ob das Kapitel bereits gelöst war
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

                # XP & Level berechnen
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

        # 5. KLASSENRAUM ERSTELLEN (LEHRER)
        elif path == "/api/classrooms/create":
            user_token = self.get_auth_user()
            if not user_token or user_token.get("role") != "teacher":
                return self.send_json({"error": "Nur für Lehrkräfte gestattet"}, 403)

            name = body.get("name", "").strip()
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

        # 6. KLASSENRAUM BEITRETEN (SCHÜLER)
        elif path == "/api/classrooms/join":
            user_token = self.get_auth_user()
            if not user_token:
                return self.send_json({"error": "Nicht authentifiziert"}, 401)

            code = body.get("invite_code", "").strip().upper()
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

        return self.send_json({"error": "Endpunkt nicht gefunden"}, 404)

# ==============================================================================
# SERVER START
# ==============================================================================

def run_server():
    init_db()
    handler = PlatformRequestHandler
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"🚀 Python Lernplattform Server läuft auf: http://localhost:{PORT}")
        print(f"📁 Root-Verzeichnis: {BASE_DIR}")
        print(f"💾 SQLite-Datenbank: {DB_FILE}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server gestoppt.")

if __name__ == "__main__":
    run_server()
