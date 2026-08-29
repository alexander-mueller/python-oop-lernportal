/**
 * ⚡ ZERO-SETUP IN-BROWSER PYTHON RUNNER (Pyodide / WebAssembly) ⚡
 * =================================================================
 * Ermöglicht das direkte Ausführen von Python-Code im Browser mit 1 Klick!
 * Funktioniert mit Pyodide (WebAssembly) oder sicherem lokalem Interpreter.
 */

(function () {
  let pyodideInstance = null;
  let isPyodideLoading = false;

  async function getPyodide() {
    if (pyodideInstance) return pyodideInstance;
    if (isPyodideLoading) {
      while (isPyodideLoading) {
        await new Promise(r => setTimeout(r, 100));
      }
      return pyodideInstance;
    }

    isPyodideLoading = true;
    try {
      if (typeof loadPyodide === "undefined") {
        // Dynamisch Pyodide-Script laden
        await new Promise((resolve, reject) => {
          const script = document.createElement("script");
          script.src = "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js";
          script.onload = resolve;
          script.onerror = reject;
          document.head.appendChild(script);
        });
      }
      pyodideInstance = await loadPyodide({
        stdout: (text) => appendOutput(text, "stdout"),
        stderr: (text) => appendOutput(text, "stderr")
      });
      isPyodideLoading = false;
      return pyodideInstance;
    } catch (e) {
      isPyodideLoading = false;
      console.warn("Pyodide CDN nicht erreichbar (Offline-Modus aktiv):", e);
      return null;
    }
  }

  let activeOutputEl = null;

  function appendOutput(text, type = "stdout") {
    if (!activeOutputEl) return;
    const span = document.createElement("div");
    span.style.color = type === "stderr" ? "#f87171" : "#a7f3d0";
    span.textContent = text;
    activeOutputEl.appendChild(span);
    activeOutputEl.scrollTop = activeOutputEl.scrollHeight;
  }

  window.initCodeRunnerWidget = function (containerId, initialCode = "") {
    const container = document.getElementById(containerId);
    if (!container) return;

    container.innerHTML = `
      <div class="card" style="border-left: 5px solid var(--purple); background: #0f172a; color: #f8fafc;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; flex-wrap: wrap; gap: 10px;">
          <h2 style="color: #c084fc; margin: 0; border: none; padding: 0;">⚡ Live Python-Playground (Direkt im Browser)</h2>
          <span style="font-size: 0.8rem; background: rgba(192, 132, 252, 0.2); color: #e9d5ff; padding: 3px 10px; border-radius: 12px;">WebAssembly Runner</span>
        </div>
        <p style="color: #94a3b8; font-size: 0.9rem; margin-bottom: 12px;">
          Teste deinen Code oder experimentiere mit Beispielen direkt hier im Browser – ohne Terminal!
        </p>

        <textarea id="runner-editor-${containerId}" style="width: 100%; height: 160px; background: #1e293b; color: #f8fafc; font-family: var(--font-mono); font-size: 0.92rem; padding: 12px; border-radius: var(--radius-sm); border: 1px solid rgba(255,255,255,0.1); resize: vertical;">${initialCode}</textarea>

        <div style="display: flex; gap: 10px; margin-top: 10px; flex-wrap: wrap;">
          <button id="runner-btn-${containerId}" class="btn" style="background: linear-gradient(135deg, #9333ea 0%, #a855f7 100%);">
            ▶️ Code ausführen
          </button>
          <button id="runner-clear-${containerId}" class="btn btn-secondary" style="background: rgba(255,255,255,0.1); color: white; border: 1px solid rgba(255,255,255,0.2);">
            🗑️ Ausgabe leeren
          </button>
        </div>

        <div style="margin-top: 15px;">
          <div style="font-size: 0.8rem; color: #94a3b8; margin-bottom: 4px; text-transform: uppercase; letter-spacing: 0.5px;">Terminal-Ausgabe:</div>
          <div id="runner-output-${containerId}" style="background: #020617; border: 1px solid rgba(255,255,255,0.1); border-radius: var(--radius-sm); padding: 12px; font-family: var(--font-mono); font-size: 0.88rem; min-height: 80px; max-height: 220px; overflow-y: auto; color: #38bdf8;">
            <div style="color: #64748b; font-style: italic;">Bereit. Klicke auf '▶️ Code ausführen'...</div>
          </div>
        </div>
      </div>
    `;

    const editor = document.getElementById(`runner-editor-${containerId}`);
    const btn = document.getElementById(`runner-btn-${containerId}`);
    const clearBtn = document.getElementById(`runner-clear-${containerId}`);
    const output = document.getElementById(`runner-output-${containerId}`);

    clearBtn.addEventListener("click", () => {
      output.innerHTML = "<div style='color: #64748b; font-style: italic;'>Ausgabe geleert.</div>";
    });

    btn.addEventListener("click", async () => {
      output.innerHTML = "<div style='color: #fbbf24;'>⏳ Führe Code aus...</div>";
      activeOutputEl = output;
      
      const code = editor.value;
      const pyodide = await getPyodide();

      if (pyodide) {
        try {
          output.innerHTML = "";
          await pyodide.runPythonAsync(code);
          if (output.innerHTML === "") {
            output.innerHTML = "<div style='color: #10b981;'>✅ Programm fehlerfrei beendet (Keine Ausgabe).</div>";
          }
        } catch (err) {
          output.innerHTML = `<div style='color: #ef4444;'>💥 Traceback:\n${err.message}</div>`;
        }
      } else {
        // Fallback wenn offline ohne CDN
        output.innerHTML = "<div style='color: #fbbf24;'>💡 Hinweis: Pyodide CDN ist offline. Bitte führe das Skript lokal im Terminal aus mit: <code>python3 aufgabe.py</code>!</div>";
      }
    });
  };

  // Automatische Initialisierung, falls Container auf der Seite vorhanden
  document.addEventListener("DOMContentLoaded", () => {
    const defaultPlayground = document.getElementById("python-live-playground");
    if (defaultPlayground) {
      window.initCodeRunnerWidget(
        "python-live-playground",
        "# Probiere hier beliebigen Python-Code aus!\nprint('Hallo aus dem interaktiven Python-Lernportal! 🚀')\n\nfor i in range(1, 4):\n    print(f'Schritt {i}: Python lernen macht Spaß!')"
      );
    }
  });
})();
