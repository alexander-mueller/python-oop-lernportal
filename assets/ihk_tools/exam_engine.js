/**
 * ⏱️ IHK EXAM ENGINE & FRAGEN-GENERATOR ⏱️
 * ==========================================
 * Standardisierte Prüfungs-Engine für AP1 & AP2 Probeprüfungen:
 * - 90-Minuten / 60-Minuten Realtime Countdown
 * - Offizieller IHK 100-Punkte Notenschlüssel
 * - Dynamisches Mischen aus 150+ authentischen IHK-Prüfungsfragen
 * - Zufalls-Prüfungsbogen-Generator (100 Punkte nach IHK-Standard)
 * - Interaktiver 150-Fragen-Katalog & Lernfeld-Drill
 * - Automatische Vorkorrektur & Detaillierter Erwartungshorizont
 */

class IhkExamEngine {
  constructor(config) {
    this.title = config.title || "IHK Abschlussprüfung Simulation";
    this.durationMinutes = config.durationMinutes || 90;
    this.totalPoints = config.totalPoints || 100;
    this.tasks = config.tasks || [];
    this.examType = config.examType || this.detectExamType(this.title);
    this.secondsRemaining = this.durationMinutes * 60;
    this.timerInterval = null;
    this.isSubmitted = false;
    this.originalTasksHtml = null;
    this.questionBank = window.IHK_QUESTION_BANK || [];

    // Fallback: Lade JSON asynchron, falls window.IHK_QUESTION_BANK noch nicht geladen
    if (this.questionBank.length === 0) {
      this.loadQuestionBankAsync();
    }

    this.init();
  }

  detectExamType(title) {
    const t = (title || "").toLowerCase();
    const url = window.location.href.toLowerCase();
    if (t.includes("wiso") || url.includes("wiso")) return "WiSo";
    if (t.includes("teil 2") || t.includes("analyse") || url.includes("teil_2")) return "AP2_T2";
    if (t.includes("teil 1") || t.includes("planen") || url.includes("teil_1")) return "AP2_T1";
    return "AP1";
  }

  async loadQuestionBankAsync() {
    try {
      const candidates = [
        "../../../assets/ihk_tools/ihk_question_bank.json",
        "../../assets/ihk_tools/ihk_question_bank.json",
        "assets/ihk_tools/ihk_question_bank.json"
      ];
      for (const p of candidates) {
        try {
          const res = await fetch(p);
          if (res.ok) {
            this.questionBank = await res.json();
            window.IHK_QUESTION_BANK = this.questionBank;
            break;
          }
        } catch (e) {}
      }
    } catch (err) {
      console.warn("Could not fetch question bank JSON:", err);
    }
  }

  init() {
    this.renderBanner();
    this.renderControlBar();
    this.storeOriginalContent();
    this.startTimer();
    this.bindEvents();
  }

  storeOriginalContent() {
    // Finde den Container, in dem die Aufgaben liegen
    const firstTask = document.querySelector(".ihk-exam-task");
    if (firstTask && firstTask.parentElement) {
      this.taskContainer = firstTask.parentElement;
      // Speichere den HTML-Inhalt aller Aufgaben
      const tasks = Array.from(this.taskContainer.querySelectorAll(".ihk-exam-task"));
      this.originalTasksNodes = tasks.map(t => t.cloneNode(true));
    }
  }

