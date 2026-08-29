/**
 * 🧭 NEXT-GEN SIDEBAR NAVIGATION & APP LAYOUT 🧭
 * ===============================================
 * Erzeugt eine moderne, responsive Sidebar auf der linken Seite
 * für das Hauptportal und alle 27 Kapitel-Seiten.
 */

(function () {
  const LEHRPFADE = [
    {
      id: "lehrpfad_1",
      title: "🌱 Lehrpfad 1: Grundlagen",
      badge: "G01–G10",
      color: "#059669",
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
      title: "🏗️ Lehrpfad 2: OOP Einstieg",
      badge: "00–06",
      color: "#4f46e5",
      items: [
        { id: "00_fehlersuche_und_grundlagen", num: "00", icon: "🔍", title: "Fehlersuche & Debugging", path: "lehrpfad_2_oop_einstieg/00_fehlersuche_und_grundlagen/index.html" },
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
      title: "🚀 Lehrpfad 3: Fortgeschritten",
      badge: "07–16",
      color: "#7c3aed",
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
    if (document.querySelector(".app-sidebar")) return;

    const prefix = detectRootPrefix();
    const currentPath = window.location.pathname;
    const isRoot = prefix === "./";

    // Gamification Data
    const gData = window.GAMIFICATION_DATA || { xp: 0, level: 1, titel: "Code-Küken 🐣", geloeste_kapitel: [] };
    const solvedSet = new Set(gData.geloeste_kapitel || []);

    // 1. Erstelle Drawer-Toggle Button für Mobile
    const toggleBtn = document.createElement("button");
    toggleBtn.type = "button";
    toggleBtn.className = "sidebar-mobile-toggle";
    toggleBtn.innerHTML = "<span>☰ Menü</span>";
    document.body.prepend(toggleBtn);

    // 2. Erstelle Overlay für Mobile
    const overlay = document.createElement("div");
    overlay.className = "sidebar-overlay";
    document.body.prepend(overlay);

    // 3. Erstelle Sidebar Container
    const sidebar = document.createElement("aside");
    sidebar.className = "app-sidebar";

    let tracksHtml = "";
    LEHRPFADE.forEach(track => {
      let itemsHtml = "";
      track.items.forEach(item => {
        const fullLink = prefix + item.path;
        const isActive = currentPath.includes(item.id);
        const isSolved = solvedSet.has(item.path.replace("/index.html", ""));

        itemsHtml += `
          <a href="${fullLink}" class="sidebar-item ${isActive ? 'active' : ''}">
            <span class="sidebar-item-icon">${item.icon}</span>
            <span class="sidebar-item-text">${item.num}. ${item.title}</span>
            ${isSolved ? '<span class="sidebar-solved-badge" title="Gelöst!">✅</span>' : ''}
          </a>
        `;
      });

      tracksHtml += `
        <div class="sidebar-section">
          <div class="sidebar-section-header">
            <span>${track.title}</span>
            <span class="sidebar-section-badge" style="background: ${track.color}22; color: ${track.color};">${track.badge}</span>
          </div>
          <div class="sidebar-nav-list">
            ${itemsHtml}
          </div>
        </div>
      `;
    });

    sidebar.innerHTML = `
      <div class="sidebar-brand">
        <a href="${prefix}index.html" class="sidebar-brand-link">
          <div class="sidebar-brand-logo">🐍</div>
          <div>
            <div class="sidebar-brand-title">Python Lernportal</div>
            <div class="sidebar-brand-sub">Interaktiver Kurs</div>
          </div>
        </a>
      </div>

      <div class="sidebar-quick-nav">
        <a href="${prefix}index.html#tutorial" class="sidebar-quick-link">📖 Anleitung & Workflow</a>
        <a href="${prefix}index.html#python-live-playground" class="sidebar-quick-link">⚡ Live-Playground</a>
        <a href="${prefix}index.html#error-interpreter-widget" class="sidebar-quick-link">🩺 Fehler-Dolmetscher</a>
        <a href="${prefix}index.html#zertifikate" class="sidebar-quick-link">🏆 Zertifikate</a>
      </div>

      <div class="sidebar-content">
        ${tracksHtml}
      </div>

      <div class="sidebar-footer">
        <div class="sidebar-user-card">
          <div class="sidebar-user-avatar">🐣</div>
          <div class="sidebar-user-info">
            <div class="sidebar-user-name">Level ${gData.level || 1}</div>
            <div class="sidebar-user-title">${gData.titel || "Code-Küken"}</div>
          </div>
          <div class="sidebar-user-xp">${gData.xp || 0} XP</div>
        </div>
      </div>
    `;

    document.body.prepend(sidebar);

    // Toggle Events
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
