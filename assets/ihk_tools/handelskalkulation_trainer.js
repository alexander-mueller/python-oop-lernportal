/**
 * Interaktiver Handelskalkulations-Trainer für ITSM & KDM
 * IHK ZPA Nord-West AP2
 */
(function() {
  function renderHandelskalkulation(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    container.innerHTML = `
      <div style="background: #0f172a; border: 1px solid #334155; border-radius: 8px; padding: 20px; color: #f8fafc;">
        <h4 style="color: #38bdf8; margin-top: 0; margin-bottom: 12px;">📊 Interaktiver Handelskalkulations-Trainer (ITSM / KDM)</h4>
        <p style="color: #94a3b8; font-size: 0.9rem; margin-bottom: 16px;">
          Geben Sie die kaufmännischen Eckdaten ein, um das Vorwärtskalkulations-Schema nach IHK-Standard durchzurechnen:
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-bottom: 20px;">
          <div style="background: #1e293b; padding: 10px; border-radius: 6px;">
            <label style="font-size: 0.8rem; color: #cbd5e1; display: block;">Listeneinkaufspreis (LEP €)</label>
            <input type="number" id="kalk_lep" value="3000" min="0" step="50" class="ihk-input" style="width: 100%; margin-top: 4px;" />
          </div>
          <div style="background: #1e293b; padding: 10px; border-radius: 6px;">
            <label style="font-size: 0.8rem; color: #cbd5e1; display: block;">Lieferantenrabatt (%)</label>
            <input type="number" id="kalk_rab" value="20" min="0" max="100" class="ihk-input" style="width: 100%; margin-top: 4px;" />
          </div>
          <div style="background: #1e293b; padding: 10px; border-radius: 6px;">
            <label style="font-size: 0.8rem; color: #cbd5e1; display: block;">Lieferantenskonto (%)</label>
            <input type="number" id="kalk_sko" value="2" min="0" max="100" class="ihk-input" style="width: 100%; margin-top: 4px;" />
          </div>
          <div style="background: #1e293b; padding: 10px; border-radius: 6px;">
            <label style="font-size: 0.8rem; color: #cbd5e1; display: block;">Bezugskosten (€)</label>
            <input type="number" id="kalk_bezug" value="50" min="0" step="5" class="ihk-input" style="width: 100%; margin-top: 4px;" />
          </div>
          <div style="background: #1e293b; padding: 10px; border-radius: 6px;">
            <label style="font-size: 0.8rem; color: #cbd5e1; display: block;">Handlungskosten HKZ (%)</label>
            <input type="number" id="kalk_hkz" value="15" min="0" class="ihk-input" style="width: 100%; margin-top: 4px;" />
          </div>
          <div style="background: #1e293b; padding: 10px; border-radius: 6px;">
            <label style="font-size: 0.8rem; color: #cbd5e1; display: block;">Gewinnzuschlag (%)</label>
            <input type="number" id="kalk_gewinn" value="25" min="0" class="ihk-input" style="width: 100%; margin-top: 4px;" />
          </div>
        </div>

        <div style="background: #1e293b; border-radius: 6px; padding: 16px; font-family: monospace; font-size: 0.9rem; line-height: 1.8;">
          <div style="display: flex; justify-content: space-between;"><span>Listeneinkaufspreis:</span> <span id="out_lep">0,00 €</span></div>
          <div style="display: flex; justify-content: space-between; color: #f87171;"><span>- Lieferantenrabatt:</span> <span id="out_rab">0,00 €</span></div>
          <div style="display: flex; justify-content: space-between; border-top: 1px solid #475569;"><span>= Zieleinkaufspreis:</span> <span id="out_zep">0,00 €</span></div>
          <div style="display: flex; justify-content: space-between; color: #f87171;"><span>- Lieferantenskonto:</span> <span id="out_sko">0,00 €</span></div>
          <div style="display: flex; justify-content: space-between; border-top: 1px solid #475569;"><span>= Bareinkaufspreis:</span> <span id="out_bep">0,00 €</span></div>
          <div style="display: flex; justify-content: space-between; color: #38bdf8;"><span>+ Bezugskosten:</span> <span id="out_bezug">0,00 €</span></div>
          <div style="display: flex; justify-content: space-between; border-top: 1px solid #475569; font-weight: bold; color: #fcd34d;"><span>= Einstandspreis (Bezugspreis):</span> <span id="out_einstand">0,00 €</span></div>
          <div style="display: flex; justify-content: space-between; color: #38bdf8;"><span>+ Handlungskosten:</span> <span id="out_hkz">0,00 €</span></div>
          <div style="display: flex; justify-content: space-between; border-top: 1px solid #475569;"><span>= Selbstkostenpreis:</span> <span id="out_sk">0,00 €</span></div>
          <div style="display: flex; justify-content: space-between; color: #4ade80;"><span>+ Gewinnzuschlag:</span> <span id="out_gewinn">0,00 €</span></div>
          <div style="display: flex; justify-content: space-between; border-top: 2px solid #38bdf8; font-weight: bold; font-size: 1.05rem; color: #38bdf8; padding-top: 4px;"><span>= Barverkaufspreis (BVP netto):</span> <span id="out_bvp">0,00 €</span></div>
        </div>
      </div>
    `;

    function update() {
      const lep = parseFloat(document.getElementById('kalk_lep').value) || 0;
      const rabP = parseFloat(document.getElementById('kalk_rab').value) || 0;
      const skoP = parseFloat(document.getElementById('kalk_sko').value) || 0;
      const bezug = parseFloat(document.getElementById('kalk_bezug').value) || 0;
      const hkzP = parseFloat(document.getElementById('kalk_hkz').value) || 0;
      const gewinnP = parseFloat(document.getElementById('kalk_gewinn').value) || 0;

      const rab = lep * (rabP / 100);
      const zep = lep - rab;
      const sko = zep * (skoP / 100);
      const bep = zep - sko;
      const einstand = bep + bezug;
      const hkz = einstand * (hkzP / 100);
      const sk = einstand + hkz;
      const gewinn = sk * (gewinnP / 100);
      const bvp = sk + gewinn;

      const fmt = (v) => v.toLocaleString('de-DE', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + ' €';

      document.getElementById('out_lep').textContent = fmt(lep);
      document.getElementById('out_rab').textContent = '- ' + fmt(rab);
      document.getElementById('out_zep').textContent = fmt(zep);
      document.getElementById('out_sko').textContent = '- ' + fmt(sko);
      document.getElementById('out_bep').textContent = fmt(bep);
      document.getElementById('out_bezug').textContent = '+ ' + fmt(bezug);
      document.getElementById('out_einstand').textContent = fmt(einstand);
      document.getElementById('out_hkz').textContent = '+ ' + fmt(hkz);
      document.getElementById('out_sk').textContent = fmt(sk);
      document.getElementById('out_gewinn').textContent = '+ ' + fmt(gewinn);
      document.getElementById('out_bvp').textContent = fmt(bvp);
    }

    ['kalk_lep', 'kalk_rab', 'kalk_sko', 'kalk_bezug', 'kalk_hkz', 'kalk_gewinn'].forEach(id => {
      document.getElementById(id).addEventListener('input', update);
    });

    update();
  }

  window.renderHandelskalkulation = renderHandelskalkulation;
  document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('handelskalkulation-app')) {
      renderHandelskalkulation('handelskalkulation-app');
    }
  });
})();
