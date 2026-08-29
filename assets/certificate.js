/**
 * 🎓 OFFIZIELLES LEISTUNGS-ZERTIFIKAT 🎓
 * =======================================
 * Generiert ein ausdruckbares Abschlusszertifikat nach Abschluss eines Lehrpfads.
 */

(function () {
  window.zeigeZertifikatModal = function (lehrpfadNummer) {
    const data = window.GAMIFICATION_DATA || { spieler_name: "Python-Entwicklerin", level: 1 };
    const dateStr = new Date().toLocaleDateString("de-DE", { day: "2-digit", month: "long", year: "numeric" });
    
    let titel = "Grundlagen der Python-Programmierung";
    let moduleDesc = "10 Module: Zahlen & Rechnen, Datentypen, f-Strings, Kontrollstrukturen, Funktionen, Listen, Strings, Dictionaries, Sets & Comprehensions";
    
    if (lehrpfadNummer === 2) {
      titel = "Einstieg in die Objektorientierung (OOP) & Entwickler-Tools";
      moduleDesc = "9 Module: Klassen, Konstruktor __init__, self, Methoden, UML-Diagramme, VS Code, Git-Versionskontrolle, Komposition & Tamagotchi-Projekt";
    } else if (lehrpfadNummer === 3) {
      titel = "Fortgeschrittenes OOP, Softwarequalität & Desktop-GUIs";
      moduleDesc = "10 Module: Speicher-Referenzen, Dunder-Methoden, TDD Unit Testing, Vererbung, Polymorphie, Exceptions, JSON-Persistenz, Tkinter GUIs, Container & Masterprojekt";
    } else if (lehrpfadNummer === "master") {
      titel = "Master of Python Software Engineering";
      moduleDesc = "Vollständiger Abschluss aller 3 Lehrpfade (27 Module, 188 bestandene automatisierte Unittests, Model-View-Controller Desktop-App)";
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
            <div class="certificate-student-name">${data.spieler_name || "Python-Entwicklerin"}</div>
            <p class="certificate-text">den anspruchsvollen Lehrpfad</p>
            <h2 class="certificate-track-title">${titel}</h2>
            <p class="certificate-desc">${moduleDesc}</p>
            <div class="certificate-meta">
              <div>
                <strong>Erreichtes Level:</strong> Level ${data.level || 1} (${data.titel || "Entwicklerin"})
              </div>
              <div>
                <strong>Datum:</strong> ${dateStr}
              </div>
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
})();
