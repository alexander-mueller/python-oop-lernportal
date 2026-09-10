/**
 * 💾 IHK RAID- & STORAGE-SIMULATOR 💾
 * ===================================
 * Interaktiver Storage-Simulator für AP2 FISI (LF 11 Storage & Hochverfügbarkeit):
 * - RAID 0, 1, 5, 6, 10
 * - Brutto-, Netto-Kapazität, Parität und Ausfallsicherheit
 * - Hot-Spare Integration & IHK-Formeln
 */

class RaidSimulator {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
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
            <span>💾</span> IHK RAID- & Storage-Simulator (LF 11)
          </div>
          <div>
            <span class="ihk-badge ihk-badge-success">IHK Formelwerkzeuge</span>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-bottom: 20px;">
          <div class="ihk-input-group">
            <label>RAID-Level:</label>
            <select id="raid-level" class="ihk-select">
              <option value="0">RAID 0 (Striping - Keine Redundanz)</option>
              <option value="1">RAID 1 (Spiegelung / Mirroring)</option>
              <option value="5" selected>RAID 5 (Verteilte Parität)</option>
              <option value="6">RAID 6 (Doppelte verteilte Parität)</option>
              <option value="10">RAID 10 (Stripe of Mirrors)</option>
            </select>
          </div>

          <div class="ihk-input-group">
            <label>Anzahl Festplatten (N):</label>
            <input type="number" id="raid-disks" class="ihk-input" min="2" max="24" value="5">
          </div>

          <div class="ihk-input-group">
            <label>Kapazität pro Platte (TB):</label>
            <input type="number" id="raid-size" class="ihk-input" min="1" max="64" value="4">
          </div>

          <div class="ihk-input-group">
            <label>Hot-Spare Platte reservieren?</label>
            <select id="raid-hotspare" class="ihk-select">
              <option value="0" selected>Nein (Keine Hot-Spare)</option>
              <option value="1">Ja (1 Dedizierte Hot-Spare)</option>
            </select>
          </div>
        </div>

        <div id="raid-metrics" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; margin-bottom: 20px;">
          <!-- Dynamisch befüllt -->
        </div>

