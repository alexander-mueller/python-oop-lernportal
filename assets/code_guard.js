/**
 * 🛡️ PYTHON CODE-GUARD & SICHERHEITS-FILTER 🛡️
 * ============================================
 * Schützt die Online-Lernumgebung vor schädlichem Code, System-Ausbrüchen,
 * DOM/Token-Exfiltration und blockiert gefährliche Module & Builtins.
 */

(function () {
  // Liste verbotener Module und gefährlicher Schlüsselwörter
  const BLOCKED_PATTERNS = [
    {
      pattern: /(?:^|\s)(?:import\s+js|from\s+js\s+import)/m,
      reason: "Zugriff auf das Browser-DOM ('js'-Modul) ist gesperrt."
    },
    {
      pattern: /(?:^|\s)(?:import\s+pyodide|from\s+pyodide\s+import)/m,
      reason: "Zugriff auf interne Pyodide-APIs ist gesperrt."
    },
    {
      pattern: /(?:^|\s)(?:import\s+subprocess|from\s+subprocess\s+import)/m,
      reason: "System-Prozesse ('subprocess') sind in der Web-Lernumgebung deaktiviert."
    },
    {
      pattern: /(?:^|\s)(?:import\s+ctypes|from\s+ctypes\s+import)/m,
      reason: "Low-Level Speicherzugriff ('ctypes') ist nicht erlaubt."
    },
    {
      pattern: /(?:^|\s)(?:import\s+socket|from\s+socket\s+import)/m,
      reason: "Netzwerk-Sockets ('socket') sind im Browser gesperrt."
    },
    {
      pattern: /(?:^|\s)(?:import\s+urllib|from\s+urllib\s+import|import\s+http|from\s+http\s+import)/m,
      reason: "Netzwerkzugriffe ('urllib' / 'http') sind in Aufgaben gesperrt."
    },
    {
      pattern: /__(?:subclasses|globals|builtins|code)__/i,
      reason: "Reflexions-Angriffe auf interne Python-Strukturen sind gesperrt."
    }
  ];

  window.CODE_GUARD = {
    /**
     * Prüft Python-Code vor der Ausführung auf Schadcode-Muster
     * @param {string} code 
     * @returns {{ safe: boolean, error?: string }}
     */
    validate(code) {
      if (!code || typeof code !== "string") {
        return { safe: true };
      }

      // 1. Obergrenze Dateigröße (Max 50.000 Zeichen / ~50 KB)
      if (code.length > 50000) {
        return {
          safe: false,
          error: "🛡️ Sicherheits-Hinweis: Dein Code überschreitet die maximale Größe von 50 KB."
        };
      }

      // 2. Scan auf gefährliche Muster
      for (const item of BLOCKED_PATTERNS) {
        if (item.pattern.test(code)) {
          return {
            safe: false,
            error: `🛡️ Sicherheits-Sperre: ${item.reason}`
          };
        }
      }

      return { safe: true };
    },

    /**
     * Python-Init-Skript für Pyodide, das interne Gefahrenquellen sperrt
     */
    getSandboxBootstrap() {
      return `
import sys

# Sperre Browser-Bridge Module im Pyodide-Interpreter
for dangerous_mod in ['js', 'pyodide', 'pyodide_js', '_socket', 'ctypes']:
    if dangerous_mod in sys.modules:
        del sys.modules[dangerous_mod]
    sys.modules[dangerous_mod] = None

# Eigene Import-Sperre
orig_import = __builtins__.__import__ if hasattr(__builtins__, '__import__') else __import__

def secure_import(name, *args, **kwargs):
    blocked = {'js', 'pyodide', 'subprocess', 'ctypes', '_socket'}
    base_name = name.split('.')[0]
    if base_name in blocked:
        raise ImportError(f"Sicherheits-Sperre: Das Modul '{name}' ist in dieser Lernumgebung deaktiviert.")
    return orig_import(name, *args, **kwargs)

if isinstance(__builtins__, dict):
    __builtins__['__import__'] = secure_import
else:
    __builtins__.__import__ = secure_import
`;
    }
  };
})();