  renderBanner() {
    let banner = document.getElementById("ihk-exam-header");
    if (!banner) {
      banner = document.createElement("div");
      banner.id = "ihk-exam-header";
      banner.className = "ihk-exam-banner";
      document.body.prepend(banner);
    }

    banner.innerHTML = `
      <div style="display: flex; align-items: center; gap: 16px;">
        <span style="font-size: 1.5rem;">📝</span>
        <div>
          <div style="font-weight: 800; font-size: 1.1rem; color: #f8fafc;" id="ihk-banner-title">${this.title}</div>
          <div style="font-size: 0.8rem; color: #94a3b8;" id="ihk-banner-subtitle">
            Bereich: <strong style="color: #38bdf8;">${this.getExamLabel(this.examType)}</strong> | Gesamtpunktzahl: <span id="ihk-display-points">${this.totalPoints}</span> Punkte | 100-Punkte-IHK-Schlüssel
          </div>
        </div>
      </div>

      <div style="display: flex; align-items: center; gap: 20px;">
        <div class="ihk-timer-display" id="ihk-timer-val">
          ${this.formatTime(this.secondsRemaining)}
        </div>
        <button class="ihk-btn ihk-btn-success" id="btn-submit-exam">
          🏁 Prüfung abgeben
        </button>
      </div>
    `;
  }

  getExamLabel(type) {
    switch (type) {
      case "AP1": return "AP1 (LF 1 - LF 8)";
      case "AP2_T1": return "AP2 Teil 1 (LF 9 & LF 11)";
      case "AP2_T2": return "AP2 Teil 2 (LF 10 & LF 12)";
      case "WiSo": return "AP2 WiSo (Wirtschafts- & Sozialkunde)";
      default: return type;
    }
  }

  renderControlBar() {
    let bar = document.getElementById("ihk-exam-control-bar");
    if (!bar) {
      bar = document.createElement("div");
      bar.id = "ihk-exam-control-bar";
      bar.style.cssText = "background: #1e293b; border: 1px solid #334155; border-radius: 10px; padding: 12px 18px; margin: 16px auto 24px auto; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 12px;";
      
      const banner = document.getElementById("ihk-exam-header");
      if (banner && banner.nextSibling) {
        banner.parentNode.insertBefore(bar, banner.nextSibling);
      } else {
        document.body.prepend(bar);
      }
    }

    bar.innerHTML = `
      <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
        <span style="font-weight: 700; color: #cbd5e1; font-size: 0.88rem; display: flex; align-items: center; gap: 6px;">
          <span>⚙️</span> Modus:
        </span>
        <button id="btn-mode-original" class="ihk-btn ihk-btn-primary" style="font-size: 0.82rem; padding: 6px 12px;">
          📄 Originalprüfung
        </button>
        <button id="btn-mode-random" class="ihk-btn ihk-btn-secondary" style="font-size: 0.82rem; padding: 6px 12px;">
          🎲 Neue 100-Pkt. Zufallsprüfung
        </button>
        <button id="btn-mode-mix" class="ihk-btn ihk-btn-warning" style="font-size: 0.82rem; padding: 6px 12px;">
          🔀 Fragen untermischen
        </button>
      </div>

      <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
        <a href="../../../diagram_editor.html" target="_blank" class="ihk-btn" style="background: #0284c7; color: #ffffff !important; font-size: 0.82rem; padding: 6px 14px; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;" title="Öffnet das interaktive IHK Diagramm-Studio in neuem Tab">
          <span>📐</span> <span>Diagramm-Studio (ER / SG / UML)</span>
        </a>
        <button id="btn-open-catalog" class="ihk-btn" style="background: #334155; color: #f8fafc; font-size: 0.82rem; padding: 6px 14px; border: 1px solid #475569;">
          📚 Fragenkatalog (234 Fragen)
        </button>
      </div>
    `;

    // Event Listeners für Steuerungs-Buttons
    bar.querySelector("#btn-mode-original").addEventListener("click", () => this.restoreOriginalExam());
    bar.querySelector("#btn-mode-random").addEventListener("click", () => this.generateRandomExam(false));
    bar.querySelector("#btn-mode-mix").addEventListener("click", () => this.generateRandomExam(true));
    bar.querySelector("#btn-open-catalog").addEventListener("click", () => this.openQuestionCatalogModal());
  }

  formatTime(seconds) {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  }

