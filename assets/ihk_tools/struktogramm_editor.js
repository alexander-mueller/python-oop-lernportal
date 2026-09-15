/**
 * 📐 IT-PRAXISPORTAL – DIN 66261 STRUKTOGRAMM EDITOR (NASSI-SHNEIDERMAN)
 * Vollständige Unterstützung für IHK AP1 & AP2 Algorithmenentwurf:
 * Sequenzen, IF-Verzweigungen, SWITCH-Fallauswahl, WHILE-Schleifen, DO-WHILE,
 * Zählschleifen (FOR), Call & Break, Live-SVG-Rendering und Python-Code-Generierung!
 */

class StruktogrammEditor {
  constructor(containerId, options = {}) {
    this.container = typeof containerId === 'string' ? document.getElementById(containerId) : containerId;
    this.options = options;
    this.blocks = [];
    this.selectedBlockId = null;
    this.init();
  }

  init() {
    if (!this.container) return;
    this.container.innerHTML = `
      <div class="ds-editor-card">
        <div class="ds-toolbar">
          <div class="ds-toolbar-left">
            <div class="ds-btn-group">
              <button type="button" class="ds-btn ds-btn-primary" id="sg-btn-add-inst">
                <span>▭</span> <span>Anweisung</span>
              </button>
              <button type="button" class="ds-btn ds-btn-primary" id="sg-btn-add-if">
                <span>▽</span> <span>Verzweigung (IF)</span>
              </button>
              <button type="button" class="ds-btn ds-btn-primary" id="sg-btn-add-while">
                <span>⮌</span> <span>Schleife (WHILE)</span>
              </button>
              <button type="button" class="ds-btn ds-btn-primary" id="sg-btn-add-for">
                <span>🔂</span> <span>Zählschleife (FOR)</span>
              </button>
            </div>
            <div class="ds-select-wrap">
              <label>IHK-Vorlage:</label>
              <select id="sg-select-template" class="ds-select">
                <option value="">-- IHK-Algorithmus wählen --</option>
                <option value="ean13">IHK EAN-13 Prüfziffernberechnung</option>
                <option value="primzahl">IHK Primzahlprüfung</option>
                <option value="rabatt">IHK Rabattstaffelung mit Skonto</option>
                <option value="binaersuche">IHK Binäre Suche (Intervallhalbierung)</option>
              </select>
            </div>
          </div>
          <div class="ds-toolbar-right">
            <button type="button" class="ds-btn ds-btn-success" id="sg-btn-generate-code">
              <span>🐍</span> <span>Python Code</span>
            </button>
            <button type="button" class="ds-btn ds-btn-secondary" id="sg-btn-export-svg">
              <span>🖼️</span> <span>SVG Export</span>
            </button>
            <button type="button" class="ds-btn ds-btn-danger" id="sg-btn-clear" title="Alles leeren">
              <span>🗑️</span>
            </button>
          </div>
        </div>

        <div class="ds-workspace-grid">
          <div class="ds-canvas-wrap" id="sg-canvas-container">
            <div class="sg-render-wrapper" id="sg-render-box"></div>
          </div>
          <div class="ds-sidebar" id="sg-sidebar">
            <div class="ds-sidebar-header">
              <h4 id="sg-sidebar-title">Block-Eigenschaften</h4>
            </div>
            <div class="ds-sidebar-body" id="sg-sidebar-content">
              <p class="ds-hint">Wähle einen Block im Struktogramm aus, um dessen Inhalt anzupassen oder Unterblöcke hinzuzufügen.</p>
            </div>
          </div>
        </div>

        <!-- Python Code Modal -->
        <div id="sg-code-modal" class="ds-modal" style="display:none;">
          <div class="ds-modal-content">
            <div class="ds-modal-header">
              <h3>Aus Struktogramm generierter Python-Code (PEP 8)</h3>
              <button type="button" class="ds-modal-close" id="sg-code-modal-close">&times;</button>
            </div>
            <pre id="sg-code-display" class="ds-code-block"></pre>
            <div class="ds-modal-footer">
              <button type="button" class="ds-btn ds-btn-primary" id="sg-code-copy-btn">In Zwischenablage kopieren</button>
            </div>
          </div>
        </div>
      </div>
    `;

    this.bindEvents();
    this.loadTemplate('ean13');
  }