        <div id="raid-explanation" style="background: #0f172a; padding: 16px; border-radius: 8px; border: 1px solid #334155; font-size: 0.95rem; line-height: 1.6; color: #cbd5e1;">
          <!-- Dynamische IHK Erklärung -->
        </div>
      </div>
    `;

    document.getElementById("raid-level").addEventListener("change", () => this.calculate());
    document.getElementById("raid-disks").addEventListener("input", () => this.calculate());
    document.getElementById("raid-size").addEventListener("input", () => this.calculate());
    document.getElementById("raid-hotspare").addEventListener("change", () => this.calculate());
  }

  calculate() {
    const level = document.getElementById("raid-level").value;
    let n = parseInt(document.getElementById("raid-disks").value, 10) || 0;
    const s = parseFloat(document.getElementById("raid-size").value) || 0;
    const hasHotSpare = parseInt(document.getElementById("raid-hotspare").value, 10) === 1;

    let activeDisks = hasHotSpare ? n - 1 : n;
    let valid = true;
    let errorMsg = "";
    let minDisks = 2;

    if (level === "0") minDisks = 2;
    if (level === "1") minDisks = 2;
    if (level === "5") minDisks = 3;
    if (level === "6") minDisks = 4;
    if (level === "10") minDisks = 4;

    if (activeDisks < minDisks) {
      valid = false;
      errorMsg = `Für RAID ${level} werden mindestens ${minDisks} aktive Platten benötigt (aktuell: ${activeDisks}).`;
    }
    if (level === "10" && activeDisks % 2 !== 0) {
      valid = false;
      errorMsg = `RAID 10 erfordert eine gerade Anzahl aktiver Platten (aktuell: ${activeDisks}).`;
    }

    const metricsBox = document.getElementById("raid-metrics");
    const explBox = document.getElementById("raid-explanation");

    if (!valid) {
      metricsBox.innerHTML = `
        <div style="grid-column: 1 / -1; padding: 12px; background: rgba(239, 68, 68, 0.15); border: 1px solid #ef4444; border-radius: 6px; color: #f87171; font-weight: 600;">
          ⚠️ ${errorMsg}
        </div>
      `;
      explBox.innerHTML = "Bitte passe die Plattenanzahl für das gewählte RAID-Level an.";
      return;
    }

    const rawTotal = n * s;
    let usable = 0;
    let faultTolerance = 0;
    let formula = "";

    if (level === "0") {
      usable = activeDisks * s;
      faultTolerance = 0;
      formula = "Nutzdaten = n × Kapazität (Keine Redundanz!)";
    } else if (level === "1") {
      usable = s;
      faultTolerance = activeDisks - 1;
      formula = "Nutzdaten = 1 × Kapazität (Gesamte Spiegelung)";
    } else if (level === "5") {
      usable = (activeDisks - 1) * s;
      faultTolerance = 1;
      formula = "Nutzdaten = (n - 1) × Kapazität (1 Platte Paritäts-Overhead)";
    } else if (level === "6") {
      usable = (activeDisks - 2) * s;
      faultTolerance = 2;
      formula = "Nutzdaten = (n - 2) × Kapazität (2 Platten Paritäts-Overhead)";
    } else if (level === "10") {
      usable = (activeDisks / 2) * s;
      faultTolerance = 1; // Garantiert 1 Platte, bis zu n/2 im besten Fall
      formula = "Nutzdaten = (n / 2) × Kapazität (50 % Nutzkapazität)";
    }

    const efficiency = Math.round((usable / rawTotal) * 100);

    metricsBox.innerHTML = `
      <div style="background: #0f172a; padding: 12px; border-radius: 6px; border: 1px solid #334155;">
        <div style="color: #94a3b8; font-size: 0.8rem;">Bruttokapazität (Roh):</div>
        <div style="font-size: 1.4rem; font-weight: 700; color: #f8fafc;">${rawTotal.toFixed(1)} TB</div>
      </div>
      <div style="background: #0f172a; padding: 12px; border-radius: 6px; border: 1px solid #0284c7;">
        <div style="color: #38bdf8; font-size: 0.8rem;">Nettokapazität (Nutzbar):</div>
        <div style="font-size: 1.4rem; font-weight: 800; color: #38bdf8;">${usable.toFixed(1)} TB</div>
      </div>
      <div style="background: #0f172a; padding: 12px; border-radius: 6px; border: 1px solid #334155;">
        <div style="color: #94a3b8; font-size: 0.8rem;">Ausfalltoleranz:</div>
        <div style="font-size: 1.4rem; font-weight: 700; color: ${faultTolerance > 0 ? '#4ade80' : '#f87171'};">
          ${faultTolerance} Platte(n)
        </div>
      </div>
      <div style="background: #0f172a; padding: 12px; border-radius: 6px; border: 1px solid #334155;">
        <div style="color: #94a3b8; font-size: 0.8rem;">Speichereffizienz:</div>
        <div style="font-size: 1.4rem; font-weight: 700; color: #facc15;">${efficiency} %</div>
      </div>
    `;

    explBox.innerHTML = `
      <h4 style="color: #38bdf8; margin-top: 0;">IHK-Prüfungswissen & Formel:</h4>
      <p>
        <strong>Angewandte Formel:</strong> <code>${formula}</code><br>
        ${hasHotSpare ? '<em>Hinweis: 1 Festplatte ist als Standby-Ersatzplatte (Hot-Spare) reserviert und zählt nicht zu den aktiven Nutzkapazitäten.</em><br>' : ''}
        <strong>Prüfungsfalle URE (Unrecoverable Read Error):</strong> Bei großen SATA-Festplatten ab 4 TB dauert der Rebuild eines RAID 5 viele Stunden bis Tage. Tritt während des Rebuilds ein Lesefehler auf einer weiteren Platte auf, ist das gesamte RAID 5 verloren! Die IHK verlangt in solchen Szenarien daher oft <strong>RAID 6</strong> (Dual-Parität) oder <strong>RAID 10</strong>.
      </p>
    `;
  }
}

window.RaidSimulator = RaidSimulator;