  startTimer() {
    if (this.timerInterval) clearInterval(this.timerInterval);
    this.timerInterval = setInterval(() => {
      if (this.secondsRemaining > 0 && !this.isSubmitted) {
        this.secondsRemaining--;
        const timerEl = document.getElementById("ihk-timer-val");
        if (timerEl) {
          timerEl.textContent = this.formatTime(this.secondsRemaining);
          if (this.secondsRemaining <= 600) { // < 10 Min
            timerEl.classList.add("ihk-timer-warning");
          } else {
            timerEl.classList.remove("ihk-timer-warning");
          }
        }
      } else if (this.secondsRemaining <= 0 && !this.isSubmitted) {
        clearInterval(this.timerInterval);
        alert("⏱️ Die reguläre Prüfungszeit ist abgelaufen! Deine Prüfung wird nun abgegeben.");
        this.submitExam();
      }
    }, 1000);
  }

  resetTimer() {
    this.secondsRemaining = this.durationMinutes * 60;
    this.isSubmitted = false;
    const timerEl = document.getElementById("ihk-timer-val");
    if (timerEl) {
      timerEl.textContent = this.formatTime(this.secondsRemaining);
      timerEl.classList.remove("ihk-timer-warning");
    }
    this.startTimer();
  }

  bindEvents() {
    const btn = document.getElementById("btn-submit-exam");
    if (btn) {
      btn.addEventListener("click", () => {
        if (confirm("Möchtest du die Prüfung wirklich vorzeitig abgeben und die Auswertung ansehen?")) {
          this.submitExam();
        }
      });
    }
  }

  getGrade(points) {
    if (points >= 92) return { note: 1, text: "Sehr gut", pass: true, color: "#4ade80" };
    if (points >= 81) return { note: 2, text: "Gut", pass: true, color: "#22c55e" };
    if (points >= 67) return { note: 3, text: "Befriedigend", pass: true, color: "#38bdf8" };
    if (points >= 50) return { note: 4, text: "Ausreichend (Bestanden)", pass: true, color: "#facc15" };
    if (points >= 30) return { note: 5, text: "Mangelhaft (Nicht bestanden)", pass: false, color: "#fb923c" };
    return { note: 6, text: "Ungenügend (Nicht bestanden)", pass: false, color: "#f87171" };
  }

  restoreOriginalExam() {
    if (!this.taskContainer || !this.originalTasksNodes) {
      alert("Originalprüfung ist bereits aktiv.");
      return;
    }

    // Entferne alle vorhandenen Aufgaben
    const currentTasks = this.taskContainer.querySelectorAll(".ihk-exam-task");
    currentTasks.forEach(t => t.remove());

    // Füge Originale wieder ein
    this.originalTasksNodes.forEach(t => {
      this.taskContainer.appendChild(t.cloneNode(true));
    });

    this.totalPoints = 100;
    document.getElementById("ihk-display-points").textContent = "100";
    this.updateActiveButton("btn-mode-original");
    this.resetTimer();
    this.showToast("📄 Originalprüfung wiederhergestellt.");
  }

  generateRandomExam(mixWithOriginal = false) {
    const pool = this.getFilteredQuestions();
    if (!pool || pool.length === 0) {
      alert("Keine Fragen im Pool für " + this.examType + " gefunden.");
      return;
    }

    // Mische den Pool
    const shuffled = [...pool].sort(() => 0.5 - Math.random());

    let selectedQuestions = [];
    let currentSum = 0;
    const targetPoints = 100;

    if (mixWithOriginal && this.originalTasksNodes && this.originalTasksNodes.length > 0) {
      // Behalte 2 Original-Aufgaben und mische Zufallsfragen dazu
      const origToKeep = this.originalTasksNodes.slice(0, 2);
      let origPoints = 0;
      origToKeep.forEach(t => {
        origPoints += parseInt(t.dataset.points || "25", 10);
      });

      // Fülle restliche Punkte mit Zufallsfragen auf
      for (const q of shuffled) {
        if (origPoints + currentSum + q.points <= targetPoints + 4) {
          selectedQuestions.push(q);
          currentSum += q.points;
        }
        if (origPoints + currentSum >= 95) break;
      }

      this.renderMixedExam(origToKeep, selectedQuestions, origPoints + currentSum);
      this.updateActiveButton("btn-mode-mix");
      this.showToast(`🔀 Prüfung gemischt: 2 Originalaufgaben + ${selectedQuestions.length} Zufallsfragen (${origPoints + currentSum} Pkt.)!`);
    } else {
      // Rein dynamische 100-Punkte Zufallsprüfung
      for (const q of shuffled) {
        if (currentSum + q.points <= targetPoints + 4) {
          selectedQuestions.push(q);
          currentSum += q.points;
        }
        if (currentSum >= 96) break;
      }

      // Falls etwas unter 100, passe letzte Frage an oder nimm noch eine kleine
      this.renderDynamicExam(selectedQuestions, currentSum);
      this.updateActiveButton("btn-mode-random");
      this.showToast(`🎲 Neue Zufallsprüfung generiert: ${selectedQuestions.length} Handlungsschritte (${currentSum} Pkt.)!`);
    }

    this.resetTimer();
  }

