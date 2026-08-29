/**
 * 🧭 NEXT-GEN SIDEBAR LOGIC 🧭
 * =============================
 * Verwaltet Mobile Drawer Toggles und Live-Lernfortschritt (✅ Gelöst-Badges).
 */

(function () {
  document.addEventListener("DOMContentLoaded", () => {
    // 1. Mobile Drawer Toggle Button
    const toggleBtn = document.querySelector(".sidebar-mobile-toggle");
    const sidebar = document.querySelector(".app-sidebar");
    const overlay = document.querySelector(".sidebar-overlay");

    if (toggleBtn && sidebar && overlay) {
      toggleBtn.addEventListener("click", () => {
        sidebar.classList.toggle("open");
        overlay.classList.toggle("active");
      });

      overlay.addEventListener("click", () => {
        sidebar.classList.remove("open");
        overlay.classList.remove("active");
      });
    }

    // 2. Mark Solved Chapters in Sidebar from LocalStorage / GAMIFICATION_DATA
    try {
      const gData = window.GAMIFICATION_DATA || JSON.parse(localStorage.getItem("python_gamification_progress") || "{}");
      const solvedList = gData.geloeste_kapitel || [];
      const solvedSet = new Set(solvedList);

      document.querySelectorAll(".app-sidebar .sidebar-link").forEach(link => {
        const href = link.getAttribute("href") || "";
        for (const chapId of solvedSet) {
          if (href.includes(chapId)) {
            if (!link.querySelector(".sidebar-check")) {
              const checkSpan = document.createElement("span");
              checkSpan.className = "sidebar-check";
              checkSpan.innerText = " ✅";
              checkSpan.style.fontSize = "0.75rem";
              link.appendChild(checkSpan);
            }
          }
        }
      });

      // Update Sidebar Footer Level
      const levelEl = document.getElementById("sidebar-level-text");
      const xpEl = document.getElementById("sidebar-xp-text");
      if (levelEl && gData.level) levelEl.innerText = "⭐ Level " + gData.level;
      if (xpEl && gData.xp !== undefined) xpEl.innerText = gData.xp + " XP";
    } catch (e) {}
  });
})();