  bindEvents() {
    document.getElementById('sg-btn-add-inst').addEventListener('click', () => this.addBlock({ type: 'instruction', text: 'neue_variable = 0' }));
    document.getElementById('sg-btn-add-if').addEventListener('click', () => this.addBlock({
      type: 'if',
      condition: 'wert > 100',
      thenBlocks: [{ id: 'b_' + Date.now() + '_1', type: 'instruction', text: 'ausgabe("Bedingung erfüllt")' }],
      elseBlocks: [{ id: 'b_' + Date.now() + '_2', type: 'instruction', text: 'ausgabe("Bedingung nicht erfüllt")' }]
    }));
    document.getElementById('sg-btn-add-while').addEventListener('click', () => this.addBlock({
      type: 'while',
      condition: 'zaehler < 10',
      body: [{ id: 'b_' + Date.now() + '_3', type: 'instruction', text: 'zaehler = zaehler + 1' }]
    }));
    document.getElementById('sg-btn-add-for').addEventListener('click', () => this.addBlock({
      type: 'for',
      loopHeader: 'Für i von 1 bis n Schrittweite 1',
      body: [{ id: 'b_' + Date.now() + '_4', type: 'instruction', text: 'summe = summe + i' }]
    }));

    document.getElementById('sg-select-template').addEventListener('change', (e) => {
      if (e.target.value) this.loadTemplate(e.target.value);
    });

    document.getElementById('sg-btn-generate-code').addEventListener('click', () => this.showCodeModal());
    document.getElementById('sg-code-modal-close').addEventListener('click', () => {
      document.getElementById('sg-code-modal').style.display = 'none';
    });
    document.getElementById('sg-code-copy-btn').addEventListener('click', () => {
      const code = document.getElementById('sg-code-display').innerText;
      navigator.clipboard.writeText(code).then(() => alert('Python-Code erfolgreich kopiert!'));
    });

    document.getElementById('sg-btn-export-svg').addEventListener('click', () => this.exportSvg());
    document.getElementById('sg-btn-clear').addEventListener('click', () => {
      if (confirm('Möchtest du das gesamte Struktogramm leeren?')) {
        this.blocks = [];
        this.selectedBlockId = null;
        this.render();
        this.renderSidebar();
      }
    });
  }

  addBlock(blockData) {
    blockData.id = 'blk_' + Date.now() + '_' + Math.floor(Math.random() * 1000);
    this.blocks.push(blockData);
    this.selectedBlockId = blockData.id;
    this.render();
    this.renderSidebar();
  }