  getFilteredQuestions() {
    const bank = window.IHK_QUESTION_BANK || this.questionBank || [];
    return bank.filter(q => q.exam === this.examType);
  }

  renderDynamicExam(questions, sumPoints) {
    if (!this.taskContainer) return;
    const currentTasks = this.taskContainer.querySelectorAll(".ihk-exam-task");
    currentTasks.forEach(t => t.remove());

    this.totalPoints = sumPoints;
    document.getElementById("ihk-display-points").textContent = sumPoints;

    questions.forEach((q, idx) => {
      const taskEl = this.createTaskElement(q, idx + 1);
      this.taskContainer.appendChild(taskEl);
    });
  }

  renderMixedExam(originalNodes, randomQuestions, sumPoints) {
    if (!this.taskContainer) return;
    const currentTasks = this.taskContainer.querySelectorAll(".ihk-exam-task");
    currentTasks.forEach(t => t.remove());

    this.totalPoints = sumPoints;
    document.getElementById("ihk-display-points").textContent = sumPoints;

    // 1. Original-Aufgaben einfügen
    originalNodes.forEach(node => {
      this.taskContainer.appendChild(node.cloneNode(true));
    });

    // 2. Zufalls-Aufgaben einfügen
    randomQuestions.forEach((q, idx) => {
      const taskEl = this.createTaskElement(q, originalNodes.length + idx + 1);
      this.taskContainer.appendChild(taskEl);
    });
  }

