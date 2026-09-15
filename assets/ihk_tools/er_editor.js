/**
 * 🗄️ IT-PRAXISPORTAL – INTERAKTIVER ER-MODELL EDITOR (ENTITY RELATIONSHIP)
 * Unterstützt Entitäten, Attribute (PK, FK, NN, UQ), Relationen (1:1, 1:n, n:m),
 * Notationen (Krähenfuß, Chen, Min-Max), automatische SQL-DDL-Generierung und SVG-Export.
 */

class EREditor {
  constructor(containerId, options = {}) {
    this.container = typeof containerId === 'string' ? document.getElementById(containerId) : containerId;
    this.options = options;
    this.entities = [];
    this.relations = [];
    this.selectedEntityId = null;
    this.notation = 'crowsfoot'; // 'crowsfoot' | 'chen' | 'minmax'
    this.draggedEntity = null;
    this.dragOffset = { x: 0, y: 0 };
    this.init();
  }

  init() {
    if (!this.container) return;
    this.container.innerHTML = `
      <div class="ds-editor-card">
        <div class="ds-toolbar">
          <div class="ds-toolbar-left">
            <button type="button" class="ds-btn ds-btn-primary" id="er-btn-add-entity">
              <span>➕</span> <span>Entität hinzufügen</span>
            </button>
            <button type="button" class="ds-btn ds-btn-secondary" id="er-btn-add-relation">
              <span>🔗</span> <span>Beziehung anlegen</span>
            </button>
            <div class="ds-select-wrap">
              <label>Notation:</label>
              <select id="er-select-notation" class="ds-select">
                <option value="crowsfoot">Krähenfuß (Crow's Foot)</option>
                <option value="chen">Chen-Notation (1, c, m, mc)</option>
                <option value="minmax">Min-Max-Notation (0,1 / 1,n)</option>
              </select>
            </div>
            <div class="ds-select-wrap">
              <label>Vorlage:</label>
              <select id="er-select-template" class="ds-select">
                <option value="">-- IHK-Vorlage wählen --</option>
                <option value="onlineshop">IHK Online-Shop (Kunde, Bestellung, Artikel)</option>
                <option value="asset_mgmt">IT-Asset Management (Server, Standort, Ticket)</option>
                <option value="schulung">IHK Ausbildungsbetrieb (Azubi, Projekt, Ausbilder)</option>
              </select>
            </div>
          </div>
          <div class="ds-toolbar-right">
            <button type="button" class="ds-btn ds-btn-success" id="er-btn-generate-sql">
              <span>💾</span> <span>SQL DDL</span>
            </button>
            <button type="button" class="ds-btn ds-btn-secondary" id="er-btn-export-svg">
              <span>🖼️</span> <span>SVG Export</span>
            </button>
            <button type="button" class="ds-btn ds-btn-danger" id="er-btn-clear" title="Alles leeren">
              <span>🗑️</span>
            </button>
          </div>
        </div>

        <div class="ds-workspace-grid">
          <div class="ds-canvas-wrap" id="er-canvas-container">
            <svg id="er-svg-canvas" width="100%" height="100%"></svg>
          </div>
          <div class="ds-sidebar" id="er-sidebar">
            <div class="ds-sidebar-header">
              <h4 id="er-sidebar-title">Eigenschaften</h4>
            </div>
            <div class="ds-sidebar-body" id="er-sidebar-content">
              <p class="ds-hint">Wähle eine Entität oder Beziehung im Diagramm aus, um Eigenschaften und Attribute zu bearbeiten.</p>
            </div>
          </div>
        </div>

        <!-- SQL DDL Modal -->
        <div id="er-sql-modal" class="ds-modal" style="display:none;">
          <div class="ds-modal-content">
            <div class="ds-modal-header">
              <h3>Generiertes SQL DDL Skript (ANSI SQL:2016)</h3>
              <button type="button" class="ds-modal-close" id="er-sql-modal-close">&times;</button>
            </div>
            <pre id="er-sql-code-display" class="ds-code-block"></pre>
            <div class="ds-modal-footer">
              <button type="button" class="ds-btn ds-btn-primary" id="er-sql-copy-btn">In Zwischenablage kopieren</button>
            </div>
          </div>
        </div>
      </div>
    `;

    this.bindEvents();
    this.loadTemplate('onlineshop');
  }

