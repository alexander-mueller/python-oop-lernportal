/**
 * ⚡ MONACO WEB-IDE & PYODIDE TEST-RUNNER ENGINE ⚡
 * =================================================
 * Interaktive Split-Screen Entwicklungsumgebung mit:
 * - Monaco Editor (VS Code Engine mit Autocomplete & Syntax-Highlighting)
 * - In-Browser Pyodide WebAssembly Python Runner (95% Client-Execution)
 * - Automatischer Test-Auswertung mit XP-Vergabe
 * - Cloud Auto-Save
 */

(function () {
  let monacoEditor = null;
  let pyodideInstance = null;
  let pyodideLoading = false;
  let currentChapterData = null;
  let autoSaveTimeout = null;

  // 1. Initialisiere Monaco Editor via CDN
  function initMonacoEditor(initialCode = "") {
    const editorContainer = document.getElementById("monaco-editor-container");
    if (!editorContainer) return;

    if (window.monaco) {
      createMonacoInstance(initialCode);
      return;
    }

    // Monaco CDN Loader
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
      // Fallback: Einfache Textarea falls CDN offline
      editorContainer.innerHTML = `<textarea id="fallback-code-editor" style="width: 100%; height: 100%; background: #0b0f19; color: #f8fafc; font-family: monospace; font-size: 14px; padding: 14px; border: none; outline: none;">${initialCode}</textarea>`;
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

    // Auto-Save Trigger beim Tippen
    monacoEditor.onDidChangeModelContent(() => {
      triggerAutoSave();
    });
  }

  // 2. Pyodide WebAssembly Initialisierung
  async function getPyodide() {
    if (pyodideInstance) return pyodideInstance;
    if (pyodideLoading) {
      while (pyodideLoading) {
        await new Promise((r) => setTimeout(r, 100));
      }
      return pyodideInstance;
    }

    pyodideLoading = true;
    logToTerminal("⏳ Lade Python WebAssembly Engine (Pyodide)... Bitte kurz warten.\n", "info");

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

      logToTerminal("✅ Python WebAssembly erfolgreich bereitgestellt!\n\n", "success");
    } catch (err) {
      logToTerminal(`❌ Fehler beim Laden von Pyodide: ${err.message}\n`, "error");
    } finally {
      pyodideLoading = false;
    }
    return pyodideInstance;
  }

  // 3. Code-Ausführung (Run)
  async function runCode() {
    const code = getEditorCode();
    clearTerminal();
    logToTerminal("▶ Starte Python-Skript...\n----------------------------------------\n", "info");

    const py = await getPyodide();
    if (!py) return;

    try {
      await py.runPythonAsync(code);
      logToTerminal("\n----------------------------------------\n✨ Skript erfolgreich ausgeführt!\n", "success");
    } catch (err) {
      logToTerminal(`\n❌ Ausführungsfehler:\n${err.message}\n`, "error");
      suggestErrorInterpreter(err.message);
    }
  }

  // 4. Unittest-Ausführung (Test Runner)
  async function runTests() {
    if (!currentChapterData || !currentChapterData.testCode) {
      logToTerminal("❌ Keine Unittests für dieses Kapitel gefunden.\n", "error");
      return;
    }

    const userCode = getEditorCode();
    clearTerminal();
    logToTerminal("🧪 Führe automatisierte Unittests aus...\n----------------------------------------\n", "info");

    const py = await getPyodide();
    if (!py) return;

    try {
      // 1. Schreibe aufgabe.py in das Pyodide-Dateisystem
      py.FS.writeFile("aufgabe.py", userCode);

      // 2. Führe test_aufgabe.py aus
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

      const [isSuccess, totalRuns, fails, errs, outputText] = await py.runPythonAsync(testRunnerScript);

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
    }, 1500); // 1.5s nach letztem Tastenanschlag speichern
  }

  async function saveProgressDraft() {
    if (!currentChapterData || !currentChapterData.chapterId) return;
    const code = getEditorCode();

    // 1. Lokal in LocalStorage
    localStorage.setItem(`code_draft_${currentChapterData.chapterId}`, code);

    // 2. In Backend-Cloud falls angemeldet
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

    // 1. Lokale Gamification
    if (window.addXP) {
      window.addXP(100, currentChapterData.chapterId);
    }

    // 2. Backend Cloud
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
  }

  // 6. Init Workspace Controller
  window.initWorkspace = function (chapterData) {
    currentChapterData = chapterData;

    // Lade gespeicherten Code-Draft oder Startercode
    const savedDraft = localStorage.getItem(`code_draft_${chapterData.chapterId}`);
    const initialCode = savedDraft || chapterData.starterCode || "";

    initMonacoEditor(initialCode);

    // Event Listener für Buttons
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
