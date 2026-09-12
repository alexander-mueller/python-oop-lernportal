/**
 * 🧭 DYNAMIC COURSE SIDEBAR & RESPONSIVE DRAWER SYSTEM 🧭
 * =======================================================
 * IT-Praxisportal – Vollständig responsive Kurs-Sidebar für alle 13 Kurse & Web-IDE.
 */

(function () {
  'use strict';

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
      authScript.src = `${rootPrefix}assets/app_auth.js`;
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
          <a href="${rootPrefix}index.html" class="course-sidebar-brand" title="Zur IT-Praxisportal Startseite">
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
        <a href="${rootPrefix}index.html" style="display: inline-flex; align-items: center; gap: 4px;" title="Zur Startseite">
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

    // Workspace: Topbar "☰ Kapitel" Button einbinden
    if (context.isWorkspace) {
      const topbarTitle = document.querySelector('.workspace-title');
      if (topbarTitle && !document.getElementById('btn-toggle-chapter-drawer')) {
        const toggleBtn = document.createElement('button');
        toggleBtn.type = 'button';
        toggleBtn.id = 'btn-toggle-chapter-drawer';
        toggleBtn.className = 'btn btn-secondary';
        toggleBtn.style.cssText = 'font-size: 0.8rem; padding: 4px 10px; margin-right: 10px; display: inline-flex; align-items: center; gap: 6px; border: 1px solid rgba(255,255,255,0.18); background: rgba(255,255,255,0.08); color: #f8fafc; font-weight: 700; cursor: pointer; border-radius: 6px;';
        toggleBtn.innerHTML = '<span>☰</span> <span>Kapitel</span>';
        toggleBtn.title = 'Kapitel-Drawer aufklappen';
        toggleBtn.addEventListener('click', () => {
          if (sidebar.classList.contains('open')) {
            closeSidebar();
          } else {
            openSidebar();
          }
        });
        topbarTitle.insertBefore(toggleBtn, topbarTitle.firstChild);
      }
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
