/**
 * Interaktiver Konfusionsmatrix- & ML-Kennzahlen-Rechner für FIDP
 * IHK ZPA Nord-West AP2
 */
(function() {
  function renderConfusionMatrix(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    container.innerHTML = `
      <div style="background: #0f172a; border: 1px solid #334155; border-radius: 8px; padding: 20px; color: #f8fafc;">
        <h4 style="color: #38bdf8; margin-top: 0; margin-bottom: 12px;">📊 Interaktiver Konfusionsmatrix-Rechner (FIDP)</h4>
        <p style="color: #94a3b8; font-size: 0.9rem; margin-bottom: 16px;">
          Geben Sie die Werte der 2x2-Konfusionsmatrix ein, um Accuracy, Precision, Recall und F1-Score nach IHK-Formeln live zu berechnen:
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; max-width: 480px; margin-bottom: 20px;">
          <div style="background: #1e293b; padding: 12px; border-radius: 6px; border-left: 4px solid #22c55e;">
            <label style="font-size: 0.85rem; color: #4ade80; display: block; font-weight: 600;">True Positive (TP)</label>
            <input type="number" id="cm_tp" value="80" min="0" class="ihk-input" style="width: 100%; margin-top: 6px;" />
          </div>
          <div style="background: #1e293b; padding: 12px; border-radius: 6px; border-left: 4px solid #f59e0b;">
            <label style="font-size: 0.85rem; color: #fcd34d; display: block; font-weight: 600;">False Positive (FP - Alpha-Fehler)</label>
            <input type="number" id="cm_fp" value="20" min="0" class="ihk-input" style="width: 100%; margin-top: 6px;" />
          </div>
          <div style="background: #1e293b; padding: 12px; border-radius: 6px; border-left: 4px solid #ef4444;">
            <label style="font-size: 0.85rem; color: #f87171; display: block; font-weight: 600;">False Negative (FN - Beta-Fehler)</label>
            <input type="number" id="cm_fn" value="10" min="0" class="ihk-input" style="width: 100%; margin-top: 6px;" />
          </div>
          <div style="background: #1e293b; padding: 12px; border-radius: 6px; border-left: 4px solid #3b82f6;">
            <label style="font-size: 0.85rem; color: #60a5fa; display: block; font-weight: 600;">True Negative (TN)</label>
            <input type="number" id="cm_tn" value="890" min="0" class="ihk-input" style="width: 100%; margin-top: 6px;" />
          </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; background: #1e293b; padding: 16px; border-radius: 6px;">
          <div>
            <div style="color: #94a3b8; font-size: 0.8rem;">Genauigkeit (Accuracy)</div>
            <div id="res_acc" style="font-size: 1.3rem; font-weight: bold; color: #38bdf8;">-- %</div>
            <div style="font-size: 0.75rem; color: #64748b;">(TP + TN) / Gesamt</div>
          </div>
          <div>
            <div style="color: #94a3b8; font-size: 0.8rem;">Präzision (Precision)</div>
            <div id="res_prec" style="font-size: 1.3rem; font-weight: bold; color: #fcd34d;">-- %</div>
            <div style="font-size: 0.75rem; color: #64748b;">TP / (TP + FP)</div>
          </div>
          <div>
            <div style="color: #94a3b8; font-size: 0.8rem;">Trefferquote (Recall)</div>
            <div id="res_rec" style="font-size: 1.3rem; font-weight: bold; color: #4ade80;">-- %</div>
            <div style="font-size: 0.75rem; color: #64748b;">TP / (TP + FN)</div>
          </div>
          <div>
            <div style="color: #94a3b8; font-size: 0.8rem;">Harmonisches Mittel (F1)</div>
            <div id="res_f1" style="font-size: 1.3rem; font-weight: bold; color: #c084fc;">--</div>
            <div style="font-size: 0.75rem; color: #64748b;">2 * (P * R) / (P + R)</div>
          </div>
        </div>
      </div>
    `;

    function update() {
      const tp = parseFloat(document.getElementById('cm_tp').value) || 0;
      const fp = parseFloat(document.getElementById('cm_fp').value) || 0;
      const fn = parseFloat(document.getElementById('cm_fn').value) || 0;
      const tn = parseFloat(document.getElementById('cm_tn').value) || 0;
      const total = tp + fp + fn + tn;

      if (total === 0) return;

      const acc = ((tp + tn) / total) * 100;
      const prec = (tp + fp > 0) ? (tp / (tp + fp)) * 100 : 0;
      const rec = (tp + fn > 0) ? (tp / (tp + fn)) * 100 : 0;
      const p = prec / 100;
      const r = rec / 100;
      const f1 = (p + r > 0) ? (2 * (p * r) / (p + r)) : 0;

      document.getElementById('res_acc').textContent = acc.toFixed(2) + ' %';
      document.getElementById('res_prec').textContent = prec.toFixed(2) + ' %';
      document.getElementById('res_rec').textContent = rec.toFixed(2) + ' %';
      document.getElementById('res_f1').textContent = f1.toFixed(3);
    }

    ['cm_tp', 'cm_fp', 'cm_fn', 'cm_tn'].forEach(id => {
      document.getElementById(id).addEventListener('input', update);
    });

    update();
  }

  window.renderConfusionMatrix = renderConfusionMatrix;
  document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('confusion-matrix-app')) {
      renderConfusionMatrix('confusion-matrix-app');
    }
  });
})();
