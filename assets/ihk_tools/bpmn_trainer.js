/**
 * 🔄 IHK BPMN 2.0 & EPK INTERAKTIVER TRAINER 🔄
 * ============================================
 * Interaktiver Trainer zur Geschäftsprozessmodellierung:
 * 1. Gateway-Logik (XOR, AND, OR) und Pfad-Entscheidungen
 * 2. Pool & Lane Regeln (Sequenzfluss vs. Nachrichtenfluss)
 * 3. EPK-Syntaxregeln (Ereignis-Funktions-Alternation, Konnektoren)
 */

class BpmnTrainer {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    this.currentTask = 0;
    this.tasks = [
      {
        title: "Aufgabe 1: BPMN 2.0 Gateway-Auswahl für IT-Support",
        scenario: "Ein Kunde meldet ein Softwareproblem im Ticketsystem. Der First-Level-Support analysiert die Anfrage. Wenn das Problem durch Standardwissen gelöst werden kann, wird sofort eine Lösung an den Kunden geschickt. Falls Spezialwissen erforderlich ist, wird das Ticket an das Entwicklerteam eskaliert. Es wird EXAKT EINER dieser beiden Pfade gewählt.",
        question: "Welches BPMN 2.0 Gateway muss für diese Verzweigung eingesetzt werden?",
        options: [
          { text: "Exklusives Gateway (XOR) - Raute mit 'X' oder leer", correct: true, hint: "Richtig! XOR (Exclusive OR) schlägt genau einen Alternativpfad basierend auf Bedingungen ein." },
          { text: "Paralleles Gateway (AND) - Raute mit '+'", correct: false, hint: "Falsch. AND würde BEIDE Pfade gleichzeitig auslösen." },
          { text: "Inklusives Gateway (OR) - Raute mit 'O'", correct: false, hint: "Falsch. OR erlaubt eine beliebige Kombination (1 bis alle Pfade)." },
          { text: "Ereignisbasiertes Gateway - Raute mit Doppelkreis und Fünfeck", correct: false, hint: "Falsch. Ein event-basiertes Gateway wartet auf externe Ereignisse, nicht auf Datenbedingungen." }
        ]
      },
      {
        title: "Aufgabe 2: Sequenzfluss vs. Nachrichtenfluss über Pool-Grenzen",
        scenario: "Ein Onlineshop (Pool 'Webshop AG') kommuniziert mit einem externen Logistikdienstleister (Pool 'LogiTrans GmbH'). Eine Bestellung wurde abgeschlossen und soll an LogiTrans übertragen werden.",
        question: "Welche Verbindungslinie ist zwischen zwei getrennten Pools (Blackbox oder Whitebox) nach BPMN 2.0-Standard zulässig?",
        options: [
          { text: "Durchgezogene Linie mit gefülltem Pfeil (Sequenzfluss)", correct: false, hint: "Regelverstoß! Ein Sequenzfluss darf NIEMALS eine Pool-Grenze überschreiten." },
          { text: "Gestrichelte Linie mit offenem Pfeil und Kreis am Ursprung (Nachrichtenfluss)", correct: true, hint: "Perfekt! Nachrichtenflüsse (Message Flow) sind das EINZIGE Mittel zur Kommunikation zwischen getrennten Pools." },
          { text: "Gepunktete Linie ohne Pfeilspitze (Assoziation)", correct: false, hint: "Assoziationen verbinden lediglich Datenobjekte oder Textanmerkungen mit Elementen." },
          { text: "Doppelte durchgezogene Linie", correct: false, hint: "Dieses Symbol existiert im BPMN 2.0 Standard nicht." }
        ]
      },
      {
        title: "Aufgabe 3: EPK Syntaxregeln (Ereignisgesteuerte Prozesskette)",
        scenario: "Ein Auszubildender zeichnet eine EPK für die Serverüberwachung. Nach dem Ereignis 'Server ausgefallen' setzt er direkt einen XOR-Konnektor, um zwischen zwei Folgeaktionen zu verzweigen.",
        question: "Ist diese Konstruktion nach den formalen Syntaxregeln einer EPK zulässig?",
        options: [
          { text: "Nein! Ein Ereignis hat keine Entscheidungskraft. Eine XOR- oder ODER-Verzweigung darf nur nach einer FUNKTION erfolgen.", correct: true, hint: "Hervorragend! Ein Ereignis ist ein passiver Zustand ohne logische Intelligenz. Nur Funktionen treffen Entscheidungen, die danach mit XOR/ODER verzweigen dürfen." },
          { text: "Ja, jedes Element darf beliebig mit Konnektoren verzweigen.", correct: false, hint: "Falsch. Die Konnektorenregeln der EPK verbieten XOR/ODER direkt nach einem einzelnen Ereignis." },
          { text: "Nein, Konnektoren dürfen in EPKs grundsätzlich nur zur Zusammenführung, nie zur Verzweigung genutzt werden.", correct: false, hint: "Falsch. Konnektoren können sowohl verzweigen als auch zusammenführen." },
          { text: "Ja, solange das Ereignis ein Sechseck ist.", correct: false, hint: "Falsch. Die geometrische Form ändert nichts an den logischen Verknüpfungsregeln." }
        ]
      }
    ];
    this.init();
  }

  init() {
    if (!this.container) return;
    this.render();
  }

  render() {
    const t = this.tasks[this.currentTask];
    this.container.innerHTML = `
      <div class="ihk-tool-card" style="background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 24px; margin-bottom: 24px;">
        <div class="ihk-tool-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
          <div>
            <h3 style="color: #38bdf8; margin: 0; font-size: 1.3rem;">🔄 BPMN 2.0 & EPK Modellierungs-Trainer</h3>
            <p style="color: #94a3b8; font-size: 0.9rem; margin: 4px 0 0 0;">Frage ${this.currentTask + 1} von ${this.tasks.length}</p>
          </div>
          <div style="display: flex; gap: 8px;">
            ${this.tasks.map((_, i) => `
              <button class="ihk-btn ${i === this.currentTask ? 'ihk-btn-primary' : 'ihk-btn-secondary'}" style="padding: 4px 10px; font-size: 0.8rem;" onclick="window.bpmnTrainer.switchTask(${i})">
                ${i + 1}
              </button>
            `).join("")}
          </div>
        </div>

        <div style="background: #0f172a; padding: 16px; border-radius: 8px; border: 1px solid #334155; margin-bottom: 20px;">
          <h4 style="color: #facc15; margin: 0 0 8px 0; font-size: 1.05rem;">${t.title}</h4>
          <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6; margin: 0 0 12px 0;">
            ${t.scenario}
          </p>
          <strong style="color: #38bdf8; font-size: 0.95rem;">${t.question}</strong>
        </div>

        <div style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 20px;">
          ${t.options.map((opt, i) => `
            <div id="bpmn-opt-${i}" style="background: #0f172a; border: 1px solid #334155; border-radius: 8px; padding: 14px 16px; cursor: pointer; transition: all 0.2s;" onclick="window.bpmnTrainer.selectOption(${i})">
              <label style="cursor: pointer; display: flex; align-items: center; gap: 12px; color: #f8fafc; font-size: 0.92rem;">
                <input type="radio" name="bpmn-radio" value="${i}" style="transform: scale(1.2);">
                <span>${opt.text}</span>
              </label>
            </div>
          `).join("")}
        </div>

        <div style="display: flex; gap: 10px;">
          <button class="ihk-btn ihk-btn-success" id="btn-check-bpmn">✓ Antwort prüfen</button>
          <button class="ihk-btn ihk-btn-secondary" id="btn-next-bpmn" ${this.currentTask === this.tasks.length - 1 ? 'disabled' : ''}>Nächste Aufgabe →</button>
        </div>

        <div id="bpmn-feedback" class="ihk-result-box" style="margin-top: 16px;"></div>
      </div>
    `;

    document.getElementById("btn-check-bpmn").addEventListener("click", () => this.check());
    document.getElementById("btn-next-bpmn").addEventListener("click", () => {
      if (this.currentTask < this.tasks.length - 1) {
        this.switchTask(this.currentTask + 1);
      }
    });
  }

  selectOption(index) {
    const radios = document.getElementsByName("bpmn-radio");
    if (radios[index]) radios[index].checked = true;
  }

  switchTask(index) {
    this.currentTask = index;
    this.render();
  }

  check() {
    const t = this.tasks[this.currentTask];
    const radios = document.getElementsByName("bpmn-radio");
    let selected = -1;
    for (let i = 0; i < radios.length; i++) {
      if (radios[i].checked) {
        selected = i;
        break;
      }
    }

    const box = document.getElementById("bpmn-feedback");
    box.style.display = "block";

    if (selected === -1) {
      box.innerHTML = `<span style="color: #facc15;">⚠️ Bitte wählen Sie eine Antwort aus.</span>`;
      return;
    }

    const chosen = t.options[selected];
    t.options.forEach((opt, idx) => {
      const card = document.getElementById(`bpmn-opt-${idx}`);
      if (opt.correct) {
        card.style.borderColor = "#22c55e";
        card.style.background = "rgba(34, 197, 94, 0.15)";
      } else if (idx === selected) {
        card.style.borderColor = "#ef4444";
        card.style.background = "rgba(239, 68, 68, 0.15)";
      }
    });

    if (chosen.correct) {
      box.innerHTML = `
        <div style="border-left: 4px solid #22c55e; padding-left: 12px; color: #4ade80;">
          <strong>🎉 Ausgezeichnet!</strong><br>${chosen.hint}
        </div>
      `;
    } else {
      box.innerHTML = `
        <div style="border-left: 4px solid #ef4444; padding-left: 12px; color: #f87171;">
          <strong>❌ Nicht ganz:</strong><br>${chosen.hint}
        </div>
      `;
    }
  }
}

document.addEventListener("DOMContentLoaded", () => {
  if (document.getElementById("bpmn-trainer-container")) {
    window.bpmnTrainer = new BpmnTrainer("bpmn-trainer-container");
  }
});
