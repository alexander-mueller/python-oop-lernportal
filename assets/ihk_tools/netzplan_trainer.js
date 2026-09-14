/**
 * 📅 IHK NETZPLAN-TRAINER (DIN 69900) 📅
 * =====================================
 * Interaktiver Trainer zur Berechnung von:
 * - Vorwärtsrechnung: FAZ (Frühester Anfangszeitpunkt) & FEZ (Frühester Endzeitpunkt)
 * - Rückwärtsrechnung: SAZ (Spätester Anfangszeitpunkt) & SEZ (Spätester Endzeitpunkt)
 * - Pufferzeiten: GP (Gesamtpuffer = SAZ - FAZ) & FP (Freier Puffer = min(FAZ_Nachfolger) - FEZ)
 * - Kritischer Pfad (Vorgänge mit GP = 0)
 */

class NetzplanTrainer {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    this.scenarioIndex = 0;
    this.scenarios = [
      {
        title: "Szenario 1: Rollout eines neuen Firmennetzwerks (PrintTop GmbH)",
        nodes: [
          { id: "A", name: "Anforderungsanalyse", d: 3, preds: [], faz: 0, fez: 3, saz: 0, sez: 3, gp: 0, fp: 0 },
          { id: "B", name: "Hardware-Beschaffung", d: 5, preds: ["A"], faz: 3, fez: 8, saz: 3, sez: 8, gp: 0, fp: 0 },
          { id: "C", name: "Kabelverlegung (Cat 7)", d: 4, preds: ["A"], faz: 3, fez: 7, saz: 4, sez: 8, gp: 1, fp: 1 },
          { id: "D", name: "Switch-/Router-Konfiguration", d: 4, preds: ["B"], faz: 8, fez: 12, saz: 8, sez: 12, gp: 0, fp: 0 },
          { id: "E", name: "Patchfeld & Dosen auflegen", d: 3, preds: ["C"], faz: 7, fez: 10, saz: 9, sez: 12, gp: 2, fp: 2 },
          { id: "F", name: "End-to-End Funktionstest", d: 2, preds: ["D", "E"], faz: 12, fez: 14, saz: 12, sez: 14, gp: 0, fp: 0 },
          { id: "G", name: "Übergabe & Abnahme", d: 1, preds: ["F"], faz: 14, fez: 15, saz: 14, sez: 15, gp: 0, fp: 0 }
        ],
        criticalPath: ["A", "B", "D", "F", "G"]
      },
      {
        title: "Szenario 2: Migration auf Microsoft Active Directory",
        nodes: [
          { id: "A", name: "Ist-Aufnahme AD DS", d: 2, preds: [], faz: 0, fez: 2, saz: 0, sez: 2, gp: 0, fp: 0 },
          { id: "B", name: "OU-Struktur & GPO-Design", d: 4, preds: ["A"], faz: 2, fez: 6, saz: 2, sez: 6, gp: 0, fp: 0 },
          { id: "C", name: "Bereitstellung DC-Hardware", d: 3, preds: ["A"], faz: 2, fez: 5, saz: 3, sez: 6, gp: 1, fp: 1 },
          { id: "D", name: "Benutzerdaten CSV-Export", d: 2, preds: ["A"], faz: 2, fez: 4, saz: 6, sez: 8, gp: 4, fp: 4 },
          { id: "E", name: "Installation Domain Controller", d: 2, preds: ["B", "C"], faz: 6, fez: 8, saz: 6, sez: 8, gp: 0, fp: 0 },
          { id: "F", name: "PowerShell Massenimport", d: 3, preds: ["D", "E"], faz: 8, fez: 11, saz: 8, sez: 11, gp: 0, fp: 0 },
          { id: "G", name: "Client-Domain-Join & Tests", d: 2, preds: ["F"], faz: 11, fez: 13, saz: 11, sez: 13, gp: 0, fp: 0 }
        ],
        criticalPath: ["A", "B", "E", "F", "G"]
      }
    ];
    this.init();
  }

  init() {
    if (!this.container) return;
    this.render();
  }

  render() {
    const sc = this.scenarios[this.scenarioIndex];
    this.container.innerHTML = `
      <div class="ihk-tool-card" style="background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 24px;">
        <div class="ihk-tool-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
          <div>
            <h3 style="color: #38bdf8; margin: 0; font-size: 1.3rem;">📊 DIN 69900 Netzplantechnik Trainer</h3>
            <p style="color: #94a3b8; font-size: 0.9rem; margin: 4px 0 0 0;">${sc.title}</p>
          </div>
          <div style="display: flex; gap: 8px;">
            <button class="ihk-btn ihk-btn-secondary" id="np-prev-scenario" style="padding: 6px 12px; font-size: 0.85rem;">← Szenario 1</button>
            <button class="ihk-btn ihk-btn-secondary" id="np-next-scenario" style="padding: 6px 12px; font-size: 0.85rem;">Szenario 2 →</button>
          </div>
        </div>

        <div style="background: #0f172a; border: 1px solid #334155; border-radius: 8px; padding: 16px; margin-bottom: 20px;">
          <p style="color: #cbd5e1; font-size: 0.9rem; margin: 0 0 10px 0;">
            <strong>Aufgabe:</strong> Berechnen Sie für jeden Vorgang die Zeitpunkte der <em>Vorwärtsrechnung</em> (FAZ, FEZ), der <em>Rückwärtsrechnung</em> (SAZ, SEZ) sowie den <em>Gesamtpuffer (GP)</em> und <em>Freien Puffer (FP)</em>. Identifizieren Sie anschließend alle Vorgänge auf dem <strong>Kritischen Pfad</strong>.
          </p>
          <div style="display: flex; gap: 16px; flex-wrap: wrap; font-size: 0.82rem; color: #94a3b8;">
            <span>ℹ️ <code>FEZ = FAZ + D</code></span>
            <span>ℹ️ <code>FAZ = max(FEZ aller Vorgänger)</code></span>
            <span>ℹ️ <code>SAZ = SEZ - D</code></span>
            <span>ℹ️ <code>SEZ = min(SAZ aller Nachfolger)</code></span>
            <span>ℹ️ <code>GP = SAZ - FAZ = SEZ - FEZ</code></span>
            <span>ℹ️ <code>FP = min(FAZ Nachfolger) - FEZ</code></span>
          </div>
        </div>

        <!-- Interaktive Tabelle -->
        <div style="overflow-x: auto; margin-bottom: 20px;">
          <table class="ihk-table" style="width: 100%; border-collapse: collapse; font-size: 0.85rem; text-align: center;">
            <thead>
              <tr style="background: #0f172a; color: #38bdf8;">
                <th style="padding: 10px; border: 1px solid #334155;">ID</th>
                <th style="padding: 10px; border: 1px solid #334155; text-align: left;">Vorgang</th>
                <th style="padding: 10px; border: 1px solid #334155;">Dauer (D)</th>
                <th style="padding: 10px; border: 1px solid #334155;">Vorgänger</th>
                <th style="padding: 10px; border: 1px solid #334155; background: #1e3a8a; color: #93c5fd;">FAZ</th>
                <th style="padding: 10px; border: 1px solid #334155; background: #1e3a8a; color: #93c5fd;">FEZ</th>
                <th style="padding: 10px; border: 1px solid #334155; background: #701a75; color: #f0abfc;">SAZ</th>
                <th style="padding: 10px; border: 1px solid #334155; background: #701a75; color: #f0abfc;">SEZ</th>
                <th style="padding: 10px; border: 1px solid #334155; color: #facc15;">GP</th>
                <th style="padding: 10px; border: 1px solid #334155; color: #facc15;">FP</th>
                <th style="padding: 10px; border: 1px solid #334155; color: #f87171;">Kritisch?</th>
              </tr>
            </thead>
            <tbody>
              ${sc.nodes.map(n => `
                <tr id="row-node-${n.id}" style="border: 1px solid #334155;">
                  <td style="padding: 8px; font-weight: bold; color: #38bdf8;">${n.id}</td>
                  <td style="padding: 8px; text-align: left; color: #f8fafc;">${n.name}</td>
                  <td style="padding: 8px; font-weight: 600;">${n.d}</td>
                  <td style="padding: 8px; color: #94a3b8;">${n.preds.length > 0 ? n.preds.join(", ") : "-"}</td>
                  <td style="padding: 6px;"><input type="number" id="in-faz-${n.id}" class="ihk-input" style="width: 55px; text-align: center; padding: 4px;" min="0"></td>
                  <td style="padding: 6px;"><input type="number" id="in-fez-${n.id}" class="ihk-input" style="width: 55px; text-align: center; padding: 4px;" min="0"></td>
                  <td style="padding: 6px;"><input type="number" id="in-saz-${n.id}" class="ihk-input" style="width: 55px; text-align: center; padding: 4px;" min="0"></td>
                  <td style="padding: 6px;"><input type="number" id="in-sez-${n.id}" class="ihk-input" style="width: 55px; text-align: center; padding: 4px;" min="0"></td>
                  <td style="padding: 6px;"><input type="number" id="in-gp-${n.id}" class="ihk-input" style="width: 50px; text-align: center; padding: 4px;" min="0"></td>
                  <td style="padding: 6px;"><input type="number" id="in-fp-${n.id}" class="ihk-input" style="width: 50px; text-align: center; padding: 4px;" min="0"></td>
                  <td style="padding: 6px;"><input type="checkbox" id="in-crit-${n.id}" style="transform: scale(1.3); cursor: pointer;"></td>
                </tr>
              `).join("")}
            </tbody>
          </table>
        </div>

        <div style="display: flex; gap: 12px; flex-wrap: wrap;">
          <button class="ihk-btn ihk-btn-success" id="np-check-btn">✓ Berechnungen prüfen</button>
          <button class="ihk-btn ihk-btn-secondary" id="np-solve-btn">💡 Musterlösung ausfüllen</button>
          <button class="ihk-btn ihk-btn-secondary" id="np-reset-btn">Zurücksetzen</button>
        </div>

        <div id="np-feedback-box" class="ihk-result-box" style="margin-top: 18px;"></div>
      </div>
    `;

    this.attachEvents();
  }

  attachEvents() {
    document.getElementById("np-check-btn").addEventListener("click", () => this.checkAnswers());
    document.getElementById("np-solve-btn").addEventListener("click", () => this.solve());
    document.getElementById("np-reset-btn").addEventListener("click", () => this.render());
    document.getElementById("np-prev-scenario").addEventListener("click", () => {
      this.scenarioIndex = 0;
      this.render();
    });
    document.getElementById("np-next-scenario").addEventListener("click", () => {
      this.scenarioIndex = 1;
      this.render();
    });
  }

  checkAnswers() {
    const sc = this.scenarios[this.scenarioIndex];
    let correctCount = 0;
    let totalFields = sc.nodes.length * 7;
    const errors = [];

    sc.nodes.forEach(n => {
      const row = document.getElementById(`row-node-${n.id}`);
      const valFaz = parseInt(document.getElementById(`in-faz-${n.id}`).value, 10);
      const valFez = parseInt(document.getElementById(`in-fez-${n.id}`).value, 10);
      const valSaz = parseInt(document.getElementById(`in-saz-${n.id}`).value, 10);
      const valSez = parseInt(document.getElementById(`in-sez-${n.id}`).value, 10);
      const valGp = parseInt(document.getElementById(`in-gp-${n.id}`).value, 10);
      const valFp = parseInt(document.getElementById(`in-fp-${n.id}`).value, 10);
      const valCrit = document.getElementById(`in-crit-${n.id}`).checked;
      const isActuallyCrit = sc.criticalPath.includes(n.id);

      let nodeOk = true;

      const checkField = (elemId, actual, expected, name) => {
        const el = document.getElementById(elemId);
        if (actual === expected) {
          el.style.border = "1px solid #22c55e";
          el.style.background = "#064e3b";
          correctCount++;
        } else {
          el.style.border = "1px solid #ef4444";
          el.style.background = "#450a0a";
          nodeOk = false;
          errors.push(`Vorgang ${n.id} (${n.name}): ${name} sollte ${expected} sein (Eingabe: ${isNaN(actual) ? 'leer' : actual}).`);
        }
      };

      checkField(`in-faz-${n.id}`, valFaz, n.faz, "FAZ");
      checkField(`in-fez-${n.id}`, valFez, n.fez, "FEZ");
      checkField(`in-saz-${n.id}`, valSaz, n.saz, "SAZ");
      checkField(`in-sez-${n.id}`, valSez, n.sez, "SEZ");
      checkField(`in-gp-${n.id}`, valGp, n.gp, "GP");
      checkField(`in-fp-${n.id}`, valFp, n.fp, "FP");

      const critEl = document.getElementById(`in-crit-${n.id}`);
      if (valCrit === isActuallyCrit) {
        critEl.parentElement.style.background = "#064e3b";
        correctCount++;
      } else {
        critEl.parentElement.style.background = "#450a0a";
        nodeOk = false;
        errors.push(`Vorgang ${n.id} liegt ${isActuallyCrit ? 'AUF' : 'NICHT auf'} dem kritischen Pfad.`);
      }

      if (nodeOk) {
        row.style.background = "rgba(34, 197, 94, 0.1)";
      } else {
        row.style.background = "rgba(239, 68, 68, 0.1)";
      }
    });

    const box = document.getElementById("np-feedback-box");
    box.style.display = "block";
    const percent = Math.round((correctCount / totalFields) * 100);

    if (errors.length === 0) {
      box.innerHTML = `
        <div style="border-left: 4px solid #22c55e; padding-left: 14px;">
          <h4 style="color: #4ade80; margin: 0 0 6px 0; font-size: 1.1rem;">🎉 Perfekt! 100% Richtige Netzplanberechnung (${correctCount}/${totalFields} Felder)</h4>
          <p style="color: #cbd5e1; margin: 0; line-height: 1.5;">
            Gesamtdauer des Projekts: <strong>${sc.nodes[sc.nodes.length - 1].fez} Zeiteinheiten</strong>.<br>
            Der kritische Pfad verläuft über: <strong style="color: #f87171;">${sc.criticalPath.join(" → ")}</strong>. Alle Vorgänge hier haben Gesamtpuffer <code>GP = 0</code>.
          </p>
        </div>
      `;
    } else {
      box.innerHTML = `
        <div style="border-left: 4px solid #ef4444; padding-left: 14px;">
          <h4 style="color: #f87171; margin: 0 0 6px 0; font-size: 1.1rem;">⚠️ ${errors.length} Fehler gefunden (${percent}% korrekt)</h4>
          <ul style="color: #cbd5e1; margin: 8px 0 0 0; padding-left: 20px; font-size: 0.88rem; line-height: 1.6;">
            ${errors.slice(0, 6).map(e => `<li>${e}</li>`).join("")}
            ${errors.length > 6 ? `<li>... und ${errors.length - 6} weitere Abweichungen.</li>` : ""}
          </ul>
        </div>
      `;
    }
  }

  solve() {
    const sc = this.scenarios[this.scenarioIndex];
    sc.nodes.forEach(n => {
      document.getElementById(`in-faz-${n.id}`).value = n.faz;
      document.getElementById(`in-fez-${n.id}`).value = n.fez;
      document.getElementById(`in-saz-${n.id}`).value = n.saz;
      document.getElementById(`in-sez-${n.id}`).value = n.sez;
      document.getElementById(`in-gp-${n.id}`).value = n.gp;
      document.getElementById(`in-fp-${n.id}`).value = n.fp;
      document.getElementById(`in-crit-${n.id}`).checked = sc.criticalPath.includes(n.id);
    });
    this.checkAnswers();
  }
}

document.addEventListener("DOMContentLoaded", () => {
  if (document.getElementById("netzplan-trainer-container")) {
    window.netzplanTrainer = new NetzplanTrainer("netzplan-trainer-container");
  }
});
