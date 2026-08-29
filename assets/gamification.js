/**
 * 🎮 GAMIFICATION ENGINE FÜR DAS PYTHON LERNPORTAL 🎮
 * ====================================================
 * Funktioniert 100% lokal ohne Server (file://) via gamification_data.js & localStorage!
 */

(function () {
  // Standard-Kataloge als Fallback, falls gamification_data.js noch nicht existiert
  const DEFAULT_LEVELS = [
    { level: 1, min_xp: 0, max_xp: 150, titel: "Code-Küken 🐣", rang: "Bronze I" },
    { level: 2, min_xp: 151, max_xp: 400, titel: "Code-Detektivin 🔍", rang: "Bronze II" },
    { level: 3, min_xp: 401, max_xp: 800, titel: "Logik-Bastlerin ⚙️", rang: "Silber I" },
    { level: 4, min_xp: 801, max_xp: 1300, titel: "Klassen-Baumeisterin 🏗️", rang: "Silber II" },
    { level: 5, min_xp: 1301, max_xp: 2000, titel: "Git-Strategin 🌿", rang: "Gold I" },
    { level: 6, min_xp: 2001, max_xp: 2900, titel: "TDD-Qualitätsprüferin 🧪", rang: "Gold II" },
    { level: 7, min_xp: 2901, max_xp: 4000, titel: "Vererbungs-Meisterin 🧬", rang: "Platin I" },
    { level: 8, min_xp: 4001, max_xp: 5300, titel: "Exception-Wächterin 🛡️", rang: "Platin II" },
    { level: 9, min_xp: 5301, max_xp: 6800, titel: "GUI-Entwicklerin 🖥️", rang: "Diamant" },
    { level: 10, min_xp: 6801, max_xp: 99999, titel: "Software-Architektin 🏆", rang: "Großmeisterin" }
  ];

  const DEFAULT_BADGES = {
    rechenkonegin: { icon: "🧮", name: "Rechenkönigin", desc: "Grundlagen G01 & G02 abgeschlossen (Zahlen, Operatoren & Typen gemeistert)." },
    dialog_profi: { icon: "💬", name: "Dialog-Profi", desc: "Grundlagen G03 abgeschlossen (Interaktive Ein-/Ausgabe mit f-Strings)." },
    weichenstellerin: { icon: "🚦", name: "Weichenstellerin", desc: "Grundlagen G04 abgeschlossen (Bedingungslogik & Schaltjahre gemeistert)." },
    schleifen_dompteurin: { icon: "🎡", name: "Schleifen-Dompteurin", desc: "Grundlagen G05 abgeschlossen (While- & For-Schleifen gebändigt)." },
    funktions_zauberin: { icon: "🪄", name: "Funktions-Zauberin", desc: "Grundlagen G06 abgeschlossen (Eigene Funktionen & Module gebaut)." },
    listen_archivarin: { icon: "📋", name: "Listen-Archivarin", desc: "Grundlagen G07 & G08 abgeschlossen (Sequenzen & Strings analysiert)." },
    daten_strategin: { icon: "🗃️", name: "Daten-Strategin", desc: "Grundlagen G09 & G10 abgeschlossen (Dicts, Sets & Comprehensions gemeistert)." },
    bug_jaegerin: { icon: "🔍", name: "Bug-Jägerin", desc: "Kapitel 00 gelöst (Alle Fehler-Bugs im Warm-up aufgespürt)." },
    erste_architektin: { icon: "🏗️", name: "Erste Architektin", desc: "Kapitel 01 bis 03 gelöst (Erste OOP-Klassen, Konstruktoren & Methoden)." },
    zeit_reisende: { icon: "🌿", name: "Git-Zeitreisende", desc: "Kapitel 04c Git-Versionskontrolle verstanden & Spielstände gesichert." },
    tamagotchi_mama: { icon: "🥚", name: "Tamagotchi-Mama", desc: "Kapitel 06 Mini-Projekt abgeschlossen (Ein lebendiges Haustier gebaut)." },
    qualitaets_garantin: { icon: "🧪", name: "TDD-Qualitätsgarantin", desc: "Kapitel 09 abgeschlossen (Eigene professionelle Unit Tests geschrieben)." },
    oop_grossmeisterin: { icon: "🧬", name: "Vererbungs-Koryphäe", desc: "Kapitel 10 bis 12 abgeschlossen (Vererbung, Polymorphie & Exceptions)." },
    software_architektin: { icon: "🏆", name: "Meister-Entwicklerin", desc: "Kapitel 16 Master-Projekt abgeschlossen & vollwertige Desktop-App gebaut!" }
  };

  // Daten abrufen
  function getGamificationData() {
    if (window.GAMIFICATION_DATA) {
      return window.GAMIFICATION_DATA;
    }
    const saved = localStorage.getItem("python_gamification_state");
    if (saved) {
      try { return JSON.parse(saved); } catch (e) { }
    }
    return {
      spieler_name: "Python-Entwicklerin",
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

  function getLevelInfo(xp) {
    const levels = window.GAMIFICATION_LEVEL_STUFEN || DEFAULT_LEVELS;
    for (let info of levels) {
      if (xp >= info.min_xp && xp <= info.max_xp) {
        const nextXp = info.max_xp + 1;
        const xpInLevel = xp - info.min_xp;
        const xpForLevel = nextXp - info.min_xp;
        const prozent = xpForLevel > 0 ? Math.min(100, Math.round((xpInLevel / xpForLevel) * 100)) : 100;
        return { ...info, naechste_stufe_xp: nextXp, prozent: prozent };
      }
    }
    return { level: 10, titel: "Software-Architektin 🏆", rang: "Großmeisterin", naechste_stufe_xp: 99999, prozent: 100 };
  }

  // HUD & Trophäenraum rendern
  function renderGamificationHUD() {
    const data = getGamificationData();
    const lvlInfo = getLevelInfo(data.xp || 0);
    const badgesKatalog = window.GAMIFICATION_BADGES_KATALOG || DEFAULT_BADGES;
    const unlockedBadges = new Set(data.freigeschaltete_badges || []);
    const badgeCount = unlockedBadges.size;
    const totalBadges = Object.keys(badgesKatalog).length;

    // Finde oder erstelle den HUD-Container
    let hud = document.getElementById("gamer-hud");
    if (!hud) {
      const mainContainer = document.querySelector(".container") || document.body;
      hud = document.createElement("div");
      hud.id = "gamer-hud";
      mainContainer.prepend(hud);
    }

    hud.innerHTML = `
      <div class="hud-card">
        <div class="hud-header">
          <div class="hud-user">
            <div class="hud-avatar">🎮</div>
            <div>
              <div class="hud-name">${data.spieler_name || "Python-Entwicklerin"}</div>
              <div class="hud-title">${lvlInfo.titel} &bull; <span class="hud-rank">${lvlInfo.rang}</span></div>
            </div>
          </div>
          <div class="hud-stats">
            <div class="hud-stat-box">
              <span class="hud-stat-value">⭐ Level ${lvlInfo.level}</span>
              <span class="hud-stat-label">${data.xp || 0} XP</span>
            </div>
            <div class="hud-stat-box">
              <span class="hud-stat-value">🔥 ${data.streak_tage || 1} Tage</span>
              <span class="hud-stat-label">Lern-Streak</span>
            </div>
            <div class="hud-stat-box">
              <span class="hud-stat-value">🏆 ${badgeCount}/${totalBadges}</span>
              <span class="hud-stat-label">Trophäen</span>
            </div>
          </div>
        </div>

        <div class="hud-progress-container">
          <div class="hud-progress-labels">
            <span>Fortschritt zu Level ${lvlInfo.level + 1}</span>
            <span><strong>${data.xp || 0}</strong> / ${lvlInfo.naechste_stufe_xp} XP (${lvlInfo.prozent}%)</span>
          </div>
          <div class="hud-progress-bar-bg">
            <div class="hud-progress-bar-fill" style="width: ${lvlInfo.prozent}%;"></div>
          </div>
        </div>

        <div class="hud-footer">
          <button id="toggle-trophies-btn" class="hud-btn">
            🏆 Trophäenraum öffnen (${badgeCount}/${totalBadges} freigeschaltet)
          </button>
          <div class="hud-cli-tip">
            ⌨️ Im Terminal: <code>python3 profil.py</code> oder <code>python3 test_all.py</code>
          </div>
        </div>

        <div id="trophy-room" class="trophy-room" style="display: none;">
          <h3 style="margin: 15px 0 10px 0; color: var(--text-main);">🎖️ Dein Trophäenraum</h3>
          <div class="trophy-grid">
            ${Object.keys(badgesKatalog).map(bId => {
              const b = badgesKatalog[bId];
              const isUnlocked = unlockedBadges.has(bId);
              return `
                <div class="trophy-card ${isUnlocked ? 'trophy-unlocked' : 'trophy-locked'}">
                  <div class="trophy-icon">${isUnlocked ? b.icon : '🔒'}</div>
                  <div class="trophy-info">
                    <div class="trophy-title">${b.name}</div>
                    <div class="trophy-desc">${b.desc}</div>
                    <div class="trophy-badge-status">${isUnlocked ? '✅ Freigeschaltet' : '🔒 Gesperrt'}</div>
                  </div>
                </div>
              `;
            }).join("")}
          </div>
        </div>
      </div>
    `;

    // Event Listener für Trophäenraum Toggle
    const toggleBtn = document.getElementById("toggle-trophies-btn");
    const trophyRoom = document.getElementById("trophy-room");
    if (toggleBtn && trophyRoom) {
      toggleBtn.addEventListener("click", function () {
        const isHidden = trophyRoom.style.display === "none";
        trophyRoom.style.display = isHidden ? "block" : "none";
        toggleBtn.innerText = isHidden
          ? `🔼 Trophäenraum einklappen (${badgeCount}/${totalBadges})`
          : `🏆 Trophäenraum öffnen (${badgeCount}/${totalBadges} freigeschaltet)`;
      });
    }
  }

  // Checkbox-Persistenz für alle Aufgaben-Seiten (localStorage)
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

  // Initialisierung beim Laden
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      renderGamificationHUD();
      initTaskCheckboxes();
    });
  } else {
    renderGamificationHUD();
    initTaskCheckboxes();
  }
})();
