/**
 * 🔐 AUTHENTIFIZIERUNG & ZUGANGSSCHUTZ (AUTH GUARD) 🔐
 * =======================================================
 * IT-Praxisportal – Benutzer-Authentifizierung, Wartungsmodus und Zugangsschutz.
 * - Strikter Login-Zwang für den Alpha-Test (sessionStorage als Standard).
 * - Vollständiger Wartungsmodus mit Fullscreen-Blockade für Nicht-Admins.
 * - Live-Statusabfrage (/api/platform/status) & Ankündigungsbanner.
 * - Vollständige Beseitigung unsicherer Offline-/Dummy-Fallbacks.
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

  // Session-Speicher auslesen (sessionStorage bevorzugt für Sitzungsbindung im Test)
  function getStoredToken() {
    return sessionStorage.getItem('auth_token') || localStorage.getItem('auth_token') || null;
  }

  function getStoredUser() {
    try {
      const raw = sessionStorage.getItem('auth_user') || localStorage.getItem('auth_user') || 'null';
      return JSON.parse(raw);
    } catch (e) {
      return null;
    }
  }

  // Bereinigung veralteter oder gefälschter Dummy-Tokens
  const initialToken = getStoredToken();
  const initialUser = getStoredUser();
  if ((initialToken && initialToken.startsWith('local_token_')) || (initialUser && initialUser.isGuest)) {
    sessionStorage.removeItem('auth_token');
    sessionStorage.removeItem('auth_user');
    localStorage.removeItem('auth_token');
    localStorage.removeItem('auth_user');
  }

  window.AUTH = {
    token: getStoredToken(),
    user: getStoredUser(),
    platformStatus: { maintenance: false, announcement: '', allow_registration: true },

    getToken() {
      if (!this.token) {
        this.token = getStoredToken();
      }
      return this.token;
    },

    getUser() {
      if (!this.user) {
        this.user = getStoredUser();
      }
      return this.user;
    },

    isLoggedIn() {
      const token = this.getToken();
      const user = this.getUser();
      return !!(token && user && !user.isGuest && user.email);
    },

    isAdmin() {
      const user = this.getUser();
      return !!(this.isLoggedIn() && user && user.role === 'admin');
    },

    isTeacher() {
      const user = this.getUser();
      return !!(this.isLoggedIn() && user && (user.role === 'teacher' || user.role === 'admin'));
    },

    setSession(token, user, rememberMe = true) {
      this.token = token;
      this.user = user;

      try {
        localStorage.setItem('auth_token', token);
        localStorage.setItem('auth_user', JSON.stringify(user));
        sessionStorage.setItem('auth_token', token);
        sessionStorage.setItem('auth_user', JSON.stringify(user));
      } catch (e) {}

      this.updateUI();
      this.handleMaintenanceDisplay();
    },

    logout(redirect = true) {
      this.token = null;
      this.user = null;
      sessionStorage.removeItem('auth_token');
      sessionStorage.removeItem('auth_user');
      localStorage.removeItem('auth_token');
      localStorage.removeItem('auth_user');
      this.updateUI();

      if (redirect) {
        const p = window.location.pathname;
        if (p.includes('/courses/') || p.includes('/lehrpfad_') || p.endsWith('workspace.html') || p.endsWith('dashboard.html') || p.endsWith('teacher.html') || p.endsWith('admin.html')) {
          window.location.href = window.location.origin + '/index.html?auth=login';
        } else {
          this.handleMaintenanceDisplay();
        }
      }
    },

    async register(name, email, password, role = 'solo', rememberMe = false) {
      try {
        const res = await fetch('/api/auth/register', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ name, email, password, role })
        });
        const data = await res.json().catch(() => ({}));
        if (!res.ok) {
          return { success: false, error: data.error || 'Registrierung fehlgeschlagen' };
        }

        this.setSession(data.token, data.user, rememberMe);
        return { success: true, user: data.user };
      } catch (err) {
        return { success: false, error: 'Netzwerkfehler: Backend-Server nicht erreichbar.' };
      }
    },

    async login(email, password, rememberMe = false) {
      try {
        const res = await fetch('/api/auth/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email, password })
        });
        const data = await res.json().catch(() => ({}));

        if (!res.ok) {
          return { success: false, error: data.error || 'Anmeldung fehlgeschlagen' };
        }

        this.setSession(data.token, data.user, rememberMe);
        return { success: true, user: data.user };
      } catch (err) {
        return { success: false, error: 'Netzwerkfehler: Backend-Server nicht erreichbar.' };
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
          if (localStorage.getItem('auth_token')) {
            localStorage.setItem('auth_user', JSON.stringify(data.user));
          } else {
            sessionStorage.setItem('auth_user', JSON.stringify(data.user));
          }
          this.updateUI();
          this.handleMaintenanceDisplay();
        } else {
          const errData = await res.json().catch(() => ({}));
          if (res.status === 401 || res.status === 404) {
            this.logout(false);
          } else if (res.status === 503 && errData.maintenance) {
            this.handleMaintenanceDisplay();
          }
        }
      } catch (e) {
        // Offline
      }
    },

    async checkStatus() {
      try {
        const res = await fetch('/api/platform/status');
        if (res.ok) {
          this.platformStatus = await res.json();
          this.handleMaintenanceDisplay();
          this.handleAnnouncementDisplay();
        }
      } catch (e) {
        // Ignorieren
      }
    },

    handleMaintenanceDisplay() {
      const isMaintenance = this.platformStatus && this.platformStatus.maintenance;
      const isAdmin = this.isAdmin();

      let screen = document.getElementById('itp-maintenance-screen');
      let adminBanner = document.getElementById('itp-maintenance-admin-banner');

      if (isMaintenance) {
        if (!isAdmin) {
          if (!screen) {
            screen = document.createElement('div');
            screen.id = 'itp-maintenance-screen';
            screen.style.cssText = `
              position: fixed; inset: 0; z-index: 999999;
              background: rgba(10, 15, 29, 0.96); backdrop-filter: blur(12px);
              display: flex; align-items: center; justify-content: center;
              padding: 24px; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
              color: #f8fafc; text-align: center;
            `;
            screen.innerHTML = `
              <div style="max-width: 520px; background: #0f172a; border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 20px; padding: 40px 32px; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.7);">
                <div style="width: 72px; height: 72px; margin: 0 auto 20px; background: rgba(239, 68, 68, 0.12); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 20px; display: flex; align-items: center; justify-content: center; font-size: 2.2rem;">🛠️</div>
                <h1 style="font-size: 1.75rem; font-weight: 800; color: #ffffff; margin-bottom: 12px; letter-spacing: -0.5px;">Wartungsmodus aktiv</h1>
                <p style="font-size: 0.98rem; color: #94a3b8; line-height: 1.6; margin-bottom: 28px;">
                  Das IT-Praxisportal wird derzeit planmäßig gewartet, um Sicherheits-Updates und neue Lernmodule einzuspielen. Reguläre Kurszugänge sind vorübergehend pausiert.
                </p>
                <div style="display: flex; flex-direction: column; gap: 12px;">
                  <button type="button" id="maintenance-admin-login-btn" style="background: #0284c7; color: white; border: none; padding: 13px 24px; border-radius: 10px; font-weight: 700; font-size: 0.95rem; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; gap: 8px;">
                    🔐 Administrator-Anmeldung
                  </button>
                  <div style="font-size: 0.8rem; color: #64748b;">
                    IT-Praxisportal Alpha • Alle Daten sind sicher
                  </div>
                </div>
              </div>
            `;
            document.body.appendChild(screen);

            const btn = document.getElementById('maintenance-admin-login-btn');
            if (btn) {
              btn.onclick = () => {
                window.openAuthModal('login', {
                  allowClose: true,
                  title: '🔐 Administrator-Login',
                  message: 'Wartungsmodus aktiv: Der Zugang ist derzeit exklusiv für System-Administratoren freigeschaltet.',
                  onSuccess: () => {
                    window.location.reload();
                  }
                });
              };
            }
          }
        } else {
          if (screen) screen.remove();
          if (!adminBanner) {
            adminBanner = document.createElement('div');
            adminBanner.id = 'itp-maintenance-admin-banner';
            adminBanner.style.cssText = `
              background: linear-gradient(90deg, #b91c1c, #ea580c);
              color: white; padding: 8px 16px; font-size: 0.84rem; font-weight: 700;
              display: flex; align-items: center; justify-content: space-between;
              position: sticky; top: 0; z-index: 999998; box-shadow: 0 2px 8px rgba(0,0,0,0.3);
            `;
            adminBanner.innerHTML = `
              <div style="display: flex; align-items: center; gap: 8px;">
                <span>⚠️ WARTUNGSMODUS AKTIV</span>
                <span style="opacity: 0.85; font-weight: 400;">| Nur Administratoren haben derzeit Zugriff auf die Plattform.</span>
              </div>
              <a href="${window.location.origin}/admin.html" style="color: white; background: rgba(255,255,255,0.2); padding: 4px 10px; border-radius: 6px; text-decoration: none; font-size: 0.78rem;">⚙️ Admin-Panel öffnen</a>
            `;
            document.body.insertBefore(adminBanner, document.body.firstChild);
          }
        }
      } else {
        if (screen) screen.remove();
        if (adminBanner) adminBanner.remove();
      }
    },

    handleAnnouncementDisplay() {
      const bannerText = this.platformStatus && this.platformStatus.announcement;
      let el = document.getElementById('itp-announcement-banner');
      if (!bannerText) {
        if (el) el.remove();
        return;
      }

      if (sessionStorage.getItem('dismissed_announcement') === bannerText) {
        return;
      }

      if (!el) {
        el = document.createElement('div');
        el.id = 'itp-announcement-banner';
        el.style.cssText = `
          background: #0284c7; color: white; padding: 8px 16px; font-size: 0.85rem; font-weight: 600;
          display: flex; align-items: center; justify-content: space-between;
          position: sticky; top: 0; z-index: 999990;
        `;
        document.body.insertBefore(el, document.body.firstChild);
      }
      el.innerHTML = `
        <div style="display: flex; align-items: center; gap: 8px; margin: 0 auto;">
          <span>📢 ${escapeHtml(bannerText)}</span>
        </div>
        <button type="button" style="background: transparent; border: none; color: white; font-size: 1.1rem; cursor: pointer; line-height: 1;" title="Schließen">✕</button>
      `;
      el.querySelector('button').onclick = () => {
        sessionStorage.setItem('dismissed_announcement', bannerText);
        el.remove();
      };
    },

    requireAuth(options = {}) {
      if (this.isLoggedIn()) {
        return true;
      }
      this.showAuthBarrier(options);
      return false;
    },

    showAuthBarrier(options = {}) {
      window.openAuthModal(options.mode || 'login', {
        allowClose: options.allowClose !== undefined ? options.allowClose : false,
        title: options.title || '🔒 Anmeldung erforderlich',
        message: options.message || 'Dieser Lernbereich erfordert ein Benutzerkonto. Bitte melde dich an oder erstelle einen kostenlosen Account.',
        onSuccess: () => {
          if (options.onSuccess) options.onSuccess();
          else window.location.reload();
        }
      });
    },

    updateUI() {
      const loggedIn = this.isLoggedIn();
      const user = this.getUser();

      // Topbar Elemente in index.html
      const userSpan = document.getElementById('nav-auth-user');
      const loginBtn = document.getElementById('nav-btn-login');
      const registerBtn = document.getElementById('nav-btn-register');
      const guestBtn = document.getElementById('nav-btn-guest');
      const teacherLink = document.getElementById('nav-teacher-link');
      const heroPrimaryCta = document.getElementById('hero-primary-cta');

      // Dashboard Links auf index.html / impressum / datenschutz
      const navDashLink = document.getElementById('nav-dashboard-link');
      const mobDashLink = document.getElementById('mobile-drawer-dash-link');
      const landingBanner = document.getElementById('landing-logged-in-banner');
      const landingUserName = document.getElementById('landing-user-name');

      if (guestBtn) guestBtn.style.display = 'none'; // Gast-Button permanent ausblenden

      if (loggedIn && user) {
        if (userSpan) {
          userSpan.style.display = 'inline-flex';
          userSpan.innerHTML = `👤 ${escapeHtml(user.name || user.email)}`;
        }
        if (loginBtn) {
          loginBtn.style.display = 'inline-flex';
          loginBtn.innerText = 'Abmelden';
          loginBtn.style.background = 'rgba(239, 68, 68, 0.15)';
          loginBtn.style.color = '#f87171';
          loginBtn.style.borderColor = 'rgba(239, 68, 68, 0.3)';
          loginBtn.removeAttribute('onclick');
          loginBtn.onclick = () => {
            if (confirm('Möchtest du dich wirklich abmelden?')) {
              this.logout();
            }
          };
        }
        if (registerBtn) {
          registerBtn.style.display = 'inline-flex';
          registerBtn.innerHTML = '<span class="btn-text-desktop">💻 Zum Kurs-Dashboard</span><span class="btn-text-mobile">💻 Dashboard</span>';
          registerBtn.style.background = '#10b981';
          registerBtn.removeAttribute('onclick');
          registerBtn.onclick = (e) => {
            e.preventDefault();
            window.location.href = 'dashboard.html';
          };
        }
        if (heroPrimaryCta) {
          heroPrimaryCta.innerHTML = '<span>▶ Zum Dashboard &amp; Kurse wählen &rarr;</span>';
          heroPrimaryCta.removeAttribute('onclick');
          heroPrimaryCta.onclick = (e) => {
            e.preventDefault();
            window.location.href = 'dashboard.html';
          };
        }

        // Alle allgemeinen Landing-Page Action Buttons anpassen
        document.querySelectorAll('.landing-cta-btn').forEach(btn => {
          btn.innerHTML = '<span>▶ Zum Dashboard &amp; Kurse wählen &rarr;</span>';
          btn.style.background = '#10b981';
          btn.removeAttribute('onclick');
          btn.onclick = (e) => {
            e.preventDefault();
            window.location.href = 'dashboard.html';
          };
        });

        const footerLoginBtn = document.getElementById('footer-cta-login');
        if (footerLoginBtn) footerLoginBtn.style.display = 'none';

        // Banner und Dashboard-Links einblenden
        if (landingBanner) {
          landingBanner.style.display = 'flex';
          if (landingUserName) {
            landingUserName.innerText = user.name || user.email.split('@')[0];
          }
        }
        if (navDashLink) navDashLink.style.display = 'inline-flex';
        if (mobDashLink) mobDashLink.style.display = 'flex';
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
          registerBtn.innerHTML = '<span class="btn-text-desktop">✨ Kostenlos registrieren</span><span class="btn-text-mobile">✨ Registrieren</span>';
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

        // Alle allgemeinen Landing-Page Action Buttons für Besucher
        document.querySelectorAll('.landing-cta-btn').forEach(btn => {
          btn.innerHTML = '<span>✨ Jetzt kostenlos registrieren &amp; Kurse wählen &rarr;</span>';
          btn.style.background = '#0284c7';
          btn.onclick = (e) => {
            e.preventDefault();
            window.openAuthModal('register', { allowClose: true });
          };
        });

        const footerLoginBtn = document.getElementById('footer-cta-login');
        if (footerLoginBtn) footerLoginBtn.style.display = 'inline-flex';

        if (landingBanner) landingBanner.style.display = 'none';
        if (navDashLink) navDashLink.style.display = 'none';
        if (mobDashLink) mobDashLink.style.display = 'none';
      }

      // 🔒 Strikter Rollen-Filter für Dozenten- und Admin-Funktionen
      const isTeacherOrAdmin = loggedIn && user && (user.role === 'teacher' || user.role === 'admin');
      const isAdmin = loggedIn && user && user.role === 'admin';

      document.querySelectorAll('.teacher-only, #nav-teacher-link, #mobile-drawer-teacher-link, #footer-teacher-link').forEach(el => {
        if (isTeacherOrAdmin) {
          el.style.display = (el.tagName === 'LI' || el.tagName === 'DIV') ? 'block' : 'inline-flex';
        } else {
          el.style.display = 'none';
        }
      });

      document.querySelectorAll('.admin-only, #nav-admin-link, #mobile-drawer-admin-link, #footer-admin-link').forEach(el => {
        if (isAdmin) {
          el.style.display = (el.tagName === 'LI' || el.tagName === 'DIV') ? 'block' : 'inline-flex';
        } else {
          el.style.display = 'none';
        }
      });

      // Aktualisiere ggf. vorhandene Curriculum-Aktions-Buttons
      document.querySelectorAll('.portal-card-action-btn').forEach(btn => {
        if (loggedIn) {
          btn.innerHTML = '<span>▶ Im Lernbereich öffnen</span> <span>&rarr;</span>';
          btn.classList.remove('locked');
          btn.style.background = '#10b981';
          btn.onclick = () => { window.location.href = 'dashboard.html'; };
        } else {
          btn.innerHTML = '<span>✨ Lehrplan freischalten &amp; starten</span>';
          btn.classList.add('locked');
          btn.style.background = '#0284c7';
          btn.onclick = (e) => {
            e.preventDefault();
            window.openAuthModal('register', {
              allowClose: true,
              title: '🔒 Lehrplan freischalten',
              message: 'Erstelle einen kostenlosen Account in unter 30 Sekunden, um sofort vollen Zugriff auf alle Kurse und Module im Lernbereich zu erhalten.'
            });
          };
        }
      });
    }
  };

  // Auth Modal UI
  window.openAuthModal = function (initialMode = 'login', options = {}) {
    if (window.AUTH && window.AUTH.isLoggedIn()) {
      window.location.href = 'dashboard.html';
      return;
    }
    const allowClose = options.allowClose !== false;
    let modal = document.getElementById('auth-modal-overlay');
    if (modal) modal.remove();

    const allowReg = window.AUTH.platformStatus.allow_registration !== false && !window.AUTH.platformStatus.maintenance;

    modal = document.createElement('div');
    modal.id = 'auth-modal-overlay';
    modal.className = 'certificate-overlay';
    modal.style.zIndex = '999999';

    modal.innerHTML = `
      <div class="certificate-container" style="max-width: 460px; padding: 28px 30px; text-align: left; position: relative; border: 1px solid rgba(255, 255, 255, 0.15); box-shadow: 0 20px 40px rgba(0,0,0,0.6); border-radius: 16px; background: #ffffff;">
        ${allowClose ? `
          <button type="button" id="auth-modal-close-x" style="position: absolute; top: 16px; right: 18px; background: transparent; border: none; font-size: 1.3rem; color: #94a3b8; cursor: pointer; line-height: 1;" title="Schließen">✕</button>
        ` : ''}

        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 14px;">
          <div style="width: 36px; height: 36px; border-radius: 8px; background: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.4); display: flex; align-items: center; justify-content: center; font-size: 1.2rem;">🎓</div>
          <div>
            <div style="font-size: 1.15rem; font-weight: 800; color: #0f172a;" id="auth-modal-title">
              ${escapeHtml(options.title || (initialMode === 'register' && allowReg ? '✨ Kostenlos registrieren' : '🔑 Anmelden'))}
            </div>
            <div style="font-size: 0.72rem; color: #64748b; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px;">IT-PRAXISPORTAL AUTHENTICATION</div>
          </div>
        </div>

        <p id="auth-modal-desc" style="font-size: 0.88rem; color: #64748b; margin-bottom: 18px; line-height: 1.5;">
          ${escapeHtml(options.message || 'Erhalte sofortigen Zugriff auf 13 Praxis-Kurse, 216 interaktive Module und die Web-IDE.')}
        </p>

        <!-- Mode Tabs -->
        <div style="display: flex; background: #f1f5f9; border-radius: 8px; padding: 4px; margin-bottom: 18px;">
          <button type="button" id="auth-tab-login" style="flex: 1; padding: 8px; font-size: 0.84rem; font-weight: 700; border: none; border-radius: 6px; cursor: pointer; transition: all 0.15s ease;">Anmelden</button>
          ${allowReg ? `
            <button type="button" id="auth-tab-register" style="flex: 1; padding: 8px; font-size: 0.84rem; font-weight: 700; border: none; border-radius: 6px; cursor: pointer; transition: all 0.15s ease;">Konto erstellen</button>
          ` : `
            <button type="button" disabled style="flex: 1; padding: 8px; font-size: 0.84rem; font-weight: 600; border: none; border-radius: 6px; color: #94a3b8; cursor: not-allowed; background: transparent;">Registrierung pausiert</button>
          `}
        </div>

        <form id="auth-form" style="display: flex; flex-direction: column; gap: 13px;">
          <div id="auth-field-name" style="display: none;">
            <label style="display: block; font-size: 0.8rem; font-weight: 700; color: #0f172a; margin-bottom: 4px;">Dein vollständiger Name:</label>
            <input type="text" id="auth-input-name" style="width: 100%; padding: 9px 12px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 0.92rem; outline: none; box-sizing: border-box;" placeholder="z.B. Alex Müller">
          </div>

          <div>
            <label style="display: block; font-size: 0.8rem; font-weight: 700; color: #0f172a; margin-bottom: 4px;">E-Mail-Adresse:</label>
            <input type="email" id="auth-input-email" required style="width: 100%; padding: 9px 12px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 0.92rem; outline: none; box-sizing: border-box;" placeholder="name@beispiel.de">
          </div>

          <div>
            <label style="display: block; font-size: 0.8rem; font-weight: 700; color: #0f172a; margin-bottom: 4px;">Passwort:</label>
            <input type="password" id="auth-input-password" required minlength="6" style="width: 100%; padding: 9px 12px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 0.92rem; outline: none; box-sizing: border-box;" placeholder="Mindestens 6 Zeichen">
          </div>

          <div id="auth-field-role" style="display: none;">
            <label style="display: block; font-size: 0.8rem; font-weight: 700; color: #0f172a; margin-bottom: 4px;">Deine Rolle / Lernziel:</label>
            <select id="auth-select-role" style="width: 100%; padding: 9px 12px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 0.88rem; outline: none; background: white; box-sizing: border-box;">
              <option value="solo">🎓 Solo-Selbstlerner & Quereinsteiger</option>
              <option value="student">💼 Auszubildender Fachinformatiker (FIAE / FISI)</option>
              <option value="teacher">👨‍🏫 Lehrkraft / Dozent / Ausbilder</option>
            </select>
          </div>

          <!-- Session-Einstellung (Standard: nicht angehakt für Login-Zwang nach Schließen des Browsers) -->
          <div style="display: flex; align-items: center; gap: 8px; margin-top: 2px;">
            <input type="checkbox" id="auth-remember-me" style="width: 16px; height: 16px; cursor: pointer;">
            <label for="auth-remember-me" style="font-size: 0.82rem; color: #64748b; cursor: pointer;">Angemeldet bleiben (dauerhafte Sitzung)</label>
          </div>

          <div id="auth-error-box" style="display: none; background: #fef2f2; border: 1px solid #fecaca; color: #b91c1c; padding: 9px 12px; border-radius: 6px; font-size: 0.82rem;"></div>

          <button type="submit" id="auth-submit-btn" style="width: 100%; justify-content: center; padding: 11px; font-size: 0.92rem; font-weight: 800; background: #0284c7; color: white; border-radius: 8px; margin-top: 4px; border: none; cursor: pointer;">
            Anmelden &rarr;
          </button>

          ${!allowClose ? `
            <a href="${window.location.origin}/index.html" style="width: 100%; text-align: center; padding: 9px; font-size: 0.86rem; text-decoration: none; border-radius: 8px; color: #64748b; background: #f1f5f9; display: block; box-sizing: border-box;">
              &larr; Zurück zur Startseite
            </a>
          ` : `
            <button type="button" id="auth-cancel-btn" style="width: 100%; text-align: center; padding: 9px; font-size: 0.86rem; border-radius: 8px; color: #64748b; background: #f1f5f9; border: none; cursor: pointer;">
              Abbrechen
            </button>
          `}
        </form>

        <div style="margin-top: 14px; text-align: center; font-size: 0.76rem; color: #94a3b8;">
          🔒 100% DSGVO-konform • Deutsche Server • Keine Tracking-Cookies
        </div>
      </div>
    `;

    document.body.appendChild(modal);

    let isRegister = (initialMode === 'register' && allowReg);
    const tabLog = document.getElementById('auth-tab-login');
    const tabReg = document.getElementById('auth-tab-register');
    const nameField = document.getElementById('auth-field-name');
    const roleField = document.getElementById('auth-field-role');
    const submitBtn = document.getElementById('auth-submit-btn');
    const errorBox = document.getElementById('auth-error-box');
    const form = document.getElementById('auth-form');

    function switchMode(reg) {
      isRegister = reg && allowReg;
      if (isRegister) {
        if (tabReg) {
          tabReg.style.background = '#ffffff';
          tabReg.style.color = '#0284c7';
          tabReg.style.boxShadow = '0 1px 3px rgba(0,0,0,0.1)';
        }
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
        if (tabReg) {
          tabReg.style.background = 'transparent';
          tabReg.style.color = '#64748b';
          tabReg.style.boxShadow = 'none';
        }

        nameField.style.display = 'none';
        roleField.style.display = 'none';
        submitBtn.innerText = 'Anmelden →';
        submitBtn.style.background = '#059669';
      }
      errorBox.style.display = 'none';
    }

    tabLog.onclick = () => switchMode(false);
    if (tabReg) tabReg.onclick = () => switchMode(true);
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
      const rememberMe = document.getElementById('auth-remember-me')?.checked || false;

      submitBtn.disabled = true;
      submitBtn.innerText = 'Bitte warten...';

      let result;
      if (isRegister) {
        result = await window.AUTH.register(name, email, password, role, rememberMe);
      } else {
        result = await window.AUTH.login(email, password, rememberMe);
      }

      submitBtn.disabled = false;
      submitBtn.innerText = isRegister ? 'Jetzt kostenlos registrieren →' : 'Anmelden →';

      if (result.success) {
        modal.remove();
        if (options.onSuccess) {
          options.onSuccess(result.user);
        } else {
          try { window.AUTH.updateUI(); } catch (e) {}
          window.location.href = 'dashboard.html';
        }
      } else {
        errorBox.innerText = result.error || 'Fehler bei der Authentifizierung';
        errorBox.style.display = 'block';
      }
    };
  };

  // Initialisierung beim Laden des DOMs
  document.addEventListener('DOMContentLoaded', () => {
    window.AUTH.updateUI();
    window.AUTH.checkStatus();
    window.AUTH.fetchMe();

    const params = new URLSearchParams(window.location.search);
    const authParam = params.get('auth');
    if (authParam === 'login' || authParam === 'register') {
      if (!window.AUTH.isLoggedIn()) {
        window.openAuthModal(authParam, { allowClose: true });
      } else {
        window.location.replace('dashboard.html');
      }
    }
  });
})();
