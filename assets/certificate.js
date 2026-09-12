/**
 * 🎓 OFFIZIELLES LEISTUNGS-ZERTIFIKAT 🎓
 * =======================================
 * Generiert ein ausdruckbares Abschlusszertifikat nach Abschluss eines Lehrpfads.
 */

(function () {
  function escapeHtml(text) {
    if (!text) return "";
    return String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  window.zeigeZertifikatModal = async function (lehrpfadNummer) {
    const data = window.GAMIFICATION_DATA || { spieler_name: "Python-Entwickler", level: 1 };
    const user = window.AUTH ? window.AUTH.user : null;
    const studentName = (user && user.name) ? user.name : (data.spieler_name || "Python-Entwickler");
    const dateStr = new Date().toLocaleDateString("de-DE", { day: "2-digit", month: "long", year: "numeric" });
    
    let titel = "Grundlagen der Python-Programmierung";
    let moduleDesc = "10 Module: Zahlen & Rechnen, Datentypen, f-Strings, Kontrollstrukturen, Funktionen, Listen, Strings, Dictionaries, Sets & Comprehensions";
    let trackKey = "lehrpfad_1";

    if (lehrpfadNummer === 2 || lehrpfadNummer === "lehrpfad_2") {
      titel = "Einstieg in die Objektorientierung (OOP) & Entwickler-Tools";
      moduleDesc = "9 Module: Klassen, Konstruktor __init__, self, Methoden, UML-Diagramme, VS Code, Git-Versionskontrolle, Komposition & Tamagotchi-Projekt";
      trackKey = "lehrpfad_2";
    } else if (lehrpfadNummer === 3 || lehrpfadNummer === "lehrpfad_3") {
      titel = "Fortgeschrittenes OOP, Softwarequalität & Desktop-GUIs";
      moduleDesc = "10 Module: Speicher-Referenzen, Dunder-Methoden, TDD Unit Testing, Vererbung, Polymorphie, Exceptions, JSON-Persistenz, Tkinter GUIs, Container & Masterprojekt";
      trackKey = "lehrpfad_3";
    } else if (lehrpfadNummer === 4 || lehrpfadNummer === "lehrpfad_4") {
      titel = "Python Professional & Data Engineering";
      moduleDesc = "6 Master-Module: Reguläre Ausdrücke (re), Functional Programming (lambda, zip, map), Generatoren & itertools, Dataclasses & Type Hints, Relationale DBs mit SQLite, REST-APIs & JSON-Feeds";
      trackKey = "lehrpfad_4";
    } else if (lehrpfadNummer === "js_grundlagen") {
      titel = "JavaScript Grundlagen, Kontrollfluss & ES6";
      moduleDesc = "5 Module: Variablen (let/const), Verzweigungen & Schleifen, Funktionen & Closures, Arrays/Sets/Maps und Objekte & Destructuring";
      trackKey = "js_grundlagen";
    } else if (lehrpfadNummer === "js_oop") {
      titel = "Moderne ES6+ Datenmodelle, OOP & Robustes Debugging";
      moduleDesc = "3 Module: ES6-Klassen & Vererbung, Reguläre Ausdrücke (RegExp) & strukturierte Fehlerbehandlung mit Error-Klassen";
      trackKey = "js_oop";
    } else if (lehrpfadNummer === "js_async") {
      titel = "Web-APIs, DOM-Manipulation & Asynchrones JavaScript";
      moduleDesc = "4 Module: DOM Event-Delegation, Web Storage API (LocalStorage), Promises/Chaining und Async/Await mit Fetch";
      trackKey = "js_async";
    } else if (lehrpfadNummer === "js_master") {
      titel = "Master of Modern JavaScript & TypeScript Engineering";
      moduleDesc = "Vollständiger Abschluss des JS/TS Curriculums (16 Module, ES-Module, TypeScript Interfaces/Generics & MVC Task-App)";
      trackKey = "js_master";
    } else if (lehrpfadNummer === "bash_grundlagen") {
      titel = "Linux Terminal Mastery & Core Unix Tools";
      moduleDesc = "4 Module: Navigation, Globbing, I/O Streams, Pipes & Redirection, Umgebungsvariablen, Dateirechte und Job Control";
      trackKey = "bash_grundlagen";
    } else if (lehrpfadNummer === "bash_scripting") {
      titel = "Professionelles Bash-Scripting & Text-Mining";
      moduleDesc = "4 Module: Kontrollfluss, Assoziative Arrays, grep, sed, awk, jq und Unofficial Strict Mode (set -euo pipefail)";
      trackKey = "bash_scripting";
    } else if (lehrpfadNummer === "bash_performance") {
      titel = "High-Performance Bash, Parallelisierung & Netzwerke";
      moduleDesc = "4 Module: Multithreading mit xargs -P & parallel, Prozess-Substitution, REST-Pipelines mit curl und Systemd Automation";
      trackKey = "bash_performance";
    } else if (lehrpfadNummer === "bash_master") {
      titel = "Master of Linux Shell & Cloud DevOps Engineering";
      moduleDesc = "Vollständiger Abschluss des Linux Bash Curriculums (16 Module, Docker Lifecycle, CI/CD Pipelines, BATS Testing & DevOps Suite)";
      trackKey = "bash_master";
    } else if (lehrpfadNummer === "ps_grundlagen") {
      titel = "PowerShell 7+ Essentials & Objekt-Pipeline";
      moduleDesc = "4 Module: Cmdlet-Architektur, .NET-Objekt-Pipeline, Where-Object Filterung, Select-Object Projektion und PSCustomObjects";
      trackKey = "ps_grundlagen";
    } else if (lehrpfadNummer === "ps_scripting") {
      titel = "PowerShell Scripting, Kontrollfluss & Error-Handling";
      moduleDesc = "4 Module: Moderne PS7 Operatoren (Ternary/Null-Coalescing), Schleifen, Cmdlets mit [CmdletBinding()] und Try/Catch";
      trackKey = "ps_scripting";
    } else if (lehrpfadNummer === "ps_performance") {
      titel = "PowerShell Parallelisierung, REST-APIs & SecretManagement";
      moduleDesc = "4 Module: ForEach-Object -Parallel, Start-ThreadJob, Invoke-RestMethod, JSON-Pipelines, PSDrives und SecretManagement";
      trackKey = "ps_performance";
    } else if (lehrpfadNummer === "ps_master") {
      titel = "Master of Modern PowerShell & Cloud Automation";
      moduleDesc = "Vollständiger Abschluss des PowerShell Curriculums (16 Module, Modul-Manifeste .psd1, Pester v5 Testing & Cloud Ops Engine)";
      trackKey = "ps_master";
    } else if (lehrpfadNummer === "sql_grundlagen") {
      titel = "SQL Grundlagen & Relationale CRUD-Operationen";
      moduleDesc = "4 Module: CREATE TABLE, Primary Keys, Datentypen, Constraints, INSERT, SELECT, UPDATE & DELETE";
      trackKey = "sql_grundlagen";
    } else if (lehrpfadNummer === "sql_joins") {
      titel = "Relationale Joins & Datenbank-Design";
      moduleDesc = "4 Module: Foreign Keys, INNER/LEFT/RIGHT/FULL JOINs, Normalisierung (1NF bis 3NF) & n:m Junction Tables";
      trackKey = "sql_joins";
    } else if (lehrpfadNummer === "sql_analytics") {
      titel = "SQL Analytics, CTEs & Window Functions";
      moduleDesc = "4 Module: GROUP BY, HAVING, Subqueries, Common Table Expressions (WITH ...) & Window Functions (ROW_NUMBER, OVER)";
      trackKey = "sql_analytics";
    } else if (lehrpfadNummer === "sql_master") {
      titel = "Master of SQL, Data Analytics & Database Engineering";
      moduleDesc = "Vollständiger Abschluss des SQL Curriculums (16 Module, B-Tree Indizes, ACID Transaktionen, Views & Data Warehouse Master)";
      trackKey = "sql_master";
    } else if (lehrpfadNummer === "html_grundlagen") {
      titel = "Semantisches HTML5 & Barrierefreie Web-Struktur";
      moduleDesc = "4 Module: HTML5 Semantik, Dokumentstruktur, Formulare, Validierung & Accessibility (A11y/ARIA)";
      trackKey = "html_grundlagen";
    } else if (lehrpfadNummer === "css_styling") {
      titel = "Modern CSS3 Styling & Box Model Engineering";
      moduleDesc = "4 Module: Spezifität, Kaskade, CSS Box Model, Custom Properties (CSS-Variablen) & Responsive Typografie";
      trackKey = "css_styling";
    } else if (lehrpfadNummer === "css_responsive") {
      titel = "Modern CSS Layouts: Flexbox, Grid & Animationen";
      moduleDesc = "4 Module: Flexbox 1D-Layouts, CSS Grid 2D-Matrix, Media Queries (@media) & Keyframe-Animationen";
      trackKey = "css_responsive";
    } else if (lehrpfadNummer === "html_css_master") {
      titel = "Master of Modern HTML5, CSS3 & Responsive UI Design";
      moduleDesc = "Vollständiger Abschluss des HTML/CSS Curriculums (16 Module, BEM, Dark/Light Themes & SaaS Landingpage Master)";
      trackKey = "html_css_master";
    } else if (lehrpfadNummer === "go_grundlagen") {
      titel = "Go Syntax, Typensystem & Kontrollfluss";
      moduleDesc = "4 Module: Variablen, Datentypen, Slices, Maps, Arrays, Schleifen und Verzweigungen";
      trackKey = "go_grundlagen";
    } else if (lehrpfadNummer === "go_oop") {
      titel = "Idiomatisches Go: Structs, Interfaces & Error Handling";
      moduleDesc = "4 Module: Structs, Pointer-Receiver-Methoden, Interfaces (Duck Typing) & Explizites Error-Handling (if err != nil)";
      trackKey = "go_oop";
    } else if (lehrpfadNummer === "go_concurrency") {
      titel = "Go Concurrency: Goroutines, Channels & Synchronisation";
      moduleDesc = "4 Module: Goroutines (go worker), Buffered Channels, select-Multiplexing, sync.WaitGroup & Mutexes";
      trackKey = "go_concurrency";
    } else if (lehrpfadNummer === "go_master") {
      titel = "Master of Go (Golang) Cloud Microservices & Systems Engineering";
      moduleDesc = "Vollständiger Abschluss des Go Curriculums (16 Module, net/http REST APIs, Middleware, Testing & Cloud API Master)";
      trackKey = "go_master";
    } else if (lehrpfadNummer === "java_grundlagen") {
      titel = "Java Syntax, Primitive Typen & Kontrollfluss";
      moduleDesc = "4 Module: Primitive Typen, main(), switch-Expressions (->), Arrays und Methodenüberladung";
      trackKey = "java_grundlagen";
    } else if (lehrpfadNummer === "java_oop") {
      titel = "Reine Objektorientierung & Kapselung in Java";
      moduleDesc = "4 Module: Klassen, Konstruktor-Chaining, Kapselung, Immutability, Records, Vererbung & Interfaces";
      trackKey = "java_oop";
    } else if (lehrpfadNummer === "java_streams") {
      titel = "Java Generics, Collections & Modern Streams API";
      moduleDesc = "4 Module: List/Set/Map, Bounded Generics, Checked Exceptions, try-with-resources, Streams API & Optional";
      trackKey = "java_streams";
    } else if (lehrpfadNummer === "java_master") {
      titel = "Master of Java 21+ Enterprise & Banking Systems";
      moduleDesc = "Vollständiger Abschluss des Java Curriculums (16 Module, NIO.2, Virtual Threads Loom, JUnit 5 & Banking Core Master)";
      trackKey = "java_master";
    } else if (lehrpfadNummer === "rust_grundlagen") {
      titel = "Rust Syntax, Ownership & Borrowing System";
      moduleDesc = "4 Module: Mutabilität, Move-Semantik, Stack vs. Heap, Referenzen &mut, Slices und Pattern Matching";
      trackKey = "rust_grundlagen";
    } else if (lehrpfadNummer === "rust_structs") {
      titel = "Rust Structs, Enums & Robust Error-Handling";
      moduleDesc = "4 Module: Structs, impl-Methoden, Option<T>, Result<T, E> mit ?-Operator und Cargo Multi-File Modules";
      trackKey = "rust_structs";
    } else if (lehrpfadNummer === "rust_traits") {
      titel = "Rust Traits, Generics & Smart Pointer";
      moduleDesc = "4 Module: Traits, Trait Bounds, Monomorphisierung, Closures, Iterator-Adapter, Box, Rc und RefCell";
      trackKey = "rust_traits";
    } else if (lehrpfadNummer === "rust_master") {
      titel = "Master of Rust Systems Programming & WebAssembly";
      moduleDesc = "Vollständiger Abschluss des Rust Curriculums (16 Module, Fearless Concurrency, Arc/Mutex, Cargo Test & In-Memory LRU Cache Master)";
      trackKey = "rust_master";
    } else if (lehrpfadNummer === "csharp_grundlagen") {
      titel = "C# 12 Syntax, Datentypen & Top-Level Statements";
      moduleDesc = "4 Module: Top-Level Statements, Nullable Reference Types, Switch Expressions, Collections und Tupel";
      trackKey = "csharp_grundlagen";
    } else if (lehrpfadNummer === "csharp_oop") {
      titel = "Modernes C# OOP, Records & Dependency Injection";
      moduleDesc = "4 Module: Primary Constructors, Records mit with-Expressions, Polymorphismus & Interfaces";
      trackKey = "csharp_oop";
    } else if (lehrpfadNummer === "csharp_linq") {
      titel = "C# LINQ, Generics & Asynchrone Task Pipelines";
      moduleDesc = "4 Module: LINQ (.Where/.Select/.GroupBy), Generic Constraints, async/await Tasks und using-Disposal";
      trackKey = "csharp_linq";
    } else if (lehrpfadNummer === "csharp_master") {
      titel = "Master of C# 12 & Modern .NET 8+ Enterprise Cloud";
      moduleDesc = "Vollständiger Abschluss des C# Curriculums (16 Module, System.Text.Json, Events/Delegates, xUnit & Order Engine Master)";
      trackKey = "csharp_master";
    } else if (lehrpfadNummer === "cpp_c_grundlagen") {
      titel = "C Fundamente & Manuelles Memory Management";
      moduleDesc = "4 Module: Pointer, Adressoperatoren (&/*), Pointer-Arithmetik, Stack vs. Heap, malloc/free & Header-Dateien";
      trackKey = "cpp_c_grundlagen";
    } else if (lehrpfadNummer === "cpp_oop") {
      titel = "Modern C++ Einstieg, RAII & Objektorientierung";
      moduleDesc = "4 Module: std::cout, Referenzen, Klassen, Konstruktoren, RAII-Prinzip, virtual Methoden & Operator-Overloading";
      trackKey = "cpp_oop";
    } else if (lehrpfadNummer === "cpp_modern") {
      titel = "Modern C++20: Smart Pointer, Templates & STL";
      moduleDesc = "4 Module: Templates, std::unique_ptr / shared_ptr, STL-Container (vector/map), Algorithmen & Lambdas";
      trackKey = "cpp_modern";
    } else if (lehrpfadNummer === "cpp_master") {
      titel = "Master of C & Modern C++20 Systems Engineering";
      moduleDesc = "Vollständiger Abschluss des C/C++ Curriculums (16 Module, std::thread/mutex, GoogleTest & 2D Physics Simulation Master)";
      trackKey = "cpp_master";
    } else if (lehrpfadNummer === "ihk_ap1_systeme") {
      titel = "IHK AP1: IT-Systeme, Netzwerke & Sicherheit (LF 2–4)";
      moduleDesc = "4 Module: Hardware, Schnittstellen, Ergonomie, IPv4/IPv6 Subnetting, CIA-Schutzziele & DSGVO/TOMs";
      trackKey = "ihk_ap1_systeme";
    } else if (lehrpfadNummer === "ihk_ap1_programmierung") {
      titel = "IHK AP1: Programmierung, UML & SQL-Datenbanken (LF 5)";
      moduleDesc = "4 Module: Struktogramme (DIN 66261), PAP (DIN 66001), Trace-Tabellen, OOP-Klassendiagramme & SQL";
      trackKey = "ihk_ap1_programmierung";
    } else if (lehrpfadNummer === "ihk_ap1_prozesse") {
      titel = "IHK AP1: Service (ITIL), IoT & Geschäftsprozesse (LF 6–8)";
      moduleDesc = "3 Module: ITIL Incident/Problem Management, Cyber-physische Systeme / IoT & BPMN/EPK Modellierung";
      trackKey = "ihk_ap1_prozesse";
    } else if (lehrpfadNummer === "ihk_ap1_master") {
      titel = "Zertifikat: IHK Abschlussprüfung Teil 1 (AP1) Meister";
      moduleDesc = "Vollständiger Abschluss der IHK AP1 Prüfungsvorbereitung (12 Module inkl. 90-Minuten Probeprüfung)";
      trackKey = "ihk_ap1_master";
    } else if (lehrpfadNummer === "ihk_ap2_netzwerke") {
      titel = "IHK AP2: Enterprise Netzwerke & Serverdienste (LF 9 & 10)";
      moduleDesc = "3 Module: VLANs (802.1Q), LACP, Spanning Tree, OSPF-Routing, Active Directory & PowerShell-Automation";
      trackKey = "ihk_ap2_netzwerke";
    } else if (lehrpfadNummer === "ihk_ap2_sicherheit") {
      titel = "IHK AP2: Storage, Hochverfügbarkeit & IT-Sicherheit (LF 11)";
      moduleDesc = "3 Module: RAID-Simulator (0/1/5/6/10), SAN/NAS, BSI IT-Grundschutz, DMZ-Firewalls & IPsec-VPN";
      trackKey = "ihk_ap2_sicherheit";
    } else if (lehrpfadNummer === "ihk_ap2_wiso_projekt") {
      titel = "IHK AP2: Virtualisierung, WiSo & 40h-Projektarbeit (LF 12)";
      moduleDesc = "3 Module: Hypervisor Typ 1 vs. 2, Docker-Container, WiSo-Arbeitsrecht & 40h-Projektarbeits-Leitfaden";
      trackKey = "ihk_ap2_wiso_projekt";
    } else if (lehrpfadNummer === "ihk_ap2_fisi_master") {
      titel = "Zertifikat: IHK Abschlussprüfung Teil 2 (AP2 FISI) Meister";
      moduleDesc = "Vollständiger Abschluss der IHK AP2 Fachinformatiker Systemintegration (12 Module inkl. 3 Probeprüfungen)";
      trackKey = "ihk_ap2_fisi_master";
    } else if (lehrpfadNummer === "git_basics") {
      titel = "Git Grundlagen & Lokale Repositories";
      moduleDesc = "4 Module: Initialisierung, 3-Bereiche-Architektur, Staging, atomare Commits, Diff & .gitignore";
      trackKey = "git_basics";
    } else if (lehrpfadNummer === "git_branching") {
      titel = "Git Branching, Fast-Forward & Merge-Konflikte";
      moduleDesc = "4 Module: Feature-Branches, Fast-Forward vs 3-Way Merge, Konfliktbehandlung & Git Stash";
      trackKey = "git_branching";
    } else if (lehrpfadNummer === "git_collaboration") {
      titel = "Git Remotes, Upstream & Team-Collaboration";
      moduleDesc = "4 Module: Remote Tracking, Git Fetch vs Pull, SemVer Tags & Cherry-Picking";
      trackKey = "git_collaboration";
    } else if (lehrpfadNummer === "git_master") {
      titel = "Master of Git Version Control & DevOps Workflows";
      moduleDesc = "Vollständiger Abschluss des Git Curriculums (16 Module, Rebase -i, Pre-Commit Hooks & Git-Flow Release Master)";
      trackKey = "git_master";
    } else if (lehrpfadNummer === "ad_architektur") {
      titel = "Active Directory Architektur, OUs & FSMO";
      moduleDesc = "4 Module: Gesamtstruktur & Domänen, die 5 FSMO-Rollen, OU-Design & AD Sites/Replikation";
      trackKey = "ad_architektur";
    } else if (lehrpfadNummer === "ad_identity") {
      titel = "Active Directory Identitätsmanagement & AGDLP";
      moduleDesc = "4 Module: Benutzerkonten, Maschinenkonten, Gruppenbereiche & saubere Rechtevergabe nach AGDLP";
      trackKey = "ad_identity";
    } else if (lehrpfadNummer === "ad_gpo") {
      titel = "Active Directory Gruppenrichtlinien (GPO) Design";
      moduleDesc = "4 Module: LSDOU-Vererbung, Computer vs Benutzer, WMI-Sicherheitsfilter & GPO Troubleshooting (gpresult)";
      trackKey = "ad_gpo";
    } else if (lehrpfadNummer === "ad_master") {
      titel = "Master of Active Directory & Windows Server Administration";
      moduleDesc = "Vollständiger Abschluss des AD Curriculums (16 Module, PowerShell AD Module, CSV-Bulk Provisioning & AD Automation Master)";
      trackKey = "ad_master";
    } else if (lehrpfadNummer === "dns_architektur") {
      titel = "DNS-Architektur, Root-Server & Namensauflösung";
      moduleDesc = "4 Module: DNS-Hierarchie, rekursive/iterative Queries, Port 53 UDP/TCP & TTL-Propagation";
      trackKey = "dns_architektur";
    } else if (lehrpfadNummer === "dns_records_core") {
      titel = "DNS Resource Records & Zonenverwaltung";
      moduleDesc = "4 Module: A/AAAA Records, CNAME Alias & Apex-Problem, SOA-Header & PTR Reverse-Lookups";
      trackKey = "dns_records_core";
    } else if (lehrpfadNummer === "dns_email_security") {
      titel = "DNS E-Mail-Sicherheit & Anti-Spoofing (SPF, DKIM, DMARC)";
      moduleDesc = "4 Module: MX-Prioritäten, SPF TXT-Records, DKIM Kryptosignaturen & DMARC Quarantäne/Reject";
      trackKey = "dns_email_security";
    } else if (lehrpfadNummer === "dns_master") {
      titel = "Master of DNS Records, Domain Security & Infrastructure";
      moduleDesc = "Vollständiger Abschluss des DNS Curriculums (16 Module, SRV Records, DNSSEC Vertrauenskette, dig-Troubleshooting & Zone Auditor)";
      trackKey = "dns_master";
    } else if (lehrpfadNummer === "master") {
      titel = "Grandmaster of Software & Systems Engineering (Polyglot)";
      moduleDesc = "Vollständiger Abschluss aller 16 plattformweiten Curricula (Python, JS/TS, Bash, PowerShell, SQL, HTML/CSS, Go, Java, Rust, C#, C++, AD, Git, DNS & IHK)";
      trackKey = "master";
    }

    let certUuid = "CERT-" + Math.random().toString(36).substring(2, 10).toUpperCase();

    // Registriere Zertifikat im Backend falls angemeldet
    const token = localStorage.getItem("auth_token");
    if (token) {
      try {
        const res = await fetch("/api/certificates/create", {
          method: "POST",
          headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}` },
          body: JSON.stringify({ track_id: trackKey, student_name: studentName })
        });
        const resData = await res.json();
        if (resData.uuid) certUuid = resData.uuid;
      } catch (e) {}
    }

    const modal = document.createElement("div");
    modal.className = "certificate-overlay";
    modal.innerHTML = `
      <div class="certificate-container">
        <div class="certificate-border">
          <div class="certificate-inner">
            <div class="certificate-badge">🎓 OFFIZIELLES ZERTIFIKAT 🎓</div>
            <h1 class="certificate-headline">Erfolgreicher Abschluss</h1>
            <p class="certificate-sub">Hiermit wird bescheinigt, dass</p>
            <div class="certificate-student-name">${escapeHtml(studentName)}</div>
            <p class="certificate-text">den anspruchsvollen Lehrpfad</p>
            <h2 class="certificate-track-title">${escapeHtml(titel)}</h2>
            <p class="certificate-desc">${escapeHtml(moduleDesc)}</p>
            <div class="certificate-meta">
              <div>
                <strong>Erreichtes Level:</strong> Level ${data.level || 1} (${escapeHtml(data.titel || "Entwickler")})
              </div>
              <div>
                <strong>Datum:</strong> ${dateStr}
              </div>
            </div>
            <div style="margin-top: 14px; font-size: 0.72rem; font-family: monospace; color: #64748b;">
              Zertifikats-ID: ${escapeHtml(certUuid)}
            </div>
            <div class="certificate-seal">🏆 EXZELLENZ-SIEGEL</div>
          </div>
        </div>
        <div class="certificate-actions">
          <button onclick="window.print()" class="btn" style="background: var(--success);">🖨️ Zertifikat drucken / Als PDF speichern</button>
          <button onclick="document.querySelector('.certificate-overlay').remove()" class="btn btn-secondary">Schließen</button>
        </div>
      </div>
    `;

    document.body.appendChild(modal);
  };

  // Alias für index.html Buttons
  window.openCertificate = window.zeigeZertifikatModal;
})();
