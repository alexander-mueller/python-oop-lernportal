/**
 * 🔷 IT-PRAXISPORTAL – UML DIAGRAMM STUDIO (KLASSEN, SEQUENZ, USE CASE)
 * Standard für IHK FIAE & FISI:
 * - Klassendiagramme (Attribute +, -, #, Methoden, Vererbung, Assoziation, Komposition)
 * - Sequenzdiagramme (Lebenslinien, synchrone/asynchrone Aufrufe, Return)
 * - Use Case Diagramme (Akteure, Systemgrenze, <<include>>, <<extend>>)
 * Synchronisierte Mermaid-Live-Vorschau mit interaktiver Generierung!
 */

class UMLEditor {
  constructor(containerId, options = {}) {
    this.container = typeof containerId === 'string' ? document.getElementById(containerId) : containerId;
    this.options = options;
    this.diagramType = 'class'; // 'class' | 'sequence' | 'usecase'
    this.mermaidCode = '';
    this.init();
  }

  init() {
    if (!this.container) return;
    this.container.innerHTML = `
      <div class="ds-editor-card">
        <div class="ds-toolbar">
          <div class="ds-toolbar-left">
            <div class="ds-select-wrap">
              <label>Diagrammtyp:</label>
              <select id="uml-select-type" class="ds-select">
                <option value="class">UML 2.5 Klassendiagramm</option>
                <option value="sequence">UML 2.5 Sequenzdiagramm</option>
                <option value="usecase">UML 2.5 Anwendungsfalldiagramm (Use Case)</option>
              </select>
            </div>
            <div class="ds-select-wrap">
              <label>IHK-Vorlage:</label>
              <select id="uml-select-template" class="ds-select">
                <option value="">-- Vorlage laden --</option>
                <option value="class_ecommerce">IHK Klassendiagramm: E-Commerce & Zahlung</option>
                <option value="class_ticket">IHK Klassendiagramm: IT-Helpdesk & Rollen</option>
                <option value="seq_login">IHK Sequenz: 2FA Benutzer-Authentifizierung</option>
                <option value="seq_order">IHK Sequenz: Warenkorb-Bestellprozess</option>
                <option value="uc_hotel">IHK Use-Case: Hotel-Reservierungssystem</option>
              </select>
            </div>
          </div>
          <div class="ds-toolbar-right">
            <button type="button" class="ds-btn ds-btn-success" id="uml-btn-render">
              <span>▶</span> <span>Neu Rendern</span>
            </button>
            <button type="button" class="ds-btn ds-btn-secondary" id="uml-btn-export-svg">
              <span>🖼️</span> <span>SVG Export</span>
            </button>
            <button type="button" class="ds-btn ds-btn-danger" id="uml-btn-clear" title="Code leeren">
              <span>🗑️</span>
            </button>
          </div>
        </div>

        <div class="ds-workspace-grid">
          <div class="ds-canvas-wrap" style="display:flex; align-items:center; justify-content:center; overflow:auto; background:#090d16;" id="uml-canvas-container">
            <div id="uml-render-target" style="width:100%; min-height:100%; display:flex; align-items:center; justify-content:center; padding:24px;"></div>
          </div>
          <div class="ds-sidebar" style="width:340px;">
            <div class="ds-sidebar-header">
              <h4>UML Quellcode (Mermaid / PlantUML Standard)</h4>
            </div>
            <div class="ds-sidebar-body" style="padding:10px; display:flex; flex-direction:column; height:calc(100% - 46px);">
              <textarea id="uml-code-input" class="ds-textarea" style="flex:1; font-family:monospace; font-size:0.84rem; line-height:1.45; resize:none; background:#060911; color:#f8fafc; border:1px solid #334155; padding:12px; border-radius:6px;"></textarea>
              <div style="margin-top:10px; font-size:0.75rem; color:#94a3b8; line-height:1.4;">
                💡 Tipp: Bearbeite den Diagrammcode direkt links in der Textbox oder lade eine IHK-Vorlage. Klicke auf <strong>Neu Rendern</strong> zur Aktualisierung.
              </div>
            </div>
          </div>
        </div>
      </div>
    `;

    this.bindEvents();
    this.loadTemplate('class_ecommerce');
  }

