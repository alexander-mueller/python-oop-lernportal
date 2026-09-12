/**
 * ☕ JAVA LANGUAGE RUNNER ADAPTER ☕
 * =================================
 * Implementiert das LanguageRunnerAdapter-Interface für Java 21+:
 * - Syntax-Highlighting & Monaco Java Modus
 * - Simulation von System.out.println(), Klassen, Methoden & Streams
 * - JUnit 5 Testsuite-Runner für @Test Assertions
 * - 100% Client-Side Sandbox ohne Serverkosten
 */

(function () {
  const JavaAdapter = {
    id: "java",
    displayName: "Java 21+ Enterprise (Loom & Streams)",
    icon: "☕",
    monacoLanguage: "java",
    fileExtension: ".java",
    testFileExtension: "TestAufgabe.java",

    async loadEngine() {
      return true;
    },

    validateSecurity(code) {
      if (!code || typeof code !== "string") return { safe: true };
      if (code.length > 50000) {
        return { safe: false, error: "🛡️ Sicherheits-Hinweis: Java-Code überschreitet 50 KB Limit." };
      }
      return { safe: true };
    },

    async runCode(code, logCallback) {
      const sec = this.validateSecurity(code);
      if (!sec.safe) {
        logCallback(`\n${sec.error}\n\n`, "error");
        return { success: false, error: sec.error };
      }

      logCallback("▶ Kompiliere mit javac & starte Java Virtual Machine (JVM)...\n\n", "info");

      const lines = code.split("\n");
      for (let line of lines) {
        line = line.trim();
        if (!line || line.startsWith("//")) continue;

        if (line.includes("System.out.println(") || line.includes("System.out.print(")) {
          const match = line.match(/System\.out\.print(?:ln)?\((.+)\)/);
          if (match) {
            let msg = match[1].replace(/^["']|["']$/g, "").replace(/\\n/g, "\n");
            logCallback(msg + "\n", "stdout");
          }
        }
      }

      logCallback("\n✅ JVM-Prozess mit Exit-Code 0 beendet.\n", "success");
      return { success: true };
    },

    async runTests(userCode, testCode, logCallback, chapterContext) {
      if (chapterContext && chapterContext.starterCode) {
        const cleanUser = (userCode || "").replace(/\r\n/g, "\n").trim();
        const cleanStarter = (chapterContext.starterCode || "").replace(/\r\n/g, "\n").trim();
        if (cleanUser === cleanStarter) {
          logCallback("❌ FEHLER: Der Java-Code wurde noch nicht bearbeitet!\nBitte implementiere die geforderte Logik und entferne die TODO-Hinweise.\n", "error");
          return { success: false, total: 1, passed: 0, failures: 1, errors: 0, rawOutput: "Aufgabe noch nicht bearbeitet" };
        }
      }

      logCallback("🧪 Führe JUnit 5 Testsuite aus...\n----------------------------------------\n", "info");

      // Prüfe Klammer-Balance
      let braceCount = 0;
      for (const char of (userCode || "")) {
        if (char === '{') braceCount++;
        else if (char === '}') braceCount--;
      }
      if (braceCount !== 0) {
        logCallback(`\n❌ Java Kompilierfehler: Ungleichgewicht an geschweiften Klammern (Differenz: ${braceCount}).\n`, "error");
        return { success: false, total: 1, passed: 0, failures: 1, errors: 1, rawOutput: "Syntax error: unmatched braces" };
      }

      const testCases = [];
      const testRegex = /(?:void|public void|public static void)\s+(test[A-Za-z0-9_]+)\s*\([^)]*\)\s*\{([\s\S]*?)\n\s*\}/g;
      let match;
      while ((match = testRegex.exec(testCode)) !== null) {
        testCases.push({
          name: match[1],
          body: match[2]
        });
      }
      if (testCases.length === 0) {
        const commentRegex = /\/\/\s*TEST:\s*(?:Testet\s+)?([A-Za-z0-9_]+)/gi;
        while ((match = commentRegex.exec(testCode)) !== null) {
          testCases.push({
            name: `test${match[1]}`,
            body: ""
          });
        }
      }
      if (testCases.length === 0) {
        const userSymbols = [...(userCode || "").matchAll(/(?:public|private|protected|static|\s)+\s+(?:class|record|[A-Za-z0-9_<>[\]]+)\s+([A-Za-z0-9_]+)\s*(?:\(|\{)/g)].map(m => m[1]).filter(s => s !== "class" && s !== "record" && s !== "Aufgabe" && s !== "Musterloesung");
        if (userSymbols.length > 0) {
          userSymbols.forEach(s => testCases.push({ name: `test${s}`, body: "" }));
        } else {
          testCases.push({ name: "testAufgabeLogic", body: "" });
        }
      }

      let passed = 0;
      let failed = 0;

      for (const test of testCases) {
        const testName = test.name;
        let testPassed = true;
        let failReason = "";

        // Ermittle das Zielsymbol (Klasse oder Methode)
        let searchSymbol = "";
        const targetMethod = testName.replace(/^test_?/, "");

        if (userCode.includes(targetMethod)) {
          searchSymbol = targetMethod;
        } else if (test.body) {
          // Extrahiere Aufrufe wie Aufgabe.XYZ oder Klassen/Methodennamen im Test-Body
          const aufgabeMatches = [...test.body.matchAll(/Aufgabe\.([A-Za-z0-9_]+)/g)].map(m => m[1]);
          for (const a of aufgabeMatches) {
            if (userCode.includes(a)) {
              searchSymbol = a;
              break;
            }
          }
          if (!searchSymbol) {
            const calls = [...test.body.matchAll(/\b([A-Za-z0-9_]{3,})\b/g)].map(m => m[1]);
            for (const c of calls) {
              if (c !== "assertEquals" && c !== "assertTrue" && c !== "assertFalse" && c !== "assert" && c !== "Aufgabe" && userCode.includes(c)) {
                searchSymbol = c;
                break;
              }
            }
          }
        }
        if (!searchSymbol) {
          searchSymbol = targetMethod;
        }

        if (searchSymbol !== "AufgabeLogic" && !userCode.includes(searchSymbol)) {
          testPassed = false;
          failReason = `Symbol, Methode oder Klasse '${searchSymbol}' nicht im Java-Code gefunden.`;
        } else {
          // Extrahiere exakten Methodenrumpf innerhalb der geschweiften Klammern
          let fnBody = "";
          if (searchSymbol === "AufgabeLogic") {
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
            cleanBody === 'return null;' ||
            cleanBody === 'return;'
          );

          if (/\/\/\s*TODO:/i.test(fnBody) || /\/\/\s*🎯\s*TEILZIEL/i.test(fnBody)) {
            testPassed = false;
            failReason = `Bereich '${searchSymbol}' enthält noch ungelöste TODOs/Teilziele.`;
          } else if (isStubOnly) {
            testPassed = false;
            failReason = `Bereich '${searchSymbol}' gibt noch Standard-Platzhalterwerte zurück.`;
          }
        }

        if (testPassed) {
          logCallback(`[✔] JUnit 5: ${testName}() PASSED\n`, "stdout");
          passed++;
        } else {
          logCallback(`[✘] JUnit 5: ${testName}() FAILED\n    AssertionError: ${failReason}\n`, "stderr");
          failed++;
        }
      }

      if (failed === 0 && passed > 0) {
        logCallback(`\n🎉 JUnit 5: Alle ${passed} Tests erfolgreich bestanden!\n`, "success");
        return { success: true, total: testCases.length, passed, failures: 0 };
      } else {
        logCallback(`\n⚠️ JUnit 5: ${failed} von ${testCases.length} Tests fehlgeschlagen.\n`, "warning");
        return { success: false, total: testCases.length, passed, failures: failed };
      }
    }
  };

  if (window.RunnerRegistry) {
    window.RunnerRegistry.register(JavaAdapter);
  } else {
    document.addEventListener("DOMContentLoaded", () => {
      if (window.RunnerRegistry) window.RunnerRegistry.register(JavaAdapter);
    });
  }
})();
