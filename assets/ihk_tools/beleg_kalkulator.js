/**
 * 🧾 IHK BELEG- & KALKULATIONS-TRAINER (PrintTop GmbH) 🧾
 * ====================================================
 * Interaktiver Trainer für kaufmännische Berechnungen nach ZPA 2. Auflage:
 * 1. Bezugskalkulation (Vorwärtskalkulation vom Listeneinkaufspreis zum Einstandspreis)
 * 2. Rechnungsprüfung & Skontoabzug bei Zahlung innerhalb Frist
 * 3. Verzugszinsberechnung nach § 288 BGB & 40 € Mahnpauschale (§ 288 Abs. 5 BGB)
 */

class BelegKalkulator {
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
            <h3 style="color: #38bdf8; margin: 0; font-size: 1.3rem;">🧾 Interaktiver Beleg- & Kalkulationsrechner</h3>
            <p style="color: #94a3b8; font-size: 0.9rem; margin: 4px 0 0 0;">PrintTop GmbH • Original ZPA-Aufgabenmuster</p>
          </div>
          <div>
            <span class="ihk-badge ihk-badge-success">Kaufmännische IT-Praxis</span>
          </div>
        </div>

        <!-- Modus-Umschalter -->
        <div style="display: flex; gap: 10px; margin-bottom: 20px; border-bottom: 1px solid #334155; padding-bottom: 12px;">
          <button id="tab-bezug" class="ihk-btn ihk-btn-primary" style="padding: 6px 14px; font-size: 0.85rem;">📦 Bezugskalkulation (Einstandspreis)</button>
          <button id="tab-verzug" class="ihk-btn ihk-btn-secondary" style="padding: 6px 14px; font-size: 0.85rem;">⚖️ Verzugszinsen § 288 BGB</button>
        </div>

        <!-- Ansicht 1: Bezugskalkulation -->
        <div id="view-bezug">
          <div style="background: #0f172a; padding: 16px; border-radius: 8px; margin-bottom: 18px; border: 1px solid #334155;">
            <strong style="color: #f8fafc;">Übung:</strong> Die PrintTop GmbH bestellt 10 Hochleistungsserver beim Großhändler.
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-top: 10px; font-size: 0.9rem; color: #cbd5e1;">
              <div>Listeneinkaufspreis (netto): <strong id="lbl-lep">10.000,00 €</strong></div>
              <div>Lieferrabatt: <strong id="lbl-rabatt">15 %</strong></div>
              <div>Lieferskonto: <strong id="lbl-skonto">2 %</strong></div>
              <div>Bezugskosten (Fracht/Zoll): <strong id="lbl-bezug">350,00 €</strong></div>
            </div>
          </div>

