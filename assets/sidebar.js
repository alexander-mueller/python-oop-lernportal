/**
 * 🧭 NEXT-GEN SIDEBAR COMPONENT 🧭
 * =================================
 * Rendert eine saubere, linksbündige Sidebar-Navigation
 * für das Hauptportal und alle 27 Kapitel-Seiten.
 */

(function () {
  const LEHRPFADE = [
    {
      id: "lehrpfad_1",
      title: "🌱 1. Grundlagen",
      badge: "G01–G10",
      items: [
        { id: "01_erste_schritte_taschenrechner", num: "G01", icon: "🧮", title: "Taschenrechner", path: "lehrpfad_1_grundlagen/01_erste_schritte_taschenrechner/index.html" },
        { id: "02_variablen_und_datentypen", num: "G02", icon: "📦", title: "Variablen & Typen", path: "lehrpfad_1_grundlagen/02_variablen_und_datentypen/index.html" },
        { id: "03_ein_und_ausgabe", num: "G03", icon: "💬", title: "Ein- & Ausgabe", path: "lehrpfad_1_grundlagen/03_ein_und_ausgabe/index.html" },
        { id: "04_verzweigungen_und_bedingungen", num: "G04", icon: "🚦", title: "Bedingungen (if)", path: "lehrpfad_1_grundlagen/04_verzweigungen_und_bedingungen/index.html" },
        { id: "05_schleifen_und_wiederholungen", num: "G05", icon: "🎡", title: "Schleifen (for/while)", path: "lehrpfad_1_grundlagen/05_schleifen_und_wiederholungen/index.html" },
        { id: "06_funktionen_und_module", num: "G06", icon: "🪄", title: "Funktionen & Module", path: "lehrpfad_1_grundlagen/06_funktionen_und_module/index.html" },
        { id: "07_listen_und_sequenzen", num: "G07", icon: "📋", title: "Listen & Sequenzen", path: "lehrpfad_1_grundlagen/07_listen_und_sequenzen/index.html" },
        { id: "08_textverarbeitung_und_strings", num: "G08", icon: "🔤", title: "String-Methoden", path: "lehrpfad_1_grundlagen/08_textverarbeitung_und_strings/index.html" },
        { id: "09_dictionaries_und_sets", num: "G09", icon: "🗃️", title: "Dicts & Sets", path: "lehrpfad_1_grundlagen/09_dictionaries_und_sets/index.html" },
        { id: "10_comprehensions_datum_algorithmen", num: "G10", icon: "🚀", title: "Comprehensions", path: "lehrpfad_1_grundlagen/10_comprehensions_datum_algorithmen/index.html" },
      ]
    },
    {
      id: "lehrpfad_2",
      title: "🏗️ 2. OOP Einstieg",
      badge: "00–06",
      items: [
        { id: "00_fehlersuche_und_grundlagen", num: "00", icon: "🔍", title: "Fehlersuche & Debug", path: "lehrpfad_2_oop_einstieg/00_fehlersuche_und_grundlagen/index.html" },
        { id: "01_einstieg_klassen", num: "01", icon: "🏗️", title: "Einstieg in Klassen", path: "lehrpfad_2_oop_einstieg/01_einstieg_klassen/index.html" },
        { id: "02_init_und_self", num: "02", icon: "⚙️", title: "Konstruktor & self", path: "lehrpfad_2_oop_einstieg/02_init_und_self/index.html" },
        { id: "03_methoden_und_verhalten", num: "03", icon: "🏎️", title: "Methoden & Verhalten", path: "lehrpfad_2_oop_einstieg/03_methoden_und_verhalten/index.html" },
        { id: "04_str_und_darstellung", num: "04", icon: "🧾", title: "__str__ Darstellung", path: "lehrpfad_2_oop_einstieg/04_str_und_darstellung/index.html" },
        { id: "04b_umstieg_vscode", num: "04b", icon: "💻", title: "VS Code Setup", path: "lehrpfad_2_oop_einstieg/04b_umstieg_vscode/index.html" },
        { id: "04c_git_und_versionskontrolle", num: "04c", icon: "🌿", title: "Git-Versionskontrolle", path: "lehrpfad_2_oop_einstieg/04c_git_und_versionskontrolle/index.html" },
        { id: "05_objekte_kombinieren", num: "05", icon: "🎵", title: "Objekte kombinieren", path: "lehrpfad_2_oop_einstieg/05_objekte_kombinieren/index.html" },
        { id: "06_abschlussprojekt_tamagotchi", num: "06", icon: "🥚", title: "Projekt: Tamagotchi", path: "lehrpfad_2_oop_einstieg/06_abschlussprojekt_tamagotchi/index.html" },
      ]
    },
    {
      id: "lehrpfad_3",
      title: "🚀 3. Fortgeschritten",
      badge: "07–16",
      items: [
        { id: "07_referenzen_und_speicher", num: "07", icon: "🧠", title: "Referenzen & Speicher", path: "lehrpfad_3_fortgeschrittenes_oop/07_referenzen_und_speicher/index.html" },
        { id: "08_operator_overloading_dunder", num: "08", icon: "➕", title: "Operator Overloading", path: "lehrpfad_3_fortgeschrittenes_oop/08_operator_overloading_dunder/index.html" },
        { id: "09_eigene_unit_tests_schreiben", num: "09", icon: "🧪", title: "Unit Tests & TDD", path: "lehrpfad_3_fortgeschrittenes_oop/09_eigene_unit_tests_schreiben/index.html" },
        { id: "10_vererbung_und_super", num: "10", icon: "🧬", title: "Vererbung & super()", path: "lehrpfad_3_fortgeschrittenes_oop/10_vererbung_und_super/index.html" },
        { id: "11_polymorphie_und_interfaces", num: "11", icon: "🎭", title: "Polymorphie", path: "lehrpfad_3_fortgeschrittenes_oop/11_polymorphie_und_interfaces/index.html" },
        { id: "12_exceptions_und_fehlerbehandlung", num: "12", icon: "🛡️", title: "Exceptions & Fehler", path: "lehrpfad_3_fortgeschrittenes_oop/12_exceptions_und_fehlerbehandlung/index.html" },
        { id: "13_persistenz_json_und_csv", num: "13", icon: "💾", title: "Persistenz (JSON/CSV)", path: "lehrpfad_3_fortgeschrittenes_oop/13_persistenz_json_und_csv/index.html" },
        { id: "14_gui_mit_tkinter", num: "14", icon: "🖥️", title: "Desktop-GUIs (Tkinter)", path: "lehrpfad_3_fortgeschrittenes_oop/14_gui_mit_tkinter/index.html" },
        { id: "15_parameter_und_container", num: "15", icon: "🎒", title: "Container & *args", path: "lehrpfad_3_fortgeschrittenes_oop/15_parameter_und_container/index.html" },
        { id: "16_master_abschlussprojekt", num: "16", icon: "🏆", title: "Master-Abschlussprojekt", path: "lehrpfad_3_fortgeschrittenes_oop/16_master_abschlussprojekt/index.html" },
      ]
    }
  ];

  function detectRootPrefix() {
    const p = window.location.pathname;
    if (p.includes("/lehrpfad_1_grundlagen/") || p.includes("/lehrpfad_2_oop_einstieg/") || p.includes("/lehrpfad_3_fortgeschrittenes_oop/")) {
      return "../../";
    }
    return "./";
  }

  function initSidebar() {
    const prefix = detectRootPrefix();
    const currentPath = window.location.pathname;

    // Wrap existing body content in .app-main if not wrapped yet
    if (!document.querySelector(".app-main")) {
      const mainWrapper = document.createElement("div");
      mainWrapper.className = "app-main";
      while (document.body.firstChild) {
        mainWrapper.appendChild(document.body.firstChild);
      }
      document.body.appendChild(mainWrapper);
    }

    // Check if sidebar already exists
    if (document.querySelector(".app-sidebar")) return;

    // Gamification Data
    const gData = window.GAMIFICATION_DATA || { xp: 0, level: 1, titel: "Code-Küken 🐣", geloeste_kapitel: [] };
    const solvedSet = new Set(gData.geloeste_kapitel || []);

    // 1. Mobile Drawer Toggle Button
    const toggleBtn = document.createElement("button");
    toggleBtn.type = "button";
    toggleBtn.className = "sidebar-mobile-toggle";
    toggleBtn.innerHTML = "<span>☰ Menü</span>";
    document.body.appendChild(toggleBtn);

    // 2. Mobile Overlay
    const overlay = document.createElement("div");
    overlay.className = "sidebar-overlay";
    document.body.appendChild(overlay);

    // 3. Sidebar Element
    const sidebar = document.createElement("aside");
    sidebar.className = "app-sidebar";

    let navSectionsHtml = "";
    LEHRPFADE.forEach(track => {
      let itemsHtml = "";
      track.items.forEach(item => {
        const fullLink = prefix + item.path;
        const isActive = currentPath.includes(item.id);
        const isSolved = solvedSet.has(item.path.replace("/index.html", ""));

        itemsHtml += `
          <a href="${fullLink}" class="sidebar-link ${isActive ? 'active' : ''}">
            <span class="sidebar-link-icon">${item.icon}</span>
            <span class="sidebar-link-text">${item.num}. ${item.title}</span>
            ${isSolved ? '<span style="font-size: 0.75rem;">✅</span>' : ''}
          </a>
        `;
      });

      navSectionsHtml += `
        <div class="sidebar-group">
          <div class="sidebar-group-title">
            <span>${track.title}</span>
            <span style="background: rgba(255,255,255,0.1); padding: 2px 6px; border-radius: 99px; font-size: 0.7rem;">${track.badge}</span>
          </div>
          <div style="display: flex; flex-direction: column; gap: 2px;">
            ${itemsHtml}
          </div>
        </div>
      `;
    });

    sidebar.innerHTML = `
      <div class="sidebar-header">
        <a href="${prefix}index.html" style="display: flex; align-items: center; gap: 10px; text-decoration: none; color: white;">
          <div class="sidebar-logo">🐍</div>
          <div>
            <div class="sidebar-title">Python Portal</div>
            <div class="sidebar-subtitle">Lernplattform</div>
          </div>
        </a>
      </div>

      <div style="padding: 10px 14px; border-bottom: 1px solid var(--border-dark); display: flex; flex-direction: column; gap: 2px; background: rgba(0,0,0,0.15);">
        <a href="${prefix}index.html" class="sidebar-link">🏠 Startseite</a>
        <a href="${prefix}index.html#tutorial" class="sidebar-link">📖 Tutorial & Workflow</a>
        <a href="${prefix}index.html#zertifikate" class="sidebar-link">🏆 Zertifikate</a>
      </div>

      <div class="sidebar-nav">
        ${navSectionsHtml}
      </div>

      <div class="sidebar-footer">
        <div style="display: flex; align-items: center; justify-content: space-between;">
          <div style="font-size: 0.85rem; font-weight: 700; color: white;">⭐ Level ${gData.level || 1}</div>
          <div style="font-size: 0.82rem; font-weight: 700; color: #38bdf8;">${gData.xp || 0} XP</div>
        </div>
      </div>
    `;

    document.body.prepend(sidebar);

    // Toggle Handler
    toggleBtn.addEventListener("click", () => {
      sidebar.classList.toggle("open");
      overlay.classList.toggle("active");
    });

    overlay.addEventListener("click", () => {
      sidebar.classList.remove("open");
      overlay.classList.remove("active");
    });
  }

  document.addEventListener("DOMContentLoaded", initSidebar);
})();
