/**
 * 🔐 AUTHENTIFIZIERUNG & USER MANAGEMENT 🔐
 * ==========================================
 * Verarbeitet Login, Registrierung, JWT-Tokens und Lehrer-Klassenzuweisung.
 * Mit automatischem Offline-Fallback (LocalStorage), falls kein Server läuft.
 */

(function () {
  window.AUTH = {
    token: localStorage.getItem("auth_token") || null,
    user: JSON.parse(localStorage.getItem("auth_user") || "null"),

    async register(name, email, password, role = "student") {
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
        if (err.message.includes("Failed to fetch")) {
          const mockUser = { id: Date.now(), name, email, role, xp: 0, level: 1 };
          this.setSession("offline_token_" + Date.now(), mockUser);
          return { success: true, user: mockUser, offline: true };
        }
        return { success: false, error: err.message };
      }
    },

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
        if (err.message.includes("Failed to fetch")) {
          const mockUser = { id: 1, name: email.split("@")[0], email, role: "student", xp: 150, level: 2 };
          this.setSession("offline_token", mockUser);
          return { success: true, user: mockUser, offline: true };
        }
        return { success: false, error: err.message };
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
      if (!this.token) return null;
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

      if (this.user) {
        if (userBadge) {
          userBadge.style.display = "inline-flex";
          userBadge.innerHTML = `<span>👤 ${this.user.name}</span> <span style="background: rgba(255,255,255,0.2); padding: 2px 8px; border-radius: 99px; font-size: 0.75rem;">${this.user.xp || 0} XP</span>`;
        }
        if (loginBtn) loginBtn.style.display = "none";
        if (registerBtn) {
          registerBtn.innerText = "Abmelden";
          registerBtn.onclick = (e) => {
            e.preventDefault();
            this.logout();
          };
        }
        if (teacherLink && this.user.role === "teacher") {
          teacherLink.style.display = "inline-flex";
        }
      } else {
        if (userBadge) userBadge.style.display = "none";
        if (loginBtn) loginBtn.style.display = "inline-flex";
        if (registerBtn) {
          registerBtn.innerText = "Konto erstellen";
          registerBtn.onclick = () => window.openAuthModal("register");
        }
        if (teacherLink) teacherLink.style.display = "none";
      }
    }
  };

  // Auth Modal UI
  window.openAuthModal = function (mode = "login") {
    let modal = document.getElementById("auth-modal-overlay");
    if (!modal) {
      modal = document.createElement("div");
      modal.id = "auth-modal-overlay";
      modal.className = "certificate-overlay";
      modal.innerHTML = `
        <div class="certificate-container" style="max-width: 420px; padding: 28px;">
          <h3 id="auth-modal-title" style="margin-top: 0; font-size: 1.35rem; color: var(--text-main);">🔑 Anmelden</h3>
          <p id="auth-modal-sub" style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 18px;">Melde dich an, um deinen Code und deine XP in der Cloud zu speichern.</p>
          
          <form id="auth-form" style="display: flex; flex-direction: column; gap: 12px;">
            <div id="auth-field-name" style="display: none;">
              <label style="font-size: 0.82rem; font-weight: 700; color: var(--text-main);">Dein Name:</label>
              <input type="text" id="auth-input-name" style="width: 100%; padding: 8px 12px; border: 1px solid var(--border-color); border-radius: var(--radius-sm); font-size: 0.92rem;" placeholder="z.B. Anna Schmidt">
            </div>

            <div>
              <label style="font-size: 0.82rem; font-weight: 700; color: var(--text-main);">E-Mail-Adresse:</label>
              <input type="email" id="auth-input-email" required style="width: 100%; padding: 8px 12px; border: 1px solid var(--border-color); border-radius: var(--radius-sm); font-size: 0.92rem;" placeholder="name@schule.de">
            </div>

            <div>
              <label style="font-size: 0.82rem; font-weight: 700; color: var(--text-main);">Passwort:</label>
              <input type="password" id="auth-input-password" required minlength="6" style="width: 100%; padding: 8px 12px; border: 1px solid var(--border-color); border-radius: var(--radius-sm); font-size: 0.92rem;" placeholder="Mindestens 6 Zeichen">
            </div>

            <div id="auth-field-role" style="display: none;">
              <label style="font-size: 0.82rem; font-weight: 700; color: var(--text-main);">Rolle:</label>
              <select id="auth-select-role" style="width: 100%; padding: 8px 12px; border: 1px solid var(--border-color); border-radius: var(--radius-sm); font-size: 0.92rem;">
                <option value="student">🎓 Schüler / Selbstlerner</option>
                <option value="teacher">👨‍🏫 Lehrkraft / Dozent</option>
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
      const role = document.getElementById("auth-select-role")?.value || "student";

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
        alert(`Willkommen zurück, ${result.user.name}! 👋`);
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
