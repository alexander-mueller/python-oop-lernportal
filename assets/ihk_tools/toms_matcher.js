/**
 * 🛡️ IHK DSGVO & TOMS-KLASSIFIZIERER 🛡️
 * =====================================
 * Interaktiver Zuordnungs-Trainer für AP1 (LF 1 & LF 4) & AP2 (LF 11):
 * - Die 8 klassischen technisch-organisatorischen Maßnahmen (BDSG / DSGVO)
 * - Fallstudien & Praxisbeispiele mit Sofort-Feedback
 */

class TomsMatcher {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    this.categories = [
      { id: "zutritt", name: "1. Zutrittskontrolle (Räume/Gebäude)" },
      { id: "zugang", name: "2. Zugangskontrolle (Systemanmeldung)" },
      { id: "zugriff", name: "3. Zugriffskontrolle (Berechtigungen auf Daten)" },
      { id: "weitergabe", name: "4. Weitergabekontrolle (Transport & Übertragung)" },
      { id: "eingabe", name: "5. Eingabekontrolle (Protokollierung & Audit)" },
      { id: "auftrag", name: "6. Auftragskontrolle (AVV & Weisung)" },
      { id: "verfuegbarkeit", name: "7. Verfügbarkeitskontrolle (Backups & USV)" },
      { id: "trennung", name: "8. Trennungskontrolle (Zweckbindung & Testdaten)" }
    ];

    this.scenarios = [
      { text: "Serverraumtür mit elektronischem RFID-Chip und Vereinzelungsschleuse", target: "zutritt" },
      { text: "Erzwingen von Multi-Faktor-Authentifizierung (MFA) für alle Windows-Logins", target: "zugang" },
      { text: "Vergabe von NTFS-Rechten nach dem Least-Privilege-Prinzip auf Abteilungsordner", target: "zugriff" },
      { text: "Ende-zu-Ende-Verschlüsselung von E-Mails via S/MIME und TLS-Tunnel", target: "weitergabe" },
      { text: "Zentrales SIEM-Logfile protokolliert das Ändern und Löschen von Kundendatensätzen", target: "eingabe" },
      { text: "Abschluss eines Auftragsverarbeitungsvertrages (AVV) mit einem Cloud-Hosting-Dienstleister", target: "auftrag" },
      { text: "Installation einer USV-Anlage und tägliche Auslagerung von Backups in ein zweites Brandabteil", target: "verfuegbarkeit" },
      { text: "Strikte Trennung von Entwicklungs-, Test- und Produktivsystemen", target: "trennung" }
    ];

    this.init();
  }

  init() {
    if (!this.container) return;
    this.render();
  }

  render() {
    this.container.innerHTML = `
      <div class="ihk-tool-card">
        <div class="ihk-tool-header">
          <div class="ihk-tool-title">
            <span>🛡️</span> IHK DSGVO & TOMs-Klassifizierer (LF 4 & LF 11)
          </div>
          <div>
            <span class="ihk-badge">8 IHK-Kernkategorien</span>
          </div>
        </div>

        <p style="color: #94a3b8; font-size: 0.9rem; margin-top: 0;">
          Ordne die folgenden 8 typischen IHK-Praxismaßnahmen der jeweils exakt zutreffenden technisch-organisatorischen Maßnahme (TOM) zu:
        </p>

        <div style="display: flex; flex-direction: column; gap: 12px; margin-bottom: 20px;">
          ${this.scenarios.map((s, idx) => `
            <div style="background: #0f172a; padding: 12px 16px; border-radius: 8px; border: 1px solid #334155; display: flex; align-items: center; justify-content: space-between; gap: 16px; flex-wrap: wrap;">
              <div style="flex: 1; font-size: 0.95rem; color: #f8fafc;">
                <strong>Fall ${idx + 1}:</strong> ${s.text}
              </div>
              <div style="width: 280px;">
                <select class="ihk-select tom-select" data-idx="${idx}">
                  <option value="">-- Maßnahme wählen --</option>
                  ${this.categories.map(c => `<option value="${c.id}">${c.name}</option>`).join('')}
                </select>
              </div>
            </div>
          `).join('')}
        </div>

        <div style="display: flex; gap: 12px;">
          <button class="ihk-btn ihk-btn-success" id="btn-check-toms">✓ Zuordnungen prüfen</button>
          <button class="ihk-btn ihk-btn-secondary" id="btn-reset-toms">Zurücksetzen</button>
        </div>

        <div id="toms-result" class="ihk-result-box"></div>
      </div>
    `;

    document.getElementById("btn-check-toms").addEventListener("click", () => this.check());
    document.getElementById("btn-reset-toms").addEventListener("click", () => this.render());
  }

  check() {
    const selects = this.container.querySelectorAll(".tom-select");
    let correct = 0;

    selects.forEach((sel, idx) => {
      const target = this.scenarios[idx].target;
      const val = sel.value;
      if (val === target) {
        correct++;
        sel.style.borderColor = "#4ade80";
        sel.style.background = "rgba(34, 197, 94, 0.15)";
      } else {
        sel.style.borderColor = "#f87171";
        sel.style.background = "rgba(239, 68, 68, 0.15)";
      }
    });

    const resBox = document.getElementById("toms-result");
    const allRight = correct === this.scenarios.length;
    resBox.innerHTML = `
      <h4 style="color: ${allRight ? '#4ade80' : '#f87171'}; margin-top: 0;">
        ${allRight ? '🎉 Perfekt! Alle 8 TOMs exakt zugeordnet.' : `${correct} von ${this.scenarios.length} Maßnahmen richtig zugeordnet.`}
      </h4>
      <p style="color: #94a3b8; font-size: 0.9rem;">
        <strong>IHK-Merksatz:</strong> Zutritt = Räumlich/Physisch | Zugang = Am System einloggen | Zugriff = Innerhalb des Systems Dateien/Ordner lesen/ändern.
      </p>
    `;
    resBox.classList.add("active");
  }
}

window.TomsMatcher = TomsMatcher;