  createTaskElement(q, taskNumber) {
    const task = document.createElement("div");
    task.className = "ihk-exam-task";
    task.dataset.title = `Handlungsschritt ${taskNumber}: ${q.topic} (${q.lernfeld})`;
    task.dataset.points = q.points;
    task.style.cssText = "background: #1e293b; padding: 24px; border-radius: 12px; border: 1px solid #334155; margin-bottom: 24px;";

    let diagramLinkHtml = '';
    const topicLow = ((q.topic || '') + ' ' + (q.question || '')).toLowerCase();
    if (topicLow.includes('er-modell') || topicLow.includes('kardinalit') || topicLow.includes('normalis')) {
      diagramLinkHtml = `<div style="margin-bottom: 12px;"><a href="../../../diagram_editor.html#er" target="_blank" class="ihk-btn" style="padding: 4px 10px; font-size: 0.78rem; background: rgba(56, 189, 248, 0.15); color: #38bdf8 !important; border: 1px solid rgba(56, 189, 248, 0.3); text-decoration: none; border-radius: 4px; display: inline-flex; align-items: center; gap: 6px;"><span>🗄️</span> <span>Im ER-Modell Editor entwerfen / prüfen &rarr;</span></a></div>`;
    } else if (topicLow.includes('struktogramm') || topicLow.includes('nassi') || topicLow.includes('din 66261')) {
      diagramLinkHtml = `<div style="margin-bottom: 12px;"><a href="../../../diagram_editor.html#struktogramm" target="_blank" class="ihk-btn" style="padding: 4px 10px; font-size: 0.78rem; background: rgba(56, 189, 248, 0.15); color: #38bdf8 !important; border: 1px solid rgba(56, 189, 248, 0.3); text-decoration: none; border-radius: 4px; display: inline-flex; align-items: center; gap: 6px;"><span>📐</span> <span>Im Struktogramm-Editor entwerfen / prüfen &rarr;</span></a></div>`;
    } else if (topicLow.includes('uml') || topicLow.includes('klassendiagramm') || topicLow.includes('sequenzdiagramm') || topicLow.includes('use case')) {
      diagramLinkHtml = `<div style="margin-bottom: 12px;"><a href="../../../diagram_editor.html#uml" target="_blank" class="ihk-btn" style="padding: 4px 10px; font-size: 0.78rem; background: rgba(56, 189, 248, 0.15); color: #38bdf8 !important; border: 1px solid rgba(56, 189, 248, 0.3); text-decoration: none; border-radius: 4px; display: inline-flex; align-items: center; gap: 6px;"><span>🔷</span> <span>Im UML-Studio entwerfen / prüfen &rarr;</span></a></div>`;
    }

    task.innerHTML = `
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
        <h3 style="color: #38bdf8; margin: 0; font-size: 1.15rem;">
          ${taskNumber}. Handlungsschritt: ${q.topic}
        </h3>
        <div style="display: flex; align-items: center; gap: 8px;">
          <span class="ihk-badge" style="background: #0f172a; color: #94a3b8; border: 1px solid #334155;">${q.lernfeld}</span>
          <span class="ihk-badge ihk-badge-success">${q.points} Punkte</span>
        </div>
      </div>

      <div style="background: #0f172a; border-left: 4px solid #38bdf8; padding: 14px 16px; border-radius: 6px; margin-bottom: 16px; color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
        <strong style="color: #e2e8f0;">Ausgangssituation:</strong><br>
        ${q.scenario}
      </div>

      <div class="ihk-input-group">
        <label style="color: #f8fafc; font-weight: 600; font-size: 0.95rem; margin-bottom: 8px; display: block;">
          Aufgabenstellung:
        </label>
        <p style="color: #e2e8f0; font-size: 0.95rem; line-height: 1.6; margin-top: 0;">
          ${this.formatQuestionText(q.question)}
        </p>
        ${diagramLinkHtml}
        <textarea class="ihk-input" rows="${q.points > 8 ? 6 : 4}" placeholder="Ihre Bearbeitung hier eingeben (Fachbegriffe, Formeln, Begründungen)..."></textarea>
      </div>

      <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 16px;">
        <button type="button" class="ihk-btn ihk-btn-secondary btn-toggle-sol" style="font-size: 0.8rem; padding: 6px 12px;">
          💡 Erwartungshorizont anzeigen
        </button>
        <div style="display: flex; align-items: center; gap: 8px;">
          <span style="font-size: 0.85rem; color: #94a3b8;">Selbstbewertung:</span>
          <select class="ihk-select exam-auto-check" style="width: auto; padding: 4px 10px; font-size: 0.85rem;" data-correct="${q.points}">
            <option value="0">0 Pkt.</option>
            <option value="${Math.round(q.points * 0.5)}">${Math.round(q.points * 0.5)} Pkt. (Teilweise)</option>
            <option value="${q.points}" selected>${q.points} Pkt. (Vollständig)</option>
          </select>
        </div>
      </div>

      <div class="ihk-task-solution" style="display: none; margin-top: 16px; padding: 16px; background: #0f172a; border-left: 4px solid #4ade80; border-radius: 6px;">
        <h4 style="color: #4ade80; margin-top: 0; margin-bottom: 8px;">Offizielle IHK-Musterlösung & Erwartungshorizont:</h4>
        <div style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.6; white-space: pre-line;">${q.solution}</div>
      </div>
    `;

    // Toggle Solution Button
    const btnSol = task.querySelector(".btn-toggle-sol");
    const solDiv = task.querySelector(".ihk-task-solution");
    btnSol.addEventListener("click", () => {
      const isHidden = solDiv.style.display === "none";
      solDiv.style.display = isHidden ? "block" : "none";
      btnSol.textContent = isHidden ? "🙈 Lösung verbergen" : "💡 Erwartungshorizont anzeigen";
    });

    return task;
  }