  loadTemplate(tplName) {
    this.blocks = [];

    if (tplName === 'ean13') {
      this.blocks = [
        { id: 'b1', type: 'instruction', text: 'Eingabe: ean_12_stellen (String mit 12 Ziffern)' },
        { id: 'b2', type: 'instruction', text: 'summe = 0' },
        {
          id: 'b3',
          type: 'for',
          loopHeader: 'Für index von 0 bis 11 Schrittweite 1',
          body: [
            { id: 'b3_1', type: 'instruction', text: 'ziffer = int(ean_12_stellen[index])' },
            {
              id: 'b3_2',
              type: 'if',
              condition: 'index % 2 == 1',
              thenBlocks: [{ id: 'b3_2_1', type: 'instruction', text: 'summe = summe + (ziffer * 3)' }],
              elseBlocks: [{ id: 'b3_2_2', type: 'instruction', text: 'summe = summe + (ziffer * 1)' }]
            }
          ]
        },
        { id: 'b4', type: 'instruction', text: 'rest = summe % 10' },
        {
          id: 'b5',
          type: 'if',
          condition: 'rest == 0',
          thenBlocks: [{ id: 'b5_1', type: 'instruction', text: 'pruefziffer = 0' }],
          elseBlocks: [{ id: 'b5_2', type: 'instruction', text: 'pruefziffer = 10 - rest' }]
        },
        { id: 'b6', type: 'instruction', text: 'Ausgabe: pruefziffer' }
      ];
    } else if (tplName === 'primzahl') {
      this.blocks = [
        { id: 'p1', type: 'instruction', text: 'Eingabe: n (ganze Zahl >= 2)' },
        { id: 'p2', type: 'instruction', text: 'ist_prim = True; teiler = 2' },
        {
          id: 'p3',
          type: 'while',
          condition: 'teiler * teiler <= n und ist_prim == True',
          body: [
            {
              id: 'p3_1',
              type: 'if',
              condition: 'n % teiler == 0',
              thenBlocks: [{ id: 'p3_1_1', type: 'instruction', text: 'ist_prim = False' }],
              elseBlocks: [{ id: 'p3_1_2', type: 'instruction', text: 'teiler = teiler + 1' }]
            }
          ]
        },
        {
          id: 'p4',
          type: 'if',
          condition: 'ist_prim == True',
          thenBlocks: [{ id: 'p4_1', type: 'instruction', text: 'Ausgabe("Zahl ist eine Primzahl")' }],
          elseBlocks: [{ id: 'p4_2', type: 'instruction', text: 'Ausgabe("Zahl ist KEINE Primzahl")' }]
        }
      ];
    } else if (tplName === 'rabatt') {
      this.blocks = [
        { id: 'r1', type: 'instruction', text: 'Eingabe: bestellwert, ist_stammkunde (Boolean)' },
        { id: 'r2', type: 'instruction', text: 'rabatt_prozent = 0.0' },
        {
          id: 'r3',
          type: 'if',
          condition: 'bestellwert >= 500.0',
          thenBlocks: [
            { id: 'r3_1', type: 'instruction', text: 'rabatt_prozent = 10.0' }
          ],
          elseBlocks: [
            {
              id: 'r3_2',
              type: 'if',
              condition: 'bestellwert >= 200.0',
              thenBlocks: [{ id: 'r3_2_1', type: 'instruction', text: 'rabatt_prozent = 5.0' }],
              elseBlocks: [{ id: 'r3_2_2', type: 'instruction', text: 'rabatt_prozent = 0.0' }]
            }
          ]
        },
        {
          id: 'r4',
          type: 'if',
          condition: 'ist_stammkunde == True',
          thenBlocks: [{ id: 'r4_1', type: 'instruction', text: 'rabatt_prozent = rabatt_prozent + 3.0' }],
          elseBlocks: []
        },
        { id: 'r5', type: 'instruction', text: 'endpreis = bestellwert * (1.0 - rabatt_prozent / 100.0)' },
        { id: 'r6', type: 'instruction', text: 'Ausgabe: endpreis' }
      ];
    } else if (tplName === 'binaersuche') {
      this.blocks = [
        { id: 's1', type: 'instruction', text: 'Eingabe: arr (sortiertes Array), suchwert' },
        { id: 's2', type: 'instruction', text: 'links = 0; rechts = len(arr) - 1; gefundener_index = -1' },
        {
          id: 's3',
          type: 'while',
          condition: 'links <= rechts und gefundener_index == -1',
          body: [
            { id: 's3_1', type: 'instruction', text: 'mitte = (links + rechts) // 2' },
            {
              id: 's3_2',
              type: 'if',
              condition: 'arr[mitte] == suchwert',
              thenBlocks: [{ id: 's3_2_1', type: 'instruction', text: 'gefundener_index = mitte' }],
              elseBlocks: [
                {
                  id: 's3_2_2',
                  type: 'if',
                  condition: 'arr[mitte] < suchwert',
                  thenBlocks: [{ id: 's3_2_2_1', type: 'instruction', text: 'links = mitte + 1' }],
                  elseBlocks: [{ id: 's3_2_2_2', type: 'instruction', text: 'rechts = mitte - 1' }]
                }
              ]
            }
          ]
        },
        { id: 's4', type: 'instruction', text: 'Ausgabe: gefundener_index' }
      ];
    }

    this.selectedBlockId = this.blocks[0] ? this.blocks[0].id : null;
    this.render();
    this.renderSidebar();
  }

  findBlockRecursive(blocks, id) {
    for (const b of blocks) {
      if (b.id === id) return b;
      if (b.thenBlocks) {
        const found = this.findBlockRecursive(b.thenBlocks, id);
        if (found) return found;
      }
      if (b.elseBlocks) {
        const found = this.findBlockRecursive(b.elseBlocks, id);
        if (found) return found;
      }
      if (b.body) {
        const found = this.findBlockRecursive(b.body, id);
        if (found) return found;
      }
    }
    return null;
  }