  bindEvents() {
    document.getElementById('uml-select-type').addEventListener('change', (e) => {
      this.diagramType = e.target.value;
      if (this.diagramType === 'class') this.loadTemplate('class_ecommerce');
      else if (this.diagramType === 'sequence') this.loadTemplate('seq_login');
      else if (this.diagramType === 'usecase') this.loadTemplate('uc_hotel');
    });

    document.getElementById('uml-select-template').addEventListener('change', (e) => {
      if (e.target.value) this.loadTemplate(e.target.value);
    });

    document.getElementById('uml-btn-render').addEventListener('click', () => {
      this.mermaidCode = document.getElementById('uml-code-input').value;
      this.render();
    });

    document.getElementById('uml-btn-clear').addEventListener('click', () => {
      if (confirm('Möchtest du das aktuelle UML-Diagramm leeren?')) {
        document.getElementById('uml-code-input').value = 'classDiagram\n  class MeineKlasse {\n    +int id\n  }';
        this.mermaidCode = document.getElementById('uml-code-input').value;
        this.render();
      }
    });

    document.getElementById('uml-btn-export-svg').addEventListener('click', () => this.exportSvg());
  }

  loadTemplate(tpl) {
    let code = '';
    if (tpl === 'class_ecommerce') {
      this.diagramType = 'class';
      document.getElementById('uml-select-type').value = 'class';
      code = `classDiagram
    direction TB

    class Benutzer {
        <<abstract>>
        #int id
        #String email
        #String passwortHash
        +anmelden() boolean
        +abmelden() void
    }

    class Kunde {
        -String vorname
        -String nachname
        -String lieferadresse
        +bestellen(Warenkorb w) Bestellung
    }

    class Administrator {
        -int rechteStufe
        +artikelAnlegen(Artikel a) void
        +sperreBenutzer(int userId) void
    }

    class Bestellung {
        -int bestellId
        -Date datum
        -String status
        +berechneGesamtsumme() double
    }

    class Bestellposition {
        -int menge
        -double einzelpreis
    }

    class Artikel {
        -int artikelId
        -String bezeichnung
        -double preis
        -int bestand
    }

    class IPaymentMethod {
        <<interface>>
        +processPayment(double amount) boolean
    }

    Benutzer <|-- Kunde : Generalisierung
    Benutzer <|-- Administrator : Generalisierung
    Kunde "1" --> "*" Bestellung : gibt auf
    Bestellung "1" *-- "1..*" Bestellposition : Komposition
    Bestellposition "*" --> "1" Artikel : Assoziation
    Bestellung ..> IPaymentMethod : Realisierung`;
    } else if (tpl === 'class_ticket') {
      this.diagramType = 'class';
      document.getElementById('uml-select-type').value = 'class';
      code = `classDiagram
    class Ticket {
        -int ticketNummer
        -String titel
        -String prioritaet
        -Date erstelltAm
        +statusAendern(String status) void
        +zuweisen(Mitarbeiter m) void
    }

    class Mitarbeiter {
        -int mitarbeiterId
        -String name
        -String abteilung
    }

    class HardwareAsset {
        -String seriennummer
        -String hostname
        -String standort
    }

    Ticket "*" --> "1" Mitarbeiter : Melder
    Ticket "*" --> "0..1" Mitarbeiter : Bearbeiter
    Ticket "*" --> "1" HardwareAsset : Betrifft`;
    } else if (tpl === 'seq_login') {
      this.diagramType = 'sequence';
      document.getElementById('uml-select-type').value = 'sequence';
      code = `sequenceDiagram
    autonumber
    actor User as Benutzer
    participant Browser as Client / Browser
    participant AuthAPI as Auth-Service
    participant DB as Datenbank
    participant Mail as 2FA-Mail-Service

    User->>Browser: Login-Formular ausfüllen (Email, Passwort)
    Browser->>AuthAPI: POST /api/v1/auth/login
    activate AuthAPI
    AuthAPI->>DB: SELECT * FROM users WHERE email = ?
    activate DB
    DB-->>AuthAPI: User-Record mit Password-Hash
    deactivate DB
    AuthAPI->>AuthAPI: Passwort-Hash validieren (Argon2id)
    
    alt Passwort korrekt
        AuthAPI->>Mail: 2FA-Einmalcode senden (SMS/Email)
        AuthAPI-->>Browser: 200 OK (Requires 2FA)
        User->>Browser: 2FA-Code eingeben
        Browser->>AuthAPI: POST /api/v1/auth/verify-otp
        AuthAPI-->>Browser: 200 OK (JWT Access Token & Cookie)
    else Passwort falsch
        AuthAPI-->>Browser: 401 Unauthorized (Ungültige Anmeldedaten)
    end
    deactivate AuthAPI`;
    } else if (tpl === 'seq_order') {
      this.diagramType = 'sequence';
      document.getElementById('uml-select-type').value = 'sequence';
      code = `sequenceDiagram
    autonumber
    actor Kunde
    participant Webshop
    participant Lager as ERP / Lager
    participant Bank as Payment-Gateway

    Kunde->>Webshop: "Jetzt kaufen" klicken
    activate Webshop
    Webshop->>Lager: Bestand prüfen & reservieren
    activate Lager
    Lager-->>Webshop: Bestand bestätigt
    deactivate Lager
    Webshop->>Bank: Kreditkarte autorisieren (129.90 EUR)
    activate Bank
    Bank-->>Webshop: Zahlung genehmigt (Auth-Token)
    deactivate Bank
    Webshop->>Lager: Kommissionierauftrag erstellen
    Webshop-->>Kunde: Bestellbestätigung per E-Mail
    deactivate Webshop`;
    } else if (tpl === 'uc_hotel') {
      this.diagramType = 'usecase';
      document.getElementById('uml-select-type').value = 'usecase';
      code = `flowchart LR
    subgraph Hotelverwaltungssystem [Systemgrenze: Hotel-Reservierung]
        UC1((Zimmer suchen))
        UC2((Zimmer reservieren))
        UC3((Zahlung durchführen))
        UC4((Reservierung stornieren))
        UC5((Zimmerrechnung erstellen))
    end

    Gast[Gast / Kunde] --> UC1
    Gast --> UC2
    Gast --> UC4

    Rezeption[Rezeptionist] --> UC2
    Rezeption --> UC4
    Rezeption --> UC5

    UC2 -.->|<<include>>| UC3
    UC4 -.->|<<extend>>| UC5`;
    }

    document.getElementById('uml-code-input').value = code;
    this.mermaidCode = code;
    this.render();
  }

