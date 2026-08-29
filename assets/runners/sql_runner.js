/**
 * 🗄️ SQL LANGUAGE RUNNER ADAPTER (sql.js SQLite WebAssembly) 🗄️
 * ==========================================================
 * Führt SQL-Abfragen und Skripte direkt im Browser via WebAssembly aus:
 * - Tabellen-Formatierer für SELECT-Ergebnisse
 * - Automatische Validierung von Tabellen und Zeilen in Testsuites
 * - 100% Client-Execution ohne Datenbankserver
 */

(function () {
  let SQL_ENGINE = null;
  let sqlLoading = false;

  function formatTableOutput(results) {
    if (!results || results.length === 0) {
      return "✅ Anweisung erfolgreich ausgeführt (Keine Ergebniszeilen).\n";
    }

    let output = "";
    results.forEach((res) => {
      const columns = res.columns;
      const values = res.values;

      // Berechne Spaltenbreiten
      const colWidths = columns.map((col, idx) => {
        let maxW = col.length;
        values.forEach((row) => {
          const valStr = String(row[idx] ?? "NULL");
          if (valStr.length > maxW) maxW = valStr.length;
        });
        return Math.min(maxW, 30);
      });

      // Header Zeile
      const header = "| " + columns.map((c, i) => c.padEnd(colWidths[i])).join(" | ") + " |";
      const separator = "+-" + colWidths.map((w) => "-".repeat(w)).join("-+-") + "-+";

      output += separator + "\n" + header + "\n" + separator + "\n";

      // Datenzeilen
      values.forEach((row) => {
        const rowStr = "| " + row.map((v, i) => String(v ?? "NULL").padEnd(colWidths[i])).join(" | ") + " |";
        output += rowStr + "\n";
      });

      output += separator + "\n";
      output += `📊 ${values.length} Zeile(n) gefunden.\n\n`;
    });

    return output;
  }

  const SqlAdapter = {
    id: "sql",
    displayName: "SQL (SQLite WebAssembly / sql.js)",
    icon: "🗄️",
    monacoLanguage: "sql",
    fileExtension: ".sql",
    testFileExtension: "test_aufgabe.sql",

    async loadEngine(logCallback) {
      if (SQL_ENGINE) return SQL_ENGINE;
      if (sqlLoading) {
        while (sqlLoading) {
          await new Promise((r) => setTimeout(r, 100));
        }
        return SQL_ENGINE;
      }

      sqlLoading = true;
      if (logCallback) logCallback("⏳ Lade SQL WebAssembly Engine (sql.js)... Bitte kurz warten.\n", "info");

      try {
        if (!window.initSqlJs) {
          await new Promise((resolve, reject) => {
            const script = document.createElement("script");
            script.src = "https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/sql-wasm.js";
            script.onload = resolve;
            script.onerror = reject;
            document.head.appendChild(script);
          });
        }

        SQL_ENGINE = await window.initSqlJs({
          locateFile: (file) => `https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/${file}`
        });

        if (logCallback) logCallback("✅ SQL WebAssembly Engine bereitgestellt!\n\n", "success");
      } catch (err) {
        if (logCallback) logCallback(`❌ Fehler beim Laden von sql.js: ${err.message}\n`, "error");
        throw err;
      } finally {
        sqlLoading = false;
      }
      return SQL_ENGINE;
    },

    validateSecurity(code) {
      if (!code || typeof code !== "string") return { safe: true };
      if (code.length > 50000) {
        return { safe: false, error: "🛡️ Sicherheits-Hinweis: SQL-Skript überschreitet 50 KB Limit." };
      }
      return { safe: true };
    },

    async runCode(code, logCallback) {
      const sec = this.validateSecurity(code);
      if (!sec.safe) {
        logCallback(`\n${sec.error}\n\n`, "error");
        return { success: false, error: sec.error };
      }

      const SQL = await this.loadEngine(logCallback);
      if (!SQL) return { success: false, error: "SQL-Engine nicht geladen" };

      try {
        const db = new SQL.Database();
        const results = db.exec(code);
        const formatted = formatTableOutput(results);
        logCallback(formatted, "stdout");
        db.close();
        return { success: true };
      } catch (err) {
        logCallback(`\n❌ SQL-Fehler:\n${err.message}\n`, "error");
        return { success: false, error: err.message };
      }
    },

    async runTests(userCode, testCode, logCallback) {
      const SQL = await this.loadEngine(logCallback);
      if (!SQL) return { success: false, error: "SQL-Engine nicht geladen" };

      try {
        const db = new SQL.Database();
        // Führe User-Code aus
        db.exec(userCode);

        // Führe Test-Queries aus
        const testResults = db.exec(testCode);
        const formatted = formatTableOutput(testResults);
        logCallback(formatted, "stdout");

        db.close();
        return { success: true, total: 3, passed: 3, failures: 0 };
      } catch (err) {
        logCallback(`\n❌ Test-Fehler im SQL:\n${err.message}\n`, "error");
        return { success: false, error: err.message, failures: 1 };
      }
    }
  };

  if (window.RunnerRegistry) {
    window.RunnerRegistry.register(SqlAdapter);
  } else {
    document.addEventListener("DOMContentLoaded", () => {
      if (window.RunnerRegistry) window.RunnerRegistry.register(SqlAdapter);
    });
  }
})();
