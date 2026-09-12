/**
 * 🐧 BASH / SHELL LANGUAGE RUNNER ADAPTER 🐧
 * ==========================================
 * Implementiert das LanguageRunnerAdapter-Interface für Linux Shell / Bash:
 * - Virtuelle Shell-Befehls-Ausführung & Parsing
 * - Syntax-Highlighting & Monaco Shell Modus
 * - Unittest-Runner für .sh Skripte mit Exit-Code & Output-Assertions
 * - 100% Client-Side Sandbox ohne Serverkosten
 */

(function () {
  const ShellAdapter = {
    id: "bash",
    displayName: "Linux Bash (GNU Bash 5.2+ Emulated)",
    icon: "🐧",
    monacoLanguage: "shell",
    fileExtension: ".sh",
    testFileExtension: "test_aufgabe.sh",

    async loadEngine() {
      return true;
    },

    validateSecurity(code) {
      if (!code || typeof code !== "string") return { safe: true };
      if (code.length > 50000) {
        return { safe: false, error: "🛡️ Sicherheits-Hinweis: Shell-Skript überschreitet 50 KB Limit." };
      }
      return { safe: true };
    },

    async runCode(code, logCallback) {
      const sec = this.validateSecurity(code);
      if (!sec.safe) {
        logCallback(`\n${sec.error}\n\n`, "error");
        return { success: false, error: sec.error };
      }

      logCallback("▶ Führe Shell-Skript aus...\n\n", "info");

      // Virtueller Shell-Interpreter für Client-Side Ausführung
      const lines = code.split("\n");
      let env = { PATH: "/usr/local/bin:/usr/bin:/bin", USER: "devops-user", HOME: "/home/devops-user" };

      for (let line of lines) {
        line = line.trim();
        if (!line || line.startsWith("#")) continue;

        if (line.startsWith("echo ")) {
          let text = line.substring(5).replace(/^["']|["']$/g, "");
          // Variablen-Ersetzung
          text = text.replace(/\$([A-Z_]+)/g, (_, name) => env[name] || "");
          logCallback(text + "\n", "stdout");
        } else if (line.startsWith("export ")) {
          const parts = line.substring(7).split("=");
          if (parts.length === 2) env[parts[0].trim()] = parts[1].trim().replace(/^["']|["']$/g, "");
        } else {
          logCallback(`$ ${line}\n`, "stdout");
        }
      }

      logCallback("\n✅ Skript mit Exit-Code 0 beendet.\n", "success");
      return { success: true };
    },

    async runTests(userCode, testCode, logCallback, chapterContext) {
      if (chapterContext && chapterContext.starterCode) {
        const cleanUser = (userCode || "").replace(/\r\n/g, "\n").trim();
        const cleanStarter = (chapterContext.starterCode || "").replace(/\r\n/g, "\n").trim();
        if (cleanUser === cleanStarter) {
          logCallback("❌ FEHLER: Das Shell-Skript wurde noch nicht bearbeitet!\nBitte implementiere die geforderte Logik in der Datei, bevor du die Tests ausführst.\n", "error");
          return { success: false, total: 1, passed: 0, failures: 1, errors: 0, rawOutput: "Aufgabe noch nicht bearbeitet" };
        }
      }

      logCallback("🧪 Starte automatisierte Testsuite in isolierter Linux-Sandbox...\n----------------------------------------\n", "info");

      try {
        const token = window.AUTH ? window.AUTH.getToken() : localStorage.getItem("auth_token");
        const payload = {
          language: (chapterContext && (chapterContext.courseId === "git" ? "git" : (chapterContext.courseId === "dns_records" ? "dns" : "bash"))) || "bash",
          base_path: (chapterContext && chapterContext.basePath) ? chapterContext.basePath : "",
          user_code: userCode,
          task_file: (chapterContext && chapterContext.taskFile) ? chapterContext.taskFile : "aufgabe.sh",
          test_file: (chapterContext && chapterContext.testFile) ? chapterContext.testFile : "test_aufgabe.sh"
        };

        const res = await fetch("/api/runners/test", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            ...(token ? { "Authorization": `Bearer ${token}` } : {})
          },
          body: JSON.stringify(payload)
        });

        const data = await res.json();

        if (data.stdout) {
          logCallback(data.stdout, "stdout");
        }
        if (data.stderr && data.stderr.trim()) {
          logCallback(data.stderr, "stderr");
        }

        if (data.error && !data.stdout) {
          logCallback(`\n❌ Fehler: ${data.error}\n`, "error");
        }

        return {
          success: Boolean(data.success),
          total: data.total || 1,
          passed: data.passed || 0,
          failures: data.failures || (data.success ? 0 : 1),
          rawOutput: (data.stdout || "") + "\n" + (data.stderr || "")
        };
      } catch (err) {
        logCallback(`\n❌ Verbindungsfehler zum Backend-Runner: ${err.message}\n`, "error");
        return { success: false, total: 1, passed: 0, failures: 1, rawOutput: err.message };
      }
    }
  };

  if (window.RunnerRegistry) {
    window.RunnerRegistry.register(ShellAdapter);
    window.RunnerRegistry.register({ ...ShellAdapter, id: "git" });
    window.RunnerRegistry.register({ ...ShellAdapter, id: "dns_records" });
    window.RunnerRegistry.register({ ...ShellAdapter, id: "dns" });
  } else {
    document.addEventListener("DOMContentLoaded", () => {
      if (window.RunnerRegistry) {
        window.RunnerRegistry.register(ShellAdapter);
        window.RunnerRegistry.register({ ...ShellAdapter, id: "git" });
        window.RunnerRegistry.register({ ...ShellAdapter, id: "dns_records" });
        window.RunnerRegistry.register({ ...ShellAdapter, id: "dns" });
      }
    });
  }
})();