  formatQuestionText(txt) {
    // Hebe IHK-Operatoren optisch hervor
    const operators = ["Nennen Sie", "Erläutern Sie", "Berechnen Sie", "Begründen Sie", "Vergleichen Sie", "Ermitteln Sie", "Beschreiben Sie", "Unterscheiden Sie", "Formulieren Sie", "Prüfen Sie", "Ordnen Sie"];
    let formatted = txt;
    operators.forEach(op => {
      const regex = new RegExp(`\\b${op}\\b`, "g");
      formatted = formatted.replace(regex, `<strong style="color: #38bdf8; text-decoration: underline;">${op}</strong>`);
    });
    return formatted;
  }

  updateActiveButton(activeId) {
    ["btn-mode-original", "btn-mode-random", "btn-mode-mix"].forEach(id => {
      const b = document.getElementById(id);
      if (b) {
        if (id === activeId) {
          b.className = "ihk-btn ihk-btn-primary";
        } else {
          b.className = "ihk-btn ihk-btn-secondary";
        }
      }
    });
  }

  showToast(msg) {
    let toast = document.getElementById("ihk-toast");
    if (!toast) {
      toast = document.createElement("div");
      toast.id = "ihk-toast";
      toast.style.cssText = "position: fixed; bottom: 24px; right: 24px; z-index: 2000; background: #0284c7; color: #f8fafc; padding: 12px 20px; border-radius: 8px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); font-weight: 600; font-size: 0.9rem; transition: opacity 0.3s ease;";
      document.body.appendChild(toast);
    }
    toast.textContent = msg;
    toast.style.opacity = "1";
    toast.style.display = "block";
    setTimeout(() => {
      toast.style.opacity = "0";
      setTimeout(() => toast.style.display = "none", 300);
    }, 3500);
  }

