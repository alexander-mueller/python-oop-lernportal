/**
 * 🎨 IT-PRAXISPORTAL – DIAGRAMM STUDIO MAIN CONTROLLER
 * Schaltet nahtlos zwischen ER-Modell, Struktogramm (DIN 66261) und UML um.
 */

document.addEventListener('DOMContentLoaded', () => {
  const tabEr = document.getElementById('tab-btn-er');
  const tabSg = document.getElementById('tab-btn-struktogramm');
  const tabUml = document.getElementById('tab-btn-uml');

  const panelEr = document.getElementById('panel-er');
  const panelSg = document.getElementById('panel-struktogramm');
  const panelUml = document.getElementById('panel-uml');

  let erInstance = null;
  let sgInstance = null;
  let umlInstance = null;

  function switchTab(activeTab) {
    [tabEr, tabSg, tabUml].forEach(btn => btn && btn.classList.remove('active'));
    [panelEr, panelSg, panelUml].forEach(p => p && (p.style.display = 'none'));

    if (activeTab === 'er') {
      tabEr.classList.add('active');
      panelEr.style.display = 'block';
      if (!erInstance) {
        erInstance = new EREditor('panel-er');
      } else {
        erInstance.render();
      }
    } else if (activeTab === 'struktogramm') {
      tabSg.classList.add('active');
      panelSg.style.display = 'block';
      if (!sgInstance) {
        sgInstance = new StruktogrammEditor('panel-struktogramm');
      } else {
        sgInstance.render();
      }
    } else if (activeTab === 'uml') {
      tabUml.classList.add('active');
      panelUml.style.display = 'block';
      if (!umlInstance) {
        umlInstance = new UMLEditor('panel-uml');
      } else {
        umlInstance.render();
      }
    }
  }

  if (tabEr) tabEr.addEventListener('click', () => switchTab('er'));
  if (tabSg) tabSg.addEventListener('click', () => switchTab('struktogramm'));
  if (tabUml) tabUml.addEventListener('click', () => switchTab('uml'));

  // Handle URL hash parameters (z.B. #struktogramm oder #uml oder #er)
  const hash = window.location.hash.replace('#', '').toLowerCase();
  if (hash === 'struktogramm' || hash === 'sg') {
    switchTab('struktogramm');
  } else if (hash === 'uml') {
    switchTab('uml');
  } else {
    switchTab('er');
  }
});
