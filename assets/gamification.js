/**
 * 🎮 GAMIFICATION ENGINE FÜR DAS PYTHON LERNPORTAL 🎮
 * ====================================================
 * Funktioniert 100% lokal ohne Server (file://) via gamification_data.js & localStorage!
 */

(function () {
  const DEFAULT_LEVELS = [
    { level: 1, min_xp: 0, max_xp: 150, titel: "Code-Küken 🐣", rang: "Bronze I" },
    { level: 2, min_xp: 151, max_xp: 400, titel: "Code-Detektiv 🔍", rang: "Bronze II" },
    { level: 3, min_xp: 401, max_xp: 800, titel: "Logik-Bastler ⚙️", rang: "Silber I" },
    { level: 4, min_xp: 801, max_xp: 1300, titel: "Klassen-Baumeister 🏗️", rang: "Silber II" },
    { level: 5, min_xp: 1301, max_xp: 2000, titel: "Git-Stratege 🌿", rang: "Gold I" },
    { level: 6, min_xp: 2001, max_xp: 2900, titel: "TDD-Qualitätsprüfer 🧪", rang: "Gold II" },
    { level: 7, min_xp: 2901, max_xp: 4000, titel: "Vererbungs-Meister 🧬", rang: "Platin I" },
    { level: 8, min_xp: 4001, max_xp: 5300, titel: "Exception-Wächter 🛡️", rang: "Platin II" },
    { level: 9, min_xp: 5301, max_xp: 6800, titel: "GUI-Entwickler 🖥️", rang: "Diamant" },
    { level: 10, min_xp: 6801, max_xp: 99999, titel: "Software-Architekt 🏆", rang: "Großmeister" }
  ];

  const DEFAULT_BADGES = {
    rechenkonegin: { icon: "🧮", name: "Rechenkönig", desc: "Grundlagen G01 & G02 abgeschlossen (Zahlen, Operatoren & Typen gemeistert)." },
    dialog_profi: { icon: "💬", name: "Dialog-Profi", desc: "Grundlagen G03 abgeschlossen (Interaktive Ein-/Ausgabe mit f-Strings)." },
    weichenstellerin: { icon: "🚦", name: "Weichensteller", desc: "Grundlagen G04 abgeschlossen (Bedingungslogik & Schaltjahre gemeistert)." },
    schleifen_dompteurin: { icon: "🎡", name: "Schleifen-Dompteur", desc: "Grundlagen G05 abgeschlossen (While- & For-Schleifen gebändigt)." },
    funktions_zauberin: { icon: "🪄", name: "Funktions-Zauberer", desc: "Grundlagen G06 abgeschlossen (Eigene Funktionen & Module gebaut)." },
    listen_archivarin: { icon: "📋", name: "Listen-Archivar", desc: "Grundlagen G07 & G08 abgeschlossen (Sequenzen & Strings analysiert)." },
    daten_strategin: { icon: "🗃️", name: "Daten-Stratege", desc: "Grundlagen G09 & G10 abgeschlossen (Dicts, Sets & Comprehensions gemeistert)." },
    bug_jaegerin: { icon: "🔍", name: "Bug-Jäger", desc: "Kapitel 00 gelöst (Alle Fehler-Bugs im Warm-up aufgespürt)." },
    erste_architektin: { icon: "🏗️", name: "Erster Architekt", desc: "Kapitel 01 bis 03 gelöst (Erste OOP-Klassen, Konstruktoren & Methoden)." },
    zeit_reisende: { icon: "🌿", name: "Git-Zeitreisender", desc: "Kapitel 04c Git-Versionskontrolle verstanden & Spielstände gesichert." },
    tamagotchi_mama: { icon: "🥚", name: "Tamagotchi-Hüter", desc: "Kapitel 06 Mini-Projekt abgeschlossen (Ein lebendiges Haustier gebaut)." },
    qualitaets_garantin: { icon: "🧪", name: "TDD-Qualitätsgarant", desc: "Kapitel 09 abgeschlossen (Eigene professionelle Unit Tests geschrieben)." },
    oop_grossmeisterin: { icon: "🧬", name: "Vererbungs-Koryphäe", desc: "Kapitel 10 bis 12 abgeschlossen (Vererbung, Polymorphie & Exceptions)." },
    software_architektin: { icon: "🏆", name: "Meister-Entwickler", desc: "Kapitel 16 Master-Projekt abgeschlossen & vollwertige Desktop-App gebaut!" }
  };

  function getGamificationData() {
    if (window.GAMIFICATION_DATA) {
      return window.GAMIFICATION_DATA;
    }
    const saved = localStorage.getItem("python_gamification_state");
    if (saved) {
      try { return JSON.parse(saved); } catch (e) { }
    }
    return {
      spieler_name: "Python-Entwickler",
      xp: 0,
      level: 1,
      titel: "Code-Küken 🐣",
      rang: "Bronze I",
      geloeste_kapitel: [],
      bestandene_tests: 0,
      freigeschaltete_badges: [],
      streak_tage: 1
    };
  }

  function saveGamificationData(data) {
    window.GAMIFICATION_DATA = data;
    localStorage.setItem("python_gamification_state", JSON.stringify(data));
  }

  // Globaler XP-Zuwachs & Levelberechnung
  window.addXP = function (amount, chapterId = "") {
    const data = getGamificationData();
    data.xp = (data.xp || 0) + amount;

    if (chapterId && !data.geloeste_kapitel.includes(chapterId)) {
      data.geloeste_kapitel.push(chapterId);
    }

    // Level prüfen
    for (let i = DEFAULT_LEVELS.length - 1; i >= 0; i--) {
      if (data.xp >= DEFAULT_LEVELS[i].min_xp) {
        data.level = DEFAULT_LEVELS[i].level;
        data.titel = DEFAULT_LEVELS[i].titel;
        data.rang = DEFAULT_LEVELS[i].rang;
        break;
      }
    }

    saveGamificationData(data);
    window.renderGamificationHUD();
    return data;
  };

  window.renderGamificationHUD = function () {
    const data = getGamificationData();
    const levels = (window.GAMIFICATION_DATA && window.GAMIFICATION_DATA.levels) ? window.GAMIFICATION_DATA.levels : DEFAULT_LEVELS;
    const badges = (window.GAMIFICATION_DATA && window.GAMIFICATION_DATA.badges) ? window.GAMIFICATION_DATA.badges : DEFAULT_BADGES;

    const currentLevelObj = levels.find((l) => l.level === data.level) || levels[0];
    const nextLevelObj = levels.find((l) => l.level === data.level + 1);

    let progressPercent = 100;
    let xpNeeded = "Max Level";
    if (nextLevelObj) {
      const xpInCurrentLevel = data.xp - currentLevelObj.min_xp;
      const levelSpan = nextLevelObj.min_xp - currentLevelObj.min_xp;
      progressPercent = Math.min(100, Math.max(0, Math.round((xpInCurrentLevel / levelSpan) * 100)));
      xpNeeded = `${data.xp} / ${nextLevelObj.min_xp} XP`;
    }

    // Update Topbar / Sidebar Indicators
    const sbLevel = document.getElementById("sidebar-level-text");
    const sbXP = document.getElementById("sidebar-xp-text");
    if (sbLevel) sbLevel.innerText = `⭐ Level ${data.level}`;
    if (sbXP) sbXP.innerText = `${data.xp} XP`;

    // Update HUD Widget if present
    const hud = document.getElementById("gamification-hud");
    if (!hud) return;

    const avatarIcon = currentLevelObj.titel.split(" ").pop() || "🐣";
    const solvedCount = (data.geloeste_kapitel || []).length;
    const totalChapters = 27;

    const nameEl = document.getElementById("hud-user-name");
    const titleEl = document.getElementById("hud-user-title");
    const rankEl = document.getElementById("hud-user-rank");
    const levelEl = document.getElementById("hud-stat-level");
    const xpEl = document.getElementById("hud-stat-xp");
    const solvedEl = document.getElementById("hud-stat-solved");
    const streakEl = document.getElementById("hud-stat-streak");
    const barEl = document.getElementById("hud-progress-bar");
    const progressTextEl = document.getElementById("hud-progress-text");
    const avatarEl = document.getElementById("hud-avatar-icon");

    if (nameEl) nameEl.innerText = data.spieler_name || "Entwickler-Pass";
    if (titleEl) titleEl.innerText = currentLevelObj.titel;
    if (rankEl) rankEl.innerText = `Rang: ${currentLevelObj.rang}`;
    if (levelEl) levelEl.innerText = data.level;
    if (xpEl) xpEl.innerText = `${data.xp} XP`;
    if (solvedEl) solvedEl.innerText = `${solvedCount} / ${totalChapters}`;
    if (streakEl) streakEl.innerText = `🔥 ${data.streak_tage || 1} Tag${(data.streak_tage || 1) > 1 ? "e" : ""}`;
    if (barEl) barEl.style.width = `${progressPercent}%`;
    if (progressTextEl) progressTextEl.innerText = xpNeeded;
    if (avatarEl) avatarEl.innerText = avatarIcon;
  };

  function initTaskCheckboxes() {
    const checkboxes = document.querySelectorAll(".task-checkbox");
    if (!checkboxes.length) return;

    const pageKey = "task_progress_" + window.location.pathname;
    const savedStates = JSON.parse(localStorage.getItem(pageKey) || "{}");

    checkboxes.forEach((cb) => {
      const id = cb.id;
      if (id && savedStates[id]) {
        cb.checked = true;
      }
      cb.addEventListener("change", function () {
        const states = JSON.parse(localStorage.getItem(pageKey) || "{}");
        states[id] = cb.checked;
        localStorage.setItem(pageKey, JSON.stringify(states));
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      window.renderGamificationHUD();
      initTaskCheckboxes();
    });
  } else {
    window.renderGamificationHUD();
    initTaskCheckboxes();
  }
})();