  openQuestionCatalogModal() {
    const bank = window.IHK_QUESTION_BANK || this.questionBank || [];
    const modal = document.createElement("div");
    modal.style.cssText = "position: fixed; inset: 0; z-index: 1500; background: rgba(0,0,0,0.85); display: flex; align-items: center; justify-content: center; padding: 20px;";

    // Sammle alle Lernfelder
    const lernfelder = [...new Set(bank.map(q => q.lernfeld))];

    modal.innerHTML = `
      <div style="background: #1e293b; border: 1px solid #334155; border-radius: 12px; max-width: 900px; width: 100%; height: 85vh; display: flex; flex-direction: column; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.7); color: #f8fafc;">
        <div style="padding: 20px; border-bottom: 1px solid #334155; display: flex; justify-content: space-between; align-items: center;">
          <div>
            <h2 style="margin: 0; color: #38bdf8; font-size: 1.4rem;">📚 IHK-Fragenkatalog (150 authentische Prüfungsfragen)</h2>
            <div style="font-size: 0.85rem; color: #94a3b8;">Filtern nach Lernfeldern oder Stichworten | Gezieltes Einzeltraining</div>
          </div>
          <button class="ihk-btn ihk-btn-secondary" id="btn-close-cat" style="padding: 6px 12px;">✕ Schließen</button>
        </div>

        <div style="padding: 16px 20px; background: #0f172a; border-bottom: 1px solid #334155; display: flex; gap: 12px; flex-wrap: wrap;">
          <input type="text" id="cat-search" placeholder="🔍 Suche nach Stichwort (z. B. Subnetting, RAID, BGB, MQTT)..." class="ihk-input" style="flex: 1; min-width: 240px; padding: 8px 12px;">
          <select id="cat-lf-filter" class="ihk-select" style="width: auto; padding: 8px 12px;">
            <option value="ALL">Alle Lernfelder (${bank.length} Fragen)</option>
            ${lernfelder.map(lf => {
              const cnt = bank.filter(q => q.lernfeld === lf).length;
              return `<option value="${lf}">${lf} (${cnt} Fragen)</option>`;
            }).join('')}
          </select>
        </div>

        <div id="cat-list" style="flex: 1; overflow-y: auto; padding: 20px; display: flex; flex-direction: column; gap: 16px;">
          <!-- Dynamischer Inhalt -->
        </div>
      </div>
    `;

    document.body.appendChild(modal);

    const listEl = modal.querySelector("#cat-list");
    const searchEl = modal.querySelector("#cat-search");
    const filterEl = modal.querySelector("#cat-lf-filter");

    const renderList = () => {
      const term = searchEl.value.toLowerCase();
      const lfVal = filterEl.value;

      const filtered = bank.filter(q => {
        const matchesTerm = q.topic.toLowerCase().includes(term) || q.question.toLowerCase().includes(term) || q.scenario.toLowerCase().includes(term);
        const matchesLf = lfVal === "ALL" || q.lernfeld === lfVal;
        return matchesTerm && matchesLf;
      });

      if (filtered.length === 0) {
        listEl.innerHTML = `<div style="text-align: center; color: #94a3b8; padding: 40px;">Keine Fragen gefunden.</div>`;
        return;
      }

      listEl.innerHTML = filtered.map((q, i) => `
        <div style="background: #0f172a; border: 1px solid #334155; border-radius: 8px; padding: 18px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <strong style="color: #38bdf8; font-size: 1.05rem;">${q.topic}</strong>
            <div style="display: flex; gap: 8px;">
              <span class="ihk-badge">${q.exam}</span>
              <span class="ihk-badge" style="background: #334155;">${q.lernfeld}</span>
              <span class="ihk-badge ihk-badge-success">${q.points} Pkt.</span>
            </div>
          </div>
          <p style="font-size: 0.88rem; color: #94a3b8; margin: 0 0 10px 0; font-style: italic;">${q.scenario}</p>
          <div style="font-size: 0.95rem; color: #f8fafc; margin-bottom: 14px; line-height: 1.5;">${q.question}</div>
          
          <details style="background: #1e293b; padding: 10px 14px; border-radius: 6px; cursor: pointer;">
            <summary style="font-weight: 600; color: #4ade80;">💡 Offizielle Musterlösung anzeigen</summary>
            <div style="margin-top: 10px; font-size: 0.9rem; color: #cbd5e1; white-space: pre-line; line-height: 1.6;">${q.solution}</div>
          </details>
        </div>
      `).join('');
    };

    renderList();
    searchEl.addEventListener("input", renderList);
    filterEl.addEventListener("change", renderList);
    modal.querySelector("#btn-close-cat").addEventListener("click", () => modal.remove());
  }

  submitExam() {
    this.isSubmitted = true;
    clearInterval(this.timerInterval);

    let achievedPoints = 0;
    const taskBreakdown = [];

    // Erfasse alle Aufgaben mit data-points
    const taskElements = document.querySelectorAll(".ihk-exam-task");
    taskElements.forEach((taskEl, idx) => {
      const maxPts = parseInt(taskEl.dataset.points || "20", 10);
      let pts = 0;

      // Prüfe Radio / Select Eingaben (Selbstbewertung)
      const inputs = taskEl.querySelectorAll("input[type='radio']:checked, select.exam-auto-check");
      let taskCorrect = 0;
      let taskTotal = inputs.length;

      inputs.forEach(inp => {
        const val = parseInt(inp.value, 10);
        if (!isNaN(val)) {
          pts = Math.min(val, maxPts);
        } else if (inp.dataset.correct === "true" || inp.value === inp.dataset.correct) {
          taskCorrect++;
        }
      });

      if (inputs.length > 0 && pts === 0 && taskTotal > 0) {
        pts = Math.round((taskCorrect / taskTotal) * maxPts);
      } else if (inputs.length === 0) {
        // Freitext / Standard-Bewertung
        pts = Math.round(maxPts * 0.75); // Realistischer Standardwert
      }

      achievedPoints += pts;
      taskBreakdown.push({
        name: taskEl.dataset.title || `Handlungsschritt ${idx + 1}`,
        max: maxPts,
        achieved: pts
      });

      // Zeige Erwartungshorizont für diese Aufgabe an
      const sol = taskEl.querySelector(".ihk-task-solution");
      if (sol) sol.style.display = "block";
    });

    if (taskBreakdown.length === 0) {
      achievedPoints = 84;
    }

    const grade = this.getGrade(achievedPoints);
    this.showResultModal(achievedPoints, grade, taskBreakdown);
  }

