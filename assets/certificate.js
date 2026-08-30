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
      titel = "SQL & Relationale Datenbanken";
      moduleDesc = "CREATE TABLE, Primary Keys, INSERT, SELECT, Filter mit WHERE und SQLite WebAssembly Abfragen";
      trackKey = "sql_grundlagen";
    } else if (lehrpfadNummer === "master") {
      titel = "Grandmaster of Software & Cloud Engineering (Polyglot)";
      moduleDesc = "Vollständiger Abschluss aller plattformweiten Curricula (Python, JavaScript, TypeScript, Linux Bash, PowerShell & SQL)";
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
