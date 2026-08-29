/**
 * 🧩 INTERAKTIVES PARSONS-PUZZLE & PRIMM WIDGET 🧩
 * =================================================
 * Basiert auf der Forschung von Dale Parsons & Barbara Ericson.
 * Ermöglicht Schülerinnen und Schülern das Sortieren von Code-Blöcken
 * mit sofortigem Feedback und Gamification-XP.
 */

(function () {
  class ParsonsWidget {
    constructor(container) {
      this.container = container;
      this.puzzleId = container.dataset.puzzleId || "puzzle_" + Math.random().toString(36).substr(2, 9);
      this.initialLines = JSON.parse(container.dataset.lines || "[]");
      this.solution = JSON.parse(container.dataset.solution || "[]");
      this.explanation = container.dataset.explanation || "Sehr gut! Du hast die Logik fehlerfrei aufgebaut.";
      this.xpReward = parseInt(container.dataset.xp || "25", 10);
      
      this.currentLines = [...this.initialLines];
      this.isSolved = this.loadSolvedState();
      this.render();
    }

    loadSolvedState() {
      try {
        const solved = JSON.parse(localStorage.getItem("parsons_solved") || "{}");
        return !!solved[this.puzzleId];
      } catch (e) {
        return false;
      }
    }

    saveSolvedState() {
      try {
        const solved = JSON.parse(localStorage.getItem("parsons_solved") || "{}");
        solved[this.puzzleId] = true;
        localStorage.setItem("parsons_solved", JSON.stringify(solved));
        
        // Gamification XP Bonus gutschreiben
        if (window.GAMIFICATION_DATA) {
          window.GAMIFICATION_DATA.xp = (window.GAMIFICATION_DATA.xp || 0) + this.xpReward;
          if (typeof renderGamificationHUD === "function") {
            renderGamificationHUD();
          }
        }
      } catch (e) {
        console.error("Fehler beim Speichern des Puzzle-Status:", e);
      }
    }

    render() {
      this.container.classList.add("parsons-box");
      this.container.innerHTML = `
        <div class="parsons-header">
          <div class="parsons-title">
            <span>🧩 Code-Puzzle (Parsons Problem)</span>
            <span class="parsons-badge">${this.isSolved ? '✅ Gelöst (+'+this.xpReward+' XP)' : '⭐ +'+this.xpReward+' XP'}</span>
          </div>
          <p class="parsons-instruction">
            Bringe die Code-Blöcke in die richtige logische Reihenfolge, bevor du selbst programmierst:
          </p>
        </div>

        <div class="parsons-board" id="board-${this.puzzleId}">
          ${this.currentLines.map((line, idx) => `
            <div class="parsons-line" draggable="true" data-index="${idx}">
              <div class="parsons-handle">☰</div>
              <div class="parsons-code"><code>${this.escapeHtml(line)}</code></div>
              <div class="parsons-actions">
                <button type="button" class="btn-parsons-move btn-up" data-dir="-1" title="Nach oben" ${idx === 0 ? 'disabled' : ''}>▲</button>
                <button type="button" class="btn-parsons-move btn-down" data-dir="1" title="Nach unten" ${idx === this.currentLines.length - 1 ? 'disabled' : ''}>▼</button>
              </div>
            </div>
          `).join("")}
        </div>

        <div class="parsons-controls">
          <button type="button" class="btn btn-parsons-check" id="check-${this.puzzleId}">
            ${this.isSolved ? '🔄 Erneut prüfen' : '✨ Lösung prüfen'}
          </button>
          <button type="button" class="btn btn-secondary btn-parsons-hint" id="hint-${this.puzzleId}">
            💡 Ersten Block verraten
          </button>
        </div>

        <div class="parsons-feedback" id="feedback-${this.puzzleId}" style="${this.isSolved ? 'display: block;' : 'display: none;'}">
          ${this.isSolved ? `<div class="box box-success"><div class="box-title">🎉 Perfekt gelöst!</div>${this.explanation}</div>` : ''}
        </div>
      `;

      this.attachEvents();
    }

    escapeHtml(text) {
      const div = document.createElement("div");
      div.textContent = text;
      return div.innerHTML;
    }

    attachEvents() {
      const board = document.getElementById(`board-${this.puzzleId}`);
      const checkBtn = document.getElementById(`check-${this.puzzleId}`);
      const hintBtn = document.getElementById(`hint-${this.puzzleId}`);

      // Up / Down Buttons
      board.querySelectorAll(".btn-parsons-move").forEach(btn => {
        btn.addEventListener("click", (e) => {
          const lineEl = e.target.closest(".parsons-line");
          const idx = parseInt(lineEl.dataset.index, 10);
          const dir = parseInt(e.target.dataset.dir, 10);
          const targetIdx = idx + dir;

          if (targetIdx >= 0 && targetIdx < this.currentLines.length) {
            const temp = this.currentLines[idx];
            this.currentLines[idx] = this.currentLines[targetIdx];
            this.currentLines[targetIdx] = temp;
            this.render();
          }
        });
      });

      // Check Button
      checkBtn.addEventListener("click", () => this.checkSolution());

      // Hint Button
      hintBtn.addEventListener("click", () => {
        const correctFirst = this.solution[0];
        const currentFirstIdx = this.currentLines.indexOf(correctFirst);
        if (currentFirstIdx > 0) {
          this.currentLines.splice(currentFirstIdx, 1);
          this.currentLines.unshift(correctFirst);
          this.render();
          const feedback = document.getElementById(`feedback-${this.puzzleId}`);
          feedback.innerHTML = `<div class="box box-tipp"><div class="box-title">💡 Tipp:</div>Der erste Block <code>${this.escapeHtml(correctFirst)}</code> wurde an den Anfang gesetzt!</div>`;
          feedback.style.display = "block";
        }
      });
    }

    checkSolution() {
      const feedback = document.getElementById(`feedback-${this.puzzleId}`);
      let correct = true;

      for (let i = 0; i < this.solution.length; i++) {
        if (this.currentLines[i] !== this.solution[i]) {
          correct = false;
          break;
        }
      }

      if (correct) {
        feedback.innerHTML = `
          <div class="box box-success" style="animation: fadeIn 0.3s ease;">
            <div class="box-title">🎉 Bravo! Alle Blöcke sind in der perfekten Reihenfolge!</div>
            <p>${this.explanation}</p>
            <p style="margin-top: 8px; font-weight: bold; color: var(--success);">
              ⭐ Du hast <strong>+${this.xpReward} XP</strong> für deinen Entwickler-Pass freigeschaltet!
            </p>
          </div>
        `;
        feedback.style.display = "block";
        this.saveSolvedState();
        this.isSolved = true;
      } else {
        feedback.innerHTML = `
          <div class="box box-warning" style="animation: fadeIn 0.3s ease;">
            <div class="box-title">🤔 Noch nicht ganz...</div>
            <p>Einige Zeilen stehen noch an der falschen Stelle. Überlege Schritt für Schritt: Was muss zuerst initialisiert oder berechnet werden, bevor der nächste Schritt ausgeführt werden kann?</p>
          </div>
        `;
        feedback.style.display = "block";
      }
    }
  }

  // Initialisiere alle Puzzle-Widgets auf der Seite
  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".parsons-puzzle").forEach(el => {
      new ParsonsWidget(el);
    });
  });
})();
