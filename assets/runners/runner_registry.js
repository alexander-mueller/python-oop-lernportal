/**
 * 🔌 UNIVERSAL LANGUAGE RUNNER REGISTRY 🔌
 * =========================================
 * Verwaltet austauschbare Language-Runner für polyglotte Code-Ausführung
 * (Python, JavaScript, SQL, Rust etc.) in der Monaco Web-IDE.
 */

(function () {
  const runners = new Map();

  window.RunnerRegistry = {
    /**
     * Registriert einen neuen Language Runner Adapter
     * @param {Object} adapter 
     */
    register(adapter) {
      if (!adapter || !adapter.id) {
        throw new Error("Runner Adapter muss eine gültige 'id' besitzen.");
      }
      runners.set(adapter.id.toLowerCase(), adapter);
      console.log(`🔌 [RunnerRegistry] Runner '${adapter.displayName || adapter.id}' erfolgreich registriert.`);
    },

    /**
     * Ruft einen registrierten Runner anhand der Sprach-ID ab
     * @param {string} languageId 
     * @returns {Object|null}
     */
    get(languageId) {
      if (!languageId) return null;
      return runners.get(languageId.toLowerCase()) || null;
    },

    /**
     * Gibt alle registrierten Sprach-IDs zurück
     * @returns {string[]}
     */
    list() {
      return Array.from(runners.keys());
    },

    /**
     * Prüft, ob ein Runner für eine Sprache verfügbar ist
     * @param {string} languageId 
     * @returns {boolean}
     */
    has(languageId) {
      if (!languageId) return false;
      return runners.has(languageId.toLowerCase());
    }
  };
})();
