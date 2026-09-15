/**
 * Interaktiver USV- & Scheinleistungs-Kalkulator für ITSE
 * IHK ZPA Nord-West AP2
 */
(function() {
  function renderUSVCalculator(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    container.innerHTML = `
      <div style="background: #0f172a; border: 1px solid #334155; border-radius: 8px; padding: 20px; color: #f8fafc;">
        <h4 style="color: #38bdf8; margin-top: 0; margin-bottom: 12px;">⚡ Interaktiver USV-Dimensionierungs-Rechner (ITSE)</h4>
        <p style="color: #94a3b8; font-size: 0.9rem; margin-bottom: 16px;">
          Berechnen Sie die Wirkleistung, Scheinleistung und empfohlene USV-Nennleistung nach IHK-Prüfungsformel:
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; margin-bottom: 20px;">
          <div style="background: #1e293b; padding: 12px; border-radius: 6px;">
            <label style="font-size: 0.85rem; color: #38bdf8; display: block; font-weight: 600;">Wirkleistung Verbraucher P (W)</label>
            <input type="number" id="usv_p" value="2640" min="10" step="50" class="ihk-input" style="width: 100%; margin-top: 6px;" />
          </div>
          <div style="background: #1e293b; padding: 12px; border-radius: 6px;">
            <label style="font-size: 0.85rem; color: #fcd34d; display: block; font-weight: 600;">Leistungsfaktor cos φ</label>
            <input type="number" id="usv_cos" value="0.9" min="0.5" max="1.0" step="0.05" class="ihk-input" style="width: 100%; margin-top: 6px;" />
          </div>
          <div style="background: #1e293b; padding: 12px; border-radius: 6px;">
            <label style="font-size: 0.85rem; color: #4ade80; display: block; font-weight: 600;">Sicherheitsreserve (%)</label>
            <input type="number" id="usv_reserve" value="25" min="0" max="100" step="5" class="ihk-input" style="width: 100%; margin-top: 6px;" />
          </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; background: #1e293b; padding: 16px; border-radius: 6px;">
          <div>
            <div style="color: #94a3b8; font-size: 0.8rem;">Wirkleistung (P)</div>
            <div id="res_usv_p" style="font-size: 1.25rem; font-weight: bold; color: #38bdf8;">-- kW</div>
            <div style="font-size: 0.75rem; color: #64748b;">Thermische Last</div>
          </div>
          <div>
            <div style="color: #94a3b8; font-size: 0.8rem;">Scheinleistung (S = P / cos φ)</div>
            <div id="res_usv_s" style="font-size: 1.25rem; font-weight: bold; color: #fcd34d;">-- kVA</div>
            <div style="font-size: 0.75rem; color: #64748b;">Elektrische Auslegung</div>
          </div>
          <div>
            <div style="color: #94a3b8; font-size: 0.8rem;">Empf. USV-Nennleistung</div>
            <div id="res_usv_rec" style="font-size: 1.25rem; font-weight: bold; color: #4ade80;">-- kVA</div>
            <div style="font-size: 0.75rem; color: #64748b;">Inkl. Sicherheitszuschlag</div>
          </div>
        </div>
      </div>
    `;

    function update() {
      const p = parseFloat(document.getElementById('usv_p').value) || 0;
      const cos = parseFloat(document.getElementById('usv_cos').value) || 0.9;
      const reserve = parseFloat(document.getElementById('usv_reserve').value) || 20;

      const s = cos > 0 ? (p / cos) : 0;
      const rec = s * (1 + reserve / 100);

      document.getElementById('res_usv_p').textContent = (p / 1000).toFixed(2) + ' kW';
      document.getElementById('res_usv_s').textContent = (s / 1000).toFixed(2) + ' kVA';
      document.getElementById('res_usv_rec').textContent = (rec / 1000).toFixed(2) + ' kVA';
    }

    ['usv_p', 'usv_cos', 'usv_reserve'].forEach(id => {
      document.getElementById(id).addEventListener('input', update);
    });

    update();
  }

  window.renderUSVCalculator = renderUSVCalculator;
  document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('usv-calculator-app')) {
      renderUSVCalculator('usv-calculator-app');
    }
  });
})();
