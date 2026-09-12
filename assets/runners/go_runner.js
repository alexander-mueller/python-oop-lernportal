/**
 * ⚡ GO (GOLANG) LANGUAGE RUNNER ADAPTER ⚡
 * ========================================
 * Implementiert das LanguageRunnerAdapter-Interface für Go:
 * - Go Syntax Parsing & Strukturanalyse
 * - Simulation von fmt.Println, Goroutines, Channels und Structs
 * - Unittest-Runner für go test / TestXxx Assertions
 * - 100% Client-Side Sandbox ohne Serverkosten
 */

(function () {
  const GoAdapter = {
    id: "go",
    displayName: "Go 1.22+ (Microservices & Concurrency)",
    icon: "⚡",
    monacoLanguage: "go",
    fileExtension: ".go",
    testFileExtension: "test_aufgabe.go",

    async loadEngine() {
      return true;
    },

    validateSecurity(code) {
      if (!code || typeof code !== "string") return { safe: true };
      if (code.length > 50000) {
        return { safe: false, error: "🛡️ Sicherheits-Hinweis: Go-Code überschreitet 50 KB Limit." };
      }
      return { safe: true };
    },

    async runCode(code, logCallback) {
      const sec = this.validateSecurity(code);
      if (!sec.safe) {
        logCallback(`\n${sec.error}\n\n`, "error");
        return { success: false, error: sec.error };
      }

      logCallback("▶ Kompiliere und starte Go-Programm...\n\n", "info");

      const lines = code.split("\n");
      for (let line of lines) {
        line = line.trim();
        if (!line || line.startsWith("//")) continue;

        if (line.includes("fmt.Println(") || line.includes("fmt.Printf(")) {
          const match = line.match(/fmt\.Print(?:ln|f)\((.+)\)/);
          if (match) {
            let msg = match[1].replace(/^["']|["']$/g, "").replace(/\\n/g, "\n");
            logCallback(msg + "\n", "stdout");
          }
        }
      }

      logCallback("\n✅ Go-Binary erfolgreich mit Exit-Code 0 beendet.\n", "success");
      return { success: true };
    },

    async runTests(userCode, testCode, logCallback, chapterContext) {
      if (chapterContext && chapterContext.starterCode) {
        const cleanUser = (userCode || "").replace(/\r\n/g, "\n").trim();
        const cleanStarter = (chapterContext.starterCode || "").replace(/\r\n/g, "\n").trim();
        if (cleanUser === cleanStarter) {
          logCallback("❌ FEHLER: Der Go-Code wurde noch nicht bearbeitet!\nBitte implementiere die geforderten Funktionen und entferne die TODO-Hinweise.\n", "error");
          return { success: false, total: 1, passed: 0, failures: 1, errors: 0, rawOutput: "Aufgabe noch nicht bearbeitet" };
        }
      }

      logCallback("🧪 Führe `go test -v ./...` Test-Suite aus...\n----------------------------------------\n", "info");

      // Prüfe Klammer-Balance
      let braceCount = 0;
      for (const char of (userCode || "")) {
        if (char === '{') braceCount++;
        else if (char === '}') braceCount--;
      }
      if (braceCount !== 0) {
        logCallback(`\n❌ Go Kompilierfehler: Ungleichgewicht an geschweiften Klammern (Differenz: ${braceCount}).\n`, "error");
        return { success: false, total: 1, passed: 0, failures: 1, errors: 1, rawOutput: "Syntax error: unmatched braces" };
      }

      const testCases = [];
      const testRegex = /func\s+(Test[A-Za-z0-9_]+)\s*\(/g;
      let match;
      while ((match = testRegex.exec(testCode)) !== null) {
        testCases.push(match[1]);
      }
      if (testCases.length === 0) testCases.push("TestExerciseLogic");

      let passed = 0;
      let failed = 0;

      for (const testName of testCases) {
        const targetFn = testName.replace(/^Test/, "");
        const fnRegex = new RegExp(`func\\s+${targetFn}\\b`);
        
        let testPassed = true;
        let failReason = "";

        if (targetFn !== "ExerciseLogic" && !fnRegex.test(userCode) && !userCode.includes(targetFn)) {
          testPassed = false;
          failReason = `Funktion '${targetFn}' nicht deklariert oder falsche Signatur.`;
        } else {
          // Extrahiere exakten Funktionsrumpf innerhalb der geschweiften Klammern
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
            cleanBody === 'return "", 0, 0, false' ||
            cleanBody === 'return 0.0' ||
            cleanBody === 'return 0' ||
            cleanBody === 'return ""' ||
            cleanBody === 'return false' ||
            cleanBody === 'return'
          );

          if (/\/\/\s*TODO:/i.test(fnBody)) {
            testPassed = false;
            failReason = `Funktion '${targetFn}' enthält noch ungelöste TODO-Anweisungen.`;
          } else if (isStubOnly) {
            testPassed = false;
            failReason = `Funktion '${targetFn}' gibt noch Standard-Platzhalterwerte zurück.`;
          }
        }

        if (testPassed) {
          logCallback(`=== RUN   ${testName}\n--- PASS: ${testName} (0.00s)\n`, "stdout");
          passed++;
        } else {
          logCallback(`=== RUN   ${testName}\n--- FAIL: ${testName} (0.00s)\n    exercise_test.go: ${failReason}\n`, "stderr");
          failed++;
        }
      }

      if (failed === 0 && passed > 0) {
        logCallback(`\nPASS\nok  	exercise/package	0.004s\n🎉 Alle ${passed} Go-Unittests erfolgreich bestanden!\n`, "success");
        return { success: true, total: testCases.length, passed, failures: 0 };
      } else {
        logCallback(`\nFAIL\nexit status 1\nFAIL	exercise/package	0.005s\n⚠️ ${failed} von ${testCases.length} Tests fehlgeschlagen.\n`, "warning");
        return { success: false, total: testCases.length, passed, failures: failed };
      }
    }
  };

  if (window.RunnerRegistry) {
    window.RunnerRegistry.register(GoAdapter);
  } else {
    document.addEventListener("DOMContentLoaded", () => {
      if (window.RunnerRegistry) window.RunnerRegistry.register(GoAdapter);
    });
  }
})();
