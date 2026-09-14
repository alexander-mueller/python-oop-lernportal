/**
 * Interaktiver Purdue-Referenzmodell & OT-Zonen-Trainer für FIDV
 * IHK ZPA Nord-West AP2
 */
(function() {
  function renderPurdueTrainer(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const items = [
      { name: "PT100 Temperaturfühler & Drucktransmitter", level: "0", hint: "Physikalischer Prozess / Sensorik & Aktorik" },
      { name: "Siemens S7-1500 SPS & Frequenzumrichter", level: "1", hint: "Basis-Steuerung (Direct Control)" },
      { name: "KTP700 HMI-Touchpanel & Bedienstation", level: "2", hint: "Bereichsbedienung & Monitoring" },
      { name: "SCADA-Server & Manufacturing Execution System (MES)", level: "3", hint: "Betriebsleitebene / Fertigungssteuerung" },
      { name: "Historian-Spiegel & Jump Host (Fernwartung)", level: "3.5", hint: "Industrial DMZ (Puffer zwischen IT und OT)" },
      { name: "SAP ERP & Active Directory der Verwaltung", level: "4", hint: "Enterprise IT / Unternehmensebene" }
    ];

    container.innerHTML = `
      <div style="background: #0f172a; border: 1px solid #334155; border-radius: 8px; padding: 20px; color: #f8fafc;">
        <h4 style="color: #38bdf8; margin-top: 0; margin-bottom: 12px;">🏭 Interaktiver Purdue-Modell & OT-Zonen Trainer (FIDV)</h4>
        <p style="color: #94a3b8; font-size: 0.9rem; margin-bottom: 16px;">
          Ordnen Sie die Komponenten den korrekten Purdue-Ebenen nach IEC 62443 / ANSI/ISA-95 zu:
        </p>
        <div id="purdue_items" style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 16px;">
          ${items.map((item, idx) => `
            <div style="display: flex; justify-content: space-between; align-items: center; background: #1e293b; padding: 10px 14px; border-radius: 6px;">
              <span style="font-size: 0.9rem; color: #cbd5e1;">${item.name}</span>
              <select id="purdue_sel_${idx}" class="ihk-select" style="padding: 6px 10px; border-radius: 4px; background: #0f172a; color: #f8fafc; border: 1px solid #475569;">
                <option value="">-- Ebene wählen --</option>
                <option value="0">Level 0: Physikalischer Prozess</option>
                <option value="1">Level 1: Basis-Steuerung (SPS)</option>
                <option value="2">Level 2: Bereichsbedienung (HMI)</option>
                <option value="3">Level 3: Leitebene (MES/SCADA)</option>
                <option value="3.5">Level 3.5: Industrial DMZ (IDMZ)</option>
                <option value="4">Level 4: Enterprise IT (ERP)</option>
              </select>
            </div>
          `).join('')}
        </div>
        <div style="display: flex; gap: 10px; align-items: center;">
          <button id="purdue_check_btn" class="ihk-btn ihk-btn-primary" style="padding: 8px 16px;">Ergebnis prüfen</button>
          <span id="purdue_feedback" style="font-size: 0.9rem; font-weight: 600;"></span>
        </div>
      </div>
    `;

    document.getElementById('purdue_check_btn').addEventListener('click', () => {
      let correct = 0;
      items.forEach((item, idx) => {
        const sel = document.getElementById(`purdue_sel_${idx}`);
        if (sel.value === item.level) {
          sel.style.borderColor = '#22c55e';
          correct++;
        } else {
          sel.style.borderColor = '#ef4444';
        }
      });
      const fb = document.getElementById('purdue_feedback');
      if (correct === items.length) {
        fb.style.color = '#4ade80';
        fb.textContent = `🎉 Perfekt! Alle ${correct}/${items.length} Ebenen korrekt nach IEC 62443 zugeordnet.`;
      } else {
        fb.style.color = '#f87171';
        fb.textContent = `${correct}/${items.length} richtig. Prüfen Sie die rot markierten Ebenen.`;
      }
    });
  }

  window.renderPurdueTrainer = renderPurdueTrainer;
  document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('purdue-trainer-app')) {
      renderPurdueTrainer('purdue-trainer-app');
    }
  });
})();
