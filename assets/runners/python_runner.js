/**
 * 🐍 PYTHON LANGUAGE RUNNER ADAPTER (Pyodide WebAssembly) 🐍
 * ==========================================================
 * Implementiert das standardisierte LanguageRunnerAdapter-Interface:
 * - Pyodide WASM Engine mit In-Memory Python 3.12
 * - CODE_GUARD Sicherheits-Prüfung & Sandbox-Bootstrap
 * - Timeout-Schutz gegen Endlosschleifen
 * - Unittest-Runner für aufgabe.py & test_aufgabe.py
 * - Fehler-Dolmetscher Anbindung
 */

(function () {
  let pyodideInstance = null;
  let pyodideLoading = false;

  const PythonAdapter = {
    id: "python",
    displayName: "Python 3.12 (Pyodide WebAssembly)",
    icon: "🐍",
    monacoLanguage: "python",
    fileExtension: ".py",
    testFileExtension: "test_aufgabe.py",

    /**
     * Lädt und initialisiert die Pyodide WebAssembly Engine
     */
    async loadEngine(logCallback) {
      if (pyodideInstance) return pyodideInstance;
      if (pyodideLoading) {
        while (pyodideLoading) {
          await new Promise((r) => setTimeout(r, 100));
        }
        return pyodideInstance;
      }

      pyodideLoading = true;
      if (logCallback) logCallback("⏳ Initialisiere Python WebAssembly Engine (Pyodide)... Bitte kurz warten.\n", "info");

      try {
        if (!window.loadPyodide) {
          await new Promise((resolve, reject) => {
            const script = document.createElement("script");
            script.src = "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js";
            script.onload = resolve;
            script.onerror = reject;
            document.head.appendChild(script);
          });
        }

        pyodideInstance = await window.loadPyodide({
          indexURL: "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/"
        });

        // Sandbox-Härtung im Pyodide-Interpreter aktivieren
        if (window.CODE_GUARD && window.CODE_GUARD.getSandboxBootstrap) {
          await pyodideInstance.runPythonAsync(window.CODE_GUARD.getSandboxBootstrap());
        }

        if (logCallback) logCallback("✅ Python WebAssembly Sandbox bereitgestellt!\n\n", "success");
      } catch (err) {
        if (logCallback) logCallback(`❌ Fehler beim Laden der Python Sandbox: ${err.message}\n`, "error");
        throw err;
      } finally {
        pyodideLoading = false;
      }
      return pyodideInstance;
    },

    /**
     * Sicherheitsprüfung vor Code-Ausführung
     */
    validateSecurity(code) {
      if (window.CODE_GUARD && window.CODE_GUARD.validate) {
        return window.CODE_GUARD.validate(code);
      }
      return { safe: true };
    },

    /**
     * Führt Python-Code aus (▶ Code ausführen)
     */
    async runCode(code, logCallback) {
      const securityCheck = this.validateSecurity(code);
      if (!securityCheck.safe) {
        logCallback(`\n${securityCheck.error}\n\n`, "error");
        return { success: false, error: securityCheck.error };
      }

      const py = await this.loadEngine(logCallback);
      if (!py) return { success: false, error: "Pyodide nicht verfügbar" };

      // Umleitung von stdout & stderr
      py.setStdout({ batched: (text) => logCallback(text + "\n", "stdout") });
      py.setStderr({ batched: (text) => logCallback(text + "\n", "stderr") });

      try {
        let timeoutHandle;
        const timeoutPromise = new Promise((_, reject) => {
          timeoutHandle = setTimeout(() => {
            reject(new Error("Zeitüberschreitung: Dein Code lief länger als 5 Sekunden (Endlosschleife vermutet)."));
          }, 5000);
        });

        const execPromise = py.runPythonAsync(code);
        await Promise.race([execPromise, timeoutPromise]);
        clearTimeout(timeoutHandle);

        return { success: true };
      } catch (err) {
        logCallback(`\n❌ Ausführungsfehler:\n${err.message}\n`, "error");
        return { success: false, error: err.message };
      }
    },

    /**
     * Führt automatisierte Unittests aus (🧪 Tests starten)
     */
    async runTests(userCode, testCode, logCallback, chapterContext) {
      const securityCheck = this.validateSecurity(userCode);
      if (!securityCheck.safe) {
        logCallback(`\n${securityCheck.error}\n\n`, "error");
        return { success: false, error: securityCheck.error };
      }

      // Guard: Prüfe ob Startercode noch völlig unberührt ist
      if (chapterContext && chapterContext.starterCode) {
        const cleanUser = (userCode || "").replace(/\r\n/g, "\n").trim();
        const cleanStarter = (chapterContext.starterCode || "").replace(/\r\n/g, "\n").trim();
        if (cleanUser === cleanStarter) {
          logCallback("❌ FEHLER: Aufgabe noch nicht bearbeitet!\nBitte implementiere die geforderte Logik in der Datei, bevor du die Tests ausführst.\n", "error");
          return { success: false, total: 1, passed: 0, failures: 1, errors: 0, rawOutput: "Aufgabe noch nicht bearbeitet" };
        }
      }

      const py = await this.loadEngine(logCallback);
      if (!py) return { success: false, error: "Pyodide nicht verfügbar" };

      try {
        py.FS.writeFile("aufgabe.py", userCode);
        py.FS.writeFile("test_aufgabe.py", testCode);

        const testRunnerScript = `
import importlib, io, sys, unittest
from unittest import TextTestRunner

if '.' not in sys.path:
    sys.path.insert(0, '.')

for mod in list(sys.modules.keys()):
    if mod in ('aufgabe', 'test_aufgabe'):
        del sys.modules[mod]

import aufgabe
import test_aufgabe
importlib.reload(aufgabe)
importlib.reload(test_aufgabe)

loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(test_aufgabe)
stream = io.StringIO()
runner = TextTestRunner(stream=stream, verbosity=2)
result = runner.run(suite)

output_text = stream.getvalue()
total_runs = result.testsRun
failures = len(result.failures)
errors = len(result.errors)
success = (total_runs > 0) and (failures == 0) and (errors == 0) and result.wasSuccessful()

(success, total_runs, failures, errors, output_text)
`;

        let timeoutHandle;
        const timeoutPromise = new Promise((_, reject) => {
          timeoutHandle = setTimeout(() => {
            reject(new Error("Zeitüberschreitung: Unittest lief länger als 6 Sekunden."));
          }, 6000);
        });

        const [isSuccess, totalRuns, fails, errs, outputText] = await Promise.race([
          py.runPythonAsync(testRunnerScript),
          timeoutPromise
        ]);
        clearTimeout(timeoutHandle);

        logCallback(outputText + "\n", "stdout");

        const hasPassed = Boolean(isSuccess) && totalRuns > 0 && fails === 0 && errs === 0;

        return {
          success: hasPassed,
          total: totalRuns,
          passed: totalRuns - (fails + errs),
          failures: fails,
          errors: errs,
          rawOutput: outputText
        };
      } catch (err) {
        logCallback(`\n❌ Fehler beim Ausführen der Testsuite:\n${err.message}\n`, "error");
        return { success: false, error: err.message, rawOutput: err.message };
      }
    },

    /**
     * Übersetzt Python-Tracebacks
     */
    translateError(traceback) {
      if (window.INTERPRETER && window.INTERPRETER.translate) {
        return window.INTERPRETER.translate(traceback);
      }
      return null;
    }
  };

  // In Registry registrieren
  if (window.RunnerRegistry) {
    window.RunnerRegistry.register(PythonAdapter);
  } else {
    document.addEventListener("DOMContentLoaded", () => {
      if (window.RunnerRegistry) window.RunnerRegistry.register(PythonAdapter);
    });
  }
})();
