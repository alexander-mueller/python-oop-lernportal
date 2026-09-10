/**
 * 📊 IHK NUTZWERTANALYSE-KALKULATOR (NWA) 📊
 * ==========================================
 * Interaktiver Nutzwertanalyse-Trainer für AP1 (LF 2) & AP2 (LF 12):
 * - Gewichtete Kriterienmatrix (Prüfung auf 100% Summe)
 * - Live-Berechnung der Teil- und Gesamtnutzwerte
 * - Empfehlung & Rangfolge nach IHK-Standard
 */

class NwaCalculator {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    this.criteria = [
      { name: "Anschaffungspreis / TCO", weight: 30, scoreA: 8, scoreB: 5 },
      { name: "Performance & Skalierbarkeit", weight: 25, scoreA: 6, scoreB: 9 },
      { name: "Garantie & Support-SLA (24/7)", weight: 20, scoreA: 7, scoreB: 8 },
      { name: "Energieeffizienz (Stromverbrauch)", weight: 15, scoreA: 9, scoreB: 6 },
      { name: "Lieferzeit & Verfügbarkeit", weight: 10, scoreA: 5, scoreB: 10 }
    ];
    this.init();
  }

  init() {
    if (!this.container) return;
    this.render();
    this.calculate();
  }

  render() {
    this.container.innerHTML = `
      <div class="ihk-tool-card">
        <div class="ihk-tool-header">
          <div class="ihk-tool-title">
            <span>📊</span> IHK Nutzwertanalyse-Kalkulator (LF 2 & LF 12)
          </div>
          <div>
            <span class="ihk-badge" id="nwa-weight-sum">Gewichtung: 100%</span>
          </div>
        </div>

        <p style="color: #94a3b8; font-size: 0.9rem; margin-top: 0;">
          Vergleiche zwei Angebote anhand gewichteter Kriterien (Bewertungsskala: 1 = sehr schlecht bis 10 = exzellent). Die Summe der Gewichtungen muss exakt 100 % ergeben.
        </p>

        <div style="overflow-x: auto;">
          <table class="ihk-table" id="nwa-table">
            <thead>
              <tr>
                <th>Entscheidungskriterium</th>
                <th style="width: 140px;">Gewichtung (%)</th>
                <th style="width: 120px;">Punkte Angebot A</th>
                <th style="width: 120px;">Punkte Angebot B</th>
                <th style="width: 130px;">Nutzen A</th>
                <th style="width: 130px;">Nutzen B</th>
              </tr>
            </thead>
            <tbody>
              ${this.criteria.map((c, i) => `
                <tr>
                  <td><input type="text" class="ihk-input" value="${c.name}" id="nwa-crit-${i}" style="padding: 6px 10px;"></td>
                  <td><input type="number" class="ihk-input nwa-weight" value="${c.weight}" min="1" max="100" data-idx="${i}" style="padding: 6px 10px;"></td>
                  <td><input type="number" class="ihk-input nwa-score-a" value="${c.scoreA}" min="1" max="10" data-idx="${i}" style="padding: 6px 10px;"></td>
                  <td><input type="number" class="ihk-input nwa-score-b" value="${c.scoreB}" min="1" max="10" data-idx="${i}" style="padding: 6px 10px;"></td>
                  <td id="nwa-val-a-${i}" style="font-weight: bold; color: #38bdf8;">0</td>
                  <td id="nwa-val-b-${i}" style="font-weight: bold; color: #facc15;">0</td>
                </tr>
              `).join('')}
            </tbody>
            <tfoot>
              <tr style="background: #0f172a; font-weight: bold; font-size: 1.05rem;">
                <td>GESAMTSUMME:</td>
                <td id="nwa-sum-weight" style="color: #4ade80;">100 %</td>
                <td>-</td>
                <td>-</td>
                <td id="nwa-total-a" style="color: #38bdf8; font-size: 1.2rem;">0</td>
                <td id="nwa-total-b" style="color: #facc15; font-size: 1.2rem;">0</td>
              </tr>
            </tfoot>
          </table>
        </div>

        <div id="nwa-winner-banner" style="margin-top: 16px; padding: 14px; border-radius: 8px; font-weight: 600;">
          <!-- Dynamischer Gewinner -->
        </div>
      </div>
    `;

    this.container.querySelectorAll(".nwa-weight, .nwa-score-a, .nwa-score-b").forEach(el => {
      el.addEventListener("input", () => this.calculate());
    });
  }

  calculate() {
    let totalWeight = 0;
    let totalScoreA = 0;
    let totalScoreB = 0;

    this.criteria.forEach((_, i) => {
      const w = parseFloat(this.container.querySelector(`.nwa-weight[data-idx="${i}"]`).value) || 0;
      const sA = parseFloat(this.container.querySelector(`.nwa-score-a[data-idx="${i}"]`).value) || 0;
      const sB = parseFloat(this.container.querySelector(`.nwa-score-b[data-idx="${i}"]`).value) || 0;

      totalWeight += w;
      const valA = (w * sA) / 100;
      const valB = (w * sB) / 100;
      totalScoreA += valA;
      totalScoreB += valB;

      const elA = document.getElementById(`nwa-val-a-${i}`);
      const elB = document.getElementById(`nwa-val-b-${i}`);
      if (elA) elA.textContent = (w * sA).toFixed(0);
      if (elB) elB.textContent = (w * sB).toFixed(0);
    });

    const sumWeightEl = document.getElementById("nwa-sum-weight");
    const weightBadge = document.getElementById("nwa-weight-sum");
    const totAEl = document.getElementById("nwa-total-a");
    const totBEl = document.getElementById("nwa-total-b");
    const banner = document.getElementById("nwa-winner-banner");

    if (sumWeightEl) sumWeightEl.textContent = `${totalWeight} %`;
    if (weightBadge) {
      weightBadge.textContent = `Gewichtung: ${totalWeight}%`;
      weightBadge.className = totalWeight === 100 ? "ihk-badge ihk-badge-success" : "ihk-badge ihk-badge-danger";
    }

    const rawTotalA = totalScoreA * 100;
    const rawTotalB = totalScoreB * 100;
    if (totAEl) totAEl.textContent = rawTotalA.toFixed(0);
    if (totBEl) totBEl.textContent = rawTotalB.toFixed(0);

    if (totalWeight !== 100) {
      banner.style.background = "rgba(239, 68, 68, 0.15)";
      banner.style.border = "1px solid #ef4444";
      banner.style.color = "#f87171";
      banner.innerHTML = `⚠️ Achtung: Die Gesamtsumme der Gewichtungen beträgt aktuell <strong>${totalWeight} %</strong> statt 100 %. Bitte Kriterien anpassen.`;
    } else {
      const winner = rawTotalA > rawTotalB ? "Angebot A" : (rawTotalB > rawTotalA ? "Angebot B" : "Gleichstand");
      banner.style.background = "rgba(34, 197, 94, 0.15)";
      banner.style.border = "1px solid #22c55e";
      banner.style.color = "#4ade80";
      banner.innerHTML = `🏆 Wirtschaftliche Entscheidung: <strong>${winner}</strong> erzielt mit <strong>${Math.max(rawTotalA, rawTotalB).toFixed(0)} Punkten</strong> den höchsten Gesamtnutzen und wird zur Beschaffung empfohlen.`;
    }
  }
}

window.NwaCalculator = NwaCalculator;
