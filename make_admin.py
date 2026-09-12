#!/usr/bin/env python3
"""
🛡️ CLI HELPER: ADMIN STATUS VERGEBEN 🛡️
==========================================
Verwendung:
  python3 make_admin.py <email>
"""

import sys
import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).parent / "platform_data.db"

def make_admin(email: str):
    if not DB_FILE.exists():
        print(f"❌ Datenbank nicht gefunden: {DB_FILE}")
        sys.exit(1)

    conn = sqlite3.connect(str(DB_FILE))
    cur = conn.cursor()
    cur.execute("SELECT id, name, role FROM users WHERE email = ?", (email,))
    row = cur.fetchone()

    if not row:
        print(f"❌ Kein Benutzer mit E-Mail '{email}' gefunden.")
        print("Registrierte Benutzer:")
        for r in cur.execute("SELECT id, name, email, role FROM users").fetchall():
            print(f" - [{r[0]}] {r[1]} ({r[2]}) -> Rolle: {r[3]}")
        conn.close()
        sys.exit(1)

    cur.execute("UPDATE users SET role = 'admin' WHERE id = ?", (row[0],))
    conn.commit()
    conn.close()
    print(f"🎉 Erfolgreich: '{row[1]}' ({email}) ist nun vollwertiger System-Administrator (Rolle: admin)!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Verwendung: python3 make_admin.py <email>")
        sys.exit(1)
    make_admin(sys.argv[1].strip().lower())
