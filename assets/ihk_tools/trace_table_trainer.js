/**
 * 📝 IHK TRACE-TABELLEN-TRAINER 📝
 * =================================
 * Interaktiver Wertetabellen-Trainer für AP1 (Lernfeld 5 Programmierung):
 * - Schrittweiser Algorithmen-Durchlauf
 * - Zeilenweises Befüllen der Variablenzustände
 * - Automatische Validierung & Erklärungen
 */

class TraceTableTrainer {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    this.currentExerciseIndex = 0;
    this.exercises = [
      {
        title: "Aufgabe 1: Schleifenakkumulator mit Bedingung",
        code: `GANZZAHL a = 3
GANZZAHL b = 10
GANZZAHL summe = 0

SOLANGE a < b TUE
    WENN a MOD 2 == 1 DANN
        summe = summe + a
    ENDE_WENN
    a = a + 2
ENDE_SOLANGE
AUSGABE summe`,
        variables: ["Durchlauf", "Bedingung (a < b)", "a", "b", "summe"],
        rows: [
          { Durchlauf: "Start", "Bedingung (a < b)": "-", a: "3", b: "10", summe: "0" },
          { Durchlauf: "1", "Bedingung (a < b)": "wahr", a: "5", b: "10", summe: "3" },
          { Durchlauf: "2", "Bedingung (a < b)": "wahr", a: "7", b: "10", summe: "8" },
          { Durchlauf: "3", "Bedingung (a < b)": "wahr", a: "9", b: "10", summe: "15" },
          { Durchlauf: "4", "Bedingung (a < b)": "wahr", a: "11", b: "10", summe: "24" },
          { Durchlauf: "Ende", "Bedingung (a < b)": "falsch", a: "11", b: "10", summe: "24" }
        ],
        finalOutput: "24"
      },
      {
        title: "Aufgabe 2: Lineare Maximum-Suche im Array",
        code: `FELD zahlen = [12, 45, 8, 92, 34]
GANZZAHL max = zahlen[0]
GANZZAHL i = 1

SOLANGE i < 5 TUE
    WENN zahlen[i] > max DANN
        max = zahlen[i]
    ENDE_WENN
    i = i + 1
ENDE_SOLANGE
AUSGABE max`,
        variables: ["Schritt i", "zahlen[i]", "Vergleich (> max)", "max"],
        rows: [
          { "Schritt i": "Start", "zahlen[i]": "-", "Vergleich (> max)": "-", max: "12" },
          { "Schritt i": "1", "zahlen[i]": "45", "Vergleich (> max)": "wahr", max: "45" },
          { "Schritt i": "2", "zahlen[i]": "8", "Vergleich (> max)": "falsch", max: "45" },
          { "Schritt i": "3", "zahlen[i]": "92", "Vergleich (> max)": "wahr", max: "92" },
          { "Schritt i": "4", "zahlen[i]": "34", "Vergleich (> max)": "falsch", max: "92" }
        ],
        finalOutput: "92"
      }
    ];
    this.init();
  }

  init() {
    if (!this.container) return;
    this.render();
  }

  render() {
    const ex = this.exercises[this.currentExerciseIndex];

    this.container.innerHTML = `
      <div class="ihk-tool-card">
        <div class="ihk-tool-header">
          <div class="ihk-tool-title">
            <span>📝</span> IHK Trace-Tabellen Trainer (LF 5)
          </div>
          <div>
            <span class="ihk-badge">${ex.title}</span>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; margin-bottom: 20px;">
          <div>
            <label style="font-weight: 600; color: #94a3b8; font-size: 0.85rem;">IHK-Pseudocode:</label>
            <pre style="background: #0f172a; padding: 16px; border-radius: 8px; border: 1px solid #334155; font-family: monospace; font-size: 0.9rem; color: #38bdf8; line-height: 1.5; overflow-x: auto;"><code>${ex.code}</code></pre>
          </div>

          <div>
            <label style="font-weight: 600; color: #94a3b8; font-size: 0.85rem;">Trage die Werte für jeden Durchlauf ein:</label>
            <div style="overflow-x: auto;">
              <table class="ihk-table" id="trace-table-inputs">
                <thead>
                  <tr>
                    ${ex.variables.map(v => `<th>${v}</th>`).join('')}
                  </tr>
                </thead>
                <tbody>
                  ${ex.rows.map((row, rIdx) => `
                    <tr>
                      ${ex.variables.map((v, cIdx) => {
                        if (cIdx === 0) {
                          return `<td style="font-weight: bold; color: #94a3b8;">${row[v]}</td>`;
                        }
                        return `
                          <td>
                            <input type="text" class="ihk-input trace-cell" data-row="${rIdx}" data-var="${v}" style="padding: 6px 10px; font-size: 0.85rem; font-family: monospace;">
                          </td>
                        `;
                      }).join('')}
                    </tr>
                  `).join('')}
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <div style="display: flex; gap: 12px; flex-wrap: wrap;">
          <button class="ihk-btn ihk-btn-success" id="btn-check-trace">✓ Trace-Tabelle prüfen</button>
          <button class="ihk-btn ihk-btn-secondary" id="btn-next-trace">Nächste Übungsaufgabe →</button>
          <button class="ihk-btn ihk-btn-secondary" id="btn-solve-trace">Lösung aufdecken</button>
        </div>

        <div id="trace-result" class="ihk-result-box"></div>
      </div>
    `;

    document.getElementById("btn-check-trace").addEventListener("click", () => this.check());
    document.getElementById("btn-next-trace").addEventListener("click", () => {
      this.currentExerciseIndex = (this.currentExerciseIndex + 1) % this.exercises.length;
      this.render();
    });
    document.getElementById("btn-solve-trace").addEventListener("click", () => this.solve());
  }

  check() {
    const ex = this.exercises[this.currentExerciseIndex];
    let totalCells = 0;
    let correctCells = 0;

    const inputs = this.container.querySelectorAll(".trace-cell");
    inputs.forEach(input => {
      const rIdx = parseInt(input.dataset.row, 10);
      const varName = input.dataset.var;
      const expected = ex.rows[rIdx][varName].toString().toLowerCase().trim();
      const userVal = input.value.toString().toLowerCase().trim();

      totalCells++;
      if (userVal === expected) {
        correctCells++;
        input.style.borderColor = "#4ade80";
        input.style.background = "rgba(34, 197, 94, 0.1)";
      } else {
        input.style.borderColor = "#f87171";
        input.style.background = "rgba(239, 68, 68, 0.1)";
      }
    });

    const resBox = document.getElementById("trace-result");
    const allRight = correctCells === totalCells;
    resBox.innerHTML = `
      <h4 style="color: ${allRight ? '#4ade80' : '#f87171'}; margin-top: 0;">
        ${allRight ? '🎉 Perfekt ausgefüllt!' : `Ergebnis: ${correctCells} von ${totalCells} Zellen richtig.`}
      </h4>
      <p style="color: #94a3b8; font-size: 0.9rem;">
        Endgültige Bildschirmausgabe nach dem Durchlauf: <strong style="color: #38bdf8">${ex.finalOutput}</strong>
      </p>
    `;
    resBox.classList.add("active");
  }

  solve() {
    const ex = this.exercises[this.currentExerciseIndex];
    const inputs = this.container.querySelectorAll(".trace-cell");
    inputs.forEach(input => {
      const rIdx = parseInt(input.dataset.row, 10);
      const varName = input.dataset.var;
      input.value = ex.rows[rIdx][varName];
      input.style.borderColor = "#38bdf8";
      input.style.background = "rgba(56, 189, 248, 0.1)";
    });
  }
}

window.TraceTableTrainer = TraceTableTrainer;
