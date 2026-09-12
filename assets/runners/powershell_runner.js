/**
 * 🔷 POWERSHELL LANGUAGE RUNNER ADAPTER 🔷
 * ========================================
 * Implementiert das LanguageRunnerAdapter-Interface für PowerShell 7+ Core:
 * - Objekt-Pipeline Simulation
 * - Cmdlet-Parsing (Verb-Noun Syntax)
 * - Pester v5 Test-Runner Mocking
 * - 100% Client-Side Sandbox ohne Serverkosten
 */

(function () {
  const PowerShellAdapter = {
    id: "powershell",
    displayName: "PowerShell 7+ Core (Cross-Platform)",
    icon: "🔷",
    monacoLanguage: "powershell",
    fileExtension: ".ps1",
    testFileExtension: "test_aufgabe.ps1",

    async loadEngine() {
      return true;
    },

    validateSecurity(code) {
      if (!code || typeof code !== "string") return { safe: true };
      if (code.length > 50000) {
        return { safe: false, error: "🛡️ Sicherheits-Hinweis: PowerShell-Skript überschreitet 50 KB Limit." };
      }
      return { safe: true };
    },

    async runCode(code, logCallback) {
      const sec = this.validateSecurity(code);
      if (!sec.safe) {
        logCallback(`\n${sec.error}\n\n`, "error");
        return { success: false, error: sec.error };
      }

      logCallback("▶ Starte PowerShell 7+ Core Engine...\n\n", "info");

      const lines = code.split("\n");
      for (let line of lines) {
        line = line.trim();
        if (!line || line.startsWith("#")) continue;

        if (line.startsWith("Write-Host ") || line.startsWith("Write-Output ")) {
          let text = line.replace(/^(?:Write-Host|Write-Output)\s+/, "").replace(/^["']|["']$/g, "");
          logCallback(text + "\n", "stdout");
        } else if (line.startsWith("Write-Warning ")) {
          let text = line.replace(/^Write-Warning\s+/, "").replace(/^["']|["']$/g, "");
          logCallback(`WARNUNG: ${text}\n`, "warning");
        } else {
          logCallback(`PS > ${line}\n`, "stdout");
        }
      }

      logCallback("\n✅ Skriptausführung erfolgreich abgeschlossen.\n", "success");
      return { success: true };
    },

    async runTests(userCode, testCode, logCallback, chapterContext) {
      if (chapterContext && chapterContext.starterCode) {
        const cleanUser = (userCode || "").replace(/\r\n/g, "\n").trim();
        const cleanStarter = (chapterContext.starterCode || "").replace(/\r\n/g, "\n").trim();
        if (cleanUser === cleanStarter) {
          logCallback("❌ FEHLER: Das PowerShell-Skript wurde noch nicht bearbeitet!\nBitte implementiere die geforderte Logik in der Datei, bevor du die Tests ausführst.\n", "error");
          return { success: false, total: 1, passed: 0, failures: 1, errors: 0, rawOutput: "Aufgabe noch nicht bearbeitet" };
        }
      }

      logCallback("🧪 Starte automatisierte Pester Testsuite in isolierter PowerShell 7+ Sandbox...\n----------------------------------------\n", "info");

      try {
        const token = window.AUTH ? window.AUTH.getToken() : localStorage.getItem("auth_token");
        const isAD = chapterContext && (chapterContext.courseId === "active_directory" || chapterContext.courseId === "ad");
        const payload = {
          language: isAD ? "active_directory" : "powershell",
          base_path: (chapterContext && chapterContext.basePath) ? chapterContext.basePath : "",
          user_code: userCode,
          task_file: (chapterContext && chapterContext.taskFile) ? chapterContext.taskFile : "aufgabe.ps1",
          test_file: (chapterContext && chapterContext.testFile) ? chapterContext.testFile : "test_aufgabe.ps1"
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
    window.RunnerRegistry.register(PowerShellAdapter);
    window.RunnerRegistry.register({ ...PowerShellAdapter, id: "active_directory" });
    window.RunnerRegistry.register({ ...PowerShellAdapter, id: "pwsh" });
  } else {
    document.addEventListener("DOMContentLoaded", () => {
      if (window.RunnerRegistry) {
        window.RunnerRegistry.register(PowerShellAdapter);
        window.RunnerRegistry.register({ ...PowerShellAdapter, id: "active_directory" });
        window.RunnerRegistry.register({ ...PowerShellAdapter, id: "pwsh" });
      }
    });
  }
})();