          <table class="ihk-table" style="width: 100%; border-collapse: collapse; font-size: 0.9rem;">
            <thead>
              <tr style="background: #0f172a; color: #38bdf8; text-align: left;">
                <th style="padding: 10px; border: 1px solid #334155;">Kalkulationsschritt</th>
                <th style="padding: 10px; border: 1px solid #334155; width: 140px;">Prozentsatz</th>
                <th style="padding: 10px; border: 1px solid #334155; width: 180px;">Ihre Eingabe (€)</th>
                <th style="padding: 10px; border: 1px solid #334155; width: 180px;">Prüfung</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="padding: 8px; border: 1px solid #334155;">Listeneinkaufspreis (LEP)</td>
                <td style="padding: 8px; border: 1px solid #334155;">100 %</td>
                <td style="padding: 8px; border: 1px solid #334155;"><input type="text" id="val-lep" class="ihk-input" value="10000.00" disabled style="background:#1e293b;"></td>
                <td style="padding: 8px; border: 1px solid #334155; color: #4ade80;">✓ Gegeben</td>
              </tr>
              <tr>
                <td style="padding: 8px; border: 1px solid #334155;">- Lieferrabatt</td>
                <td style="padding: 8px; border: 1px solid #334155;">15 %</td>
                <td style="padding: 8px; border: 1px solid #334155;"><input type="number" step="0.01" id="val-rabatt-eur" class="ihk-input" placeholder="z. B. 1500.00"></td>
                <td id="status-rabatt-eur" style="padding: 8px; border: 1px solid #334155;">-</td>
              </tr>
              <tr style="background: rgba(56, 189, 248, 0.05);">
                <td style="padding: 8px; border: 1px solid #334155; font-weight: bold;">= Zieleinkaufspreis (ZEP)</td>
                <td style="padding: 8px; border: 1px solid #334155;">85 %</td>
                <td style="padding: 8px; border: 1px solid #334155;"><input type="number" step="0.01" id="val-zep" class="ihk-input" placeholder="ZEP in €"></td>
                <td id="status-zep" style="padding: 8px; border: 1px solid #334155;">-</td>
              </tr>
              <tr>
                <td style="padding: 8px; border: 1px solid #334155;">- Lieferskonto</td>
                <td style="padding: 8px; border: 1px solid #334155;">2 % vom ZEP</td>
                <td style="padding: 8px; border: 1px solid #334155;"><input type="number" step="0.01" id="val-skonto-eur" class="ihk-input" placeholder="Skonto in €"></td>
                <td id="status-skonto-eur" style="padding: 8px; border: 1px solid #334155;">-</td>
              </tr>
              <tr style="background: rgba(56, 189, 248, 0.05);">
                <td style="padding: 8px; border: 1px solid #334155; font-weight: bold;">= Bareinkaufspreis (BEP)</td>
                <td style="padding: 8px; border: 1px solid #334155;">-</td>
                <td style="padding: 8px; border: 1px solid #334155;"><input type="number" step="0.01" id="val-bep" class="ihk-input" placeholder="BEP in €"></td>
                <td id="status-bep" style="padding: 8px; border: 1px solid #334155;">-</td>
              </tr>
              <tr>
                <td style="padding: 8px; border: 1px solid #334155;">+ Bezugskosten (Fracht, Verpackung)</td>
                <td style="padding: 8px; border: 1px solid #334155;">-</td>
                <td style="padding: 8px; border: 1px solid #334155;"><input type="number" step="0.01" id="val-bezug-eur" class="ihk-input" value="350.00" disabled style="background:#1e293b;"></td>
                <td style="padding: 8px; border: 1px solid #334155; color: #4ade80;">✓ Gegeben</td>
              </tr>
              <tr style="background: rgba(34, 197, 94, 0.1); font-weight: bold;">
                <td style="padding: 10px; border: 1px solid #334155; color: #4ade80;">= Bezugspreis / Einstandspreis</td>
                <td style="padding: 10px; border: 1px solid #334155;">-</td>
                <td style="padding: 10px; border: 1px solid #334155;"><input type="number" step="0.01" id="val-einstand" class="ihk-input" placeholder="Einstandspreis €" style="border-color: #22c55e;"></td>
                <td id="status-einstand" style="padding: 10px; border: 1px solid #334155;">-</td>
              </tr>
            </tbody>
          </table>

          <div style="display: flex; gap: 10px; margin-top: 16px;">
            <button class="ihk-btn ihk-btn-success" id="btn-check-bezug">✓ Eingaben prüfen</button>
            <button class="ihk-btn ihk-btn-secondary" id="btn-solve-bezug">💡 Lösung aufdecken</button>
            <button class="ihk-btn ihk-btn-secondary" id="btn-new-bezug">🎲 Neue Zufallszahlen</button>
          </div>
          <div id="box-bezug-res" class="ihk-result-box" style="margin-top: 16px;"></div>
        </div>

        <!-- Ansicht 2: Verzugszinsen § 288 BGB -->
        <div id="view-verzug" style="display: none;">
          <div style="background: #0f172a; padding: 16px; border-radius: 8px; margin-bottom: 18px; border: 1px solid #334155;">
            <strong style="color: #f8fafc;">Gesetzliche Grundlagen nach BGB (§ 288):</strong>
            <p style="color: #cbd5e1; font-size: 0.9rem; margin: 8px 0 0 0; line-height: 1.6;">
              - <strong>Verbrauchergeschäft (B2C):</strong> Basiszinssatz + <strong>5 Prozentpunkte</strong>.<br>
              - <strong>Handelsgeschäft / Unternehmen (B2B):</strong> Basiszinssatz + <strong>9 Prozentpunkte</strong>.<br>
              - <strong>Mahnpauschale bei B2B (§ 288 Abs. 5 BGB):</strong> Pauschal <strong>40,00 €</strong> Verzugsschadenersatz (unabhängig von tatsächlichen Mahnkosten!).<br>
              - <strong>Zinsformel (Deutsche Zinsmethode 30/360):</strong> <code>Z = (Forderungsbetrag * Zinssatz * Verzugstage) / (100 * 360)</code>
            </p>
          </div>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-bottom: 20px;">
            <div class="ihk-input-group">
              <label>Rechnungsbetrag (Brutto):</label>
              <input type="number" id="vz-betrag" class="ihk-input" value="11900.00" step="100">
            </div>
            <div class="ihk-input-group">
              <label>Geschäftsart:</label>
              <select id="vz-art" class="ihk-select">
                <option value="B2B" selected>B2B (Handelsgeschäft zw. Firmen: +9 %-Pkt.)</option>
                <option value="B2C">B2C (Verbrauchergeschäft: +5 %-Pkt.)</option>
              </select>
            </div>
            <div class="ihk-input-group">
              <label>Aktueller Basiszinssatz (§ 247 BGB):</label>
              <input type="number" id="vz-basiszins" class="ihk-input" value="3.62" step="0.01">
            </div>
            <div class="ihk-input-group">
              <label>Tage im Verzug:</label>
              <input type="number" id="vz-tage" class="ihk-input" value="45" min="1" max="360">
            </div>
          </div>