  async render() {
    const target = document.getElementById('uml-render-target');
    if (!target) return;

    // Load mermaid if not already on window
    if (!window.mermaid) {
      target.innerHTML = `<div style="color:#94a3b8; font-size:0.9rem;">Lade Diagramm-Renderer...</div>`;
      await this.loadMermaidScript();
    }

    try {
      window.mermaid.initialize({
        startOnLoad: false,
        theme: 'dark',
        themeVariables: {
          darkMode: true,
          background: '#090d16',
          primaryColor: '#1e293b',
          primaryTextColor: '#f8fafc',
          primaryBorderColor: '#38bdf8',
          lineColor: '#38bdf8',
          secondaryColor: '#0f172a',
          tertiaryColor: '#1e1b4b'
        }
      });

      const id = 'mermaid_svg_' + Date.now();
      const { svg } = await window.mermaid.render(id, this.mermaidCode);
      target.innerHTML = svg;
    } catch (err) {
      target.innerHTML = `
        <div style="background:rgba(239,68,68,0.1); border:1px solid #ef4444; color:#fca5a5; padding:14px; border-radius:8px; font-size:0.85rem; max-width:600px;">
          <strong>⚠️ Syntaxfehler im UML-Code:</strong>
          <pre style="margin-top:8px; font-family:monospace; font-size:0.8rem; white-space:pre-wrap;">${err.message || err}</pre>
        </div>
      `;
    }
  }

  loadMermaidScript() {
    return new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.src = 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js';
      script.onload = () => resolve();
      script.onerror = () => reject(new Error('Mermaid CDN konnte nicht geladen werden.'));
      document.head.appendChild(script);
    });
  }

  exportSvg() {
    const svgEl = document.querySelector('#uml-render-target svg');
    if (!svgEl) {
      alert('Kein gerendertes Diagramm zum Exportieren vorhanden.');
      return;
    }
    const serializer = new XMLSerializer();
    const source = serializer.serializeToString(svgEl);
    const blob = new Blob([source], { type: 'image/svg+xml;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `uml_${this.diagramType}_ihk.svg`;
    a.click();
    URL.revokeObjectURL(url);
  }
}

window.UMLEditor = UMLEditor;