  bindEvents() {
    document.getElementById('er-btn-add-entity').addEventListener('click', () => this.addEntity());
    document.getElementById('er-btn-add-relation').addEventListener('click', () => this.promptAddRelation());
    document.getElementById('er-select-notation').addEventListener('change', (e) => {
      this.notation = e.target.value;
      this.render();
    });
    document.getElementById('er-select-template').addEventListener('change', (e) => {
      if (e.target.value) this.loadTemplate(e.target.value);
    });
    document.getElementById('er-btn-generate-sql').addEventListener('click', () => this.showSqlModal());
    document.getElementById('er-sql-modal-close').addEventListener('click', () => {
      document.getElementById('er-sql-modal').style.display = 'none';
    });
    document.getElementById('er-sql-copy-btn').addEventListener('click', () => {
      const code = document.getElementById('er-sql-code-display').innerText;
      navigator.clipboard.writeText(code).then(() => {
        alert('SQL-Skript erfolgreich kopiert!');
      });
    });
    document.getElementById('er-btn-export-svg').addEventListener('click', () => this.exportSvg());
    document.getElementById('er-btn-clear').addEventListener('click', () => {
      if (confirm('Möchtest du das aktuelle ER-Modell wirklich leeren?')) {
        this.entities = [];
        this.relations = [];
        this.selectedEntityId = null;
        this.render();
        this.renderSidebar();
      }
    });

    const canvas = document.getElementById('er-canvas-container');
    canvas.addEventListener('mousedown', (e) => this.onMouseDown(e));
    window.addEventListener('mousemove', (e) => this.onMouseMove(e));
    window.addEventListener('mouseup', () => this.onMouseUp());
  }

  addEntity(name = 'tbl_neue_tabelle', x = 60, y = 60) {
    const id = 'ent_' + Date.now() + '_' + Math.floor(Math.random() * 1000);
    const entity = {
      id: id,
      name: name,
      x: x,
      y: y,
      width: 230,
      attributes: [
        { name: 'id', type: 'INT', pk: true, fk: false, nn: true, uq: true },
        { name: 'bezeichnung', type: 'VARCHAR(100)', pk: false, fk: false, nn: true, uq: false }
      ]
    };
    this.entities.push(entity);
    this.selectEntity(id);
    this.render();
  }

  selectEntity(id) {
    this.selectedEntityId = id;
    this.render();
    this.renderSidebar();
  }

  promptAddRelation() {
    if (this.entities.length < 2) {
      alert('Du benötigst mindestens 2 Entitäten, um eine Beziehung herzustellen.');
      return;
    }
    const fromId = this.selectedEntityId || this.entities[0].id;
    const otherEntities = this.entities.filter(e => e.id !== fromId);
    const toId = otherEntities[0].id;

    const relId = 'rel_' + Date.now();
    this.relations.push({
      id: relId,
      name: 'hat',
      sourceEntityId: fromId,
      targetEntityId: toId,
      cardinalitySource: '1',
      cardinalityTarget: 'n'
    });
    this.render();
    this.renderSidebar();
  }