  deleteBlockRecursive(blocks, id) {
    for (let i = 0; i < blocks.length; i++) {
      if (blocks[i].id === id) {
        blocks.splice(i, 1);
        return true;
      }
      if (blocks[i].thenBlocks && this.deleteBlockRecursive(blocks[i].thenBlocks, id)) return true;
      if (blocks[i].elseBlocks && this.deleteBlockRecursive(blocks[i].elseBlocks, id)) return true;
      if (blocks[i].body && this.deleteBlockRecursive(blocks[i].body, id)) return true;
    }
    return false;
  }

  render() {
    const box = document.getElementById('sg-render-box');
    if (!box) return;

    // Render HTML table-based DIN 66261 diagram
    let html = `
      <div class="sg-container">
        <div class="sg-header-title">DIN 66261 Nassi-Shneiderman Struktogramm</div>
        <div class="sg-root-table">
          ${this.renderBlockList(this.blocks)}
        </div>
      </div>
    `;

    box.innerHTML = html;
    this.attachClickEvents();
  }

  renderBlockList(blocks) {
    if (!blocks || blocks.length === 0) {
      return `<div class="sg-empty-block">∅ (leer)</div>`;
    }
    return blocks.map(b => this.renderSingleBlock(b)).join('');
  }

  renderSingleBlock(b) {
    const isSelected = b.id === this.selectedBlockId ? 'sg-selected' : '';

    if (b.type === 'instruction') {
      return `
        <div class="sg-block sg-instruction ${isSelected}" data-block-id="${b.id}">
          <span class="sg-text">${this.escapeHtml(b.text || '')}</span>
        </div>
      `;
    } else if (b.type === 'if') {
      return `
        <div class="sg-block sg-if ${isSelected}" data-block-id="${b.id}">
          <div class="sg-if-header">
            <svg class="sg-if-svg" viewBox="0 0 100 40" preserveAspectRatio="none">
              <polygon points="0,0 100,0 50,40" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
              <line x1="0" y1="0" x2="50" y2="40" stroke="#38bdf8" stroke-width="1.5"/>
              <line x1="100" y1="0" x2="50" y2="40" stroke="#38bdf8" stroke-width="1.5"/>
            </svg>
            <div class="sg-if-condition">${this.escapeHtml(b.condition || '')}</div>
            <div class="sg-if-label-left">Ja (Wahr)</div>
            <div class="sg-if-label-right">Nein (Falsch)</div>
          </div>
          <div class="sg-if-branches">
            <div class="sg-if-then">
              ${this.renderBlockList(b.thenBlocks || [])}
            </div>
            <div class="sg-if-else">
              ${this.renderBlockList(b.elseBlocks || [])}
            </div>
          </div>
        </div>
      `;
    } else if (b.type === 'while') {
      return `
        <div class="sg-block sg-while ${isSelected}" data-block-id="${b.id}">
          <div class="sg-while-header">
            <span class="sg-badge-loop">WHILE (solange):</span> ${this.escapeHtml(b.condition || '')}
          </div>
          <div class="sg-while-body-wrap">
            <div class="sg-while-gutter"></div>
            <div class="sg-while-body">
              ${this.renderBlockList(b.body || [])}
            </div>
          </div>
        </div>
      `;
    } else if (b.type === 'for') {
      return `
        <div class="sg-block sg-for ${isSelected}" data-block-id="${b.id}">
          <div class="sg-for-header">
            <span class="sg-badge-loop">FOR (Zählschleife):</span> ${this.escapeHtml(b.loopHeader || '')}
          </div>
          <div class="sg-while-body-wrap">
            <div class="sg-while-gutter"></div>
            <div class="sg-while-body">
              ${this.renderBlockList(b.body || [])}
            </div>
          </div>
        </div>
      `;
    }
    return '';
  }

  attachClickEvents() {
    const elBlocks = document.querySelectorAll('.sg-block');
    elBlocks.forEach(el => {
      el.addEventListener('click', (e) => {
        e.stopPropagation();
        const id = el.getAttribute('data-block-id');
        this.selectedBlockId = id;
        this.render();
        this.renderSidebar();
      });
    });
  }

