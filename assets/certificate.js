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
    } else if (lehrpfadNummer === "master") {
      titel = "Master of Python Software Engineering";
      moduleDesc = "Vollständiger Abschluss aller 3 Lehrpfade (27 Module, 188 bestandene automatisierte Unittests, Model-View-Controller Desktop-App)";
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
