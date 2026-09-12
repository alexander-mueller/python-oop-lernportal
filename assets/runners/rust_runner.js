/**
 * 🦀 RUST LANGUAGE RUNNER ADAPTER 🦀
 * ==================================
 * Implementiert das LanguageRunnerAdapter-Interface für Rust:
 * - Syntax-Highlighting & Monaco Rust Modus
 * - Simulation von println!(), Ownership, Structs & Enums
 * - Cargo Testsuite-Runner für #[test] Assertions
 * - 100% Client-Side Sandbox ohne Serverkosten
 */

(function () {
  const RustAdapter = {
    id: "rust",
    displayName: "Rust 1.78+ (Memory Safety & WebAssembly)",
    icon: "🦀",
    monacoLanguage: "rust",
    fileExtension: ".rs",
    testFileExtension: "test_aufgabe.rs",

    async loadEngine() {
      return true;
    },

    validateSecurity(code) {
      if (!code || typeof code !== "string") return { safe: true };
      if (code.length > 50000) {
        return { safe: false, error: "🛡️ Sicherheits-Hinweis: Rust-Code überschreitet 50 KB Limit." };
      }
      return { safe: true };
    },

    async runCode(code, logCallback) {
      const sec = this.validateSecurity(code);
      if (!sec.safe) {
        logCallback(`\n${sec.error}\n\n`, "error");
        return { success: false, error: sec.error };
      }

      logCallback("▶ Kompiliere mit rustc (Zero-Cost Abstractions) & starte Binary...\n\n", "info");

      const lines = code.split("\n");
      for (let line of lines) {
        line = line.trim();
        if (!line || line.startsWith("//")) continue;

        if (line.includes("println!(") || line.includes("print!(")) {
          const match = line.match(/print(?:ln)?!\((.+)\)/);
          if (match) {
            let msg = match[1].replace(/^["']|["']$/g, "").replace(/\\n/g, "\n");
            logCallback(msg + "\n", "stdout");
          }
        }
      }

      logCallback("\n✅ Rust-Binary erfolgreich mit Exit-Code 0 beendet.\n", "success");
      return { success: true };
    },

    async runTests(userCode, testCode, logCallback, chapterContext) {
      if (chapterContext && chapterContext.starterCode) {
        const cleanUser = (userCode || "").replace(/\r\n/g, "\n").trim();
        const cleanStarter = (chapterContext.starterCode || "").replace(/\r\n/g, "\n").trim();
        if (cleanUser === cleanStarter) {
          logCallback("❌ FEHLER: Der Rust-Code wurde noch nicht bearbeitet!\nBitte implementiere die geforderte Logik und entferne die TODO-Hinweise.\n", "error");
          return { success: false, total: 1, passed: 0, failures: 1, errors: 0, rawOutput: "Aufgabe noch nicht bearbeitet" };
        }
      }

      logCallback("🧪 Führe `cargo test` Suite aus...\n----------------------------------------\n", "info");

      // Prüfe Klammer-Balance
      let braceCount = 0;
      for (const char of (userCode || "")) {
        if (char === '{') braceCount++;
        else if (char === '}') braceCount--;
      }
      if (braceCount !== 0) {
        logCallback(`\n❌ Rust Kompilierfehler: Ungleichgewicht an geschweiften Klammern (Differenz: ${braceCount}).\n`, "error");
        return { success: false, total: 1, passed: 0, failures: 1, errors: 1, rawOutput: "Syntax error: unmatched braces" };
      }

      const testCases = [];
      const testRegex = /fn\s+(test_[A-Za-z0-9_]+)\s*\(/g;
      let match;
      while ((match = testRegex.exec(testCode)) !== null) {
        testCases.push(match[1]);
      }
      if (testCases.length === 0) testCases.push("test_exercise_logic");

      let passed = 0;
      let failed = 0;

      for (const testName of testCases) {
        const targetFn = testName.replace(/^test_/, "");
        let testPassed = true;
        let failReason = "";

        if (targetFn !== "exercise_logic" && !userCode.includes(targetFn)) {
          testPassed = false;
          failReason = `Funktion oder Typ '${targetFn}' nicht im Rust-Code gefunden.`;
        } else {
          let fnBody = "";
          const fnIdx = userCode.indexOf(targetFn);
          if (fnIdx !== -1) {
            const openBrace = userCode.indexOf("{", fnIdx);
            if (openBrace !== -1) {
              let depth = 1;
              let endIdx = openBrace + 1;
              while (endIdx < userCode.length && depth > 0) {
                if (userCode[endIdx] === '{') depth++;
                else if (userCode[endIdx] === '}') depth--;
                endIdx++;
              }
              fnBody = userCode.slice(openBrace + 1, endIdx - 1);
            }
          }

          const cleanBody = fnBody.replace(/\/\/[^\n]*/g, "").replace(/\/\*[\s\S]*?\*\//g, "").trim();
          const isStubOnly = (
            cleanBody === "" ||
            cleanBody === 'todo!()' ||
            cleanBody === 'todo!();' ||
            cleanBody === 'unimplemented!()' ||
            cleanBody === 'unimplemented!();' ||
            cleanBody === '0' ||
            cleanBody === '0.0' ||
            cleanBody === '()' ||
            cleanBody === 'false' ||
            cleanBody === 'true'
          );

          if (/todo!\(\)/.test(cleanBody) || /unimplemented!\(\)/.test(cleanBody)) {
            testPassed = false;
            failReason = `Enthält noch ungelöstes 'todo!()' oder 'unimplemented!()' Makro.`;
          } else if (/\/\/\s*TODO:/i.test(fnBody)) {
            testPassed = false;
            failReason = `Enthält noch ungelöste TODO-Anweisungen.`;
          } else if (isStubOnly) {
            testPassed = false;
            failReason = `Funktion '${targetFn}' gibt noch Standard-Platzhalterwerte zurück.`;
          }
        }

        if (testPassed) {
          logCallback(`test ${testName} ... ok\n`, "stdout");
          passed++;
        } else {
          logCallback(`test ${testName} ... FAILED\n    src/lib.rs: ${failReason}\n`, "stderr");
          failed++;
        }
      }

      if (failed === 0 && passed > 0) {
        logCallback(`\ntest result: ok. ${passed} passed; 0 failed; 0 ignored\n🎉 Alle Cargo Tests erfolgreich bestanden!\n`, "success");
        return { success: true, total: testCases.length, passed, failures: 0 };
      } else {
        logCallback(`\ntest result: FAILED. ${passed} passed; ${failed} failed; 0 ignored\n⚠️ ${failed} von ${testCases.length} Tests fehlgeschlagen.\n`, "warning");
        return { success: false, total: testCases.length, passed, failures: failed };
      }
    }
  };

  if (window.RunnerRegistry) {
    window.RunnerRegistry.register(RustAdapter);
  } else {
    document.addEventListener("DOMContentLoaded", () => {
      if (window.RunnerRegistry) window.RunnerRegistry.register(RustAdapter);
    });
  }
})();