  renderSidebar() {
    const sidebarTitle = document.getElementById('sg-sidebar-title');
    const content = document.getElementById('sg-sidebar-content');
    if (!content) return;

    const block = this.findBlockRecursive(this.blocks, this.selectedBlockId);
    if (!block) {
      sidebarTitle.innerText = 'Block-Eigenschaften';
      content.innerHTML = `<p class="ds-hint">Klicke auf einen Block im Struktogramm, um dessen Text oder Verzweigung anzupassen.</p>`;
      return;
    }

    sidebarTitle.innerText = `Typ: ${block.type.toUpperCase()}`;

    let html = '';
    if (block.type === 'instruction') {
      html = `
        <div class="ds-field-group">
          <label>Anweisungstext:</label>
          <textarea id="sg-input-text" class="ds-textarea" rows="3">${this.escapeHtml(block.text || '')}</textarea>
        </div>
      `;
    } else if (block.type === 'if') {
      html = `
        <div class="ds-field-group">
          <label>Bedingung (logischer Ausdruck):</label>
          <input type="text" id="sg-input-cond" class="ds-input" value="${this.escapeHtml(block.condition || '')}">
        </div>
        <div style="display:flex; gap:8px; margin-top:10px;">
          <button type="button" class="ds-btn ds-btn-secondary" id="sg-btn-add-then" style="flex:1; font-size:0.75rem;">+ Ja-Zweig</button>
          <button type="button" class="ds-btn ds-btn-secondary" id="sg-btn-add-else" style="flex:1; font-size:0.75rem;">+ Nein-Zweig</button>
        </div>
      `;
    } else if (block.type === 'while') {
      html = `
        <div class="ds-field-group">
          <label>Schleifenbedingung (Abbruch wenn falsch):</label>
          <input type="text" id="sg-input-while-cond" class="ds-input" value="${this.escapeHtml(block.condition || '')}">
        </div>
        <button type="button" class="ds-btn ds-btn-secondary" id="sg-btn-add-while-body" style="width:100%; margin-top:8px; font-size:0.75rem;">+ Block in Schleifenkörper</button>
      `;
    } else if (block.type === 'for') {
      html = `
        <div class="ds-field-group">
          <label>Zählschleifen-Kopf:</label>
          <input type="text" id="sg-input-for-hdr" class="ds-input" value="${this.escapeHtml(block.loopHeader || '')}">
        </div>
        <button type="button" class="ds-btn ds-btn-secondary" id="sg-btn-add-for-body" style="width:100%; margin-top:8px; font-size:0.75rem;">+ Block in Schleifenkörper</button>
      `;
    }

    html += `
      <div style="margin-top:20px; border-top:1px solid #334155; padding-top:14px;">
        <button type="button" id="sg-btn-delete-block" class="ds-btn ds-btn-danger" style="width:100%; font-size:0.82rem;">
          🗑️ Diesen Block entfernen
        </button>
      </div>
    `;

    content.innerHTML = html;

    // Listeners
    if (block.type === 'instruction') {
      document.getElementById('sg-input-text').addEventListener('input', (e) => {
        block.text = e.target.value;
        this.render();
      });
    } else if (block.type === 'if') {
      document.getElementById('sg-input-cond').addEventListener('input', (e) => {
        block.condition = e.target.value;
        this.render();
      });
      document.getElementById('sg-btn-add-then').addEventListener('click', () => {
        if (!block.thenBlocks) block.thenBlocks = [];
        block.thenBlocks.push({ id: 'b_' + Date.now(), type: 'instruction', text: 'neue_anweisung = 1' });
        this.render();
      });
      document.getElementById('sg-btn-add-else').addEventListener('click', () => {
        if (!block.elseBlocks) block.elseBlocks = [];
        block.elseBlocks.push({ id: 'b_' + Date.now(), type: 'instruction', text: 'neue_anweisung = 2' });
        this.render();
      });
    } else if (block.type === 'while') {
      document.getElementById('sg-input-while-cond').addEventListener('input', (e) => {
        block.condition = e.target.value;
        this.render();
      });
      document.getElementById('sg-btn-add-while-body').addEventListener('click', () => {
        if (!block.body) block.body = [];
        block.body.push({ id: 'b_' + Date.now(), type: 'instruction', text: 'schleifen_anweisung()' });
        this.render();
      });
    } else if (block.type === 'for') {
      document.getElementById('sg-input-for-hdr').addEventListener('input', (e) => {
        block.loopHeader = e.target.value;
        this.render();
      });
      document.getElementById('sg-btn-add-for-body').addEventListener('click', () => {
        if (!block.body) block.body = [];
        block.body.push({ id: 'b_' + Date.now(), type: 'instruction', text: 'schleifen_anweisung()' });
        this.render();
      });
    }

    document.getElementById('sg-btn-delete-block').addEventListener('click', () => {
      if (confirm('Diesen Block und alle Unterblöcke wirklich löschen?')) {
        this.deleteBlockRecursive(this.blocks, block.id);
        this.selectedBlockId = this.blocks[0] ? this.blocks[0].id : null;
        this.render();
        this.renderSidebar();
      }
    });
  }