  loadTemplate(tplName) {
    this.entities = [];
    this.relations = [];

    if (tplName === 'onlineshop') {
      this.entities = [
        {
          id: 'ent_kunde',
          name: 'tbl_kunde',
          x: 50,
          y: 60,
          width: 230,
          attributes: [
            { name: 'kunde_id', type: 'INT', pk: true, fk: false, nn: true, uq: true },
            { name: 'nachname', type: 'VARCHAR(50)', pk: false, fk: false, nn: true, uq: false },
            { name: 'vorname', type: 'VARCHAR(50)', pk: false, fk: false, nn: false, uq: false },
            { name: 'email', type: 'VARCHAR(120)', pk: false, fk: false, nn: true, uq: true },
            { name: 'registriert_am', type: 'DATE', pk: false, fk: false, nn: true, uq: false }
          ]
        },
        {
          id: 'ent_bestellung',
          name: 'tbl_bestellung',
          x: 370,
          y: 60,
          width: 230,
          attributes: [
            { name: 'bestell_id', type: 'INT', pk: true, fk: false, nn: true, uq: true },
            { name: 'kunde_id', type: 'INT', pk: false, fk: true, nn: true, uq: false },
            { name: 'bestelldatum', type: 'DATETIME', pk: false, fk: false, nn: true, uq: false },
            { name: 'status', type: 'VARCHAR(20)', pk: false, fk: false, nn: true, uq: false }
          ]
        },
        {
          id: 'ent_position',
          name: 'tbl_bestellposition',
          x: 370,
          y: 280,
          width: 230,
          attributes: [
            { name: 'bestell_id', type: 'INT', pk: true, fk: true, nn: true, uq: false },
            { name: 'artikel_id', type: 'INT', pk: true, fk: true, nn: true, uq: false },
            { name: 'menge', type: 'INT', pk: false, fk: false, nn: true, uq: false },
            { name: 'einzelpreis', type: 'DECIMAL(10,2)', pk: false, fk: false, nn: true, uq: false }
          ]
        },
        {
          id: 'ent_artikel',
          name: 'tbl_artikel',
          x: 50,
          y: 280,
          width: 230,
          attributes: [
            { name: 'artikel_id', type: 'INT', pk: true, fk: false, nn: true, uq: true },
            { name: 'artikelname', type: 'VARCHAR(100)', pk: false, fk: false, nn: true, uq: false },
            { name: 'preis', type: 'DECIMAL(10,2)', pk: false, fk: false, nn: true, uq: false },
            { name: 'lagerbestand', type: 'INT', pk: false, fk: false, nn: true, uq: false }
          ]
        }
      ];

      this.relations = [
        {
          id: 'rel_kunde_bestellung',
          name: 'gibt_auf',
          sourceEntityId: 'ent_kunde',
          targetEntityId: 'ent_bestellung',
          cardinalitySource: '1',
          cardinalityTarget: 'n'
        },
        {
          id: 'rel_bestellung_pos',
          name: 'besteht_aus',
          sourceEntityId: 'ent_bestellung',
          targetEntityId: 'ent_position',
          cardinalitySource: '1',
          cardinalityTarget: 'n'
        },
        {
          id: 'rel_artikel_pos',
          name: 'enthaelt',
          sourceEntityId: 'ent_artikel',
          targetEntityId: 'ent_position',
          cardinalitySource: '1',
          cardinalityTarget: 'n'
        }
      ];
    } else if (tplName === 'asset_mgmt') {
      this.entities = [
        {
          id: 'ent_server',
          name: 'tbl_server',
          x: 60,
          y: 70,
          width: 230,
          attributes: [
            { name: 'server_id', type: 'INT', pk: true, fk: false, nn: true, uq: true },
            { name: 'hostname', type: 'VARCHAR(60)', pk: false, fk: false, nn: true, uq: true },
            { name: 'ip_adresse', type: 'VARCHAR(45)', pk: false, fk: false, nn: true, uq: true },
            { name: 'standort_id', type: 'INT', pk: false, fk: true, nn: true, uq: false }
          ]
        },
        {
          id: 'ent_standort',
          name: 'tbl_standort',
          x: 380,
          y: 70,
          width: 220,
          attributes: [
            { name: 'standort_id', type: 'INT', pk: true, fk: false, nn: true, uq: true },
            { name: 'bezeichnung', type: 'VARCHAR(50)', pk: false, fk: false, nn: true, uq: false },
            { name: 'netzwerk_cidr', type: 'VARCHAR(20)', pk: false, fk: false, nn: true, uq: false }
          ]
        }
      ];
      this.relations = [
        {
          id: 'rel_server_standort',
          name: 'steht_in',
          sourceEntityId: 'ent_standort',
          targetEntityId: 'ent_server',
          cardinalitySource: '1',
          cardinalityTarget: 'n'
        }
      ];
    } else if (tplName === 'schulung') {
      this.entities = [
        {
          id: 'ent_azubi',
          name: 'tbl_azubi',
          x: 60,
          y: 70,
          width: 230,
          attributes: [
            { name: 'azubi_id', type: 'INT', pk: true, fk: false, nn: true, uq: true },
            { name: 'name', type: 'VARCHAR(60)', pk: false, fk: false, nn: true, uq: false },
            { name: 'ausbildungsberuf', type: 'VARCHAR(40)', pk: false, fk: false, nn: true, uq: false },
            { name: 'ausbildungsjahr', type: 'INT', pk: false, fk: false, nn: true, uq: false }
          ]
        },
        {
          id: 'ent_projekt',
          name: 'tbl_projektarbeit',
          x: 390,
          y: 70,
          width: 230,
          attributes: [
            { name: 'projekt_id', type: 'INT', pk: true, fk: false, nn: true, uq: true },
            { name: 'titel', type: 'VARCHAR(150)', pk: false, fk: false, nn: true, uq: false },
            { name: 'stundenumfang', type: 'INT', pk: false, fk: false, nn: true, uq: false },
            { name: 'azubi_id', type: 'INT', pk: false, fk: true, nn: true, uq: true }
          ]
        }
      ];
      this.relations = [
        {
          id: 'rel_azubi_projekt',
          name: 'fuehrt_durch',
          sourceEntityId: 'ent_azubi',
          targetEntityId: 'ent_projekt',
          cardinalitySource: '1',
          cardinalityTarget: '1'
        }
      ];
    }

    this.selectedEntityId = this.entities[0] ? this.entities[0].id : null;
    this.render();
    this.renderSidebar();
  }

