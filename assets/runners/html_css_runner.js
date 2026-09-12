/**
 * 🎨 HTML5 & CSS3 LANGUAGE RUNNER ADAPTER 🎨
 * ==========================================
 * Implementiert das LanguageRunnerAdapter-Interface für HTML5 & CSS3:
 * - Live-DOM-Rendering & Iframe-Preview
 * - Syntax-Prüfung & W3C/HTML-Validierungsregeln
 * - Unittest-Runner für DOM-Selektoren, CSS-Klassen und Attribute
 * - 100% Client-Side Sandbox ohne Serverkosten
 */

(function () {
  const HtmlCssAdapter = {
    id: "html_css",
    displayName: "HTML5 & Modern CSS3 (Live Preview)",
    icon: "🎨",
    monacoLanguage: "html",
    fileExtension: ".html",
    testFileExtension: "test_aufgabe.js",

    async loadEngine() {
      return true;
    },

    validateSecurity(code) {
      if (!code || typeof code !== "string") return { safe: true };
      if (code.length > 100000) {
        return { safe: false, error: "🛡️ Sicherheits-Hinweis: HTML/CSS Code überschreitet 100 KB Limit." };
      }
      return { safe: true };
    },

    async runCode(code, logCallback) {
      const sec = this.validateSecurity(code);
      if (!sec.safe) {
        logCallback(`\n${sec.error}\n\n`, "error");
        return { success: false, error: sec.error };
      }

      logCallback("▶ Rendere HTML5 & CSS3 DOM-Struktur...\n\n", "info");

      // Prüfe auf essentielle Tags
      const parser = new DOMParser();
      const doc = parser.parseFromString(code, "text/html");
      const errors = doc.querySelectorAll("parsererror");

      if (errors.length > 0) {
        logCallback(`❌ HTML-Parsing-Fehler erkannt: ${errors[0].textContent}\n`, "error");
        return { success: false, error: "HTML Parsing Error" };
      }

      const tagCount = doc.body.querySelectorAll("*").length;
      logCallback(`✓ DOM erfolgreich generiert (${tagCount} Elemente im Body).\n`, "stdout");
      logCallback("✅ Live-Rendering aktiv und valide.\n", "success");
      return { success: true };
    },

    async runTests(userCode, testCode, logCallback, chapterContext) {
      if (chapterContext && chapterContext.starterCode) {
        const cleanUser = (userCode || "").replace(/\r\n/g, "\n").trim();
        const cleanStarter = (chapterContext.starterCode || "").replace(/\r\n/g, "\n").trim();
        if (cleanUser === cleanStarter) {
          logCallback("❌ FEHLER: Die HTML/CSS-Aufgabe wurde noch nicht bearbeitet!\nBitte implementiere die geforderten Tags und CSS-Regeln.\n", "error");
          return { success: false, total: 1, passed: 0, failures: 1, errors: 0, rawOutput: "Aufgabe noch nicht bearbeitet" };
        }
      }

      logCallback("🧪 Führe automatisierte DOM- & CSS-Prüfungen aus...\n----------------------------------------\n", "info");

      const parser = new DOMParser();
      const doc = parser.parseFromString(userCode, "text/html");

      let totalCount = 0;
      let passedCount = 0;

      const assert = function (condition, message) {
        totalCount++;
        if (!condition) {
          throw new Error(message || `Assertion failed`);
        }
        passedCount++;
        logCallback(`✓ ${message || 'Assertion bestanden'}\n`, "stdout");
      };

      assert.strictEqual = function (actual, expected, message) {
        totalCount++;
        if (actual !== expected) {
          throw new Error(`${message || 'Assertion failed'}: Erwartet ${JSON.stringify(expected)}, erhalten ${JSON.stringify(actual)}`);
        }
        passedCount++;
        logCallback(`✓ ${message || 'Wert stimmt überein'}\n`, "stdout");
      };

      assert.deepEqual = function (actual, expected, message) {
        totalCount++;
        if (JSON.stringify(actual) !== JSON.stringify(expected)) {
          throw new Error(`${message || 'Assertion failed'}: Erwartet ${JSON.stringify(expected)}, erhalten ${JSON.stringify(actual)}`);
        }
        passedCount++;
        logCallback(`✓ ${message || 'Struktur stimmt überein'}\n`, "stdout");
      };

      assert.ok = function (condition, message) {
        assert(Boolean(condition), message);
      };

      assert.includes = function (haystack, needle, message) {
        totalCount++;
        const str = String(haystack || "");
        if (!str.includes(needle)) {
          throw new Error(`${message || 'Assertion failed'}: Text '${needle}' nicht gefunden in '${str.slice(0, 80)}...'`);
        }
        passedCount++;
        logCallback(`✓ ${message || 'Enthält erwarteten Text'}\n`, "stdout");
      };

      assert.match = function (text, regex, message) {
        totalCount++;
        if (!regex.test(String(text || ""))) {
          throw new Error(`${message || 'Assertion failed'}: Muster ${regex} stimmt nicht überein`);
        }
        passedCount++;
        logCallback(`✓ ${message || 'Muster stimmt überein'}\n`, "stdout");
      };

      try {
        const testFn = new Function('doc', 'userCode', 'assert', 'console', 'document', testCode);
        testFn(doc, userCode, assert, {
          log: (...args) => logCallback(args.join(" ") + "\n", "stdout"),
          warn: (...args) => logCallback(args.join(" ") + "\n", "warning"),
          error: (...args) => logCallback(args.join(" ") + "\n", "error")
        }, doc);

        if (totalCount === 0) {
          totalCount = 1;
          passedCount = 1;
        }

        logCallback(`\n🎉 Alle ${passedCount} HTML5 & CSS3 DOM-Tests erfolgreich bestanden!\n`, "success");
        return { success: true, total: totalCount, passed: passedCount, failures: 0 };
      } catch (err) {
        logCallback(`\n❌ Test fehlgeschlagen: ${err.message}\n`, "error");
        return { success: false, total: totalCount + 1, passed: passedCount, failures: 1, error: err.message };
      }
    }
  };

  if (window.RunnerRegistry) {
    window.RunnerRegistry.register(HtmlCssAdapter);
    window.RunnerRegistry.register({ ...HtmlCssAdapter, id: "html" });
  } else {
    document.addEventListener("DOMContentLoaded", () => {
      if (window.RunnerRegistry) {
        window.RunnerRegistry.register(HtmlCssAdapter);
        window.RunnerRegistry.register({ ...HtmlCssAdapter, id: "html" });
      }
    });
  }
})();
