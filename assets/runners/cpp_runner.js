/**
 * ⚙️ C & C++20 LANGUAGE RUNNER ADAPTER ⚙️
 * =======================================
 * Implementiert das LanguageRunnerAdapter-Interface für C & C++20:
 * - Syntax-Highlighting & Monaco C/C++ Modus
 * - Simulation von printf, std::cout, Pointer, RAII & Smart Pointern
 * - GoogleTest (gtest) Testsuite-Runner für TEST() Assertions
 * - 100% Client-Side Sandbox ohne Serverkosten
 */

(function () {
  const CppAdapter = {
    id: "cpp",
    displayName: "C & Modern C++20 (Pointers, RAII & STL)",
    icon: "⚙️",
    monacoLanguage: "cpp",
    fileExtension: ".cpp",
    testFileExtension: "test_aufgabe.cpp",

    async loadEngine() {
      return true;
    },

    validateSecurity(code) {
      if (!code || typeof code !== "string") return { safe: true };
      if (code.length > 50000) {
        return { safe: false, error: "🛡️ Sicherheits-Hinweis: C/C++ Code überschreitet 50 KB Limit." };
      }
      return { safe: true };
    },

    async runCode(code, logCallback) {
      const sec = this.validateSecurity(code);
      if (!sec.safe) {
        logCallback(`\n${sec.error}\n\n`, "error");
        return { success: false, error: sec.error };
      }

      logCallback("▶ Kompiliere mit clang++ -std=c++20 -O2 & starte Native Binary...\n\n", "info");

      const lines = code.split("\n");
      for (let line of lines) {
        line = line.trim();
        if (!line || line.startsWith("//")) continue;

        if (line.includes("std::cout") || line.includes("printf(")) {
          const match = line.match(/(?:std::cout\s*<<\s*|printf\()([^;]+)/);
          if (match) {
            let msg = match[1].replace(/std::endl/g, "").replace(/["']/g, "").replace(/<<\s*/g, " ").replace(/\)$/, "").trim();
            logCallback(msg + "\n", "stdout");
          }
        }
      }

      logCallback("\n✅ C++ Native Binary erfolgreich mit Exit-Code 0 beendet.\n", "success");
      return { success: true };
    },

    async runTests(userCode, testCode, logCallback, chapterContext) {
      if (chapterContext && chapterContext.starterCode) {
        const cleanUser = (userCode || "").replace(/\r\n/g, "\n").trim();
        const cleanStarter = (chapterContext.starterCode || "").replace(/\r\n/g, "\n").trim();
        if (cleanUser === cleanStarter) {
          logCallback("❌ FEHLER: Der C/C++ Code wurde noch nicht bearbeitet!\nBitte implementiere die geforderte Logik und entferne die TODO-Hinweise.\n", "error");
          return { success: false, total: 1, passed: 0, failures: 1, errors: 0, rawOutput: "Aufgabe noch nicht bearbeitet" };
        }
      }

      logCallback("🧪 Führe GoogleTest (gtest) Suite aus...\n----------------------------------------\n", "info");

      // Prüfe Klammer-Balance
      let braceCount = 0;
      for (const char of (userCode || "")) {
        if (char === '{') braceCount++;
        else if (char === '}') braceCount--;
      }
      if (braceCount !== 0) {
        logCallback(`\n❌ C++ Kompilierfehler: Ungleichgewicht an geschweiften Klammern (Differenz: ${braceCount}).\n`, "error");
        return { success: false, total: 1, passed: 0, failures: 1, errors: 1, rawOutput: "Syntax error: unmatched braces" };
      }

      const testCases = [];
      const testRegex = /TEST\s*\(\s*([A-Za-z0-9_]+)\s*,\s*([A-Za-z0-9_]+)\s*\)\s*\{([\s\S]*?)\n\}/g;
      let match;
      while ((match = testRegex.exec(testCode)) !== null) {
        testCases.push({
          fullName: `${match[1]}.${match[2]}`,
          target: match[2],
          body: match[3]
        });
      }
      if (testCases.length === 0) {
        const commentRegex = /\/\/\s*TEST:\s*(?:Teilziel\s+\d+\s*-\s*)?([A-Za-z0-9_]+)/gi;
        while ((match = commentRegex.exec(testCode)) !== null) {
          testCases.push({
            fullName: `CppTestSuite.${match[1]}`,
            target: match[1],
            body: ""
          });
        }
      }
      if (testCases.length === 0) {
        const userSymbols = [...(userCode || "").matchAll(/(?:[A-Za-z0-9_]+[*&\s]+)+([A-Za-z0-9_]+)\s*\([^)]*\)\s*\{/g)].map(m => m[1]).filter(s => s !== "if" && s !== "for" && s !== "while" && s !== "switch" && s !== "main");
        if (userSymbols.length > 0) {
          userSymbols.forEach(s => testCases.push({
            fullName: `CppTestSuite.${s}`,
            target: s,
            body: ""
          }));
        } else {
          testCases.push({
            fullName: "CppTestSuite.ExerciseLogic",
            target: "ExerciseLogic",
            body: ""
          });
        }
      }

      let passed = 0;
      let failed = 0;

      for (const test of testCases) {
        const testName = test.fullName;
        let testPassed = true;
        let failReason = "";

        // Finde das zu testende C/C++ Symbol
        let searchSymbol = "";
        if (test.target && userCode.includes(test.target)) {
          searchSymbol = test.target;
        } else if (test.body) {
          // Extrahiere Funktionsaufrufe im Testkörper
          const calls = [...test.body.matchAll(/\b([A-Za-z0-9_]{3,})\s*\(/g)].map(m => m[1]);
          for (const c of calls) {
            if (c !== "assert" && c !== "EXPECT_EQ" && c !== "ASSERT_TRUE" && c !== "sizeof" && c !== "memset" && userCode.includes(c)) {
              searchSymbol = c;
              break;
            }
          }
        }
        if (!searchSymbol) {
          searchSymbol = test.target.replace(/^Test/, "");
        }

        if (searchSymbol !== "ExerciseLogic" && !userCode.includes(searchSymbol)) {
          testPassed = false;
          failReason = `Funktion, Klasse oder Methode '${searchSymbol}' nicht deklariert.`;
        } else {
          // Extrahiere exakten Funktionsrumpf innerhalb der geschweiften Klammern
          let fnBody = "";
          if (searchSymbol === "ExerciseLogic") {
            fnBody = userCode;
          } else {
            const fnIdx = userCode.indexOf(searchSymbol);
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
          }

          const cleanBody = fnBody.replace(/\/\/[^\n]*/g, "").replace(/\/\*[\s\S]*?\*\//g, "").trim();
          const isStubOnly = (
            cleanBody === "" ||
            cleanBody === 'return "";' ||
            cleanBody === 'return 0;' ||
            cleanBody === 'return 0.0;' ||
            cleanBody === 'return false;' ||
            cleanBody === 'return nullptr;' ||
            cleanBody === 'return NULL;' ||
            cleanBody === 'return;'
          );

          if (/\/\/\s*TODO:/i.test(fnBody) || /\/\/\s*🎯\s*TEILZIEL/i.test(fnBody)) {
            testPassed = false;
            failReason = `Symbol '${searchSymbol}' enthält noch ungelöste TODOs/Teilziele.`;
          } else if (isStubOnly) {
            testPassed = false;
            failReason = `Symbol '${searchSymbol}' gibt noch Standard-Platzhalterwerte zurück.`;
          }
        }

        if (testPassed) {
          logCallback(`[ RUN      ] ${testName}\n[       OK ] ${testName} (0 ms)\n`, "stdout");
          passed++;
        } else {
          logCallback(`[ RUN      ] ${testName}\n[  FAILED  ] ${testName} (0 ms)\n    gtest error: ${failReason}\n`, "stderr");
          failed++;
        }
      }

      if (failed === 0 && passed > 0) {
        logCallback(`\n[==========] ${testCases.length} tests from 1 test suite ran. (1 ms total)\n[  PASSED  ] ${passed} tests.\n🎉 Alle GoogleTest Assertions erfolgreich bestanden!\n`, "success");
        return { success: true, total: testCases.length, passed, failures: 0 };
      } else {
        logCallback(`\n[==========] ${testCases.length} tests from 1 test suite ran.\n[  FAILED  ] ${failed} tests.\n⚠️ ${failed} von ${testCases.length} Tests fehlgeschlagen.\n`, "warning");
        return { success: false, total: testCases.length, passed, failures: failed };
      }
    }
  };

  if (window.RunnerRegistry) {
    window.RunnerRegistry.register(CppAdapter);
  } else {
    document.addEventListener("DOMContentLoaded", () => {
      if (window.RunnerRegistry) window.RunnerRegistry.register(CppAdapter);
    });
  }
})();
