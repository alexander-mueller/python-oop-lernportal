/**
 * ⚡ GEHÄRTETE MONACO WEB-IDE & PYODIDE RUNNER ENGINE ⚡
 * =====================================================
 * Interaktive Entwicklungsumgebung mit:
 * - Integriertem CODE_GUARD Sicherheits-Filter (Schadcode- & Exploit-Sperre)
 * - Monaco Editor (VS Code Engine mit Autocomplete & Syntax-Highlighting)
 * - Tastatur-Shortcuts: Strg+Enter (Run), Strg+Shift+Enter (Test), Strg+S (Save)
 * - In-Browser Pyodide WebAssembly Python Runner (95% Client-Execution)
 * - Endlosschleifen-Timeout-Schutz (5000ms)
 * - Reaktivität mit Fehler-Dolmetscher & Gamification
 */

(function () {
  let monacoEditor = null;
  let pyodideInstance = null;
  let pyodideLoading = false;
  let currentChapterData = null;
  let autoSaveTimeout = null;

  function escapeHtml(text) {
    if (!text) return "";
    return String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  // 1. Initialisiere Monaco Editor via CDN
  function initMonacoEditor(initialCode = "") {
    const editorContainer = document.getElementById("monaco-editor-container");
    if (!editorContainer) return;

    if (window.monaco) {
      createMonacoInstance(initialCode);
      return;
    }

    const loaderScript = document.createElement("script");
    loaderScript.src = "https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.45.0/min/vs/loader.min.js";
    loaderScript.onload = () => {
      window.require.config({
        paths: { vs: "https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.45.0/min/vs" }
      });
      window.require(["vs/editor/editor.main"], () => {
        createMonacoInstance(initialCode);
      });
    };
    loaderScript.onerror = () => {
      editorContainer.innerHTML = `<textarea id="fallback-code-editor" style="width: 100%; height: 100%; background: #0b0f19; color: #f8fafc; font-family: monospace; font-size: 14px; padding: 14px; border: none; outline: none;">${escapeHtml(initialCode)}</textarea>`;
    };
    document.head.appendChild(loaderScript);
  }

  function createMonacoInstance(initialCode) {
    const editorContainer = document.getElementById("monaco-editor-container");
    if (!editorContainer) return;
    editorContainer.innerHTML = "";

    monacoEditor = window.monaco.editor.create(editorContainer, {
      value: initialCode,
      language: "python",
      theme: "vs-dark",
      fontSize: 14,
      fontFamily: "'JetBrains Mono', 'Fira Code', Consolas, monospace",
      automaticLayout: true,
      minimap: { enabled: false },
      scrollBeyondLastLine: false,
      tabSize: 4,
      insertSpaces: true,
      lineNumbers: "on",
      bracketPairColorization: { enabled: true }
    });

    monacoEditor.onDidChangeModelContent(() => {
      triggerAutoSave();
    });

    monacoEditor.addCommand(window.monaco.KeyMod.CtrlCmd | window.monaco.KeyCode.Enter, () => {
      runCode();
    });
    monacoEditor.addCommand(window.monaco.KeyMod.CtrlCmd | window.monaco.KeyMod.Shift | window.monaco.KeyCode.Enter, () => {
      runTests();
    });
    monacoEditor.addCommand(window.monaco.KeyMod.CtrlCmd | window.monaco.KeyCode.KeyS, () => {
      saveProgressDraft();
    });
  }

  window.addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === "s") {
      e.preventDefault();
      saveProgressDraft();
    }
  });

  // 2. Pyodide WebAssembly Initialisierung mit Sandbox-Bootstrap
  async function getPyodide() {
    if (pyodideInstance) return pyodideInstance;
    if (pyodideLoading) {
      while (pyodideLoading) {
        await new Promise((r) => setTimeout(r, 100));
      }
      return pyodideInstance;
    }

    pyodideLoading = true;
    logToTerminal("⏳ Initialisiere geschützte Python Sandbox Engine... Bitte kurz warten.\n", "info");

    try {
      if (!window.loadPyodide) {
        await new Promise((resolve, reject) => {
          const script = document.createElement("script");
          script.src = "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js";
          script.onload = resolve;
          script.onerror = reject;
          document.head.appendChild(script);
        });
      }

      pyodideInstance = await window.loadPyodide({
        stdout: (text) => logToTerminal(text + "\n", "stdout"),
        stderr: (text) => logToTerminal(text + "\n", "stderr")
      });

      // Sandbox-Härtung im Pyodide-Interpreter aktivieren
      if (window.CODE_GUARD && window.CODE_GUARD.getSandboxBootstrap) {
        await pyodideInstance.runPythonAsync(window.CODE_GUARD.getSandboxBootstrap());
      }

      logToTerminal("✅ Geschützte Python WebAssembly Sandbox bereitgestellt!\n\n", "success");
    } catch (err) {
      logToTerminal(`❌ Fehler beim Laden der Sandbox: ${err.message}\n`, "error");
    } finally {
      pyodideLoading = false;
    }
    return pyodideInstance;
  }

  // 3. Code-Ausführung mit Sicherheitsprüfung & Timeout
  async function runCode() {
    const code = getEditorCode();
    clearTerminal();

    // Layer 1: Code-Guard Sicherheits-Prüfung
    if (window.CODE_GUARD) {
      const check = window.CODE_GUARD.validate(code);
      if (!check.safe) {
        logToTerminal(`\n${check.error}\n\n`, "error");
        return;
      }
    }

    logToTerminal("▶ Starte Python-Skript (Strg+Enter)...\n----------------------------------------\n", "info");

    const py = await getPyodide();
    if (!py) return;

    try {
      let timeoutHandle;
      const timeoutPromise = new Promise((_, reject) => {
        timeoutHandle = setTimeout(() => {
          reject(new Error("Zeitüberschreitung: Dein Code lief länger als 5 Sekunden (Endlosschleife vermutet)."));
        }, 5000);
      });

      const execPromise = py.runPythonAsync(code);
      await Promise.race([execPromise, timeoutPromise]);
      clearTimeout(timeoutHandle);

      logToTerminal("\n----------------------------------------\n✨ Skript erfolgreich ausgeführt!\n", "success");
    } catch (err) {
      logToTerminal(`\n❌ Ausführungsfehler:\n${err.message}\n`, "error");
      suggestErrorInterpreter(err.message);
    }
  }

  // 4. Unittest-Ausführung mit Sicherheitsprüfung
  async function runTests() {
    if (!currentChapterData || !currentChapterData.testCode) {
      logToTerminal("❌ Keine Unittests für dieses Kapitel gefunden.\n", "error");
      return;
    }

    const userCode = getEditorCode();
    clearTerminal();

    // Layer 1: Code-Guard Sicherheits-Prüfung
    if (window.CODE_GUARD) {
      const check = window.CODE_GUARD.validate(userCode);
      if (!check.safe) {
        logToTerminal(`\n${check.error}\n\n`, "error");
        return;
      }
    }

    logToTerminal("🧪 Führe automatisierte Unittests aus (Strg+Shift+Enter)...\n----------------------------------------\n", "info");

    const py = await getPyodide();
    if (!py) return;

    try {
      py.FS.writeFile("aufgabe.py", userCode);

      const testRunnerScript = `
import unittest, io, sys
from unittest import TextTestRunner

for mod in list(sys.modules.keys()):
    if mod in ('aufgabe', 'test_aufgabe'):
        del sys.modules[mod]

import aufgabe

${currentChapterData.testCode}

suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
stream = io.StringIO()
runner = TextTestRunner(stream=stream, verbosity=2)
result = runner.run(suite)

output_text = stream.getvalue()
success = result.wasSuccessful()
total_runs = result.testsRun
failures = len(result.failures)
errors = len(result.errors)
(success, total_runs, failures, errors, output_text)
`;

      let timeoutHandle;
      const timeoutPromise = new Promise((_, reject) => {
        timeoutHandle = setTimeout(() => {
          reject(new Error("Zeitüberschreitung: Unittest lief länger als 6 Sekunden."));
        }, 6000);
      });

      const [isSuccess, totalRuns, fails, errs, outputText] = await Promise.race([
        py.runPythonAsync(testRunnerScript),
        timeoutPromise
      ]);
      clearTimeout(timeoutHandle);

      logToTerminal(outputText + "\n", "stdout");

      if (isSuccess) {
        logToTerminal(`\n🎉 HERVORRAGEND! Alle ${totalRuns} Tests erfolgreich bestanden! (+100 XP)\n`, "success");
        triggerSuccessCelebration();
        recordChapterSolved();
      } else {
        logToTerminal(`\n⚠️ ${fails + errs} von ${totalRuns} Tests fehlgeschlagen. Überarbeite deinen Code!\n`, "warning");
        suggestErrorInterpreter(outputText);
      }
    } catch (err) {
      logToTerminal(`\n❌ Fehler beim Ausführen der Testsuite:\n${err.message}\n`, "error");
      suggestErrorInterpreter(err.message);
    }
  }

  // 5. Hilfsfunktionen
  function getEditorCode() {
    if (monacoEditor) {
      return monacoEditor.getValue();
    }
    const fallback = document.getElementById("fallback-code-editor");
    return fallback ? fallback.value : "";
  }

  function setEditorCode(code) {
    if (monacoEditor) {
      monacoEditor.setValue(code);
    } else {
      const fallback = document.getElementById("fallback-code-editor");
      if (fallback) fallback.value = code;
    }
  }

  function logToTerminal(text, type = "stdout") {
    const term = document.getElementById("workspace-terminal-output");
    if (!term) return;

    const span = document.createElement("span");
    span.className = `term-line term-${type}`;
    span.innerText = text;
    term.appendChild(span);
    term.scrollTop = term.scrollHeight;
  }

  function clearTerminal() {
    const term = document.getElementById("workspace-terminal-output");
    if (term) term.innerHTML = "";
  }

  function triggerAutoSave() {
    clearTimeout(autoSaveTimeout);
    autoSaveTimeout = setTimeout(() => {
      saveProgressDraft();
    }, 1500);
  }

  async function saveProgressDraft() {
    if (!currentChapterData || !currentChapterData.chapterId) return;
    const code = getEditorCode();

    localStorage.setItem(`code_draft_${currentChapterData.chapterId}`, code);

    const token = localStorage.getItem("auth_token");
    if (token) {
      try {
        await fetch("/api/progress/save", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`
          },
          body: JSON.stringify({
            chapter_id: currentChapterData.chapterId,
            code_draft: code
          })
        });
      } catch (e) {}
    }

    const saveBadge = document.getElementById("editor-save-indicator");
    if (saveBadge) {
      saveBadge.innerText = "💾 Gespeichert";
      saveBadge.style.opacity = "1";
      setTimeout(() => {
        saveBadge.style.opacity = "0.5";
      }, 2000);
    }
  }

  async function recordChapterSolved() {
    if (!currentChapterData || !currentChapterData.chapterId) return;

    if (window.addXP) {
      window.addXP(100, currentChapterData.chapterId);
    }

    const token = localStorage.getItem("auth_token");
    if (token) {
      try {
        await fetch("/api/progress/solve", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`
          },
          body: JSON.stringify({
            chapter_id: currentChapterData.chapterId,
            xp_reward: 100
          })
        });
      } catch (e) {}
    }
  }

  function triggerSuccessCelebration() {
    const banner = document.getElementById("success-modal-banner");
    if (banner) {
      banner.style.display = "flex";
    }
  }

  function suggestErrorInterpreter(traceback) {
    const errorTab = document.getElementById("tab-btn-interpreter");
    const errorInput = document.getElementById("workspace-error-input");
    if (errorInput) {
      errorInput.value = traceback;
    }
    if (errorTab) {
      errorTab.style.borderColor = "var(--danger)";
      errorTab.innerHTML = "🩺 Fehler-Dolmetscher ⚠️";
    }
    if (window.interpretWorkspaceError) {
      window.interpretWorkspaceError();
    }
  }

  // 6. Init Workspace Controller
  window.initWorkspace = function (chapterData) {
    currentChapterData = chapterData;

    const savedDraft = localStorage.getItem(`code_draft_${chapterData.chapterId}`);
    const initialCode = savedDraft || chapterData.starterCode || "";

    initMonacoEditor(initialCode);

    document.getElementById("btn-run-code")?.addEventListener("click", runCode);
    document.getElementById("btn-run-tests")?.addEventListener("click", runTests);
    document.getElementById("btn-save-code")?.addEventListener("click", saveProgressDraft);
    document.getElementById("btn-clear-terminal")?.addEventListener("click", clearTerminal);
    document.getElementById("btn-reset-code")?.addEventListener("click", () => {
      if (confirm("Möchtest du deinen Code wirklich auf den Original-Startercode zurücksetzen?")) {
        setEditorCode(chapterData.starterCode || "");
      }
    });
  };
})();
