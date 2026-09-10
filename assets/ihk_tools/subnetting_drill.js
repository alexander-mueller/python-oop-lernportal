/**
 * 🧮 IHK SUBNETTING DRILL MASTER 🧮
 * =================================
 * Interaktiver Subnetting-Trainer für AP1 & AP2 (LF 3 & LF 9):
 * - Endlose Zufallsaufgaben (FLSM & VLSM)
 * - Magische Zahl (256 - Oktett) Erklärung
 * - Automatische Validierung aller 6 Parameter
 */

class SubnettingDrill {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    this.currentTask = null;
    this.stats = { total: 0, correct: 0, streak: 0 };
    this.init();
  }

  init() {
    if (!this.container) return;
    this.render();
    this.generateTask();
  }

  render() {
    this.container.innerHTML = `
      <div class="ihk-tool-card">
        <div class="ihk-tool-header">
          <div class="ihk-tool-title">
            <span>🧮</span> IHK Subnetting-Drill Master
          </div>
          <div>
            <span class="ihk-badge" id="drill-stats">0 gelöst (0%)</span>
            <span class="ihk-badge ihk-badge-warning" id="drill-streak">🔥 Streak: 0</span>
          </div>
        </div>

        <div style="background: #0f172a; padding: 16px; border-radius: 8px; border: 1px solid #334155; margin-bottom: 20px;">
          <div style="font-size: 0.85rem; color: #94a3b8; margin-bottom: 4px;">Gegebene IP-Adresse & CIDR-Prefix:</div>
          <div id="drill-ip-display" style="font-size: 1.6rem; font-weight: 800; color: #38bdf8; font-family: monospace;">
            192.168.10.45 / 27
          </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; margin-bottom: 20px;">
          <div class="ihk-input-group">
            <label>1. Subnetzmaske (Dezimal):</label>
            <input type="text" id="ans-mask" class="ihk-input" placeholder="z. B. 255.255.255.224">
          </div>
          <div class="ihk-input-group">
            <label>2. Netz-ID (Netzadresse):</label>
            <input type="text" id="ans-net" class="ihk-input" placeholder="z. B. 192.168.10.32">
          </div>
          <div class="ihk-input-group">
            <label>3. Erste nutzbare Host-IP:</label>
            <input type="text" id="ans-first" class="ihk-input" placeholder="z. B. 192.168.10.33">
          </div>
          <div class="ihk-input-group">
            <label>4. Letzte nutzbare Host-IP:</label>
            <input type="text" id="ans-last" class="ihk-input" placeholder="z. B. 192.168.10.62">
          </div>
          <div class="ihk-input-group">
            <label>5. Broadcast-Adresse:</label>
            <input type="text" id="ans-bcast" class="ihk-input" placeholder="z. B. 192.168.10.63">
          </div>
          <div class="ihk-input-group">
            <label>6. Anzahl nutzbarer Hosts (2^n - 2):</label>
            <input type="number" id="ans-hosts" class="ihk-input" placeholder="z. B. 30">
          </div>
        </div>

        <div style="display: flex; gap: 12px; flex-wrap: wrap;">
          <button class="ihk-btn ihk-btn-success" id="btn-check-drill">✓ Eingaben prüfen</button>
          <button class="ihk-btn ihk-btn-secondary" id="btn-next-drill">🎲 Neue Zufallsaufgabe</button>
          <button class="ihk-btn ihk-btn-secondary" id="btn-magic-hint">💡 Magische Zahl Erklärung</button>
        </div>

        <div id="drill-result" class="ihk-result-box"></div>
      </div>
    `;

    document.getElementById("btn-check-drill").addEventListener("click", () => this.checkAnswer());
    document.getElementById("btn-next-drill").addEventListener("click", () => this.generateTask());
    document.getElementById("btn-magic-hint").addEventListener("click", () => this.toggleHint());
  }

  generateTask() {
    // Generiere IP im privaten Bereich (Klasse A, B oder C)
    const type = Math.floor(Math.random() * 3);
    let ipParts = [];
    let prefix = 24;

    if (type === 0) {
      ipParts = [192, 168, Math.floor(Math.random() * 100) + 1, Math.floor(Math.random() * 254) + 1];
      prefix = Math.floor(Math.random() * 7) + 24; // /24 bis /30
    } else if (type === 1) {
      ipParts = [172, Math.floor(Math.random() * 16) + 16, Math.floor(Math.random() * 254) + 1, Math.floor(Math.random() * 254) + 1];
      prefix = Math.floor(Math.random() * 9) + 20; // /20 bis /28
    } else {
      ipParts = [10, Math.floor(Math.random() * 254) + 1, Math.floor(Math.random() * 254) + 1, Math.floor(Math.random() * 254) + 1];
      prefix = Math.floor(Math.random() * 12) + 18; // /18 bis /29
    }

    const ipInt = (ipParts[0] << 24) | (ipParts[1] << 16) | (ipParts[2] << 8) | ipParts[3];
    const maskInt = prefix === 0 ? 0 : (~0 << (32 - prefix)) >>> 0;
    const netInt = (ipInt & maskInt) >>> 0;
    const bcastInt = (netInt | ~maskInt) >>> 0;
    const firstInt = (netInt + 1) >>> 0;
    const lastInt = (bcastInt - 1) >>> 0;
    const hostBits = 32 - prefix;
    const usableHosts = Math.pow(2, hostBits) - 2;

    const intToIp = (num) => [
      (num >>> 24) & 255,
      (num >>> 16) & 255,
      (num >>> 8) & 255,
      num & 255
    ].join(".");

    this.currentTask = {
      ip: ipParts.join("."),
      prefix: prefix,
      mask: intToIp(maskInt),
      net: intToIp(netInt),
      first: intToIp(firstInt),
      last: intToIp(lastInt),
      bcast: intToIp(bcastInt),
      hosts: usableHosts,
      magicNumber: 256 - ((maskInt >>> (8 * (3 - Math.floor(prefix / 8)))) & 255 || 256)
    };

    document.getElementById("drill-ip-display").textContent = `${this.currentTask.ip} / ${this.currentTask.prefix}`;
    document.getElementById("ans-mask").value = "";
    document.getElementById("ans-net").value = "";
    document.getElementById("ans-first").value = "";
    document.getElementById("ans-last").value = "";
    document.getElementById("ans-bcast").value = "";
    document.getElementById("ans-hosts").value = "";
    
    const resBox = document.getElementById("drill-result");
    resBox.classList.remove("active");
  }

  checkAnswer() {
    if (!this.currentTask) return;

    const ansMask = document.getElementById("ans-mask").value.trim();
    const ansNet = document.getElementById("ans-net").value.trim();
    const ansFirst = document.getElementById("ans-first").value.trim();
    const ansLast = document.getElementById("ans-last").value.trim();
    const ansBcast = document.getElementById("ans-bcast").value.trim();
    const ansHosts = parseInt(document.getElementById("ans-hosts").value.trim(), 10);

    const checks = [
      { name: "Subnetzmaske", correct: ansMask === this.currentTask.mask, expected: this.currentTask.mask, user: ansMask },
      { name: "Netzadresse", correct: ansNet === this.currentTask.net, expected: this.currentTask.net, user: ansNet },
      { name: "Erste Host-IP", correct: ansFirst === this.currentTask.first, expected: this.currentTask.first, user: ansFirst },
      { name: "Letzte Host-IP", correct: ansLast === this.currentTask.last, expected: this.currentTask.last, user: ansLast },
      { name: "Broadcast", correct: ansBcast === this.currentTask.bcast, expected: this.currentTask.bcast, user: ansBcast },
      { name: "Nutzbare Hosts", correct: ansHosts === this.currentTask.hosts, expected: this.currentTask.hosts, user: ansHosts }
    ];

    const allCorrect = checks.every(c => c.correct);
    this.stats.total++;
    if (allCorrect) {
      this.stats.correct++;
      this.stats.streak++;
    } else {
      this.stats.streak = 0;
    }

    const pct = Math.round((this.stats.correct / this.stats.total) * 100);
    document.getElementById("drill-stats").textContent = `${this.stats.correct}/${this.stats.total} gelöst (${pct}%)`;
    document.getElementById("drill-streak").textContent = `🔥 Streak: ${this.stats.streak}`;

    const resBox = document.getElementById("drill-result");
    resBox.innerHTML = `
      <h4 style="color: ${allCorrect ? '#4ade80' : '#f87171'}; margin-top: 0; font-size: 1.1rem;">
        ${allCorrect ? '🎉 Perfekt! Alle 6 Werte exakt berechnet.' : '❌ Noch nicht ganz richtig – überprüfe deine Werte:'}
      </h4>
      <table class="ihk-table">
        <thead>
          <tr><th>Parameter</th><th>Deine Eingabe</th><th>Musterlösung</th><th>Status</th></tr>
        </thead>
        <tbody>
          ${checks.map(c => `
            <tr>
              <td><strong>${c.name}</strong></td>
              <td style="font-family: monospace; color: ${c.correct ? '#4ade80' : '#f87171'}">${c.user || '<em>leer</em>'}</td>
              <td style="font-family: monospace; color: #38bdf8">${c.expected}</td>
              <td>${c.correct ? '✅ Richtig' : '❌ Falsch'}</td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    `;
    resBox.classList.add("active");
  }

  toggleHint() {
    if (!this.currentTask) return;
    const resBox = document.getElementById("drill-result");
    const octetIndex = Math.floor(this.currentTask.prefix / 8);
    const bitsInOctet = this.currentTask.prefix % 8;
    const octetNum = octetIndex + (bitsInOctet > 0 ? 1 : 0);

    resBox.innerHTML = `
      <h4 style="color: #facc15; margin-top: 0;">💡 Das IHK-Geheimnis: Die „Magische Zahl“ (Schrittweite)</h4>
      <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6;">
        Für <strong>/${this.currentTask.prefix}</strong> liegt das interessante Oktett im <strong>${octetNum}. Oktett</strong>.<br>
        1. Ermittle den Maskenwert: <strong>${this.currentTask.mask}</strong>.<br>
        2. Die Schrittweite („Magische Zahl“) ist: <code>256 - Oktettwert</code>.<br>
        3. Die Netzadressen steigen immer in Vielfachen dieser Schrittweite (0, Schrittweite, 2 × Schrittweite, ...) bis kurz vor deine gegebene IP.<br>
        4. Broadcast ist immer <code>Nächste Netzadresse - 1</code>.
      </p>
    `;
    resBox.classList.add("active");
  }
}

window.SubnettingDrill = SubnettingDrill;