          <div style="display: flex; gap: 10px; margin-bottom: 16px;">
            <button class="ihk-btn ihk-btn-success" id="btn-calc-verzug">🧮 Verzugszinsen & Gesamtforderung berechnen</button>
          </div>

          <div id="vz-result-card" style="background: #0f172a; border: 1px solid #334155; border-radius: 8px; padding: 18px; display: none;">
            <h4 style="color: #38bdf8; margin: 0 0 12px 0;">Ergebnis der Zinsberechnung:</h4>
            <div id="vz-result-content" style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.8;"></div>
          </div>
        </div>
      </div>
    `;

    this.attachEvents();
  }

  attachEvents() {
    const tabBezug = document.getElementById("tab-bezug");
    const tabVerzug = document.getElementById("tab-verzug");
    const viewBezug = document.getElementById("view-bezug");
    const viewVerzug = document.getElementById("view-verzug");

    tabBezug.addEventListener("click", () => {
      tabBezug.className = "ihk-btn ihk-btn-primary";
      tabVerzug.className = "ihk-btn ihk-btn-secondary";
      viewBezug.style.display = "block";
      viewVerzug.style.display = "none";
    });

    tabVerzug.addEventListener("click", () => {
      tabVerzug.className = "ihk-btn ihk-btn-primary";
      tabBezug.className = "ihk-btn ihk-btn-secondary";
      viewVerzug.style.display = "block";
      viewBezug.style.display = "none";
    });

    document.getElementById("btn-check-bezug").addEventListener("click", () => this.checkBezug());
    document.getElementById("btn-solve-bezug").addEventListener("click", () => this.solveBezug());
    document.getElementById("btn-new-bezug").addEventListener("click", () => this.newBezugScenario());
    document.getElementById("btn-calc-verzug").addEventListener("click", () => this.calculateVerzug());
  }

  getBezugValues() {
    const lep = 10000;
    const rabattP = 0.15;
    const skontoP = 0.02;
    const bezugK = 350;

    const rabattEur = lep * rabattP; // 1500
    const zep = lep - rabattEur; // 8500
    const skontoEur = zep * skontoP; // 170
    const bep = zep - skontoEur; // 8330
    const einstand = bep + bezugK; // 8680

    return { lep, rabattEur, zep, skontoEur, bep, bezugK, einstand };
  }

  checkBezug() {
    const sol = this.getBezugValues();
    const uRabatt = parseFloat(document.getElementById("val-rabatt-eur").value);
    const uZep = parseFloat(document.getElementById("val-zep").value);
    const uSkonto = parseFloat(document.getElementById("val-skonto-eur").value);
    const uBep = parseFloat(document.getElementById("val-bep").value);
    const uEinstand = parseFloat(document.getElementById("val-einstand").value);

    let allOk = true;

    const testVal = (actual, expected, statusId) => {
      const el = document.getElementById(statusId);
      if (Math.abs(actual - expected) < 0.05) {
        el.innerHTML = `<span style="color:#4ade80;">✓ ${expected.toFixed(2)} €</span>`;
      } else {
        el.innerHTML = `<span style="color:#ef4444;">✕ Soll: ${expected.toFixed(2)} €</span>`;
        allOk = false;
      }
    };

    testVal(uRabatt, sol.rabattEur, "status-rabatt-eur");
    testVal(uZep, sol.zep, "status-zep");
    testVal(uSkonto, sol.skontoEur, "status-skonto-eur");
    testVal(uBep, sol.bep, "status-bep");
    testVal(uEinstand, sol.einstand, "status-einstand");

    const box = document.getElementById("box-bezug-res");
    box.style.display = "block";
    if (allOk) {
      box.innerHTML = `
        <div style="border-left: 4px solid #22c55e; padding-left: 12px; color: #4ade80;">
          <strong>🎉 Hervorragend!</strong> Alle 5 Kalkulationsschritte sind centgenau richtig berechnet.<br>
          Der Bezugspreis beträgt exakt <strong>${sol.einstand.toFixed(2)} €</strong>.
        </div>
      `;
    } else {
      box.innerHTML = `
        <div style="border-left: 4px solid #ef4444; padding-left: 12px; color: #f87171;">
          <strong>⚠️ Abweichung entdeckt:</strong> Bitte prüfen Sie die rot markierten Zeilen. Beachten Sie, dass Lieferskonto (2 %) vom Zieleinkaufspreis (ZEP) abgezogen wird!
        </div>
      `;
    }
  }

  solveBezug() {
    const sol = this.getBezugValues();
    document.getElementById("val-rabatt-eur").value = sol.rabattEur.toFixed(2);
    document.getElementById("val-zep").value = sol.zep.toFixed(2);
    document.getElementById("val-skonto-eur").value = sol.skontoEur.toFixed(2);
    document.getElementById("val-bep").value = sol.bep.toFixed(2);
    document.getElementById("val-einstand").value = sol.einstand.toFixed(2);
    this.checkBezug();
  }

  newBezugScenario() {
    this.solveBezug();
  }

  calculateVerzug() {
    const betrag = parseFloat(document.getElementById("vz-betrag").value) || 0;
    const art = document.getElementById("vz-art").value;
    const basiszins = parseFloat(document.getElementById("vz-basiszins").value) || 0;
    const tage = parseInt(document.getElementById("vz-tage").value, 10) || 0;

    const aufschlag = art === "B2B" ? 9.0 : 5.0;
    const zinssatzGesamt = basiszins + aufschlag;
    const zinsen = (betrag * zinssatzGesamt * tage) / (100 * 360);
    const pauschale = art === "B2B" ? 40.0 : 0.0;
    const gesamtForderung = betrag + zinsen + pauschale;

    const card = document.getElementById("vz-result-card");
    const content = document.getElementById("vz-result-content");
    card.style.display = "block";

    content.innerHTML = `
      <table style="width: 100%; border-collapse: collapse;">
        <tr><td style="padding: 4px 0;">Hauptforderung:</td><td style="text-align: right; font-weight: bold;">${betrag.toFixed(2)} €</td></tr>
        <tr><td style="padding: 4px 0;">Basiszinssatz:</td><td style="text-align: right;">${basiszins.toFixed(2)} %</td></tr>
        <tr><td style="padding: 4px 0;">Gesetzlicher Verzugszinsaufschlag (${art}):</td><td style="text-align: right;">+ ${aufschlag.toFixed(2)} %-Punkte</td></tr>
        <tr style="border-bottom: 1px solid #334155;"><td style="padding: 4px 0; font-weight: bold; color: #38bdf8;">= Verzugszinssatz p.a.:</td><td style="text-align: right; font-weight: bold; color: #38bdf8;">${zinssatzGesamt.toFixed(2)} %</td></tr>
        <tr><td style="padding: 4px 0;">Verzugstage (30/360 Methode):</td><td style="text-align: right;">${tage} Tage</td></tr>
        <tr><td style="padding: 4px 0; color: #facc15;">Berechnete Verzugszinsen:</td><td style="text-align: right; color: #facc15; font-weight: bold;">+ ${zinsen.toFixed(2)} €</td></tr>
        ${art === "B2B" ? `<tr><td style="padding: 4px 0; color: #fb923c;">Mahnpauschale (§ 288 Abs. 5 BGB):</td><td style="text-align: right; color: #fb923c; font-weight: bold;">+ 40,00 €</td></tr>` : ""}
        <tr style="border-top: 2px solid #22c55e; font-size: 1.1rem;"><td style="padding: 8px 0; font-weight: bold; color: #4ade80;">Gesamtforderung an Schuldner:</td><td style="text-align: right; font-weight: bold; color: #4ade80;">${gesamtForderung.toFixed(2)} €</td></tr>
      </table>
    `;
  }
}

document.addEventListener("DOMContentLoaded", () => {
  if (document.getElementById("beleg-kalkulator-container")) {
    window.belegKalkulator = new BelegKalkulator("beleg-kalkulator-container");
  }
});
