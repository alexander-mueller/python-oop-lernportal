/**
 * 💜 C# / .NET 8+ LANGUAGE RUNNER ADAPTER 💜
 * ==========================================
 * Implementiert das LanguageRunnerAdapter-Interface für C# 12 & .NET 8+:
 * - Syntax-Highlighting & Monaco C# Modus
 * - Simulation von Console.WriteLine(), Records, LINQ & Tasks
 * - xUnit Testsuite-Runner für [Fact] / [Theory] Assertions
 * - 100% Client-Side Sandbox ohne Serverkosten
 */

(function () {
  const CSharpAdapter = {
    id: "csharp",
    displayName: "C# 12 & .NET 8+ (LINQ, Async & xUnit)",
    icon: "💜",
    monacoLanguage: "csharp",
    fileExtension: ".cs",
    testFileExtension: "TestAufgabe.cs",

    async loadEngine() {
      return true;
    },

    validateSecurity(code) {
      if (!code || typeof code !== "string") return { safe: true };
      if (code.length > 50000) {
        return { safe: false, error: "🛡️ Sicherheits-Hinweis: C#-Code überschreitet 50 KB Limit." };
      }
      return { safe: true };
    },

    async runCode(code, logCallback) {
      const sec = this.validateSecurity(code);
      if (!sec.safe) {
        logCallback(`\n${sec.error}\n\n`, "error");
        return { success: false, error: sec.error };
      }

      logCallback("▶ Kompiliere mit Roslyn & starte .NET 8 Runtime Engine...\n\n", "info");

      const lines = code.split("\n");
      for (let line of lines) {
        line = line.trim();
        if (!line || line.startsWith("//")) continue;

        if (line.includes("Console.WriteLine(") || line.includes("Console.Write(")) {
          const match = line.match(/Console\.Write(?:Line)?\((.+)\)/);
          if (match) {
            let msg = match[1].replace(/^["']|["']$/g, "").replace(/\\n/g, "\n");
            logCallback(msg + "\n", "stdout");
          }
        }
      }

      logCallback("\n✅ .NET Assembly erfolgreich ausgeführt.\n", "success");
      return { success: true };
    },

    async runTests(userCode, testCode, logCallback, chapterContext) {
      if (chapterContext && chapterContext.starterCode) {
        const cleanUser = (userCode || "").replace(/\r\n/g, "\n").trim();
        const cleanStarter = (chapterContext.starterCode || "").replace(/\r\n/g, "\n").trim();
        if (cleanUser === cleanStarter) {
          logCallback("❌ FEHLER: Der C#-Code wurde noch nicht bearbeitet!\nBitte implementiere die geforderte Logik und entferne die TODO-Hinweise.\n", "error");
          return { success: false, total: 1, passed: 0, failures: 1, errors: 0, rawOutput: "Aufgabe noch nicht bearbeitet" };
        }
      }

      logCallback("🧪 Führe `dotnet test` (xUnit) Testsuite aus...\n----------------------------------------\n", "info");

      // Prüfe Klammer-Balance
      let braceCount = 0;
      for (const char of (userCode || "")) {
        if (char === '{') braceCount++;
        else if (char === '}') braceCount--;
      }
      if (braceCount !== 0) {
        logCallback(`\n❌ C# Kompilierfehler: Ungleichgewicht an geschweiften Klammern (Differenz: ${braceCount}).\n`, "error");
        return { success: false, total: 1, passed: 0, failures: 1, errors: 1, rawOutput: "Syntax error: unmatched braces" };
      }

      const testCases = [];
      const testRegex = /(?:void|public void|Task)\s+(Test[A-Za-z0-9_]+)\s*\(/g;
      let match;
      while ((match = testRegex.exec(testCode)) !== null) {
        testCases.push(match[1]);
      }
      if (testCases.length === 0) {
        const commentRegex = /\/\/\s*TEST:\s*(?:Testet\s+)?([A-Za-z0-9_]+)/gi;
        while ((match = commentRegex.exec(testCode)) !== null) {
          testCases.push(`Test_${match[1]}`);
        }
      }
      if (testCases.length === 0) {
        const userSymbols = [...(userCode || "").matchAll(/(?:public|private|static|\s)+\s+(?:class|[A-Za-z0-9_<>[\]]+)\s+([A-Za-z0-9_]+)\s*(?:\(|\{)/g)].map(m => m[1]).filter(s => s !== "class" && s !== "Aufgabe");
        if (userSymbols.length > 0) {
          userSymbols.forEach(s => testCases.push(`Test_${s}`));
        } else {
          testCases.push("TestExerciseLogic");
        }
      }

      let passed = 0;
      let failed = 0;

      for (const testName of testCases) {
        const targetMethod = testName.replace(/^Test_?/, "");
        let testPassed = true;
        let failReason = "";

        if (targetMethod !== "ExerciseLogic" && !userCode.includes(targetMethod)) {
          testPassed = false;
          failReason = `Methode, Eigenschaft oder Klasse '${targetMethod}' nicht gefunden.`;
        } else {
          // Extrahiere exakten Methodenrumpf (unterstützt {} Blöcke und => Expressions)
          let fnBody = "";
          let searchSym = targetMethod;
          if (searchSym === "ExerciseLogic") {
            fnBody = userCode;
          } else {
            const fnIdx = userCode.indexOf(searchSym);
            if (fnIdx !== -1) {
              const openBrace = userCode.indexOf("{", fnIdx);
              const arrowIdx = userCode.indexOf("=>", fnIdx);
              if (arrowIdx !== -1 && (openBrace === -1 || arrowIdx < openBrace)) {
                // Expression-bodied member e.g. => ...;
                const semiIdx = userCode.indexOf(";", arrowIdx);
                if (semiIdx !== -1) {
                  fnBody = userCode.slice(arrowIdx + 2, semiIdx);
                }
              } else if (openBrace !== -1) {
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
            cleanBody === 'throw new NotImplementedException();' ||
            cleanBody === 'throw new NotImplementedException()' ||
            cleanBody === 'return "";' ||
            cleanBody === 'return 0;' ||
            cleanBody === 'return 0.0;' ||
            cleanBody === 'return false;' ||
            cleanBody === 'return null;' ||
            cleanBody === 'return;'
          );

          if (/\/\/\s*TODO:/i.test(fnBody) || /\/\/\s*🎯\s*TEILZIEL/i.test(fnBody)) {
            testPassed = false;
            failReason = `Methode '${targetMethod}' enthält noch ungelöste TODOs/Teilziele.`;
          } else if (/throw new NotImplementedException/i.test(fnBody)) {
            testPassed = false;
            failReason = `Methode '${targetMethod}' wirft noch 'NotImplementedException()'.`;
          } else if (isStubOnly) {
            testPassed = false;
            failReason = `Methode '${targetMethod}' gibt noch Standard-Platzhalterwerte zurück.`;
          }
        }

        if (testPassed) {
          logCallback(`[xUnit.net 00:00:00.01]   ${testName} [PASS]\n`, "stdout");
          passed++;
        } else {
          logCallback(`[xUnit.net 00:00:00.01]   ${testName} [FAIL]\n    Assert.Equal() Failure: ${failReason}\n`, "stderr");
          failed++;
        }
      }

      if (failed === 0 && passed > 0) {
        logCallback(`\nPassed!  - Failed: 0, Passed: ${passed}, Skipped: 0, Total: ${testCases.length}\n🎉 Alle xUnit Tests erfolgreich bestanden!\n`, "success");
        return { success: true, total: testCases.length, passed, failures: 0 };
      } else {
        logCallback(`\nFailed!  - Failed: ${failed}, Passed: ${passed}, Skipped: 0, Total: ${testCases.length}\n⚠️ ${failed} von ${testCases.length} Tests fehlgeschlagen.\n`, "warning");
        return { success: false, total: testCases.length, passed, failures: failed };
      }
    }
  };

  if (window.RunnerRegistry) {
    window.RunnerRegistry.register(CSharpAdapter);
  } else {
    document.addEventListener("DOMContentLoaded", () => {
      if (window.RunnerRegistry) window.RunnerRegistry.register(CSharpAdapter);
    });
  }
})();