  onMouseDown(e) {
    const rect = document.getElementById('er-svg-canvas').getBoundingClientRect();
    const mouseX = e.clientX - rect.left;
    const mouseY = e.clientY - rect.top;

    for (let i = this.entities.length - 1; i >= 0; i--) {
      const ent = this.entities[i];
      const headerHeight = 32;
      const height = headerHeight + ent.attributes.length * 24 + 10;
      if (mouseX >= ent.x && mouseX <= ent.x + ent.width && mouseY >= ent.y && mouseY <= ent.y + height) {
        this.draggedEntity = ent;
        this.dragOffset = { x: mouseX - ent.x, y: mouseY - ent.y };
        this.selectEntity(ent.id);
        return;
      }
    }
  }

  onMouseMove(e) {
    if (!this.draggedEntity) return;
    const rect = document.getElementById('er-svg-canvas').getBoundingClientRect();
    const mouseX = e.clientX - rect.left;
    const mouseY = e.clientY - rect.top;

    this.draggedEntity.x = Math.max(10, Math.min(1200, mouseX - this.dragOffset.x));
    this.draggedEntity.y = Math.max(10, Math.min(800, mouseY - this.dragOffset.y));
    this.render();
  }

  onMouseUp() {
    this.draggedEntity = null;
  }

