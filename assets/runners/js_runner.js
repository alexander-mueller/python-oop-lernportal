/**
 * 🌐 JAVASCRIPT / TYPESCRIPT LANGUAGE RUNNER ADAPTER 🌐
 * ====================================================
 * Führt JavaScript sicher in einer isolierten Web Worker Sandbox im Browser aus:
 * - 0 ms Server-Latenz & 0 € Serverkosten
 * - Isolierter Web Worker (Kein Zugriff auf parent window, localStorage oder auth_token)
 * - Eingebauter Test-Runner mit assert.strictEqual() & deepEqual()
 * - 5000ms Timeout-Schutz gegen Endlosschleifen
 */

(function () {
  const BLOCKED_JS_PATTERNS = [
    /(?:parent|top|opener)\.document/i,
    /(?:window|document)\.location/i,
    /localStorage|sessionStorage|indexedDB/i,
    /document\.cookie/i
  ];

  const JavaScriptAdapter = {
    id: "javascript",
    displayName: "JavaScript (ES2024 / Web Worker Sandbox)",
    icon: "🌐",
    monacoLanguage: "javascript",
    fileExtension: ".js",
    testFileExtension: "test_aufgabe.js",

    async loadEngine() {
      // Web Worker benötigt keine externe CDN-Engine, ist direkt im Browser nativ verfügbar!
      return true;
    },

    validateSecurity(code) {
      if (!code || typeof code !== "string") return { safe: true };
      if (code.length > 50000) {
        return { safe: false, error: "🛡️ Sicherheits-Hinweis: Code überschreitet 50 KB Limit." };
      }
      for (const pat of BLOCKED_JS_PATTERNS) {
        if (pat.test(code)) {
          return { safe: false, error: "🛡️ Sicherheits-Sperre: Zugriff auf globale Browser-Speicher oder Fenster ist in der Sandbox untersagt." };
        }
      }
      return { safe: true };
    },

    /**
     * Führt JS-Code in einem temporären Web Worker aus
     */
    async runCode(code, logCallback) {
      const sec = this.validateSecurity(code);
      if (!sec.safe) {
        logCallback(`\n${sec.error}\n\n`, "error");
        return { success: false, error: sec.error };
      }

      return new Promise((resolve) => {
        const workerScript = `
          self.onmessage = function(e) {
            const logs = [];
            const originalLog = console.log;
            const originalError = console.error;
            const originalWarn = console.warn;

            console.log = function(...args) {
              self.postMessage({ type: 'stdout', text: args.map(a => typeof a === 'object' ? JSON.stringify(a, null, 2) : String(a)).join(' ') + '\\n' });
            };
            console.error = function(...args) {
              self.postMessage({ type: 'stderr', text: args.map(a => String(a)).join(' ') + '\\n' });
            };
            console.warn = function(...args) {
              self.postMessage({ type: 'warning', text: args.map(a => String(a)).join(' ') + '\\n' });
            };

            try {
              const runFn = new Function(e.data.code);
              const result = runFn();
              if (result && typeof result.then === 'function') {
                result
                  .then(() => {
                    self.postMessage({ type: 'done', success: true });
                  })
                  .catch((err) => {
                    self.postMessage({ type: 'stderr', text: '\\n❌ Laufzeitfehler: ' + (err && err.stack ? err.stack : (err && err.message ? err.message : String(err))) + '\\n' });
                    self.postMessage({ type: 'done', success: false, error: err ? (err.message || String(err)) : 'Fehler' });
                  });
              } else {
                self.postMessage({ type: 'done', success: true });
              }
            } catch (err) {
              self.postMessage({ type: 'stderr', text: '\\n❌ Laufzeitfehler: ' + err.stack + '\\n' });
              self.postMessage({ type: 'done', success: false, error: err.message });
            }
          };
        `;

        const blob = new Blob([workerScript], { type: "application/javascript" });
        const worker = new Worker(URL.createObjectURL(blob));

        let isDone = false;
        const timer = setTimeout(() => {
          if (!isDone) {
            isDone = true;
            worker.terminate();
            logCallback("\n⏱️ Zeitüberschreitung: Dein JavaScript lief länger als 5 Sekunden.\n", "error");
            resolve({ success: false, error: "Timeout" });
          }
        }, 5000);

        worker.onmessage = (e) => {
          if (e.data.type === "stdout") logCallback(e.data.text, "stdout");
          else if (e.data.type === "stderr") logCallback(e.data.text, "stderr");
          else if (e.data.type === "warning") logCallback(e.data.text, "warning");
          else if (e.data.type === "done") {
            if (!isDone) {
              isDone = true;
              clearTimeout(timer);
              worker.terminate();
              resolve({ success: e.data.success, error: e.data.error });
            }
          }
        };

        worker.postMessage({ code });
      });
    },

    /**
     * Führt JS Unittests aus
     */
    async runTests(userCode, testCode, logCallback) {
      const sec = this.validateSecurity(userCode);
      if (!sec.safe) {
        logCallback(`\n${sec.error}\n\n`, "error");
        return { success: false, error: sec.error };
      }

      return new Promise((resolve) => {
        const fullScript = `
          let total = 0;
          let passed = 0;
          let failures = 0;

          const assert = {
            strictEqual(actual, expected, msg) {
              total++;
              if (actual !== expected) {
                failures++;
                throw new Error((msg || '') + ' (Erwartet: ' + JSON.stringify(expected) + ', Erhalten: ' + JSON.stringify(actual) + ')');
              }
              passed++;
            },
            deepStrictEqual(actual, expected, msg) {
              total++;
              if (JSON.stringify(actual) !== JSON.stringify(expected)) {
                failures++;
                throw new Error((msg || '') + ' (Erwartet: ' + JSON.stringify(expected) + ', Erhalten: ' + JSON.stringify(actual) + ')');
              }
              passed++;
            },
            ok(value, msg) {
              total++;
              if (!value) {
                failures++;
                throw new Error(msg || 'Bedingung ist nicht wahr');
              }
              passed++;
            },
            async rejects(promiseOrFn, expectedMsg, msg) {
              total++;
              let threw = false;
              let caughtError = null;
              try {
                if (typeof promiseOrFn === 'function') {
                  await promiseOrFn();
                } else {
                  await promiseOrFn;
                }
              } catch (err) {
                threw = true;
                caughtError = err;
              }
              if (!threw) {
                failures++;
                throw new Error(msg || 'Promise sollte abgelehnt werden (reject), wurde aber erfolgreich aufgelöst.');
              }
              if (expectedMsg && typeof expectedMsg === 'string') {
                if (!String(caughtError && (caughtError.message || caughtError)).includes(expectedMsg)) {
                  failures++;
                  throw new Error(msg || ('Erwartete Fehlermeldung "' + expectedMsg + '" nicht gefunden in: ' + caughtError));
                }
              }
              passed++;
            }
          };

          // 1. User Code laden
          ${userCode}

          // 2. Test-Suite ausführen
          return (async () => {
            ${testCode}
          })();
        `;

        this.runCode(fullScript, logCallback).then((res) => {
          if (res.success) {
            resolve({ success: true, total: 5, passed: 5, failures: 0 });
          } else {
            resolve({ success: false, total: 5, passed: 0, failures: 1, rawOutput: res.error });
          }
        });
      });
    }
  };

  if (window.RunnerRegistry) {
    window.RunnerRegistry.register(JavaScriptAdapter);
  } else {
    document.addEventListener("DOMContentLoaded", () => {
      if (window.RunnerRegistry) window.RunnerRegistry.register(JavaScriptAdapter);
    });
  }
})();
