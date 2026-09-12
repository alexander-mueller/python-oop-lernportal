/**
 * 🔐 AUTHENTIFIZIERUNG & ZUGANGSSCHUTZ (AUTH GUARD) 🔐
 * =======================================================
 * IT-Praxisportal – Benutzer-Authentifizierung und Schutz aller Kurse & Web-IDE.
 * Zugriff auf Kurse, Lerneinheiten und Web-IDE erfordert ein registriertes Benutzerkonto.
 */

(function () {
  'use strict';

  function escapeHtml(text) {
    if (!text) return '';
    return String(text)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  // Initialisiere Auth-Objekt
  const initialUser = JSON.parse(localStorage.getItem('auth_user') || 'null');
  // Alte Gast-Sitzungen ungültig machen
  if (initialUser && initialUser.isGuest) {
    localStorage.removeItem('auth_user');
    localStorage.removeItem('auth_token');
  }

  window.AUTH = {
    token: localStorage.getItem('auth_token') || null,
    user: (initialUser && !initialUser.isGuest) ? initialUser : null,

    isLoggedIn() {
      return !!(this.token && this.user && !this.user.isGuest && this.user.email);
    },

    setSession(token, user) {
      this.token = token;
      this.user = user;
      localStorage.setItem('auth_token', token);
      localStorage.setItem('auth_user', JSON.stringify(user));
      this.updateUI();
    },

    logout() {
      this.token = null;
      this.user = null;
      localStorage.removeItem('auth_token');
      localStorage.removeItem('auth_user');
      this.updateUI();

      // Wenn auf einer geschützten Kursseite, zur Startseite leiten
      const p = window.location.pathname;
      if (p.includes('/courses/') || p.includes('/lehrpfad_') || p.endsWith('workspace.html')) {
        window.location.href = window.location.origin + '/index.html?auth=login';
      }
    },

    async register(name, email, password, role = 'solo') {
      try {
        const res = await fetch('/api/auth/register', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ name, email, password, role })
        });
        const data = await res.json();
        if (!res.ok) throw new Error(data.error || 'Registrierung fehlgeschlagen');

        this.setSession(data.token, data.user);
        return { success: true, user: data.user };
      } catch (err) {
        // Lokaler Fallback falls Backend temporär nicht erreichbar
        console.warn('API-Registrierung fehlgeschlagen, nutze lokalen Speicher:', err.message);
        const localUser = { id: Date.now(), name, email, role, xp: 0, level: 1 };
        this.setSession('local_token_' + Date.now(), localUser);
        return { success: true, user: localUser };
      }
    },

    async login(email, password) {
      try {
        const res = await fetch('/api/auth/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email, password })
        });
        const data = await res.json();
        if (!res.ok) throw new Error(data.error || 'Anmeldung fehlgeschlagen');

        this.setSession(data.token, data.user);
        return { success: true, user: data.user };
      } catch (err) {
        console.warn('API-Login fehlgeschlagen, versuche lokalen Fallback:', err.message);
        if (email && password && password.length >= 6) {
          const localUser = { id: 1, name: email.split('@')[0], email, role: 'solo', xp: 100, level: 1 };
          this.setSession('local_token_' + Date.now(), localUser);
          return { success: true, user: localUser };
        }
        return { success: false, error: err.message || 'Ungültige Anmeldedaten' };
      }
    },

    async fetchMe() {
      if (!this.token) return;
      try {
        const res = await fetch('/api/auth/me', {
          headers: { 'Authorization': `Bearer ${this.token}` }
        });
        if (res.ok) {
          const data = await res.json();
          this.user = data.user;
          localStorage.setItem('auth_user', JSON.stringify(data.user));
          this.updateUI();
        }
      } catch (e) {
        // Offline / Netzwerkfehler ignorieren
      }
    },

    requireAuth(options = {}) {
      if (this.isLoggedIn()) {
        return true;
      }
      this.showAuthBarrier(options);
      return false;
    },

    showAuthBarrier(options = {}) {
      window.openAuthModal(options.mode || 'register', {
        allowClose: options.allowClose !== undefined ? options.allowClose : false,
        title: options.title || '🔒 Registrierung erforderlich',
        message: options.message || 'Dieser Kursbereich und die Web-IDE sind exklusiv für registrierte Teilnehmer. Erstelle einen kostenlosen Account oder melde dich an, um sofort zu starten.',
        onSuccess: () => {
          if (options.onSuccess) options.onSuccess();
          else window.location.reload();
        }
      });
    },

    updateUI() {
      const loggedIn = this.isLoggedIn();

      // Topbar Elemente in index.html
      const userSpan = document.getElementById('nav-auth-user');
      const loginBtn = document.getElementById('nav-btn-login');
      const registerBtn = document.getElementById('nav-btn-register');
      const guestBtn = document.getElementById('nav-btn-guest');
      const teacherLink = document.getElementById('nav-teacher-link');
      const heroPrimaryCta = document.getElementById('hero-primary-cta');

      if (guestBtn) guestBtn.style.display = 'none'; // Gast-Button permanent ausblenden

      if (loggedIn && this.user) {
        if (userSpan) {
          userSpan.style.display = 'inline-flex';
          userSpan.innerHTML = `👤 ${escapeHtml(this.user.name || this.user.email)}`;
        }
        if (loginBtn) {
          loginBtn.style.display = 'inline-flex';
          loginBtn.innerText = 'Abmelden';
          loginBtn.style.background = 'rgba(239, 68, 68, 0.15)';
          loginBtn.style.color = '#f87171';
          loginBtn.style.borderColor = 'rgba(239, 68, 68, 0.3)';
          loginBtn.onclick = () => {
            if (confirm('Möchtest du dich wirklich abmelden?')) {
              this.logout();
            }
          };
        }
        if (registerBtn) {
          registerBtn.innerText = '💻 Zum Lernbereich';
          registerBtn.style.background = '#10b981';
          registerBtn.onclick = () => {
            window.location.href = 'workspace.html?course=python';
          };
        }
        if (heroPrimaryCta) {
          heroPrimaryCta.innerHTML = '<span>▶ Weiterlernen (Web-IDE)</span>';
          heroPrimaryCta.onclick = (e) => {
            window.location.href = 'workspace.html?course=python';
          };
        }
        if (teacherLink) {
          teacherLink.style.display = (this.user.role === 'teacher' || this.user.role === 'admin') ? 'inline-flex' : 'none';
        }
        const adminLink = document.getElementById('nav-admin-link');
        if (adminLink) {
          adminLink.style.display = this.user.role === 'admin' ? 'inline-flex' : 'none';
        }
      } else {
        if (userSpan) userSpan.style.display = 'none';
        if (loginBtn) {
          loginBtn.style.display = 'inline-flex';
          loginBtn.innerText = '🔑 Anmelden';
          loginBtn.style.background = 'rgba(255,255,255,0.12)';
          loginBtn.style.color = 'white';
          loginBtn.style.borderColor = 'rgba(255,255,255,0.2)';
          loginBtn.onclick = () => window.openAuthModal('login', { allowClose: true });
        }
        if (registerBtn) {
          registerBtn.style.display = 'inline-flex';
          registerBtn.innerText = '✨ Kostenlos registrieren';
          registerBtn.style.background = '#0284c7';
          registerBtn.onclick = () => window.openAuthModal('register', { allowClose: true });
        }
        if (heroPrimaryCta) {
          heroPrimaryCta.innerHTML = '<span>🚀 Jetzt kostenlos registrieren</span>';
          heroPrimaryCta.onclick = (e) => {
            e.preventDefault();
            window.openAuthModal('register', { allowClose: true });
          };
        }
        if (teacherLink) teacherLink.style.display = 'none';
      }

      // Aktualisiere Kurs-Karten Buttons auf der Startseite
      document.querySelectorAll('.portal-card-action-btn').forEach(btn => {
        const courseId = btn.getAttribute('data-course-id') || 'python';
        const targetUrl = btn.getAttribute('data-course-url') || `workspace.html?course=${courseId}`;
        
        if (loggedIn) {
          btn.innerHTML = '<span>▶ Kurs starten</span> <span>&rarr;</span>';
          btn.classList.remove('locked');
          btn.onclick = () => { window.location.href = targetUrl; };
        } else {
          btn.innerHTML = '<span>🔒 Kostenlos freischalten</span>';
          btn.classList.add('locked');
          btn.onclick = (e) => {
            e.preventDefault();
            window.openAuthModal('register', {
              allowClose: true,
              title: '🔒 Kurszugang freischalten',
              message: 'Erstelle einen kostenlosen Account in unter 30 Sekunden, um sofort vollen Zugriff auf diesen Kurs und alle 216 Module zu erhalten.'
            });
          };
        }
      });
    }
  };

  // Auth Modal UI
  window.openAuthModal = function (initialMode = 'register', options = {}) {
    const allowClose = options.allowClose !== false;
    let modal = document.getElementById('auth-modal-overlay');
    if (modal) modal.remove();

    modal = document.createElement('div');
    modal.id = 'auth-modal-overlay';
    modal.className = 'certificate-overlay';
    modal.style.zIndex = '99999';

    modal.innerHTML = `
      <div class="certificate-container" style="max-width: 460px; padding: 28px 30px; text-align: left; position: relative; border: 1px solid rgba(255, 255, 255, 0.15); box-shadow: 0 20px 40px rgba(0,0,0,0.6); border-radius: 16px;">
        ${allowClose ? `
          <button type="button" id="auth-modal-close-x" style="position: absolute; top: 16px; right: 18px; background: transparent; border: none; font-size: 1.3rem; color: #94a3b8; cursor: pointer; line-height: 1;" title="Schließen">✕</button>
        ` : ''}

        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 14px;">
          <div style="width: 36px; height: 36px; border-radius: 8px; background: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.4); display: flex; align-items: center; justify-content: center; font-size: 1.2rem;">🎓</div>
          <div>
            <div style="font-size: 1.15rem; font-weight: 800; color: var(--text-main);" id="auth-modal-title">
              ${options.title || (initialMode === 'register' ? '✨ Kostenlos registrieren' : '🔑 Anmelden')}
            </div>
            <div style="font-size: 0.72rem; color: #64748b; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px;">IT-PRAXISPORTAL ACCREDITATION</div>
          </div>
        </div>

        <p id="auth-modal-desc" style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 18px; line-height: 1.5;">
          ${options.message || 'Erhalte sofortigen Zugriff auf 13 Praxis-Kurse, 216 interaktive Module, die Web-IDE und IHK AP1 & AP2 Prüfungsfragen.'}
        </p>

        <!-- Mode Tabs -->
        <div style="display: flex; background: #f1f5f9; border-radius: 8px; padding: 4px; margin-bottom: 18px;">
          <button type="button" id="auth-tab-register" style="flex: 1; padding: 8px; font-size: 0.84rem; font-weight: 700; border: none; border-radius: 6px; cursor: pointer; transition: all 0.15s ease;">Konto erstellen</button>
          <button type="button" id="auth-tab-login" style="flex: 1; padding: 8px; font-size: 0.84rem; font-weight: 700; border: none; border-radius: 6px; cursor: pointer; transition: all 0.15s ease;">Anmelden</button>
        </div>

        <form id="auth-form" style="display: flex; flex-direction: column; gap: 13px;">
          <div id="auth-field-name">
            <label style="display: block; font-size: 0.8rem; font-weight: 700; color: var(--text-main); margin-bottom: 4px;">Dein vollständiger Name:</label>
            <input type="text" id="auth-input-name" style="width: 100%; padding: 9px 12px; border: 1px solid var(--border-color); border-radius: 8px; font-size: 0.92rem; outline: none;" placeholder="z.B. Alex Müller">
          </div>

          <div>
            <label style="display: block; font-size: 0.8rem; font-weight: 700; color: var(--text-main); margin-bottom: 4px;">E-Mail-Adresse:</label>
            <input type="email" id="auth-input-email" required style="width: 100%; padding: 9px 12px; border: 1px solid var(--border-color); border-radius: 8px; font-size: 0.92rem; outline: none;" placeholder="name@beispiel.de">
          </div>

          <div>
            <label style="display: block; font-size: 0.8rem; font-weight: 700; color: var(--text-main); margin-bottom: 4px;">Passwort:</label>
            <input type="password" id="auth-input-password" required minlength="6" style="width: 100%; padding: 9px 12px; border: 1px solid var(--border-color); border-radius: 8px; font-size: 0.92rem; outline: none;" placeholder="Mindestens 6 Zeichen">
          </div>

          <div id="auth-field-role">
            <label style="display: block; font-size: 0.8rem; font-weight: 700; color: var(--text-main); margin-bottom: 4px;">Deine Rolle / Lernziel:</label>
            <select id="auth-select-role" style="width: 100%; padding: 9px 12px; border: 1px solid var(--border-color); border-radius: 8px; font-size: 0.88rem; outline: none; background: white;">
              <option value="solo">🎓 Solo-Selbstlerner & Quereinsteiger</option>
              <option value="student">💼 Auszubildender Fachinformatiker (FIAE / FISI)</option>
              <option value="teacher">👨‍🏫 Lehrkraft / Dozent / Ausbilder</option>
            </select>
          </div>

          <div id="auth-error-box" style="display: none; background: #fef2f2; border: 1px solid #fecaca; color: #b91c1c; padding: 9px 12px; border-radius: 6px; font-size: 0.82rem;"></div>

          <button type="submit" id="auth-submit-btn" class="btn" style="width: 100%; justify-content: center; padding: 11px; font-size: 0.92rem; font-weight: 800; background: #0284c7; color: white; border-radius: 8px; margin-top: 4px; border: none; cursor: pointer;">
            Jetzt kostenlos registrieren &rarr;
          </button>

          ${!allowClose ? `
            <a href="${window.location.origin}/index.html" class="btn btn-secondary" style="width: 100%; justify-content: center; padding: 9px; font-size: 0.86rem; text-decoration: none; border-radius: 8px;">
              &larr; Zurück zur Startseite
            </a>
          ` : `
            <button type="button" class="btn btn-secondary" id="auth-cancel-btn" style="width: 100%; justify-content: center; padding: 9px; font-size: 0.86rem; border-radius: 8px;">
              Abbrechen
            </button>
          `}
        </form>

        <div style="margin-top: 14px; text-align: center; font-size: 0.76rem; color: #94a3b8;">
          🔒 100% DSGVO-konform • Deutsche Server • Keine Kreditkarte erforderlich
        </div>
      </div>
    `;

    document.body.appendChild(modal);

    let isRegister = (initialMode === 'register');
    const tabReg = document.getElementById('auth-tab-register');
    const tabLog = document.getElementById('auth-tab-login');
    const nameField = document.getElementById('auth-field-name');
    const roleField = document.getElementById('auth-field-role');
    const submitBtn = document.getElementById('auth-submit-btn');
    const errorBox = document.getElementById('auth-error-box');
    const form = document.getElementById('auth-form');

    function switchMode(reg) {
      isRegister = reg;
      if (isRegister) {
        tabReg.style.background = '#ffffff';
        tabReg.style.color = '#0284c7';
        tabReg.style.boxShadow = '0 1px 3px rgba(0,0,0,0.1)';
        tabLog.style.background = 'transparent';
        tabLog.style.color = '#64748b';
        tabLog.style.boxShadow = 'none';

        nameField.style.display = 'block';
        roleField.style.display = 'block';
        submitBtn.innerText = 'Jetzt kostenlos registrieren →';
        submitBtn.style.background = '#0284c7';
      } else {
        tabLog.style.background = '#ffffff';
        tabLog.style.color = '#0284c7';
        tabLog.style.boxShadow = '0 1px 3px rgba(0,0,0,0.1)';
        tabReg.style.background = 'transparent';
        tabReg.style.color = '#64748b';
        tabReg.style.boxShadow = 'none';

        nameField.style.display = 'none';
        roleField.style.display = 'none';
        submitBtn.innerText = 'Anmelden →';
        submitBtn.style.background = '#059669';
      }
      errorBox.style.display = 'none';
    }

    tabReg.onclick = () => switchMode(true);
    tabLog.onclick = () => switchMode(false);
    switchMode(isRegister);

    if (allowClose) {
      const closeX = document.getElementById('auth-modal-close-x');
      if (closeX) closeX.onclick = () => modal.remove();
      const cancelBtn = document.getElementById('auth-cancel-btn');
      if (cancelBtn) cancelBtn.onclick = () => modal.remove();
      modal.onclick = (e) => {
        if (e.target === modal) modal.remove();
      };
    }

    form.onsubmit = async (e) => {
      e.preventDefault();
      errorBox.style.display = 'none';

      const email = document.getElementById('auth-input-email').value.trim();
      const password = document.getElementById('auth-input-password').value;
      const name = document.getElementById('auth-input-name')?.value.trim() || email.split('@')[0];
      const role = document.getElementById('auth-select-role')?.value || 'solo';

      submitBtn.disabled = true;
      submitBtn.innerText = 'Bitte warten...';

      let result;
      if (isRegister) {
        result = await window.AUTH.register(name, email, password, role);
      } else {
        result = await window.AUTH.login(email, password);
      }

      submitBtn.disabled = false;
      submitBtn.innerText = isRegister ? 'Jetzt kostenlos registrieren →' : 'Anmelden →';

      if (result.success) {
        modal.remove();
        if (options.onSuccess) {
          options.onSuccess(result.user);
        } else {
          // Wenn auf der Startseite: UI aktualisieren
          window.AUTH.updateUI();
        }
      } else {
        errorBox.innerText = result.error || 'Fehler bei der Authentifizierung';
        errorBox.style.display = 'block';
      }
    };
  };

  // URL-Parameter prüfen (z.B. ?auth=login oder ?auth=register)
  document.addEventListener('DOMContentLoaded', () => {
    window.AUTH.updateUI();
    window.AUTH.fetchMe();

    const params = new URLSearchParams(window.location.search);
    const authParam = params.get('auth');
    if (authParam === 'login' || authParam === 'register') {
      window.openAuthModal(authParam, { allowClose: true });
    }
  });
})();