  render() {
    const svg = document.getElementById('er-svg-canvas');
    if (!svg) return;

    let html = `
      <defs>
        <pattern id="er-grid" width="20" height="20" patternUnits="userSpaceOnUse">
          <path d="M 20 0 L 0 0 0 20" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>
        </pattern>
      </defs>
      <rect width="100%" height="100%" fill="#090d16"/>
      <rect width="100%" height="100%" fill="url(#er-grid)"/>
    `;

    // 1. Relations
    this.relations.forEach(rel => {
      const src = this.entities.find(e => e.id === rel.sourceEntityId);
      const tgt = this.entities.find(e => e.id === rel.targetEntityId);
      if (!src || !tgt) return;

      const srcCenter = { x: src.x + src.width / 2, y: src.y + 45 };
      const tgtCenter = { x: tgt.x + tgt.width / 2, y: tgt.y + 45 };

      html += `<line x1="${srcCenter.x}" y1="${srcCenter.y}" x2="${tgtCenter.x}" y2="${tgtCenter.y}" stroke="#38bdf8" stroke-width="2"/>`;

      const midX = (srcCenter.x + tgtCenter.x) / 2;
      const midY = (srcCenter.y + tgtCenter.y) / 2;

      const srcOffX = srcCenter.x + (tgtCenter.x - srcCenter.x) * 0.25;
      const srcOffY = srcCenter.y + (tgtCenter.y - srcCenter.y) * 0.25 - 10;
      const tgtOffX = tgtCenter.x - (tgtCenter.x - srcCenter.x) * 0.25;
      const tgtOffY = tgtCenter.y - (tgtCenter.y - srcCenter.y) * 0.25 - 10;

      let cardSrcText = rel.cardinalitySource;
      let cardTgtText = rel.cardinalityTarget;

      if (this.notation === 'chen') {
        cardSrcText = rel.cardinalitySource === '1' ? '1' : 'n';
        cardTgtText = rel.cardinalityTarget === '1' ? '1' : 'm';
      } else if (this.notation === 'minmax') {
        cardSrcText = rel.cardinalitySource === '1' ? '(0,1)' : '(1,n)';
        cardTgtText = rel.cardinalityTarget === '1' ? '(1,1)' : '(0,n)';
      }

      html += `
        <g transform="translate(${midX}, ${midY})">
          <rect x="-36" y="-12" width="72" height="24" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
          <text x="0" y="4" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle" font-family="sans-serif">${rel.name}</text>
        </g>
        <rect x="${srcOffX - 14}" y="${srcOffY - 10}" width="28" height="20" rx="4" fill="#0f172a" stroke="#475569" stroke-width="1"/>
        <text x="${srcOffX}" y="${srcOffY + 4}" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="monospace">${cardSrcText}</text>
        
        <rect x="${tgtOffX - 14}" y="${tgtOffY - 10}" width="28" height="20" rx="4" fill="#0f172a" stroke="#475569" stroke-width="1"/>
        <text x="${tgtOffX}" y="${tgtOffY + 4}" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="monospace">${cardTgtText}</text>
      `;
    });

    // 2. Entities
    this.entities.forEach(ent => {
      const isSelected = ent.id === this.selectedEntityId;
      const headerHeight = 34;
      const attrHeight = 24;
      const totalHeight = headerHeight + ent.attributes.length * attrHeight + 8;

      html += `
        <g class="er-entity-node" transform="translate(${ent.x}, ${ent.y})" style="cursor:move;">
          <rect x="0" y="0" width="${ent.width}" height="${totalHeight}" rx="8" fill="#1e293b" stroke="${isSelected ? '#38bdf8' : '#334155'}" stroke-width="${isSelected ? 2.5 : 1.5}" filter="drop-shadow(0 4px 10px rgba(0,0,0,0.35))"/>
          <rect x="0" y="0" width="${ent.width}" height="${headerHeight}" rx="8" fill="${isSelected ? '#1d4ed8' : '#0f172a'}"/>
          <rect x="0" y="${headerHeight - 2}" width="${ent.width}" height="2" fill="${isSelected ? '#38bdf8' : '#334155'}"/>
          <text x="12" y="22" fill="#ffffff" font-size="13" font-weight="bold" font-family="sans-serif">🗄️ ${ent.name}</text>
      `;

      ent.attributes.forEach((attr, idx) => {
        const rowY = headerHeight + idx * attrHeight + 16;
        let keyBadge = '';
        let badgeColor = '#94a3b8';
        if (attr.pk) {
          keyBadge = 'PK';
          badgeColor = '#fbbf24';
        } else if (attr.fk) {
          keyBadge = 'FK';
          badgeColor = '#38bdf8';
        }

        html += `
          <g transform="translate(10, ${rowY - 12})">
            ${keyBadge ? `<rect x="0" y="0" width="22" height="15" rx="3" fill="rgba(255,255,255,0.08)" stroke="${badgeColor}" stroke-width="1"/><text x="11" y="11" fill="${badgeColor}" font-size="9" font-weight="bold" text-anchor="middle" font-family="monospace">${keyBadge}</text>` : ''}
            <text x="${keyBadge ? 28 : 6}" y="11" fill="#f8fafc" font-size="11" font-weight="${attr.pk ? 'bold' : 'normal'}" font-family="monospace">${attr.name}</text>
            <text x="${ent.width - 24}" y="11" fill="#94a3b8" font-size="10" text-anchor="end" font-family="monospace">${attr.type}</text>
          </g>
        `;
      });

      html += `</g>`;
    });

    svg.innerHTML = html;
  }

