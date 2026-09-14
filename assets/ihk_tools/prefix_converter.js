/**
 * ⚡ IHK BINÄRPRÄFIX- & TRANSFERZEIT-DRILL (IEC 60027-2) ⚡
 * ======================================================
 * Interaktiver Drill für:
 * 1. Binärpräfixe (KiB, MiB, GiB, TiB) vs. Dezimalpräfixe (kB, MB, GB, TB)
 * 2. Berechnen der tatsächlichen Speicherkapazität (Herstellerangabe vs. Betriebssystem)
 * 3. Übertragungszeit-Berechnung t = Datenmenge / Datenrate mit Einheitenkonvertierung
 */

class PrefixConverter {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    this.init();
  }

  init() {
    if (!this.container) return;
    this.render();
  }

  render() {
    this.container.innerHTML = `
      <div class="ihk-tool-card" style="background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 24px; margin-bottom: 24px;">
        <div class="ihk-tool-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
          <div>
            <h3 style="color: #38bdf8; margin: 0; font-size: 1.3rem;">⚡ IEC-Binärpräfixe & Transferzeit Drill-Master</h3>
            <p style="color: #94a3b8; font-size: 0.9rem; margin: 4px 0 0 0;">Strikte ZPA 2. Auflage Normierung (KiB, MiB, GiB, TiB)</p>
          </div>
          <div>
            <span class="ihk-badge ihk-badge-warning">ZPA Pflichtstoff</span>
          </div>
        </div>

        <div style="display: flex; gap: 10px; margin-bottom: 20px; border-bottom: 1px solid #334155; padding-bottom: 12px;">
          <button id="pfx-tab-drill" class="ihk-btn ihk-btn-primary" style="padding: 6px 14px; font-size: 0.85rem;">💾 Festplatten-Kapazität (SI vs. IEC)</button>
          <button id="pfx-tab-time" class="ihk-btn ihk-btn-secondary" style="padding: 6px 14px; font-size: 0.85rem;">⏱️ Datentransferzeit-Rechner</button>
        </div>

        <!-- Ansicht 1: Festplattenkapazität -->
        <div id="pfx-view-drill">
          <div style="background: #0f172a; padding: 16px; border-radius: 8px; border: 1px solid #334155; margin-bottom: 18px;">
            <p style="color: #cbd5e1; font-size: 0.92rem; margin: 0; line-height: 1.6;">
              Festplattenhersteller verkaufen Speicher nach <strong>Dezimalpräfixen (SI: 10er-Potenzen)</strong>.<br>
              Betriebssysteme (Windows, Linux) verwalten Speicher jedoch in <strong>Binärpräfixen (IEC: 2er-Potenzen)</strong>.<br>
              <em>1 TB (Hersteller) = 1.000.000.000.000 Byte. 1 TiB (IEC) = 1.024⁴ = 1.099.511.627.776 Byte.</em>
            </p>
          </div>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 20px;">
            <div class="ihk-input-group">
              <label>Herstellerangabe (Dezimal):</label>
              <input type="number" id="pfx-disk-val" class="ihk-input" value="2" min="1" max="100">
            </div>
            <div class="ihk-input-group">
              <label>Einheit:</label>
              <select id="pfx-disk-unit" class="ihk-select">
                <option value="GB">GB (10⁹ Byte)</option>
                <option value="TB" selected>TB (10¹² Byte)</option>
              </select>
            </div>
          </div>

          <button class="ihk-btn ihk-btn-success" id="btn-calc-pfx">🧮 Echte Kapazität in GiB / TiB berechnen</button>

          <div id="pfx-disk-result" style="margin-top: 18px; background: #0f172a; border: 1px solid #334155; border-radius: 8px; padding: 18px; display: none;"></div>
        </div>

        <!-- Ansicht 2: Datentransferzeit -->
        <div id="pfx-view-time" style="display: none;">
          <div style="background: #0f172a; padding: 16px; border-radius: 8px; border: 1px solid #334155; margin-bottom: 18px;">
            <p style="color: #cbd5e1; font-size: 0.92rem; margin: 0; line-height: 1.6;">
              <strong>IHK-Klassiker:</strong> Übertragungszeit berechnen unter Berücksichtigung von Byte $\rightarrow$ Bit (Faktor 8) und Protokoll-Overhead!
            </p>
          </div>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 20px;">
            <div class="ihk-input-group">
              <label>Datenmenge:</label>
              <input type="number" id="pfx-data-amount" class="ihk-input" value="50" min="1">
            </div>
            <div class="ihk-input-group">
              <label>Datenmengen-Einheit:</label>
              <select id="pfx-data-unit" class="ihk-select">
                <option value="MiB">MiB (1.024² Byte)</option>
                <option value="GiB" selected>GiB (1.024³ Byte)</option>
                <option value="TiB">TiB (1.024⁴ Byte)</option>
              </select>
            </div>
            <div class="ihk-input-group">
              <label>Netzwerk-Bandbreite:</label>
              <input type="number" id="pfx-net-speed" class="ihk-input" value="100" min="1">
            </div>
            <div class="ihk-input-group">
              <label>Bandbreiten-Einheit:</label>
              <select id="pfx-speed-unit" class="ihk-select">
                <option value="Mbit">Mbit/s (10⁶ Bit/s)</option>
                <option value="Gbit">Gbit/s (10⁹ Bit/s)</option>
              </select>
            </div>
          </div>

          <div class="ihk-input-group" style="margin-bottom: 20px;">
            <label>Protokoll-Overhead (z. B. TCP/IP, Verschlüsselung):</label>
            <select id="pfx-overhead" class="ihk-select">
              <option value="0">0 % (Theoretisches Maximum)</option>
              <option value="5">5 % (Typischer TCP/IP Overhead)</option>
              <option value="10" selected>10 % (Realistischer Netzwerk-Overhead)</option>
            </select>
          </div>

          <button class="ihk-btn ihk-btn-success" id="btn-calc-time">⏱️ Übertragungsdauer berechnen</button>

          <div id="pfx-time-result" style="margin-top: 18px; background: #0f172a; border: 1px solid #334155; border-radius: 8px; padding: 18px; display: none;"></div>
        </div>
      </div>
    `;

    this.attachEvents();
  }

  attachEvents() {
    const tabDrill = document.getElementById("pfx-tab-drill");
    const tabTime = document.getElementById("pfx-tab-time");
    const viewDrill = document.getElementById("pfx-view-drill");
    const viewTime = document.getElementById("pfx-view-time");

    tabDrill.addEventListener("click", () => {
      tabDrill.className = "ihk-btn ihk-btn-primary";
      tabTime.className = "ihk-btn ihk-btn-secondary";
      viewDrill.style.display = "block";
      viewTime.style.display = "none";
    });

    tabTime.addEventListener("click", () => {
      tabTime.className = "ihk-btn ihk-btn-primary";
      tabDrill.className = "ihk-btn ihk-btn-secondary";
      viewTime.style.display = "block";
      viewDrill.style.display = "none";
    });

    document.getElementById("btn-calc-pfx").addEventListener("click", () => this.calcCapacity());
    document.getElementById("btn-calc-time").addEventListener("click", () => this.calcTime());
  }

  calcCapacity() {
    const val = parseFloat(document.getElementById("pfx-disk-val").value) || 0;
    const unit = document.getElementById("pfx-disk-unit").value;
    const resBox = document.getElementById("pfx-disk-result");
    resBox.style.display = "block";

    let bytes = 0;
    if (unit === "GB") bytes = val * 1e9;
    if (unit === "TB") bytes = val * 1e12;

    const gib = bytes / Math.pow(1024, 3);
    const tib = bytes / Math.pow(1024, 4);
    const diffPct = (1 - (gib / (unit === "TB" ? val * 1024 : val))) * 100;

    resBox.innerHTML = `
      <table style="width: 100%; border-collapse: collapse; color: #cbd5e1; font-size: 0.92rem;">
        <tr><td style="padding: 6px 0;">Hersteller-Angabe:</td><td style="text-align: right; font-weight: bold; color: #f8fafc;">${val} ${unit} = ${bytes.toLocaleString()} Byte</td></tr>
        <tr><td style="padding: 6px 0;">Nutzbare Kapazität in GiB (IEC):</td><td style="text-align: right; font-weight: bold; color: #38bdf8;">${gib.toFixed(2)} GiB</td></tr>
        <tr><td style="padding: 6px 0;">Nutzbare Kapazität in TiB (IEC):</td><td style="text-align: right; font-weight: bold; color: #38bdf8;">${tib.toFixed(3)} TiB</td></tr>
        <tr style="border-top: 1px solid #334155;"><td style="padding: 8px 0; color: #facc15;">Scheinbarer Verlust durch Präfix-Unterschied:</td><td style="text-align: right; color: #facc15; font-weight: bold;">ca. ${unit === 'TB' ? '9,09 %' : '6,87 %'}</td></tr>
      </table>
      <div style="margin-top: 12px; font-size: 0.85rem; color: #94a3b8;">
        💡 <em>IHK-Prüfungsbegründung: Das Betriebssystem rechnet mit der Basis 1.024 (${unit === 'TB' ? '1.024⁴' : '1.024³'}). Es handelt sich um keinen physischen Datenverlust, sondern eine Diskrepanz zwischen SI- und IEC-Standard.</em>
      </div>
    `;
  }

  calcTime() {
    const amount = parseFloat(document.getElementById("pfx-data-amount").value) || 0;
    const unit = document.getElementById("pfx-data-unit").value;
    const speed = parseFloat(document.getElementById("pfx-net-speed").value) || 0;
    const speedUnit = document.getElementById("pfx-speed-unit").value;
    const overheadPct = parseFloat(document.getElementById("pfx-overhead").value) || 0;

    let bytes = 0;
    if (unit === "MiB") bytes = amount * Math.pow(1024, 2);
    if (unit === "GiB") bytes = amount * Math.pow(1024, 3);
    if (unit === "TiB") bytes = amount * Math.pow(1024, 4);

    let totalBits = bytes * 8 * (1 + overheadPct / 100);

    let bitsPerSec = 0;
    if (speedUnit === "Mbit") bitsPerSec = speed * 1e6;
    if (speedUnit === "Gbit") bitsPerSec = speed * 1e9;

    const seconds = totalBits / bitsPerSec;
    const minutes = seconds / 60;
    const hours = minutes / 60;

    const resBox = document.getElementById("pfx-time-result");
    resBox.style.display = "block";

    let timeString = "";
    if (hours >= 1) {
      const h = Math.floor(hours);
      const m = Math.floor((hours - h) * 60);
      const s = Math.round(seconds % 60);
      timeString = `${h} Stunden, ${m} Minuten, ${s} Sekunden`;
    } else if (minutes >= 1) {
      const m = Math.floor(minutes);
      const s = Math.round(seconds % 60);
      timeString = `${m} Minuten, ${s} Sekunden`;
    } else {
      timeString = `${seconds.toFixed(1)} Sekunden`;
    }

    resBox.innerHTML = `
      <table style="width: 100%; border-collapse: collapse; color: #cbd5e1; font-size: 0.92rem;">
        <tr><td style="padding: 6px 0;">Datenmenge (inkl. ${overheadPct}% Overhead):</td><td style="text-align: right; font-weight: bold; color: #f8fafc;">${(totalBits / 8 / 1024 / 1024).toFixed(1)} MiB (${(totalBits / 1e6).toFixed(0)} Mbit)</td></tr>
        <tr><td style="padding: 6px 0;">Nettoreichweite Übertragung:</td><td style="text-align: right; font-weight: bold; color: #38bdf8;">${speed} ${speedUnit}/s</td></tr>
        <tr style="border-top: 2px solid #22c55e;"><td style="padding: 10px 0; font-size: 1.05rem; font-weight: bold; color: #4ade80;">Berechnete Übertragungsdauer (t):</td><td style="text-align: right; font-size: 1.05rem; font-weight: bold; color: #4ade80;">${timeString} (${seconds.toFixed(1)} s)</td></tr>
      </table>
    `;
  }
}

document.addEventListener("DOMContentLoaded", () => {
  if (document.getElementById("prefix-converter-container")) {
    window.prefixConverter = new PrefixConverter("prefix-converter-container");
  }
});
