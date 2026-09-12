# 🚀 IT-Praxisportal

[![Status](https://img.shields.io/badge/Status-Alpha%201.0%20Live-success.svg)](https://alpha.it-praxisportal.de/)
[![Kurse](https://img.shields.io/badge/Fachdisziplinen-13%20Kurse-blue.svg)](https://alpha.it-praxisportal.de/#curriculum)
[![Module](https://img.shields.io/badge/Inhalte-216%2B%20Module-indigo.svg)](https://alpha.it-praxisportal.de/#curriculum)
[![IHK Prüfung](https://img.shields.io/badge/IHK%20Standard-AP1%20%26%20AP2%20(AO%202020)-gold.svg)](https://alpha.it-praxisportal.de/#ihk-section)
[![Editor](https://img.shields.io/badge/Web--IDE-Monaco%20(VS%20Code)-purple.svg)](https://alpha.it-praxisportal.de/workspace.html)
[![Compliance](https://img.shields.io/badge/Datenschutz-100%25%20DSGVO%20(DE)-green.svg)](https://alpha.it-praxisportal.de/)

> **Die interaktive Lern- und Prüfungsvorbereitungs-Plattform für Fachinformatiker, IT-Systemelektroniker und Software-Entwickler.**  
> Echte IT-Praxis statt trockener Theorie: 13 Schlüsseltechnologien, 216 didaktisch aufbereitete Module, Monaco Web-IDE und realistische IHK-Abschlussprüfungssimulationen – direkt im Browser ohne lokale Installation.

---

## 📋 Inhaltsverzeichnis

1. [Überblick & Vision](#-überblick--vision)
2. [Systemarchitektur & Komponenten](#-systemarchitektur--komponenten)
3. [Die 13 Fachdisziplinen & Modul-Matrix](#-die-13-fachdisziplinen--modul-matrix)
4. [Monaco Web-IDE & Multi-Runner Engine](#-monaco-web-ide--multi-runner-engine)
5. [IHK-Prüfungstrainer & Simulations-Engine](#-ihk-prüfungstrainer--simulations-engine)
6. [Backend, Sicherheit & Authentifizierung](#-backend-sicherheit--authentifizierung)
7. [Datenbank-Schema & Persistenz](#-datenbank-schema--persistenz)
8. [Setup, Deployment & Betriebsführung](#-setup-deployment--betriebsführung)
9. [REST-API Dokumentation](#-rest-api-dokumentation)
10. [Rollen- & Berechtigungskonzept](#-rollen--berechtigungskonzept)

---

## 💡 Überblick & Vision

Das **IT-Praxisportal** schließt die Lücke zwischen theoretischem Berufsschulunterricht und den realen Anforderungen moderner IT-Unternehmen. 

- **Didaktik mit Sofort-Feedback:** Jedes Modul gliedert sich in ein prägnantes Theoriestück, nummerierte Teilziele (Subgoals) und automatisierte Testsuiten, die geschriebenen Code im Sekundentakt auf syntaktische und semantische Korrektheit prüfen.
- **Zero-Install Workflow:** Schüler, Azubis und Umschüler benötigen keinerlei vorkonfigurierte Entwicklungsumgebung. Der Microsoft Monaco Editor (Kern von VS Code) stellt Syntax-Highlighting, Autocomplete und Terminal-Output direkt im Browser zur Verfügung.
- **Offizieller IHK-Prüfungsstandard:** Vollständige Abdeckung der gemeinsamen Kernqualifikationen (Lernfelder 1–8) für die **Abschlussprüfung Teil 1 (AP1)** sowie fachspezifischer Inhalte (LF 9–12) für die **Abschlussprüfung Teil 2 (AP2)** der Fachrichtung Systemintegration nach Ausbildungsordnung AO 2020.
- **100% Datenschutz & DSGVO:** Vollständiger Verzicht auf externe Tracking-Skripte oder US-Cloud-Abhängigkeiten. Gehostet auf dedizierten Servern in Deutschland.

---

## 🏛️ Systemarchitektur & Komponenten

Das Projekt folgt einer sauberen Trennung zwischen einer statischen, hochperformanten Frontend-Schicht, einem leichtgewichtigen Multi-Threaded Python REST-Backend und einem Caddy Reverse Proxy mit automatischem TLS.

```
                    ┌────────────────────────────────────────────────────────┐
                    │               Internet / Webbrowser                    │
                    └───────────────────────────┬────────────────────────────┘
                                                │ HTTPS (Port 443 / TLS 1.3)
                                                ▼
┌────────────────────────────────────────────────────────────────────────────────────────────┐
│                               Caddy 2 Reverse Proxy                                       │
│  - HSTS, CSP, SAMEORIGIN, nosniff Security Header                                          │
│  - No-Cache Richtlinien für HTML/JS Kernskripte                                            │
│  - Download-Schutz für .db, .env, .secret_key, Backups & Prüfungen                         │
└───────────────────────────────┬────────────────────────────┬───────────────────────────────┘
                                │                            │
          Statische Assets      │                            │  /api/* REST-Routen
         (HTML, CSS, JS, WASM)  │                            │  (Reverse Proxy 127.0.0.1:8008)
                                ▼                            ▼
┌──────────────────────────────────────────────┐ ┌──────────────────────────────────────────┐
│          Statische Plattform                 │ │        Python 3 REST-API Backend         │
│                                              │ │             (server.py)                  │
│ • index.html      (Marketing & Curriculum)   │ │ • Token Auth (HMAC SHA-256)              │
│ • dashboard.html  (Geschützter Kurs-Hub)     │ │ • PBKDF2 Password Hashing                │
│ • workspace.html  (Monaco Web-IDE)           │ │ • IP-basiertes Rate Limiting             │
│ • teacher.html    (Dozenten-Dashboard)       │ │ • Wartungsmodus & System-Settings        │
│ • admin.html      (System-Admin Panel)       │ │ • Multi-Tenancy (Klassenräume)           │
│ • assets/         (CSS, JS, Tools, Pyodide)  │ │ • ThreadingMixIn für hohe Nebenläufigkeit│
│ • courses/        (13 Kursbäume / 216 Module)│ └────────────────────┬─────────────────────┘
└──────────────────────────────────────────────┘                      │
                                                                      │ SQLite3
                                                                      ▼
                                                 ┌──────────────────────────────────────────┐
                                                 │        SQLite3 Datenbank                 │
                                                 │         (platform_data.db)               │
                                                 │ • users, chapter_progress                │
                                                 │ • classrooms, class_enrollments          │
                                                 │ • certificates, platform_settings        │
                                                 │ • audit_log                              │
                                                 └──────────────────────────────────────────┘
```

---

## 📚 Die 13 Fachdisziplinen & Modul-Matrix

Das Portal umfasst insgesamt **216 strukturierte Lerneinheiten**, gegliedert in 4 Schwerpunktbereiche:

| # | Fachdisziplin | ID | Module | Lehrpfade | Runner / Engine | Themenschwerpunkte |
| :-: | :--- | :--- | :-: | :-: | :--- | :--- |
| **01** | **IHK AP1 Prüfungsvorbereitung** | `ihk_ap1` | 12 | 2 | Web-IDE / JS | LF 1–8 Kernqualifikation, Datenschutz/DSGVO, IPv4/IPv6 Subnetting, Trace-Tabellen, SQL-Labor, 90-Min Probeprüfung |
| **02** | **IHK AP2 Systemintegration** | `ihk_ap2_fisi` | 9 | 2 | Web-IDE / JS | LF 9–12 FISI: Routing & VLANs, Active Directory & GPO, Storage/RAID, Cloud/Docker, WiSo-Fragen, 40h-Projektarbeit |
| **03** | **Python 3 Professional** | `python` | 35 | 4 | Pyodide WASM | Variablen, Kontrollfluss, Listen/Dicts, OOP, Vererbung, TDD Unittests, Tkinter Desktop-GUIs, SQLite & REST-APIs |
| **04** | **Linux Bash & Cloud DevOps** | `bash` | 16 | 4 | Bash Test-Runner | Streams, Pipes, Text-Mining (`jq`, `sed`, `awk`), Strict Mode (`set -euo pipefail`), `xargs` Parallelisierung, Docker, BATS Tests |
| **05** | **PowerShell 7+ Core** | `powershell` | 16 | 4 | PS / Pester | Cmdlets, .NET Objekt-Pipeline, `[PSCustomObject]`, Moderne Operatoren, `ForEach-Object -Parallel`, REST-APIs, Pester v5 Unit Tests |
| **06** | **SQL & Datenbank-Architektur** | `sql` | 16 | 4 | SQLite SQL-Runner | 1NF–3NF Normalisierung, Multi-Table JOINs, Subqueries, CTEs (`WITH`), Window Functions (`OVER`), ACID Transaktionen |
| **07** | **JavaScript & TypeScript** | `javascript` | 16 | 4 | Node / Browser-JS | ES6+ Syntax, Klassen & OOP, Async/Await, DOM-Events, LocalStorage, ES-Module, TypeScript Generics & Type Guards |
| **08** | **Java 21+ Enterprise** | `java` | 16 | 4 | JUnit 5 Runner | Strikte Typisierung, Records, OOP-Vererbung, Interfaces, Generics, Streams API, Virtual Threads (Project Loom), JUnit 5 Tests |
| **09** | **Rust Systems & Safety** | `rust` | 16 | 4 | Cargo Testsuite | Ownership- & Borrowing-System, Lifetimes, Option/Result Monaden, Traits, Smart Pointer (`Arc`, `Mutex`), Concurrency, LRU-Cache |
| **10** | **Go Cloud Microservices** | `go` | 16 | 4 | Go Test-Runner | Slices, Maps, Structs, Duck Typing Interfaces, Goroutines, Channels & Select, `net/http` REST Server, Table-Driven Tests |
| **11** | **C# 12 & .NET 8 Enterprise** | `csharp` | 16 | 4 | xUnit Test-Runner | Top-Level Statements, Pattern Matching, Records, LINQ funktionale Abfragen, Async/Await Tasks, xUnit Tests, Order Engine Master |
| **12** | **C & Modernes C++20 Systems** | `cpp` | 16 | 4 | GoogleTest Runner | Pointer & Adressoperatoren, manueller Heap (`malloc`/`free`), RAII-Prinzip, Rule of Five, Templates, Smart Pointer, STL Container |
| **13** | **HTML5, CSS3 & Responsive UI** | `html_css` | 16 | 4 | DOM Assertion | Semantische Tags, Barrierefreiheit (ARIA/A11y), CSS Box-Modell, Flexbox, CSS Grid, Media Queries, Dark Mode Themes |

---

## 💻 Monaco Web-IDE & Multi-Runner Engine

Die Arbeitsumgebung ([`workspace.html`](workspace.html)) ist für produktives, ablenkungsfreies Arbeiten konzipiert:

- **VS Code Monaco Editor:** Vollwertige Editor-Features inklusive Zeilennummern, Syntax-Färbung, Klammerpaar-Highlighting und Shortcuts (`Strg+Enter` zum Ausführen, `Strg+Shift+Enter` für Tests).
- **Split-Screen Ergonomie:** Linke Hälfte für didaktische Aufgabenstellung, Subgoals, Theorie-Spickzettel und gestuftes Tipp-System; rechte Hälfte für Code-Editor und Live-Terminal.
- **Client-Side Python (Pyodide):** Python-Code wird vollständig im Browser via WebAssembly (WASM) ausgeführt – maximale Geschwindigkeit ohne Serverlast.
- **Multi-Language Runners:** Vorbereitete Ausführungspipelines für alle 13 Sprachen mit farbiger Standard-Out- und Standard-Error-Differenzierung.
- **Automatisches Cloud-Save:** Editierter Code wird verzögerungsfrei via Debouncing im Browser und in der Cloud gesichert.

---

## 🎓 IHK-Prüfungstrainer & Simulations-Engine

Im Prüfungsbereich können Auszubildende ihr Wissen unter echten Prüfungsbedingungen testen:

- **90-Minuten Countdown:** Realistische Zeiteinteilung wie in der IHK-Abschlussprüfung.
- **Offizieller IHK-Notenschlüssel:** Automatische Berechnung von Prozentwerten, Punkten (max. 100) und IHK-Noten (1 bis 6) gemäß Prüfungsstandard.
- **Subnetting-Drill Generator:** Unendlicher Aufgabenpool für IPv4- und IPv6-Berechnungen (Netz-ID, Broadcast, erste/letzte nutzbare Hostadresse, Binär- und CIDR-Masken).
- **Trace-Tabellen Simulator:** Schrittweise Ausführung von Pseudocode- und Struktogramm-Logiken mit Überprüfung von Variablenzuständen.

---

## 🛡️ Backend, Sicherheit & Authentifizierung

Das Backend ([`server.py`](server.py)) ist auf maximale Zuverlässigkeit, Wartungsfreundlichkeit und Sicherheit gehärtet:

- **HMAC-SHA256 Token Sessions:** Zustandsloses, kryptografisch signiertes Sitzungsformat mit 12-stündiger Gültigkeit (`exp`) und Timing-Safe Verifikation (`hmac.compare_digest`).
- **Passwort-Sicherheit:** Passwörter werden mit `PBKDF2-HMAC-SHA256` unter Verwendung von 100.000 Iterationen und individuellem 16-Byte kryptografischem Salz gespeichert.
- **Schutz vor Brute-Force:** In-Memory Rate-Limiter beschränkt fehlgeschlagene Anmelde- und Registrierungsversuche pro IP-Adresse.
- **Reverse-Proxy Trusted IP Check:** Authentifizierungs- und Schutzmechanismen prüfen `X-Real-IP` und `X-Forwarded-For` ausschließlich dann, wenn die Verbindung von einem vertrauenswürdigen lokalen Reverse-Proxy (`127.0.0.1`, `::1`, Docker-Bridge `172.16.0.0/12`) stammt.
- **Wartungsmodus (Maintenance Mode):** Per Klick im Admin-Panel aktivierbar. Nicht-Admins erhalten HTTP 503 und einen bildschirmfüllenden Wartungsscreen; Administratoren behalten uneingeschränkten Zugriff für Deployments.

---

## 🗄️ Datenbank-Schema & Persistenz

Alle Anwendungsdaten werden in einer relationalen SQLite-Datenbank (`platform_data.db`) mit Foreign-Key-Unterstützung und Indizes verwaltet:

```sql
-- 1. Benutzer & Rollen
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    salt TEXT NOT NULL,
    name TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'student',  -- 'admin', 'teacher', 'student', 'solo'
    xp INTEGER NOT NULL DEFAULT 0,
    level INTEGER NOT NULL DEFAULT 1,
    streak_days INTEGER NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Kapitel-Fortschritt
CREATE TABLE IF NOT EXISTS chapter_progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    chapter_id TEXT NOT NULL,
    code_draft TEXT,
    subgoals_json TEXT,
    is_solved BOOLEAN NOT NULL DEFAULT 0,
    solved_at TIMESTAMP,
    UNIQUE(user_id, chapter_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- 3. Klassenräume & Einschreibungen
CREATE TABLE IF NOT EXISTS classrooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    invite_code TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (teacher_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS class_enrollments (
    classroom_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (classroom_id, user_id),
    FOREIGN KEY (classroom_id) REFERENCES classrooms(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- 4. Verifizierbare Zertifikate
CREATE TABLE IF NOT EXISTS certificates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    uuid TEXT UNIQUE NOT NULL,
    user_id INTEGER NOT NULL,
    track_id TEXT NOT NULL,
    student_name TEXT NOT NULL,
    issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- 5. Globale Plattform-Einstellungen & Wartung
CREATE TABLE IF NOT EXISTS platform_settings (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 6. Revisionssicheres Audit-Log
CREATE TABLE IF NOT EXISTS audit_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    action TEXT NOT NULL,
    details TEXT,
    ip_address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🚀 Setup, Deployment & Betriebsführung

### 1. Lokale Entwicklung

```bash
# Repository klonen
git clone ssh://git@git.alex-mueller.biz:2222/alex-mueller/it-praxisportal.git
cd it-praxisportal

# Server starten
python3 server.py
# Server läuft auf http://localhost:8008
```

### 2. Systemd Service (Production)

Der API-Server wird über einen systemd-Dienst im Hintergrund betrieben:

```ini
# /etc/systemd/system/it-praxisportal-backend.service
[Unit]
Description=IT-Praxisportal API Backend Server
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/uebungen_python
ExecStart=/usr/bin/python3 /root/uebungen_python/server.py
Restart=always
RestartSec=3
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

Service steuern:
```bash
systemctl daemon-reload
systemctl restart it-praxisportal-backend.service
systemctl status it-praxisportal-backend.service
```

### 3. Caddy Reverse Proxy Konfiguration

```caddy
alpha.it-praxisportal.de {
    encode gzip zstd

    # Sicherheits-Header
    header {
        X-Frame-Options "SAMEORIGIN"
        X-Content-Type-Options "nosniff"
        Referrer-Policy "strict-origin-when-cross-origin"
        Permissions-Policy "camera=(), microphone=(), geolocation=()"
        Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
    }

    # Frische-Garantie für Plattform-Skripte & HTML
    @noCache {
        path / /index.html *.html /assets/app_auth.js /assets/course_sidebar.js /assets/courses_manifest.js
    }
    header @noCache Cache-Control "no-cache, no-store, must-revalidate"

    # Backend REST API
    handle /api/* {
        reverse_proxy 172.17.0.1:8008 {
            header_up Host {host}
            header_up X-Real-IP {remote_host}
        }
    }

    # Schutz für vertrauliche Dateien
    @forbidden {
        path *.db *.sqlite* *.secret_key .git* *.py *.sh *.php *.sql *.env* *.bak *.log /exams/*
    }
    handle @forbidden {
        respond "Access denied" 403
    }

    # Statische Plattform-Auslieferung
    handle {
        root * /srv/it-praxisportal
        file_server
    }
}
```

---

## 📡 REST-API Dokumentation

| Methode | Pfad | Authentifizierung | Beschreibung |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/platform/status` | Öffentlich | Liefert Wartungsstatus, Ankündigungen & Registrierungs-Flag |
| `POST` | `/api/auth/register` | Öffentlich | Registriert einen neuen Nutzer (`email`, `password`, `name`, `role`) |
| `POST` | `/api/auth/login` | Öffentlich | Meldet Nutzer an und liefert HMAC-Bearer-Token |
| `GET` | `/api/auth/me` | Bearer Token | Liefert Profildaten des angemeldeten Nutzers |
| `GET` | `/api/progress/get` | Bearer Token | Liefert gelöste Kapitel und optional Code-Drafts |
| `POST` | `/api/progress/save` | Bearer Token | Speichert Code-Entwurf und Teilziele für ein Modul |
| `POST` | `/api/progress/solve` | Bearer Token | Markiert Modul als gelöst und vergibt XP/Level-Aufstieg |
| `GET` | `/api/classrooms/list` | Bearer Token | Listet Klassenräume (für Schüler oder Dozenten) |
| `POST` | `/api/classrooms/create`| Dozent / Admin | Erstellt neuen Klassenraum mit individuellem Einladungscode |
| `POST` | `/api/classrooms/join` | Schüler | Tritt einer Schulklasse via Invite-Code bei |
| `GET` | `/api/classrooms/matrix`| Dozent / Admin | Liefert Live-Fortschrittsmatrix aller Schüler einer Klasse |
| `POST` | `/api/certificates/create`| Bearer Token | Generiert verifizierbare Zertifikats-UUID |
| `GET` | `/api/admin/stats` | Admin | Liefert System-KPIs, Benutzerzahlen und Aktivitätsmetriken |
| `GET` | `/api/admin/users` | Admin | Listet registrierte Benutzer mit Filter und Paginierung |
| `POST` | `/api/admin/users/role` | Admin | Ändert Benutzerrolle (`student`, `teacher`, `admin`) |
| `POST` | `/api/admin/users/reset-password` | Admin | Setzt Benutzerpasswort administrativ zurück |
| `POST` | `/api/admin/users/delete` | Admin | Löscht Benutzerkonto und zugehörige Daten |
| `POST` | `/api/admin/settings` | Admin | Ändert Plattform-Einstellungen (Wartungsmodus, Banner etc.) |

---

## 👥 Rollen- & Berechtigungskonzept

1. **Gast / Unangemeldeter Besucher:**
   - Sieht die Marketing-Landingpage ([`index.html`](index.html)) mit vollständiger Curriculum-Auflistung.
   - Kann keine Module in der Web-IDE starten (erhält Registrierungs-Modal).
2. **Schüler / Auszubildender (`student` / `solo`):**
   - Hat vollen Zugriff auf den Lernbereich ([`dashboard.html`](dashboard.html)), alle 13 Kurse, 216 Module und die Web-IDE ([`workspace.html`](workspace.html)).
   - Kann Klassenräumen beitreten, Lernfortschritte synchronisieren und Zertifikate ausstellen.
3. **Dozent / Ausbilder (`teacher`):**
   - Beinhaltet alle Schülerrechte.
   - Hat Zugriff auf das Dozenten-Dashboard ([`teacher.html`](teacher.html)).
   - Kann Klassenräume erstellen, Einladungscodes vergeben und die Live-Lernmatrix der Klassenmitglieder einsehen.
4. **Administrator (`admin`):**
   - Beinhaltet alle Schüler- und Dozentenrechte.
   - Hat exklusiven Zugriff auf das Admin Control Panel ([`admin.html`](admin.html)).
   - Kann globale Plattform-Parameter (Wartungsmodus, Ankündigungen) konfigurieren, Benutzer verwalten, Passwörter zurücksetzen und das Audit-Log einsehen.
   - Hat auch bei aktivem Wartungsmodus vollen Zugriff auf alle Schnittstellen.

---

## 📄 Lizenz & Autoren

- **Entwickler & Maintainer:** Alexander Müller ([alex-mueller.biz](https://alex-mueller.biz))
- **Plattform-Domain:** [alpha.it-praxisportal.de](https://alpha.it-praxisportal.de/)
- **Git-Repository:** [git.alex-mueller.biz/alex-mueller/it-praxisportal](https://git.alex-mueller.biz/alex-mueller/it-praxisportal)
- **Version:** 1.0 Alpha • 2026