  renderSidebar() {
    const sidebarTitle = document.getElementById('er-sidebar-title');
    const content = document.getElementById('er-sidebar-content');
    if (!content) return;

    const ent = this.entities.find(e => e.id === this.selectedEntityId);
    if (!ent) {
      sidebarTitle.innerText = 'Eigenschaften';
      content.innerHTML = `<p class="ds-hint">Klicke auf eine Entität im Diagramm, um Eigenschaften und Attribute zu bearbeiten.</p>`;
      return;
    }

    sidebarTitle.innerText = `Entität: ${ent.name}`;

    let html = `
      <div class="ds-field-group">
        <label>Tabellenname:</label>
        <input type="text" id="er-edit-ent-name" class="ds-input" value="${ent.name}">
      </div>

      <div style="display:flex; justify-content:space-between; align-items:center; margin:12px 0 8px 0;">
        <span style="font-size:0.8rem; font-weight:700; color:#38bdf8; text-transform:uppercase;">Attribute / Spalten:</span>
        <button type="button" class="ds-btn ds-btn-primary" id="er-btn-add-attr" style="padding:4px 8px; font-size:0.75rem;">+ Spalte</button>
      </div>

      <div style="display:flex; flex-direction:column; gap:8px; max-height:280px; overflow-y:auto; padding-right:4px;">
    `;

    ent.attributes.forEach((attr, idx) => {
      html += `
        <div class="ds-attr-card">
          <div style="display:flex; gap:6px; margin-bottom:6px;">
            <input type="text" data-idx="${idx}" class="ds-input er-attr-name" value="${attr.name}" style="padding:4px 6px; font-size:0.8rem; flex:1;" placeholder="Spaltenname">
            <select data-idx="${idx}" class="ds-select er-attr-type" style="padding:4px 6px; font-size:0.8rem; width:100px;">
              <option value="INT" ${attr.type === 'INT' ? 'selected' : ''}>INT</option>
              <option value="VARCHAR(50)" ${attr.type === 'VARCHAR(50)' ? 'selected' : ''}>VARCHAR(50)</option>
              <option value="VARCHAR(100)" ${attr.type === 'VARCHAR(100)' ? 'selected' : ''}>VARCHAR(100)</option>
              <option value="DATE" ${attr.type === 'DATE' ? 'selected' : ''}>DATE</option>
              <option value="DATETIME" ${attr.type === 'DATETIME' ? 'selected' : ''}>DATETIME</option>
              <option value="DECIMAL(10,2)" ${attr.type === 'DECIMAL(10,2)' ? 'selected' : ''}>DECIMAL</option>
              <option value="BOOLEAN" ${attr.type === 'BOOLEAN' ? 'selected' : ''}>BOOLEAN</option>
            </select>
            <button type="button" data-idx="${idx}" class="er-attr-del-btn ds-icon-btn" title="Löschen">&times;</button>
          </div>
          <div style="display:flex; gap:10px; font-size:0.75rem; color:#cbd5e1;">
            <label><input type="checkbox" data-idx="${idx}" class="er-attr-pk" ${attr.pk ? 'checked' : ''}> PK</label>
            <label><input type="checkbox" data-idx="${idx}" class="er-attr-fk" ${attr.fk ? 'checked' : ''}> FK</label>
            <label><input type="checkbox" data-idx="${idx}" class="er-attr-nn" ${attr.nn ? 'checked' : ''}> Not Null</label>
          </div>
        </div>
      `;
    });

    html += `
      </div>
      <div style="margin-top:16px; border-top:1px solid #334155; padding-top:12px;">
        <button type="button" id="er-btn-delete-entity" class="ds-btn ds-btn-danger" style="width:100%; font-size:0.82rem;">
          🗑️ Diese Entität löschen
        </button>
      </div>
    `;

    content.innerHTML = html;

    document.getElementById('er-edit-ent-name').addEventListener('input', (e) => {
      ent.name = e.target.value;
      this.render();
    });

    document.getElementById('er-btn-add-attr').addEventListener('click', () => {
      ent.attributes.push({ name: 'neues_feld', type: 'VARCHAR(50)', pk: false, fk: false, nn: false, uq: false });
      this.render();
      this.renderSidebar();
    });

    content.querySelectorAll('.er-attr-name').forEach(inp => {
      inp.addEventListener('input', (e) => {
        const idx = parseInt(e.target.dataset.idx, 10);
        ent.attributes[idx].name = e.target.value;
        this.render();
      });
    });

    content.querySelectorAll('.er-attr-type').forEach(sel => {
      sel.addEventListener('change', (e) => {
        const idx = parseInt(e.target.dataset.idx, 10);
        ent.attributes[idx].type = e.target.value;
        this.render();
      });
    });

    content.querySelectorAll('.er-attr-pk').forEach(chk => {
      chk.addEventListener('change', (e) => {
        const idx = parseInt(e.target.dataset.idx, 10);
        ent.attributes[idx].pk = e.target.checked;
        this.render();
      });
    });

    content.querySelectorAll('.er-attr-fk').forEach(chk => {
      chk.addEventListener('change', (e) => {
        const idx = parseInt(e.target.dataset.idx, 10);
        ent.attributes[idx].fk = e.target.checked;
        this.render();
      });
    });

    content.querySelectorAll('.er-attr-nn').forEach(chk => {
      chk.addEventListener('change', (e) => {
        const idx = parseInt(e.target.dataset.idx, 10);
        ent.attributes[idx].nn = e.target.checked;
        this.render();
      });
    });

    content.querySelectorAll('.er-attr-del-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const idx = parseInt(e.target.dataset.idx, 10);
        ent.attributes.splice(idx, 1);
        this.render();
        this.renderSidebar();
      });
    });

    document.getElementById('er-btn-delete-entity').addEventListener('click', () => {
      if (confirm(`Entität "${ent.name}" wirklich löschen?`)) {
        this.entities = this.entities.filter(e => e.id !== ent.id);
        this.relations = this.relations.filter(r => r.sourceEntityId !== ent.id && r.targetEntityId !== ent.id);
        this.selectedEntityId = this.entities[0] ? this.entities[0].id : null;
        this.render();
        this.renderSidebar();
      }
    });
  }

  generateSqlDDL() {
    let sql = `-- ========================================================\n`;
    sql += `-- IHK Prüfungsvorbereitung: Relationales Datenbankschema\n`;
    sql += `-- Generiert vom IT-Praxisportal ER-Modell Studio\n`;
    sql += `-- Standard: ANSI SQL:2016\n`;
    sql += `-- ========================================================\n\n`;

    this.entities.forEach(ent => {
      sql += `CREATE TABLE ${ent.name} (\n`;
      const pks = ent.attributes.filter(a => a.pk).map(a => a.name);
      const lines = [];

      ent.attributes.forEach(attr => {
        let line = `  ${attr.name} ${attr.type}`;
        if (attr.nn) line += ` NOT NULL`;
        if (attr.uq && !attr.pk) line += ` UNIQUE`;
        lines.push(line);
      });

      if (pks.length > 0) {
        lines.push(`  PRIMARY KEY (${pks.join(', ')})`);
      }

      sql += lines.join(',\n');
      sql += `\n);\n\n`;
    });

    if (this.relations.length > 0) {
      sql += `-- Fremdschlüssel-Beziehungen (Referentielle Integrität)\n`;
      this.relations.forEach(rel => {
        const src = this.entities.find(e => e.id === rel.sourceEntityId);
        const tgt = this.entities.find(e => e.id === rel.targetEntityId);
        if (src && tgt) {
          const srcPk = src.attributes.find(a => a.pk) || { name: 'id' };
          sql += `ALTER TABLE ${tgt.name} ADD CONSTRAINT fk_${tgt.name}_${src.name}\n`;
          sql += `  FOREIGN KEY (${src.name}_id) REFERENCES ${src.name}(${srcPk.name})\n`;
          sql += `  ON DELETE RESTRICT ON UPDATE CASCADE;\n\n`;
        }
      });
    }

    return sql;
  }

  showSqlModal() {
    const ddl = this.generateSqlDDL();
    document.getElementById('er-sql-code-display').innerText = ddl;
    document.getElementById('er-sql-modal').style.display = 'flex';
  }

  exportSvg() {
    const svgEl = document.getElementById('er-svg-canvas');
    if (!svgEl) return;
    const serializer = new XMLSerializer();
    const source = serializer.serializeToString(svgEl);
    const blob = new Blob([source], { type: 'image/svg+xml;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'er_modell_ihk.svg';
    a.click();
    URL.revokeObjectURL(url);
  }
}

window.EREditor = EREditor;
