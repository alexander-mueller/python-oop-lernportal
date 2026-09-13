/**
 * 🧭 DYNAMIC COURSE SIDEBAR & RESPONSIVE DRAWER SYSTEM 🧭
 * =======================================================
 * IT-Praxisportal – Vollständig responsive Kurs-Sidebar für alle 13 Kurse & Web-IDE.
 */

(function () {
  'use strict';

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  function getRootPrefix() {
    const scripts = document.querySelectorAll('script[src*="course_sidebar.js"]');
    if (scripts.length > 0) {
      const src = scripts[scripts.length - 1].getAttribute('src');
      const idx = src.indexOf('assets/course_sidebar.js');
      if (idx !== -1) {
        return src.substring(0, idx);
      }
    }
    const p = window.location.pathname;
    if (p.includes('/courses/')) return '../../../';
    if (p.includes('/lehrpfad_')) return '../../';
    return '';
  }

  function detectContext() {
    const isWorkspace = window.location.pathname.endsWith('workspace.html') || !!document.querySelector('.workspace-topbar');
    const urlParams = new URLSearchParams(window.location.search);

    if (isWorkspace) {
      return {
        isWorkspace: true,
        courseId: urlParams.get('course') || 'python',
        trackId: urlParams.get('track') || '',
        chapterFolder: urlParams.get('chapter') || ''
      };
    }

    const path = window.location.pathname;
    const courseMatch = path.match(/courses\/([^\/]+)\/([^\/]+)/);
    if (courseMatch) {
      return {
        isWorkspace: false,
        courseId: courseMatch[1],
        chapterFolder: courseMatch[2],
        trackId: ''
      };
    }

    const pythonMatch = path.match(/(lehrpfad_[^\/]+)\/([^\/]+)/);
    if (pythonMatch) {
      return {
        isWorkspace: false,
        courseId: 'python',
        trackId: pythonMatch[1],
        chapterFolder: pythonMatch[2]
      };
    }

    return {
      isWorkspace: false,
      courseId: 'python',
      chapterFolder: '',
      trackId: ''
    };
  }

  function getSolvedChapters() {
    const solved = new Set();
    try {
      const stateStr = localStorage.getItem('python_gamification_state');
      if (stateStr) {
        const s = JSON.parse(stateStr);
        if (Array.isArray(s.geloeste_kapitel)) {
          s.geloeste_kapitel.forEach(id => solved.add(id));
        }
      }
      const progStr = localStorage.getItem('python_gamification_progress');
      if (progStr) {
        const p = JSON.parse(progStr);
        if (Array.isArray(p.geloeste_kapitel)) {
          p.geloeste_kapitel.forEach(id => solved.add(id));
        }
      }
    } catch (e) {
      console.warn('Lernfortschritt konnte nicht geladen werden:', e);
    }
    return solved;
  }

  function initSidebar() {
    const rootPrefix = getRootPrefix();

    function proceed() {
      if (!window.COURSES_MANIFEST) {
        const manifestScript = document.createElement('script');
        manifestScript.src = `${rootPrefix}assets/courses_manifest.js`;
        manifestScript.onload = () => buildSidebar();
        manifestScript.onerror = () => console.error('Konnte courses_manifest.js nicht laden.');
        document.head.appendChild(manifestScript);
      } else {
        buildSidebar();
      }
    }

    if (!window.AUTH) {
      const authScript = document.createElement('script');
      authScript.src = `${rootPrefix}assets/app_auth.js?v=2.2.3`;
      authScript.onload = () => proceed();
      authScript.onerror = () => proceed();
      document.head.appendChild(authScript);
    } else {
      proceed();
    }
  }

  function buildSidebar() {
    if (!window.COURSES_MANIFEST) return;

    // Zugangsschutz: Kurse & Web-IDE erfordern Authentifizierung
    if (window.AUTH && typeof window.AUTH.requireAuth === 'function') {
      window.AUTH.requireAuth({
        allowClose: false,
        title: '🔒 Registrierung erforderlich',
        message: 'Um die interaktiven Kursmodule und die Web-IDE zu nutzen, erstelle bitte einen kostenlosen Account oder melde dich an.'
      });
    }

    // Alte legacy sidebars entfernen falls vorhanden
    document.querySelectorAll('.app-sidebar, .sidebar-mobile-toggle, .sidebar-overlay').forEach(el => el.remove());
    const existingSidebar = document.getElementById('courseSidebar');
    if (existingSidebar) existingSidebar.remove();
    const existingBackdrop = document.getElementById('courseSidebarBackdrop');
    if (existingBackdrop) existingBackdrop.remove();
    const existingMobileBtn = document.getElementById('courseSidebarMobileToggle');
    if (existingMobileBtn) existingMobileBtn.remove();

    const rootPrefix = getRootPrefix();
    const context = detectContext();
    const manifest = window.COURSES_MANIFEST;
    const currentCourse = manifest[context.courseId] || manifest['python'];
    if (!currentCourse) return;

    const solvedSet = getSolvedChapters();

    if (!context.chapterFolder && currentCourse.tracks && currentCourse.tracks[0] && currentCourse.tracks[0].chapters && currentCourse.tracks[0].chapters[0]) {
      context.chapterFolder = currentCourse.tracks[0].chapters[0].folder;
      if (!currentTrackId) currentTrackId = currentCourse.tracks[0].id;
    }

    // Zähle Kapitel & gelöste Aufgaben für den aktiven Kurs
    let totalChapters = 0;
    let solvedCount = 0;
    let currentTrackId = context.trackId || '';

    (currentCourse.tracks || []).forEach(tr => {
      (tr.chapters || []).forEach(ch => {
        totalChapters++;
        const isSolved = solvedSet.has(ch.folder) ||
                         solvedSet.has(`${context.courseId}/${ch.folder}`) ||
                         solvedSet.has(`${tr.id}/${ch.folder}`);
        if (isSolved) solvedCount++;
        if (ch.folder === context.chapterFolder && !currentTrackId) {
          currentTrackId = tr.id;
        }
      });
    });

    const percent = totalChapters > 0 ? Math.round((solvedCount / totalChapters) * 100) : 0;

    if (context.isWorkspace) {
      document.body.classList.add('workspace-page');
    } else {
      document.body.classList.add('has-course-sidebar');
    }

    // Erstelle Sidebar Container
    const sidebar = document.createElement('aside');
    sidebar.className = 'course-sidebar';
    sidebar.id = 'courseSidebar';

    // Header mit Branding, Close-Button & Dropdown
    let courseOptionsHtml = '';
    const courseKeys = Object.keys(manifest);
    courseKeys.forEach(cid => {
      const c = manifest[cid];
      const selected = cid === context.courseId ? 'selected' : '';
      const icon = c.icon || '📚';
      courseOptionsHtml += `<option value="${cid}" ${selected}>${icon} ${c.title}</option>`;
    });

    // Navigation Tracks & Chapters generieren
    let navHtml = '';
    (currentCourse.tracks || []).forEach((tr) => {
      navHtml += `<div class="course-sidebar-track-group">`;
      navHtml += `<div class="course-sidebar-track-title">${tr.title}</div>`;
      navHtml += `<div style="display: flex; flex-direction: column; gap: 2px;">`;

      (tr.chapters || []).forEach((ch) => {
        const isActive = (ch.folder === context.chapterFolder);
        const isSolved = solvedSet.has(ch.folder) ||
                         solvedSet.has(`${context.courseId}/${ch.folder}`) ||
                         solvedSet.has(`${tr.id}/${ch.folder}`);

        let linkUrl = '';
        if (context.isWorkspace) {
          linkUrl = `${rootPrefix}workspace.html?course=${context.courseId}&track=${tr.id}&chapter=${ch.folder}`;
        } else {
          if (context.courseId === 'python') {
            linkUrl = `${rootPrefix}${tr.id}/${ch.folder}/index.html`;
          } else {
            linkUrl = `${rootPrefix}courses/${context.courseId}/${ch.folder}/index.html`;
          }
        }

        let statusIconHtml = '';
        if (isSolved) {
          statusIconHtml = `<span class="course-sidebar-status-icon status-icon-solved" title="Gelöst">✓</span>`;
        } else if (isActive) {
          statusIconHtml = `<span class="course-sidebar-status-icon status-icon-open" title="Aktuell in Bearbeitung">●</span>`;
        } else {
          statusIconHtml = `<span class="course-sidebar-status-icon status-icon-open"></span>`;
        }

        navHtml += `
          <a href="${linkUrl}" class="course-sidebar-link ${isActive ? 'active' : ''}" ${isActive ? 'id="activeSidebarChapter"' : ''} title="${ch.title}">
            ${statusIconHtml}
            <span class="course-sidebar-title-text">${ch.title}</span>
          </a>
        `;
      });

      navHtml += `</div></div>`;
    });

    // Footer Action (Theorie lesen vs. Web-IDE)
    let footerActionHtml = '';
    if (context.isWorkspace) {
      let theoryUrl = '';
      if (context.courseId === 'python') {
        theoryUrl = `${rootPrefix}${currentTrackId || 'lehrpfad_1_grundlagen'}/${context.chapterFolder}/index.html`;
      } else {
        theoryUrl = `${rootPrefix}courses/${context.courseId}/${context.chapterFolder}/index.html`;
      }
      footerActionHtml = `
        <a href="${theoryUrl}" title="Zurück zur ausführlichen Theorie-Lektion" style="display: inline-flex; align-items: center; gap: 5px; color: #38bdf8; font-weight: 700;">
          <span>📖</span> <span>Theorie lesen</span>
        </a>
      `;
    } else {
      const ideUrl = `${rootPrefix}workspace.html?course=${context.courseId}&track=${currentTrackId}&chapter=${context.chapterFolder}`;
      footerActionHtml = `
        <a href="${ideUrl}" title="Aufgabe in der interaktiven Web-IDE bearbeiten" style="display: inline-flex; align-items: center; gap: 5px; color: #10b981; font-weight: 700;">
          <span>💻</span> <span>Web-IDE</span>
        </a>
      `;
    }

    sidebar.innerHTML = `
      <div class="course-sidebar-header">
        <div class="course-sidebar-brand-row">
          <a href="${rootPrefix}dashboard.html" class="course-sidebar-brand" title="Zum Lernbereich Dashboard">
            <div class="course-sidebar-logo">🎓</div>
            <div>
              <div class="course-sidebar-title">IT-Praxisportal</div>
              <div style="font-size: 0.65rem; color: #64748b; font-weight: 800; text-transform: uppercase; letter-spacing: 0.8px;">PRO LERNPFAD</div>
            </div>
          </a>
          <button type="button" class="course-sidebar-close-btn" id="courseSidebarClose" aria-label="Sidebar schließen" title="Schließen">✕</button>
        </div>

        <label for="courseSidebarSelect" style="display: block; font-size: 0.68rem; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 5px;">Aktiver Kurs</label>
        <select class="course-sidebar-select" id="courseSidebarSelect">
          ${courseOptionsHtml}
        </select>

        <div class="course-sidebar-progress-container">
          <div class="course-sidebar-progress-text">
            <span>Kursfortschritt</span>
            <span id="course-sidebar-progress-stat">${solvedCount} / ${totalChapters} (${percent}%)</span>
          </div>
          <div class="course-sidebar-progress-bar-bg">
            <div class="course-sidebar-progress-bar-fill" style="width: ${percent}%;"></div>
          </div>
        </div>
      </div>

      <nav class="course-sidebar-nav" id="courseSidebarNav">
        ${navHtml}
      </nav>

      <div class="course-sidebar-footer">
        ${footerActionHtml}
        <a href="${rootPrefix}dashboard.html" style="display: inline-flex; align-items: center; gap: 4px;" title="Zum Lernbereich Dashboard">
          <span>🏠</span> <span>Dashboard</span>
        </a>
      </div>
    `;

    document.body.appendChild(sidebar);

    // Backdrop erstellen
    const backdrop = document.createElement('div');
    backdrop.className = 'course-sidebar-backdrop';
    backdrop.id = 'courseSidebarBackdrop';
    document.body.appendChild(backdrop);

    // Kurswechsler Event Listener
    const selectEl = document.getElementById('courseSidebarSelect');
    if (selectEl) {
      selectEl.addEventListener('change', (e) => {
        const newCourseId = e.target.value;
        if (newCourseId === context.courseId) return;

        const targetCourse = manifest[newCourseId];
        if (!targetCourse || !targetCourse.tracks || !targetCourse.tracks.length) return;
        const targetTrack = targetCourse.tracks[0];
        const targetChapter = targetTrack.chapters && targetTrack.chapters.length ? targetTrack.chapters[0].folder : '';

        if (context.isWorkspace) {
          window.location.href = `${rootPrefix}workspace.html?course=${newCourseId}&track=${targetTrack.id}&chapter=${targetChapter}`;
        } else {
          if (newCourseId === 'python') {
            window.location.href = `${rootPrefix}${targetTrack.id}/${targetChapter}/index.html`;
          } else {
            window.location.href = `${rootPrefix}courses/${newCourseId}/${targetChapter}/index.html`;
          }
        }
      });
    }

    // Toggle-Funktionen für Drawer
    function openSidebar() {
      sidebar.classList.add('open');
      backdrop.classList.add('active');
    }

    function closeSidebar() {
      sidebar.classList.remove('open');
      backdrop.classList.remove('active');
    }

    const closeBtn = document.getElementById('courseSidebarClose');
    if (closeBtn) closeBtn.addEventListener('click', closeSidebar);
    backdrop.addEventListener('click', closeSidebar);

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeSidebar();
    });

    // Mobil-Toggle Button für Leseansicht
    if (!context.isWorkspace) {
      const mobileBtn = document.createElement('button');
      mobileBtn.type = 'button';
      mobileBtn.className = 'course-sidebar-mobile-btn';
      mobileBtn.id = 'courseSidebarMobileToggle';
      mobileBtn.setAttribute('aria-label', 'Module und Kapitel öffnen');
      mobileBtn.innerHTML = `<span>☰</span> <span>Kapitel (${solvedCount}/${totalChapters})</span>`;
      mobileBtn.addEventListener('click', () => {
        if (sidebar.classList.contains('open')) {
          closeSidebar();
        } else {
          openSidebar();
        }
      });
      document.body.appendChild(mobileBtn);
    }

    // ==========================================================================
    // 🧭 KURS- & MODUL-NAVIGATIONSSYSTEM (Keine langweiligen Hyperlinks!)
    // ==========================================================================
    const ORDERED_COURSE_KEYS = [
      'python',
      'bash',
      'powershell',
      'active_directory',
      'git',
      'dns_records',
      'sql',
      'html_css',
      'javascript',
      'java',
      'csharp',
      'cpp',
      'go',
      'rust',
      'ihk_ap1',
      'ihk_ap2_fisi'
    ];

    const courseIdx = ORDERED_COURSE_KEYS.indexOf(context.courseId);
    const prevCourseKey = courseIdx > 0 ? ORDERED_COURSE_KEYS[courseIdx - 1] : null;
    const nextCourseKey = (courseIdx >= 0 && courseIdx < ORDERED_COURSE_KEYS.length - 1) ? ORDERED_COURSE_KEYS[courseIdx + 1] : null;
    const prevCourse = prevCourseKey ? manifest[prevCourseKey] : null;
    const nextCourse = nextCourseKey ? manifest[nextCourseKey] : null;

    const allChapters = [];
    (currentCourse.tracks || []).forEach(tr => {
      (tr.chapters || []).forEach(ch => {
        allChapters.push({
          trackId: tr.id,
          folder: ch.folder,
          title: ch.title,
          taskFile: ch.taskFile,
          testFile: ch.testFile
        });
      });
    });

    const currentChapIdx = allChapters.findIndex(ch => ch.folder === context.chapterFolder);
    const prevChapter = currentChapIdx > 0 ? allChapters[currentChapIdx - 1] : null;
    const nextChapter = (currentChapIdx >= 0 && currentChapIdx < allChapters.length - 1) ? allChapters[currentChapIdx + 1] : null;

    function buildTheoryUrl(cid, tid, folder) {
      if (cid === 'python') {
        return `${rootPrefix}${tid || 'lehrpfad_1_grundlagen'}/${folder}/index.html`;
      }
      return `${rootPrefix}courses/${cid}/${folder}/index.html`;
    }

    function buildFirstLessonTheoryUrl(cid, courseObj) {
      if (!courseObj || !courseObj.tracks || !courseObj.tracks.length) return `${rootPrefix}dashboard.html`;
      const t = courseObj.tracks[0];
      const f = t.chapters && t.chapters.length ? t.chapters[0].folder : '';
      if (!f) return `${rootPrefix}dashboard.html`;
      return buildTheoryUrl(cid, t.id, f);
    }

    function buildWorkspaceUrl(cid, tid, folder) {
      return `${rootPrefix}workspace.html?course=${encodeURIComponent(cid)}&track=${encodeURIComponent(tid || '')}&chapter=${encodeURIComponent(folder)}`;
    }

    function buildFirstLessonWorkspaceUrl(cid, courseObj) {
      if (!courseObj || !courseObj.tracks || !courseObj.tracks.length) return `${rootPrefix}workspace.html`;
      const t = courseObj.tracks[0];
      const f = t.chapters && t.chapters.length ? t.chapters[0].folder : '';
      return buildWorkspaceUrl(cid, t.id, f);
    }

    // 1. THEORIE-SEITEN: Prominente Navigationsleiste am Ende der Lerneinheit
    function renderTheoryNavigator() {
      const mainEl = document.querySelector('main.container') || document.querySelector('main') || document.querySelector('.container');
      if (!mainEl) return;

      const existingNav = document.getElementById('courseModuleNavigator');
      if (existingNav) existingNav.remove();

      // Legacy-Buttons ausblenden / entfernen
      const legacyCandidates = mainEl.querySelectorAll(
        '.card > div[style*="flex"]:last-child, main > div[style*="flex"]:last-child, div[style*="flex"]:last-child, ' +
        '.border-t, div[class*="border-t"], div[class*="justify-between"], div.mt-8.pt-6'
      );
      legacyCandidates.forEach(el => {
        if (el.querySelector('a[href*="index.html"]') || el.querySelector('a[href*="workspace.html"]') || el.querySelector('.ihk-btn') || el.innerText.includes('Nächstes Modul') || el.innerText.includes('Vorheriges Modul')) {
          el.remove();
        }
      });

      const nav = document.createElement('nav');
      nav.className = 'course-module-navigator';
      nav.id = 'courseModuleNavigator';
      nav.setAttribute('aria-label', 'Kurs- und Modulnavigation');

      // Linker Button (Vorheriges Modul oder Vorheriger Kurs)
      let leftBtnHtml = '';
      if (prevChapter) {
        const prevUrl = buildTheoryUrl(context.courseId, prevChapter.trackId, prevChapter.folder);
        leftBtnHtml = `
          <a href="${prevUrl}" class="lesson-nav-btn lesson-nav-prev" title="Vorheriges Modul: ${escapeHtml(prevChapter.title)}">
            <span class="nav-arrow">◀</span>
            <span class="nav-text">
              <span class="nav-subtitle">VORHERIGES MODUL</span>
              <span class="nav-title">${escapeHtml(prevChapter.title)}</span>
            </span>
          </a>
        `;
      } else if (prevCourse) {
        const prevCourseUrl = buildFirstLessonTheoryUrl(prevCourseKey, prevCourse);
        leftBtnHtml = `
          <a href="${prevCourseUrl}" class="lesson-nav-btn lesson-nav-course-prev" title="Vorheriger Kurs: ${escapeHtml(prevCourse.title)}">
            <span class="nav-arrow">⏮</span>
            <span class="nav-text">
              <span class="nav-subtitle">VORHERIGER KURS</span>
              <span class="nav-title">${escapeHtml(prevCourse.icon || '📚')} ${escapeHtml(prevCourse.title)}</span>
            </span>
          </a>
        `;
      } else {
        leftBtnHtml = `
          <a href="${rootPrefix}dashboard.html" class="lesson-nav-btn" style="opacity: 0.85;" title="Zurück zum Lern-Dashboard">
            <span class="nav-arrow">🏠</span>
            <span class="nav-text">
              <span class="nav-subtitle">START</span>
              <span class="nav-title">Zum Dashboard</span>
            </span>
          </a>
        `;
      }

      // Mittlere Buttons (Dashboard & Web-IDE)
      const ideUrl = buildWorkspaceUrl(context.courseId, currentTrackId, context.chapterFolder);
      const centerHtml = `
        <div class="lesson-nav-center">
          <a href="${rootPrefix}dashboard.html" class="lesson-nav-btn lesson-nav-dashboard" title="Zurück zur Übersicht aller Kurse">
            <span>🏠</span>
            <span>Dashboard</span>
          </a>
          <a href="${ideUrl}" class="lesson-nav-btn lesson-nav-ide" title="Aufgabe interaktiv in der Web-IDE lösen">
            <span>💻</span>
            <span>In Web-IDE lösen →</span>
          </a>
        </div>
      `;

      // Rechter Button (Nächstes Modul oder Nächster Kurs)
      let rightBtnHtml = '';
      if (nextChapter) {
        const nextUrl = buildTheoryUrl(context.courseId, nextChapter.trackId, nextChapter.folder);
        rightBtnHtml = `
          <a href="${nextUrl}" class="lesson-nav-btn lesson-nav-next" title="Nächstes Modul: ${escapeHtml(nextChapter.title)}">
            <span class="nav-text">
              <span class="nav-subtitle">NÄCHSTES MODUL</span>
              <span class="nav-title">${escapeHtml(nextChapter.title)}</span>
            </span>
            <span class="nav-arrow">▶</span>
          </a>
        `;
      } else if (nextCourse) {
        const nextCourseUrl = buildFirstLessonTheoryUrl(nextCourseKey, nextCourse);
        rightBtnHtml = `
          <a href="${nextCourseUrl}" class="lesson-nav-btn lesson-nav-course-next" title="Nächster Kurs: ${escapeHtml(nextCourse.title)}">
            <span class="nav-text">
              <span class="nav-subtitle">NÄCHSTER KURS</span>
              <span class="nav-title">${escapeHtml(nextCourse.icon || '🚀')} ${escapeHtml(nextCourse.title)}</span>
            </span>
            <span class="nav-arrow">⏭</span>
          </a>
        `;
      } else {
        rightBtnHtml = `
          <a href="${rootPrefix}dashboard.html" class="lesson-nav-btn lesson-nav-course-next" title="Alle Kurse gemeistert!">
            <span class="nav-text">
              <span class="nav-subtitle">ABSCHLUSS</span>
              <span class="nav-title">🎉 Kurs gemeistert!</span>
            </span>
            <span class="nav-arrow">🏆</span>
          </a>
        `;
      }

      nav.innerHTML = leftBtnHtml + centerHtml + rightBtnHtml;
      mainEl.appendChild(nav);
    }

    // 2. WORKSPACE-PANE: Navigationsbuttons innerhalb des Theorie-Tabs der Web-IDE
    function renderWorkspaceTheoryInlineNavigator() {
      const theoriePane = document.getElementById('tab-content-theorie');
      if (!theoriePane) return;

      const existingPaneNav = theoriePane.querySelector('.course-module-navigator');
      if (existingPaneNav) existingPaneNav.remove();

      const legacyCandidates = theoriePane.querySelectorAll(
        '.card > div[style*="flex"]:last-child, div[style*="flex"]:last-child, ' +
        '.border-t, div[class*="border-t"], div[class*="justify-between"], div.mt-8.pt-6'
      );
      legacyCandidates.forEach(el => {
        if (el.querySelector('a[href*="index.html"]') || el.querySelector('a[href*="workspace.html"]') || el.querySelector('.ihk-btn') || el.innerText.includes('Nächstes Modul') || el.innerText.includes('Vorheriges Modul')) {
          el.remove();
        }
      });

      const paneNav = document.createElement('nav');
      paneNav.className = 'course-module-navigator';
      paneNav.style.marginTop = '28px';
      paneNav.setAttribute('aria-label', 'Modulnavigation');

      // Left
      let leftHtml = '';
      if (prevChapter) {
        const prevWsUrl = buildWorkspaceUrl(context.courseId, prevChapter.trackId, prevChapter.folder);
        leftHtml = `
          <a href="${prevWsUrl}" class="lesson-nav-btn lesson-nav-prev" title="Vorheriges Modul: ${escapeHtml(prevChapter.title)}">
            <span class="nav-arrow">◀</span>
            <span class="nav-text">
              <span class="nav-subtitle">VORHERIGES MODUL</span>
              <span class="nav-title">${escapeHtml(prevChapter.title)}</span>
            </span>
          </a>
        `;
      } else if (prevCourse) {
        const prevCourseWsUrl = buildFirstLessonWorkspaceUrl(prevCourseKey, prevCourse);
        leftHtml = `
          <a href="${prevCourseWsUrl}" class="lesson-nav-btn lesson-nav-course-prev" title="Vorheriger Kurs: ${escapeHtml(prevCourse.title)}">
            <span class="nav-arrow">⏮</span>
            <span class="nav-text">
              <span class="nav-subtitle">VORHERIGER KURS</span>
              <span class="nav-title">${escapeHtml(prevCourse.icon || '📚')} ${escapeHtml(prevCourse.title)}</span>
            </span>
          </a>
        `;
      } else {
        leftHtml = `
          <a href="${rootPrefix}dashboard.html" class="lesson-nav-btn" title="Zurück zum Lern-Dashboard">
            <span class="nav-arrow">🏠</span>
            <span class="nav-text">
              <span class="nav-subtitle">START</span>
              <span class="nav-title">Dashboard</span>
            </span>
          </a>
        `;
      }

      // Center
      const theoryFullUrl = buildTheoryUrl(context.courseId, currentTrackId, context.chapterFolder);
      const centerHtml = `
        <div class="lesson-nav-center">
          <a href="${theoryFullUrl}" target="_blank" rel="noopener noreferrer" class="lesson-nav-btn lesson-nav-dashboard" title="Theorie in voller Seite lesen">
            <span>📖</span>
            <span>Vollbild-Theorie ↗</span>
          </a>
        </div>
      `;

      // Right
      let rightHtml = '';
      if (nextChapter) {
        const nextWsUrl = buildWorkspaceUrl(context.courseId, nextChapter.trackId, nextChapter.folder);
        rightHtml = `
          <a href="${nextWsUrl}" class="lesson-nav-btn lesson-nav-next" title="Nächstes Modul: ${escapeHtml(nextChapter.title)}">
            <span class="nav-text">
              <span class="nav-subtitle">NÄCHSTES MODUL</span>
              <span class="nav-title">${escapeHtml(nextChapter.title)}</span>
            </span>
            <span class="nav-arrow">▶</span>
          </a>
        `;
      } else if (nextCourse) {
        const nextCourseWsUrl = buildFirstLessonWorkspaceUrl(nextCourseKey, nextCourse);
        rightHtml = `
          <a href="${nextCourseWsUrl}" class="lesson-nav-btn lesson-nav-course-next" title="Nächster Kurs: ${escapeHtml(nextCourse.title)}">
            <span class="nav-text">
              <span class="nav-subtitle">NÄCHSTER KURS</span>
              <span class="nav-title">${escapeHtml(nextCourse.icon || '🚀')} ${escapeHtml(nextCourse.title)}</span>
            </span>
            <span class="nav-arrow">⏭</span>
          </a>
        `;
      } else {
        rightHtml = `
          <a href="${rootPrefix}dashboard.html" class="lesson-nav-btn lesson-nav-course-next" title="Alle Kurse gemeistert!">
            <span class="nav-text">
              <span class="nav-subtitle">ABSCHLUSS</span>
              <span class="nav-title">🎉 Kurs gemeistert!</span>
            </span>
            <span class="nav-arrow">🏆</span>
          </a>
        `;
      }

      paneNav.innerHTML = leftHtml + centerHtml + rightHtml;
      theoriePane.appendChild(paneNav);
    }

    // Global für dynamisches Nachladen in workspace.html bereitstellen
    window.renderWorkspaceTheoryNavigator = renderWorkspaceTheoryInlineNavigator;

    // 3. WORKSPACE: Topbar-Steuerleiste verdrahten
    function renderWorkspaceNavigation() {
      const topbarTitle = document.querySelector('.workspace-title');
      if (!topbarTitle) return;

      // 1. Drawer Button "☰ Kapitel"
      let toggleBtn = document.getElementById('btn-toggle-chapter-drawer');
      if (!toggleBtn) {
        toggleBtn = document.createElement('button');
        toggleBtn.type = 'button';
        toggleBtn.id = 'btn-toggle-chapter-drawer';
        toggleBtn.className = 'workspace-topbar-btn';
        toggleBtn.innerHTML = '<span>☰</span> <span>Kapitel</span>';
        toggleBtn.title = 'Kapitel-Übersicht aufklappen';
        topbarTitle.insertBefore(toggleBtn, topbarTitle.firstChild);
      }
      toggleBtn.onclick = () => {
        if (sidebar.classList.contains('open')) {
          closeSidebar();
        } else {
          openSidebar();
        }
      };

      // 2. Dashboard Button
      let dashBtn = document.getElementById('btn-topbar-dashboard');
      if (!dashBtn) {
        dashBtn = document.createElement('a');
        dashBtn.href = `${rootPrefix}dashboard.html`;
        dashBtn.id = 'btn-topbar-dashboard';
        dashBtn.className = 'workspace-topbar-btn';
        dashBtn.innerHTML = '<span>🏠</span> <span>Dashboard</span>';
        dashBtn.title = 'Zurück zum Lern-Dashboard';
        toggleBtn.insertAdjacentElement('afterend', dashBtn);
      }

      // 3. Navigation Cluster
      let navCluster = document.getElementById('workspace-nav-cluster');
      if (!navCluster) {
        navCluster = document.createElement('div');
        navCluster.id = 'workspace-nav-cluster';
        navCluster.className = 'workspace-nav-cluster';
        navCluster.innerHTML = `
          <button type="button" class="workspace-topbar-btn" id="btn-topbar-prev-course" title="Vorheriger Kurs">⏮ Kurs</button>
          <button type="button" class="workspace-topbar-btn" id="btn-topbar-prev-chapter" title="Vorheriges Modul">◀ Zurück</button>
          <span class="workspace-chapter-badge" id="workspace-chapter-badge">Modul - / -</span>
          <button type="button" class="workspace-topbar-btn primary" id="btn-topbar-next-chapter" title="Nächstes Modul">Weiter ▶</button>
          <button type="button" class="workspace-topbar-btn" id="btn-topbar-next-course" title="Nächster Kurs">Kurs ⏭</button>
        `;
        dashBtn.insertAdjacentElement('afterend', navCluster);
      }

      // Update Badge
      const badge = document.getElementById('workspace-chapter-badge');
      if (badge) {
        const modNumber = currentChapIdx >= 0 ? currentChapIdx + 1 : 1;
        badge.innerText = `MODUL ${modNumber} / ${allChapters.length || 16}`;
      }

      const btnPrevCourse = document.getElementById('btn-topbar-prev-course');
      if (btnPrevCourse) {
        if (prevCourseKey && prevCourse) {
          btnPrevCourse.classList.remove('disabled');
          btnPrevCourse.disabled = false;
          btnPrevCourse.title = `Zum vorherigen Kurs: ${prevCourse.title}`;
          btnPrevCourse.onclick = () => {
            window.location.href = buildFirstLessonWorkspaceUrl(prevCourseKey, prevCourse);
          };
        } else {
          btnPrevCourse.classList.add('disabled');
          btnPrevCourse.disabled = true;
        }
      }

      const btnPrevChap = document.getElementById('btn-topbar-prev-chapter');
      if (btnPrevChap) {
        if (prevChapter) {
          btnPrevChap.classList.remove('disabled');
          btnPrevChap.disabled = false;
          btnPrevChap.title = `Vorheriges Modul: ${prevChapter.title}`;
          btnPrevChap.onclick = () => {
            window.location.href = buildWorkspaceUrl(context.courseId, prevChapter.trackId, prevChapter.folder);
          };
        } else {
          btnPrevChap.classList.add('disabled');
          btnPrevChap.disabled = true;
        }
      }

      const btnNextChap = document.getElementById('btn-topbar-next-chapter');
      if (btnNextChap) {
        if (nextChapter) {
          btnNextChap.classList.remove('disabled');
          btnNextChap.disabled = false;
          btnNextChap.title = `Nächstes Modul: ${nextChapter.title}`;
          btnNextChap.onclick = () => {
            window.location.href = buildWorkspaceUrl(context.courseId, nextChapter.trackId, nextChapter.folder);
          };
        } else {
          btnNextChap.classList.add('disabled');
          btnNextChap.disabled = true;
        }
      }

      const btnNextCourse = document.getElementById('btn-topbar-next-course');
      if (btnNextCourse) {
        if (nextCourseKey && nextCourse) {
          btnNextCourse.classList.remove('disabled');
          btnNextCourse.disabled = false;
          btnNextCourse.title = `Zum nächsten Kurs: ${nextCourse.title}`;
          btnNextCourse.onclick = () => {
            window.location.href = buildFirstLessonWorkspaceUrl(nextCourseKey, nextCourse);
          };
        } else {
          btnNextCourse.classList.add('disabled');
          btnNextCourse.disabled = true;
        }
      }

      renderWorkspaceTheoryInlineNavigator();
    }

    if (context.isWorkspace) {
      renderWorkspaceNavigation();
    } else {
      renderTheoryNavigator();
    }

    // Aktives Kapitel automatisch mittig in der Sidebar sichtbar scrollen
    setTimeout(() => {
      const activeItem = document.getElementById('activeSidebarChapter');
      if (activeItem) {
        activeItem.scrollIntoView({ block: 'center', behavior: 'smooth' });
      }
    }, 150);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSidebar);
  } else {
    initSidebar();
  }
})();