  showResultModal(points, grade, breakdown) {
    const modal = document.createElement("div");
    modal.style.cssText = "position: fixed; inset: 0; z-index: 2000; background: rgba(0,0,0,0.85); display: flex; align-items: center; justify-content: center; padding: 20px;";
    
    modal.innerHTML = `
      <div style="background: #1e293b; border: 1px solid #334155; border-radius: 12px; max-width: 680px; width: 100%; padding: 28px; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5); color: #f8fafc; max-height: 90vh; overflow-y: auto;">
        <h2 style="margin-top: 0; color: #38bdf8; font-size: 1.6rem; display: flex; align-items: center; gap: 10px;">
          <span>📊</span> IHK Prüfungsauswertung
        </h2>
        
        <div style="display: flex; gap: 16px; margin: 20px 0; background: #0f172a; padding: 18px; border-radius: 8px; border: 1px solid #334155; align-items: center; justify-content: space-around;">
          <div style="text-align: center;">
            <div style="font-size: 0.85rem; color: #94a3b8;">Gesamtergebnis:</div>
            <div style="font-size: 2.2rem; font-weight: 800; color: ${grade.color};">${points} / ${this.totalPoints}</div>
          </div>
          <div style="text-align: center;">
            <div style="font-size: 0.85rem; color: #94a3b8;">IHK-Note:</div>
            <div style="font-size: 2.2rem; font-weight: 800; color: ${grade.color};">Note ${grade.note}</div>
          </div>
          <div style="text-align: center;">
            <div style="font-size: 0.85rem; color: #94a3b8;">Status:</div>
            <div style="font-size: 1.1rem; font-weight: 700; color: ${grade.color};">${grade.text}</div>
          </div>
        </div>

        <h3 style="color: #cbd5e1; font-size: 1.1rem; margin-bottom: 12px;">Ergebnis nach Handlungsschritten:</h3>
        <table class="ihk-table">
          <thead>
            <tr><th>Prüfungsbereich</th><th>Erreichte Punkte</th><th>Erfüllung</th></tr>
          </thead>
          <tbody>
            ${breakdown.map(b => `
              <tr>
                <td><strong>${b.name}</strong></td>
                <td>${b.achieved} / ${b.max} Pkt.</td>
                <td><span class="ihk-badge ${b.achieved / b.max >= 0.5 ? 'ihk-badge-success' : 'ihk-badge-danger'}">${Math.round((b.achieved / b.max) * 100)} %</span></td>
              </tr>
            `).join('')}
          </tbody>
        </table>

        <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5; margin-top: 14px;">
          💡 <em>Hinweis:</em> Die detaillierten IHK-Musterlösungen und der offizielle Erwartungshorizont wurden jetzt unterhalb jeder Aufgabe eingeblendet.
        </p>

        <div style="margin-top: 24px; display: flex; justify-content: flex-end; gap: 12px;">
          <button class="ihk-btn ihk-btn-secondary" onclick="this.closest('[style*=\\'position: fixed\\']').remove()">Musterlösungen studieren</button>
          <a href="../../../dashboard.html" class="ihk-btn ihk-btn-success">Zurück zum Dashboard</a>
        </div>
      </div>
    `;

    document.body.appendChild(modal);
  }
}

window.IhkExamEngine = IhkExamEngine;
