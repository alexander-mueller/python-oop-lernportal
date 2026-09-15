/**
 * 🎓 KMK RAHMENLEHRPLAN 2020: IT-AUSBILDUNGSBERUFE & LERNFELDER MANIFEST
 * ======================================================================
 * Vollständige Abbildung aller 7 deutschen IT-Ausbildungsberufe:
 * 1. Fachinformatiker/in für Systemintegration (FISI)
 * 2. Fachinformatiker/in für Anwendungsentwicklung (FIAE)
 * 3. Fachinformatiker/in für Daten- und Prozessanalyse (FIDP)
 * 4. Fachinformatiker/in für Digitale Vernetzung (FIDV)
 * 5. IT-System-Elektroniker/in (ITSE)
 * 6. Kaufleute für IT-System-Management (ITSM)
 * 7. Kaufleute für Digitalisierungsmanagement (KDM)
 *
 * Strukturierung nach:
 * - 1. Ausbildungsjahr: Lernfelder 1 bis 5 (Kernqualifikationen)
 * - 2. Ausbildungsjahr: Lernfelder 6 bis 9 (Kern & Differenzierung + IHK AP1)
 * - 3. Ausbildungsjahr: Lernfelder 10 bis 12 (Fachspezifisch + IHK AP2)
 */

(function () {
  'use strict';

  const IT_AUSBILDUNGEN = {
    professions: {
      "FISI": {
        id: "FISI",
        name: "Fachinformatiker/in für Systemintegration",
        shortName: "Systemintegration",
        icon: "🖥️",
        color: "#0284c7",
        badgeClass: "badge-fisi",
        description: "Planung, Aufbau, Absicherung und Administration komplexer IT-Infrastrukturen, Netzwerke, Server- und Cloud-Systeme.",
        coreCourses: ["ihk_ap1", "ihk_ap2_fisi", "bash", "powershell", "active_directory", "dns_records", "sql", "python"],
        years: {
          1: {
            title: "1. Ausbildungsjahr (Grundlagen & IT-Arbeitsplatz)",
            lernfelder: [1, 2, 3, 4, 5],
            recommendedCourses: ["ihk_ap1", "bash", "python"]
          },
          2: {
            title: "2. Ausbildungsjahr (Netzwerke, Daten & AP1-Prüfung)",
            lernfelder: [6, 7, 8, 9],
            recommendedCourses: ["ihk_ap1", "sql", "powershell", "dns_records"]
          },
          3: {
            title: "3. Ausbildungsjahr (Enterprise Server, AD & AP2-Prüfung)",
            lernfelder: [10, 11, 12],
            recommendedCourses: ["ihk_ap2_fisi", "active_directory", "dns_records", "powershell", "bash"]
          }
        }
      },
      "FIAE": {
        id: "FIAE",
        name: "Fachinformatiker/in für Anwendungsentwicklung",
        shortName: "Anwendungsentwicklung",
        icon: "💻",
        color: "#7c3aed",
        badgeClass: "badge-fiae",
        description: "Konzeption, Entwicklung und Testen moderner Softwarelösungen, Web-Apps, APIs und datenbankbasierter Anwendungen.",
        coreCourses: ["ihk_ap1", "python", "javascript", "html_css", "sql", "git", "java", "csharp"],
        years: {
          1: {
            title: "1. Ausbildungsjahr (Programmiergrundlagen & Algorithmen)",
            lernfelder: [1, 2, 3, 4, 5],
            recommendedCourses: ["ihk_ap1", "python", "git"]
          },
          2: {
            title: "2. Ausbildungsjahr (OOP, Web-Frontend & SQL-Datenbanken)",
            lernfelder: [6, 7, 8, 9],
            recommendedCourses: ["ihk_ap1", "sql", "javascript", "html_css", "git"]
          },
          3: {
            title: "3. Ausbildungsjahr (Enterprise OOP, Clean Code, CI/CD & AP2)",
            lernfelder: [10, 11, 12],
            recommendedCourses: ["java", "csharp", "go", "git"]
          }
        }
      },
      "FIDP": {
        id: "FIDP",
        name: "Fachinformatiker/in für Daten- und Prozessanalyse",
        shortName: "Daten- & Prozessanalyse",
        icon: "📊",
        color: "#059669",
        badgeClass: "badge-fidp",
        description: "Analyse datenbasierter Geschäftsprozesse, Data Warehousing, Machine Learning und Bereitstellung analytischer Dashboards.",
        coreCourses: ["ihk_ap1", "python", "sql", "git", "bash"],
        years: {
          1: {
            title: "1. Ausbildungsjahr (IT-Basissysteme & Skripting)",
            lernfelder: [1, 2, 3, 4, 5],
            recommendedCourses: ["ihk_ap1", "python", "git"]
          },
          2: {
            title: "2. Ausbildungsjahr (Datenmodellierung & Schnittstellen)",
            lernfelder: [6, 7, 8, 9],
            recommendedCourses: ["ihk_ap1", "sql", "python", "bash"]
          },
          3: {
            title: "3. Ausbildungsjahr (Machine Learning, BPMN & Data Warehousing)",
            lernfelder: [10, 11, 12],
            recommendedCourses: ["python", "sql", "git"]
          }
        }
      },
      "FIDV": {
        id: "FIDV",
        name: "Fachinformatiker/in für Digitale Vernetzung",
        shortName: "Digitale Vernetzung",
        icon: "🌐",
        color: "#ea580c",
        badgeClass: "badge-fidv",
        description: "Vernetzung von Industrie 4.0 Cyber-Physical Systems (CPS), OT-Netzwerksicherheit und Analyse digitaler Datenflüsse.",
        coreCourses: ["ihk_ap1", "bash", "python", "dns_records", "cpp", "powershell"],
        years: {
          1: {
            title: "1. Ausbildungsjahr (Netzwerk-Basics & Hardware-Infrastruktur)",
            lernfelder: [1, 2, 3, 4, 5],
            recommendedCourses: ["ihk_ap1", "bash", "python"]
          },
          2: {
            title: "2. Ausbildungsjahr (CPS-Systeme, Sensoren & IoT-Protokolle)",
            lernfelder: [6, 7, 8, 9],
            recommendedCourses: ["ihk_ap1", "bash", "dns_records"]
          },
          3: {
            title: "3. Ausbildungsjahr (OT-Security, Edge Computing & Netze)",
            lernfelder: [10, 11, 12],
            recommendedCourses: ["cpp", "bash", "dns_records"]
          }
        }
      },
      "ITSE": {
        id: "ITSE",
        name: "IT-System-Elektroniker/in",
        shortName: "System-Elektronik",
        icon: "⚡",
        color: "#d97706",
        badgeClass: "badge-itse",
        description: "Planung, Errichtung und Instandhaltung elektrotechnischer Schutz- und Stromversorgungssysteme sowie optischer Leitungsnetze.",
        coreCourses: ["ihk_ap1", "ihk_ap2_itse", "bash", "dns_records", "cpp"],
        years: {
          1: {
            title: "1. Ausbildungsjahr (Elektrotechnische Grundlagen & Arbeitsplatz)",
            lernfelder: [1, 2, 3, 4, 5],
            recommendedCourses: ["ihk_ap1", "bash"]
          },
          2: {
            title: "2. Ausbildungsjahr (Netzwerkinstallation, LWL & Signalübertragung)",
            lernfelder: [6, 7, 8, 9],
            recommendedCourses: ["ihk_ap1", "dns_records"]
          },
          3: {
            title: "3. Ausbildungsjahr (VDE-Prüfungen, USV-Anlagen & Messtechnik)",
            lernfelder: [10, 11, 12],
            recommendedCourses: ["ihk_ap2_itse", "cpp", "bash"]
          }
        }
      },
      "ITSM": {
        id: "ITSM",
        name: "Kaufleute für IT-System-Management",
        shortName: "IT-System-Management",
        icon: "💼",
        color: "#2563eb",
        badgeClass: "badge-itsm",
        description: "Kaufmännische IT-Beratung, Konzeption und Vertrieb von IT-Lösungen, ITIL-Serviceverträge und IT-Projektmanagement.",
        coreCourses: ["ihk_ap1", "ihk_ap2_itsm", "sql", "python", "html_css"],
        years: {
          1: {
            title: "1. Ausbildungsjahr (IT-Märkte, Hard-/Software & Kalkulation)",
            lernfelder: [1, 2, 3, 4, 5],
            recommendedCourses: ["ihk_ap1", "python"]
          },
          2: {
            title: "2. Ausbildungsjahr (Kaufmännische Beurteilung & Datenbanken)",
            lernfelder: [6, 7, 8, 9],
            recommendedCourses: ["ihk_ap1", "sql"]
          },
          3: {
            title: "3. Ausbildungsjahr (SLA-Vertrieb, ITIL-Services & IT-Projekte)",
            lernfelder: [10, 11, 12],
            recommendedCourses: ["ihk_ap2_itsm", "sql", "html_css"]
          }
        }
      },
      "KDM": {
        id: "KDM",
        name: "Kaufleute für Digitalisierungsmanagement",
        shortName: "Digitalisierungsmanagement",
        icon: "📈",
        color: "#0891b2",
        badgeClass: "badge-kdm",
        description: "Analyse und Digitalisierung betriebswirtschaftlicher Wertschöpfungsketten, ERP-Systeme, Datenökonomie und Compliance.",
        coreCourses: ["ihk_ap1", "ihk_ap2_kdm", "sql", "python", "git"],
        years: {
          1: {
            title: "1. Ausbildungsjahr (Geschäftsprozesse & IT-Organisation)",
            lernfelder: [1, 2, 3, 4, 5],
            recommendedCourses: ["ihk_ap1", "python"]
          },
          2: {
            title: "2. Ausbildungsjahr (Datenanalyse, ERP-Integration & AP1)",
            lernfelder: [6, 7, 8, 9],
            recommendedCourses: ["ihk_ap1", "sql", "git"]
          },
          3: {
            title: "3. Ausbildungsjahr (Plattformökonomie, Digital ROI & Controlling)",
            lernfelder: [10, 11, 12],
            recommendedCourses: ["ihk_ap2_kdm", "sql", "python"]
          }
        }
      }
    },

    // 12 KMK LERNFELDER IM DETAIL (1-5 Jahr 1, 6-9 Jahr 2, 10-12 Jahr 3)
    lernfelder: {
      1: {
        number: 1,
        year: 1,
        title: "Das Unternehmen und die eigene Rolle im Betrieb beschreiben",
        shortTitle: "Unternehmen & Rolle",
        examRelevance: "AP1",
        description: "Organisation, Arbeits- & Tarifrecht, duale Ausbildung, Mitbestimmung, Arbeitssicherheit und betriebliche Wertschöpfung.",
        relatedCourses: ["ihk_ap1"]
      },
      2: {
        number: 2,
        year: 1,
        title: "Arbeitsplätze nach Kundenbedürfnissen ausstatten",
        shortTitle: "Arbeitsplatz & Hardware",
        examRelevance: "AP1",
        description: "Hardwarekomponenten (CPU, RAM, PCIe), Schnittstellen, Ergonomie, Betriebssysteme, Energieversorgung & Nutzwertanalyse.",
        relatedCourses: ["ihk_ap1", "bash"]
      },
      3: {
        number: 3,
        year: 1,
        title: "Clients in Netzwerke einbinden",
        shortTitle: "Netzwerke & IPv4/IPv6",
        examRelevance: "AP1",
        description: "OSI-Schichtenmodell, TCP/IP, IPv4 Subnetting, IPv6 Adressierung, WLAN-Standards, Verkabelungsklassen & Routing-Basics.",
        relatedCourses: ["ihk_ap1", "bash", "dns_records"]
      },
      4: {
        number: 4,
        year: 1,
        title: "Schutzbedarfsanalyse im eigenen Arbeitsbereich durchführen",
        shortTitle: "IT-Sicherheit & DSGVO",
        examRelevance: "AP1",
        description: "Schutzziele (CIA: Vertraulichkeit, Integrität, Verfügbarkeit), DSGVO, BSI IT-Grundschutz, Bedrohungsanalyse, Backup & TOMs.",
        relatedCourses: ["ihk_ap1", "powershell", "bash"]
      },
      5: {
        number: 5,
        year: 1,
        title: "Software zur Arbeitsorganisation und Unterstützung von Betriebsprozessen anpassen",
        shortTitle: "Software- & Algorithmen",
        examRelevance: "AP1",
        description: "Strukturierte Programmierung, Kontrollstrukturen, Schleifen, Funktionen, Trace-Tabellen, UML-Aktivitätsdiagramme & Skripte.",
        relatedCourses: ["ihk_ap1", "python", "bash", "git"]
      },
      6: {
        number: 6,
        year: 2,
        title: "Das Unternehmen am Markt und in der Gesamtwirtschaft positionieren",
        shortTitle: "Markt & Wirtschaft",
        examRelevance: "AP2 / WiSo",
        description: "Marktformen, Marketing-Mix, Rechtsformen, Beschaffungsverfahren, Angebotsvergleiche, Vertragsrecht & Kosten-Leistungs-Rechnung.",
        relatedCourses: ["ihk_ap1", "ihk_ap2_fisi"]
      },
      7: {
        number: 7,
        year: 2,
        title: "Cyber-physische Systeme ergänzen",
        shortTitle: "CPS & Sensorik",
        examRelevance: "AP1 / AP2",
        description: "Sensoren, Aktoren, Mikrocontroller, IoT-Architekturen, Bussysteme, MQTT-Protokoll und Signalübertragung.",
        relatedCourses: ["ihk_ap1", "python", "cpp"]
      },
      8: {
        number: 8,
        year: 2,
        title: "Daten systemübergreifend bereitstellen",
        shortTitle: "Datenbanken & SQL",
        examRelevance: "AP1 / AP2",
        description: "Relationales Datenmodell, ER-Modellierung, 1NF-3NF Normalisierung, SQL DDL (CREATE/ALTER) und DML (SELECT/JOIN), REST-APIs & JSON.",
        relatedCourses: ["sql", "ihk_ap1", "python", "javascript"]
      },
      9: {
        number: 9,
        year: 2,
        title: "Netzwerke und Dienste bereitstellen",
        shortTitle: "Netzwerkdienste & Server",
        examRelevance: "AP2",
        description: "Serverbetriebssysteme (Linux/Windows), DHCP, DNS-Auflösung, Webserver, VLANs, NAT, Firewalling & Access Control Lists (ACLs).",
        relatedCourses: ["dns_records", "bash", "powershell", "ihk_ap2_fisi"]
      },
      10: {
        number: 10,
        year: 3,
        title: "Fachrichtungsspezifische Systemintegration / Softwareentwicklung / Datenanalyse",
        shortTitle: "LF 10: Fachvertiefung I",
        examRelevance: "AP2",
        descriptionsByProfession: {
          "FISI": "Serverdienste bereitstellen und Administrationsaufgaben automatisieren (Active Directory, PowerShell, GPOs, Bash Automation, LDAP/Kerberos).",
          "FIAE": "Benutzeroberflächen gestalten und anpassen (Modernes UI/UX, Web-Frontend HTML5/CSS3/JavaScript, A11y Barrierefreiheit & State Management).",
          "FIDP": "Werkzeuge des maschinellen Lernens und der künstlichen Intelligenz einsetzen (ML-Pipelines, Python Pandas/NumPy, Data Cleaning & Predictive Modeling).",
          "FIDV": "Cyber-physische Systeme vernetzen und absichern (Industrie 4.0, OT-Feldbusse wie PROFINET/Modbus, IIoT-Gateways & Protokolle).",
          "ITSE": "Stromversorgungs- und Schutzsysteme planen und errichten (Elektrotechnik, VDE 0100 / DGUV Vorschrift 3, USV & Überspannungsschutz).",
          "ITSM": "IT-Dienstleistungen vermarkten und vertreiben (SLA Service Level Agreements, ITIL Incident/Change Management, Vertriebskonzepte).",
          "KDM": "Wertschöpfungsprozesse digitalisieren und optimieren (ERP-Systeme, Geschäftsprozess-Digitalisierung, Dokumentenmanagement / DMS)."
        },
        relatedCourses: {
          "FISI": ["active_directory", "powershell", "bash", "ihk_ap2_fisi"],
          "FIAE": ["ihk_ap2_fiae", "html_css", "javascript", "git"],
          "FIDP": ["ihk_ap2_fidp", "python", "sql", "git"],
          "FIDV": ["ihk_ap2_fidv", "bash", "dns_records", "cpp"],
          "ITSE": ["ihk_ap2_itse", "bash", "cpp"],
          "ITSM": ["ihk_ap2_itsm", "sql", "python"],
          "KDM": ["ihk_ap2_kdm", "sql", "git"]
        }
      },
      11: {
        number: 11,
        year: 3,
        title: "Fachrichtungsspezifische Netze / Backend / Prozessmodellierung",
        shortTitle: "LF 11: Fachvertiefung II",
        examRelevance: "AP2",
        descriptionsByProfession: {
          "FISI": "Betriebliche Netzwerke und Speicherlösungen anpassen und überwachen (DNS-Records & Mail Security, SAN/NAS, Hochverfügbarkeit, Monitoring).",
          "FIAE": "Funktionalität in technischen Anwendungen umsetzen (Enterprise OOP mit Java, C#, Go oder Rust, Clean Architecture, Design Patterns).",
          "FIDP": "Betriebliche Prozesse analysieren und modellieren (BPMN 2.0 Prozessmodellierung, Process-Mining, Kennzahlensysteme / KPI).",
          "FIDV": "Datenflüsse von vernetzten Systemen analysieren und sichern (Edge Computing, Protokollanalyse mit Wireshark, Echtzeit-Kommunikation & OT-Security).",
          "ITSE": "Übertragungssysteme und Leitungsnetze installieren und konfigurieren (Kupfer- & Glasfaserverkabelung / LWL-Spleißen, OTDR-Messung, Rack-Montage).",
          "ITSM": "Kunden akquirieren und Kundenbeziehungen pflegen (B2B-Akquise, CRM-Systeme, Bedarfsanalyse, Angebotserstellung & Verhandlung).",
          "KDM": "Digitale Geschäftsmodelle und Plattformökonomie entwickeln (Disruptive Technologien, E-Commerce, Plattformstrategien & Change Management)."
        },
        relatedCourses: {
          "FISI": ["dns_records", "active_directory", "ihk_ap2_fisi"],
          "FIAE": ["ihk_ap2_fiae", "java", "csharp", "go", "rust"],
          "FIDP": ["ihk_ap2_fidp", "python", "sql"],
          "FIDV": ["ihk_ap2_fidv", "dns_records", "bash"],
          "ITSE": ["ihk_ap2_itse", "dns_records"],
          "ITSM": ["ihk_ap2_itsm", "sql"],
          "KDM": ["ihk_ap2_kdm", "sql", "python"]
        }
      },
      12: {
        number: 12,
        year: 3,
        title: "Fachrichtungsspezifische Sicherheit / CI-CD / Data Warehouse",
        shortTitle: "LF 12: Fachvertiefung III & AP2",
        examRelevance: "AP2 / Projektarbeit",
        descriptionsByProfession: {
          "FISI": "IT-Sicherheit und Hochverfügbarkeit in Systemen und Netzen gewährleisten (Firewalls, VPN, DMZ, IDS/IPS, BSI-Notfallkonzepte & Disaster Recovery).",
          "FIAE": "Kundenspezifische Anwendungsentwicklung durchführen (Git Workflows, CI/CD Pipelines, Unittesting, Datenbankanbindung, Release & Deployment).",
          "FIDP": "Analytische Daten und Reports bereitstellen (Data Warehousing, ETL-Strecken, Business Intelligence, Advanced SQL Analytics, Dashboards).",
          "FIDV": "Vernetzte Systeme optimieren und administrieren (Instandhaltungsstrategien, Hochverfügbarkeits-Netzwerke, Störungsmanagement).",
          "ITSE": "IT-Systeme und Infrastrukturen instand halten (Messung elektrischer Größen, Fehlersuche in Hardware- und Kommunikationsanlagen, Reparatur).",
          "ITSM": "IT-Projekte leiten und controlling-gestützt abwickeln (Projektmanagement nach Scrum/Wasserfall, Budgetüberwachung, Rentabilität & Nachkalkulation).",
          "KDM": "Datengetriebene Entscheidungen vorbereiten und steuern (Controlling, Datenvisualisierung, Datenschutz-Folgenabschätzung & Compliance)."
        },
        relatedCourses: {
          "FISI": ["ihk_ap2_fisi", "active_directory", "dns_records", "bash"],
          "FIAE": ["ihk_ap2_fiae", "git", "java", "csharp", "python"],
          "FIDP": ["ihk_ap2_fidp", "sql", "python", "git"],
          "FIDV": ["ihk_ap2_fidv", "bash", "dns_records"],
          "ITSE": ["ihk_ap2_itse", "bash"],
          "ITSM": ["ihk_ap2_itsm", "sql"],
          "KDM": ["ihk_ap2_kdm", "sql"]
        }
      }
    }
  };

  // Hilfsfunktionen für Dashboard, Klassenraum und Profil
  IT_AUSBILDUNGEN.getProfession = function (profId) {
    return this.professions[profId] || this.professions["FISI"];
  };

  IT_AUSBILDUNGEN.getLernfelderForYear = function (profId, year) {
    const prof = this.getProfession(profId);
    const yr = (prof && prof.years && prof.years[year]) || (prof && prof.years && prof.years[1]) || { lernfelder: [1, 2, 3, 4, 5] };
    return yr.lernfelder.map(num => {
      const lf = { ...this.lernfelder[num] };
      if (lf.descriptionsByProfession && lf.descriptionsByProfession[prof.id]) {
        lf.description = lf.descriptionsByProfession[prof.id];
      }
      if (lf.relatedCourses && typeof lf.relatedCourses === "object" && !Array.isArray(lf.relatedCourses)) {
        lf.relatedCourses = lf.relatedCourses[prof.id] || [];
      }
      return lf;
    });
  };

  IT_AUSBILDUNGEN.getAllProfessionsList = function () {
    return Object.values(this.professions);
  };

  // Expose globally
  window.IT_AUSBILDUNGEN = IT_AUSBILDUNGEN;
})();