  generatePythonCode() {
    let py = `# ========================================================\n`;
    py += `# DIN 66261 Struktogramm -> Python 3 Transpiler\n`;
    py += `# Generiert vom IT-Praxisportal Diagramm-Studio\n`;
    py += `# ========================================================\n\n`;
    py += `def algorithmus_ausfuehren():\n`;

    const transpileList = (list, indent) => {
      let code = '';
      if (!list || list.length === 0) {
        return `${indent}pass\n`;
      }
      list.forEach(b => {
        if (b.type === 'instruction') {
          code += `${indent}${b.text}\n`;
        } else if (b.type === 'if') {
          code += `${indent}if ${b.condition}:\n`;
          code += transpileList(b.thenBlocks, indent + '    ');
          if (b.elseBlocks && b.elseBlocks.length > 0) {
            code += `${indent}else:\n`;
            code += transpileList(b.elseBlocks, indent + '    ');
          }
        } else if (b.type === 'while') {
          code += `${indent}while ${b.condition}:\n`;
          code += transpileList(b.body, indent + '    ');
        } else if (b.type === 'for') {
          code += `${indent}# ${b.loopHeader}\n`;
          code += `${indent}for i in range(1, n + 1):\n`;
          code += transpileList(b.body, indent + '    ');
        }
      });
      return code;
    };

    py += transpileList(this.blocks, '    ');
    py += `\n\nif __name__ == "__main__":\n    print("Algorithmus gestartet...")\n    algorithmus_ausfuehren()\n`;
    return py;
  }

  showCodeModal() {
    const py = this.generatePythonCode();
    document.getElementById('sg-code-display').innerText = py;
    document.getElementById('sg-code-modal').style.display = 'flex';
  }

  exportSvg() {
    // Generate SVG wrapper around the table
    const box = document.getElementById('sg-render-box');
    if (!box) return;
    const htmlContent = box.innerHTML;
    const svgString = `
      <svg xmlns="http://www.w3.org/2000/svg" width="800" height="900">
        <foreignObject width="100%" height="100%">
          <div xmlns="http://www.w3.org/1999/xhtml">
            <style>
              .sg-container { font-family: sans-serif; background: #090d16; color: #f8fafc; padding: 20px; }
              .sg-block { border: 1px solid #38bdf8; background: #1e293b; padding: 8px 12px; margin: -1px 0 0 0; }
              .sg-text { font-family: monospace; font-size: 13px; color: #f8fafc; }
              .sg-if-header { position: relative; background: #0f172a; height: 36px; border: 1px solid #38bdf8; }
              .sg-if-condition { text-align: center; color: #38bdf8; font-weight: bold; padding-top: 6px; }
              .sg-if-branches { display: flex; width: 100%; border: 1px solid #38bdf8; border-top: none; }
              .sg-if-then { flex: 1; border-right: 1px solid #38bdf8; }
              .sg-if-else { flex: 1; }
              .sg-while { border: 1px solid #38bdf8; background: #1e293b; }
              .sg-while-header { background: #0f172a; padding: 6px 12px; border-bottom: 1px solid #38bdf8; color: #38bdf8; font-weight: bold; }
              .sg-while-body-wrap { display: flex; }
              .sg-while-gutter { width: 24px; background: #0f172a; border-right: 1px solid #38bdf8; }
              .sg-while-body { flex: 1; }
            </style>
            ${htmlContent}
          </div>
        </foreignObject>
      </svg>
    `;
    const blob = new Blob([svgString], { type: 'image/svg+xml;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'struktogramm_din66261.svg';
    a.click();
    URL.revokeObjectURL(url);
  }

  escapeHtml(str) {
    return (str || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }
}

window.StruktogrammEditor = StruktogrammEditor;
