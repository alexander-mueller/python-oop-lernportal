/**
 * ⚡ UNIVERSAL MODULAR MONACO WEB-IDE ⚡
 * =======================================
 * Sprachunabhängige Entwicklungsumgebung mit:
 * - Dynamischer Monaco Editor Initialisierung (Python, JavaScript, SQL, Rust etc.)
 * - Delegierung an pluggbare Language Runner via RunnerRegistry
 * - Tastatur-Shortcuts: Strg+Enter (Run), Strg+Shift+Enter (Test), Strg+S (Save)
 * - Reaktives Terminal, Auto-Save & Gamification Integration
 */

(function () {
  let monacoEditor = null;
  let currentChapterData = null;
  let currentLanguage = "python";
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

  function getActiveRunner() {
    if (window.RunnerRegistry) {
      const runner = window.RunnerRegistry.get(currentLanguage);
      if (runner) return runner;
    }
    return null;
  }

  // 1. Initialisiere Monaco Editor
  function initMonacoEditor(initialCode = "", langId = "python") {
    currentLanguage = langId;
    const editorContainer = document.getElementById("monaco-editor-container");
    if (!editorContainer) return;

    if (window.monaco) {
      createMonacoInstance(initialCode, langId);
      return;
    }

    const loaderScript = document.createElement("script");
    loaderScript.src = "https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.45.0/min/vs/loader.min.js";
    loaderScript.onload = () => {
      window.require.config({
        paths: { vs: "https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.45.0/min/vs" }
      });
      window.require(["vs/editor/editor.main"], () => {
        createMonacoInstance(initialCode, langId);
      });
    };
    loaderScript.onerror = () => {
      editorContainer.innerHTML = `<textarea id="fallback-code-editor" style="width: 100%; height: 100%; background: #0b0f19; color: #f8fafc; font-family: monospace; font-size: 14px; padding: 14px; border: none; outline: none;">${escapeHtml(initialCode)}</textarea>`;
    };
    document.head.appendChild(loaderScript);
  }

  function createMonacoInstance(initialCode, langId) {
    const editorContainer = document.getElementById("monaco-editor-container");
    if (!editorContainer) return;
    editorContainer.innerHTML = "";

    const runner = getActiveRunner();
    const monacoLang = runner ? runner.monacoLanguage : langId;

    monacoEditor = window.monaco.editor.create(editorContainer, {
      value: initialCode,
      language: monacoLang,
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

  // 2. Code-Ausführung via aktivem Language-Runner
  async function runCode() {
    const code = getEditorCode();
    clearTerminal();

    const runner = getActiveRunner();
    if (!runner) {
      logToTerminal(`❌ Kein Language-Runner für '${currentLanguage}' registriert.\n`, "error");
      return;
    }

    logToTerminal(`▶ Starte Ausführung mit ${runner.displayName} (Strg+Enter)...\n----------------------------------------\n`, "info");

    const result = await runner.runCode(code, logToTerminal);

    if (result.success) {
      logToTerminal("\n----------------------------------------\n✨ Erfolgreich ausgeführt!\n", "success");
    } else if (result.error) {
      suggestErrorInterpreter(result.error);
    }
  }

  // 3. Test-Ausführung via aktivem Language-Runner
  async function runTests() {
    if (!currentChapterData || !currentChapterData.testCode) {
      logToTerminal("❌ Keine Unittests für dieses Kapitel gefunden.\n", "error");
      return;
    }

    const userCode = getEditorCode();
    clearTerminal();

    const runner = getActiveRunner();
    if (!runner) {
      logToTerminal(`❌ Kein Test-Runner für '${currentLanguage}' verfügbar.\n`, "error");
      return;
    }

    logToTerminal(`🧪 Führe automatisierte Tests aus (Strg+Shift+Enter)...\n----------------------------------------\n`, "info");

    const result = await runner.runTests(userCode, currentChapterData.testCode, logToTerminal);

    if (result.success) {
      logToTerminal(`\n🎉 HERVORRAGEND! Alle ${result.total || 'erforderlichen'} Tests erfolgreich bestanden! (+100 XP)\n`, "success");
      triggerSuccessCelebration();
      recordChapterSolved();
    } else {
      logToTerminal(`\n⚠️ ${result.failures || 1} Tests fehlgeschlagen. Überarbeite deinen Code!\n`, "warning");
      if (result.rawOutput) {
        suggestErrorInterpreter(result.rawOutput);
      }
    }
  }

  // 4. Hilfsfunktionen
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

  // 5. Init Workspace Controller
  window.initWorkspace = function (chapterData, language = "python") {
    currentChapterData = chapterData;
    currentLanguage = language || "python";

    const savedDraft = localStorage.getItem(`code_draft_${chapterData.chapterId}`);
    const initialCode = savedDraft || chapterData.starterCode || "";

    initMonacoEditor(initialCode, currentLanguage);

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
