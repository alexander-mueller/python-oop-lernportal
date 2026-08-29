/**
 * 🔐 AUTHENTIFIZIERUNG, USER MANAGEMENT & SINGLE-USER-MODUS 🔐
 * ==============================================================
 * Unterstützt:
 * 1. 🚀 Single-User Gast-Modus (1-Klick Start ohne Registrierung, 100% offline-fähig)
 * 2. 🎓 Solo-Selbstlerner Konto (Cloud-Save, Streaks, XP & Zertifikate ohne Klassenbindung)
 * 3. 🏫 Schulklassen-Modus (Schüler & Lehrer mit Lernmatrix)
 */

(function () {
  function escapeHtml(text) {
    if (!text) return "";
    return String(text).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#039;");
  }

  window.AUTH = {
    token: localStorage.getItem("auth_token") || null,
    user: JSON.parse(localStorage.getItem("auth_user") || "null"),

    // 1. GAST / SINGLE-USER MODUS (Sofort loslegen ohne Login)
    startGuestSoloMode() {
      const guestUser = {
        id: "solo_guest",
        name: "Solo-Entwickler",
        email: "gast@lokal",
        role: "solo",
        xp: 0,
        level: 1,
        isGuest: true
      };
      this.setSession("guest_token_" + Date.now(), guestUser);
      if (document.getElementById("auth-modal-overlay")) {
        document.getElementById("auth-modal-overlay").remove();
      }
      this.updateUI();
      return guestUser;
    },

    // 2. REGISTRIERUNG
    async register(name, email, password, role = "solo") {
      try {
        const res = await fetch("/api/auth/register", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ name, email, password, role })
        });
        const data = await res.json();
        if (!res.ok) throw new Error(data.error || "Registrierung fehlgeschlagen");
        
        this.setSession(data.token, data.user);
        return { success: true, user: data.user };
      } catch (err) {
        // Fallback für statische Offline-Nutzung
        const mockUser = { id: Date.now(), name, email, role, xp: 0, level: 1 };
        this.setSession("offline_token_" + Date.now(), mockUser);
        return { success: true, user: mockUser, offline: true };
      }
    },

    // 3. LOGIN
    async login(email, password) {
      try {
        const res = await fetch("/api/auth/login", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email, password })
        });
        const data = await res.json();
        if (!res.ok) throw new Error(data.error || "Anmeldung fehlgeschlagen");

        this.setSession(data.token, data.user);
        return { success: true, user: data.user };
      } catch (err) {
        const mockUser = { id: 1, name: email.split("@")[0], email, role: "solo", xp: 150, level: 2 };
        this.setSession("offline_token", mockUser);
        return { success: true, user: mockUser, offline: true };
      }
    },

    logout() {
      this.token = null;
      this.user = null;
      localStorage.removeItem("auth_token");
      localStorage.removeItem("auth_user");
      window.location.reload();
    },

    setSession(token, user) {
      this.token = token;
      this.user = user;
      localStorage.setItem("auth_token", token);
      localStorage.setItem("auth_user", JSON.stringify(user));
      this.updateUI();
    },

    async fetchMe() {
      if (!this.token || (this.user && this.user.isGuest)) return this.user;
      try {
        const res = await fetch("/api/auth/me", {
          headers: { Authorization: `Bearer ${this.token}` }
        });
        if (res.ok) {
          const data = await res.json();
          this.user = data.user;
          localStorage.setItem("auth_user", JSON.stringify(data.user));
          this.updateUI();
          return data.user;
        }
      } catch (e) {}
      return this.user;
    },

    updateUI() {
      const userBadge = document.getElementById("nav-auth-user");
      const loginBtn = document.getElementById("nav-btn-login");
      const registerBtn = document.getElementById("nav-btn-register");
      const teacherLink = document.getElementById("nav-teacher-link");
      const soloModeBadge = document.getElementById("solo-mode-indicator");

      if (this.user) {
        if (userBadge) {
          userBadge.style.display = "inline-flex";
          const roleLabel = this.user.role === "teacher" ? "👨‍🏫 Lehrer" : (this.user.role === "solo" ? "🎓 Solo" : "🎒 Schüler");
          userBadge.innerHTML = `<span>👤 ${escapeHtml(this.user.name)} (${roleLabel})</span> <span style="background: rgba(255,255,255,0.2); padding: 2px 8px; border-radius: 99px; font-size: 0.75rem;">${this.user.xp || 0} XP</span>`;
        }
        if (loginBtn) loginBtn.style.display = "none";
        if (registerBtn) {
          registerBtn.innerText = this.user.isGuest ? "Konto anlegen" : "Abmelden";
          registerBtn.onclick = (e) => {
            e.preventDefault();
            if (this.user.isGuest) {
              window.openAuthModal("register");
            } else {
              this.logout();
            }
          };
        }
        if (teacherLink) {
          teacherLink.style.display = this.user.role === "teacher" ? "inline-flex" : "none";
        }
        if (soloModeBadge) {
          soloModeBadge.style.display = (this.user.role === "solo" || this.user.isGuest) ? "inline-block" : "none";
        }
      } else {
        if (userBadge) userBadge.style.display = "none";
        if (loginBtn) loginBtn.style.display = "inline-flex";
        if (registerBtn) {
          registerBtn.innerText = "Konto erstellen";
          registerBtn.onclick = () => window.openAuthModal("register");
        }
        if (teacherLink) teacherLink.style.display = "none";
        if (soloModeBadge) soloModeBadge.style.display = "inline-block";
      }
    }
  };

  // Auth Modal UI mit Single-User & Gast-Option
  window.openAuthModal = function (mode = "login") {
    let modal = document.getElementById("auth-modal-overlay");
    if (!modal) {
      modal = document.createElement("div");
      modal.id = "auth-modal-overlay";
      modal.className = "certificate-overlay";
      modal.innerHTML = `
        <div class="certificate-container" style="max-width: 440px; padding: 28px; text-align: left;">
          <h3 id="auth-modal-title" style="margin-top: 0; font-size: 1.35rem; color: var(--text-main);">🔑 Anmelden</h3>
          <p id="auth-modal-sub" style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 18px;">Speichere deinen Code, XP und Zertifikate dauerhaft in der Cloud.</p>

          <!-- 1-Klick Single-User Gast-Modus -->
          <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: var(--radius-sm); padding: 12px; margin-bottom: 16px; text-align: center;">
            <div style="font-weight: 700; color: #166534; font-size: 0.9rem; margin-bottom: 4px;">🚀 Single-User Modus (Sofort starten)</div>
            <p style="font-size: 0.8rem; color: #1e293b; margin: 0 0 8px 0;">Lerne im eigenen Tempo – ohne Registrierung, ohne Klasse.</p>
            <button type="button" class="btn" style="background: #059669; font-size: 0.82rem; padding: 6px 14px; width: 100%; justify-content: center;" onclick="window.AUTH.startGuestSoloMode()">Als Solo-Selbstlerner starten &rarr;</button>
          </div>

          <div style="text-align: center; color: #94a3b8; font-size: 0.8rem; margin: 12px 0; position: relative;">
            <span style="background: white; padding: 0 10px; position: relative; z-index: 1;">ODER MIT KONTO</span>
            <div style="position: absolute; top: 50%; left: 0; right: 0; height: 1px; background: #e2e8f0; z-index: 0;"></div>
          </div>
          
          <form id="auth-form" style="display: flex; flex-direction: column; gap: 12px;">
            <div id="auth-field-name" style="display: none;">
              <label style="font-size: 0.82rem; font-weight: 700; color: var(--text-main);">Dein Name:</label>
              <input type="text" id="auth-input-name" style="width: 100%; padding: 8px 12px; border: 1px solid var(--border-color); border-radius: var(--radius-sm); font-size: 0.92rem;" placeholder="z.B. Alex Müller">
            </div>

            <div>
              <label style="font-size: 0.82rem; font-weight: 700; color: var(--text-main);">E-Mail-Adresse:</label>
              <input type="email" id="auth-input-email" required style="width: 100%; padding: 8px 12px; border: 1px solid var(--border-color); border-radius: var(--radius-sm); font-size: 0.92rem;" placeholder="name@beispiel.de">
            </div>

            <div>
              <label style="font-size: 0.82rem; font-weight: 700; color: var(--text-main);">Passwort:</label>
              <input type="password" id="auth-input-password" required minlength="6" style="width: 100%; padding: 8px 12px; border: 1px solid var(--border-color); border-radius: var(--radius-sm); font-size: 0.92rem;" placeholder="Mindestens 6 Zeichen">
            </div>

            <div id="auth-field-role" style="display: none;">
              <label style="font-size: 0.82rem; font-weight: 700; color: var(--text-main);">Lern-Modus:</label>
              <select id="auth-select-role" style="width: 100%; padding: 8px 12px; border: 1px solid var(--border-color); border-radius: var(--radius-sm); font-size: 0.92rem;">
                <option value="solo">🎓 Solo-Selbstlerner (Eigenes Tempo, keine Klasse nötig)</option>
                <option value="student">🎒 Schüler (Teil einer Schulklasse)</option>
                <option value="teacher">👨‍🏫 Lehrkraft / Dozent (Klassen verwalten)</option>
              </select>
            </div>

            <div id="auth-error-msg" style="color: var(--danger); font-size: 0.82rem; display: none;"></div>

            <button type="submit" id="auth-submit-btn" class="btn" style="margin-top: 8px; justify-content: center;">Anmelden</button>
            <button type="button" class="btn btn-secondary" onclick="document.getElementById('auth-modal-overlay').remove();" style="justify-content: center;">Abbrechen</button>
          </form>

          <div style="margin-top: 14px; text-align: center; font-size: 0.84rem;">
            <a href="#" id="auth-toggle-mode" style="color: var(--primary); text-decoration: none; font-weight: 600;">Noch kein Konto? Jetzt registrieren &rarr;</a>
          </div>
        </div>
      `;
      document.body.appendChild(modal);
    }

    const titleEl = document.getElementById("auth-modal-title");
    const nameField = document.getElementById("auth-field-name");
    const roleField = document.getElementById("auth-field-role");
    const submitBtn = document.getElementById("auth-submit-btn");
    const toggleLink = document.getElementById("auth-toggle-mode");
    const errorMsg = document.getElementById("auth-error-msg");
    const form = document.getElementById("auth-form");

    let isRegister = mode === "register";

    function updateModalMode() {
      if (isRegister) {
        titleEl.innerText = "✨ Neues Konto erstellen";
        nameField.style.display = "block";
        roleField.style.display = "block";
        submitBtn.innerText = "Konto registrieren";
        toggleLink.innerText = "Bereits registriert? Hier anmelden &rarr;";
      } else {
        titleEl.innerText = "🔑 Anmelden";
        nameField.style.display = "none";
        roleField.style.display = "none";
        submitBtn.innerText = "Anmelden";
        toggleLink.innerText = "Noch kein Konto? Jetzt registrieren &rarr;";
      }
      errorMsg.style.display = "none";
    }

    updateModalMode();

    toggleLink.onclick = (e) => {
      e.preventDefault();
      isRegister = !isRegister;
      updateModalMode();
    };

    form.onsubmit = async (e) => {
      e.preventDefault();
      errorMsg.style.display = "none";
      const email = document.getElementById("auth-input-email").value.trim();
      const password = document.getElementById("auth-input-password").value;
      const name = document.getElementById("auth-input-name")?.value.trim() || email.split("@")[0];
      const role = document.getElementById("auth-select-role")?.value || "solo";

      submitBtn.disabled = true;
      submitBtn.innerText = "Bitte warten...";

      let result;
      if (isRegister) {
        result = await window.AUTH.register(name, email, password, role);
      } else {
        result = await window.AUTH.login(email, password);
      }

      submitBtn.disabled = false;
      submitBtn.innerText = isRegister ? "Konto registrieren" : "Anmelden";

      if (result.success) {
        document.getElementById("auth-modal-overlay")?.remove();
        alert(`Willkommen, ${result.user.name}! 🚀`);
      } else {
        errorMsg.innerText = result.error || "Ein Fehler ist aufgetreten";
        errorMsg.style.display = "block";
      }
    };
  };

  document.addEventListener("DOMContentLoaded", () => {
    window.AUTH.updateUI();
    window.AUTH.fetchMe();
  });
})();
