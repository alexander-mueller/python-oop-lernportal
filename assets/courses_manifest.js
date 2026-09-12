window.COURSES_MANIFEST = {
  "bash": {
    "id": "bash",
    "title": "Linux Bash, Shell Scripting & Cloud DevOps",
    "language": "bash",
    "icon": "🐧",
    "runner": "bash",
    "description": "Vom Terminal-Einsteiger über professionelle Shell-Skripte, Text-Mining (jq/awk), Parallelisierung (xargs/parallel) bis zu Docker & BATS Unittests.",
    "tracks": [
      {
        "id": "track_1_terminal_grundlagen",
        "title": "🌱 Lehrpfad 1: Linux Terminal Mastery & Core Unix Tools",
        "description": "Navigation, Globbing, I/O Streams, Redirection, Umgebungsvariablen, Dateirechte und Prozesskontrolle.",
        "certificateKey": "bash_grundlagen",
        "chapters": [
          {
            "folder": "01_navigation_dateien_und_globbing",
            "title": "Bash 01: Terminal-Navigation & Globbing",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "02_streams_pipes_und_redirection",
            "title": "Bash 02: I/O Streams, Pipes & Redirection",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "03_variablen_environment_und_subshells",
            "title": "Bash 03: Variablen, Environment & Subshells",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "04_dateirechte_prozesskontrolle_und_jobs",
            "title": "Bash 04: Dateirechte (chmod) & Job Control",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          }
        ]
      },
      {
        "id": "track_2_skripting_und_textmining",
        "title": "⚡ Lehrpfad 2: Professionelles Bash-Scripting & Text-Mining",
        "description": "Kontrollfluss, Regex-Matching, Schleifen, Assoziative Arrays, grep, sed, awk, jq und Strict Mode (set -euo pipefail).",
        "certificateKey": "bash_scripting",
        "chapters": [
          {
            "folder": "05_kontrollfluss_und_testoperatoren",
            "title": "Bash 05: Kontrollfluss & Test-Operatoren",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "06_schleifen_arrays_und_assoziative_maps",
            "title": "Bash 06: Schleifen & Assoziative Arrays",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "07_text_mining_grep_sed_awk_und_jq",
            "title": "Bash 07: Text-Mining mit grep, sed, awk & jq",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "08_robuste_skripte_und_debugging",
            "title": "Bash 08: Robuste Skripte (set -euo pipefail)",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          }
        ]
      },
      {
        "id": "track_3_parallelisierung_und_netzwerk",
        "title": "🚀 Lehrpfad 3: High-Performance, Parallelisierung & Netzwerke",
        "description": "Multiprocessing mit xargs -P und GNU parallel, Prozess-Substitution, REST-Pipelines mit curl und Systemd Automation.",
        "certificateKey": "bash_performance",
        "chapters": [
          {
            "folder": "09_parallelisierung_mit_xargs_und_parallel",
            "title": "Bash 09: Parallelisierung mit xargs & parallel",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "10_prozess_substitution_und_coproc",
            "title": "Bash 10: Prozess-Substitution & Co-Prozesse",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "11_netzwerk_ssh_und_curl_pipelines",
            "title": "Bash 11: Remote SSH & REST-Pipelines (curl)",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "12_cron_systemd_und_service_automation",
            "title": "Bash 12: Cronjobs, Systemd & Logrotation",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          }
        ]
      },
      {
        "id": "track_4_cloud_devops_und_master",
        "title": "💎 Lehrpfad 4: Cloud DevOps, BATS Testing & Masterprojekt",
        "description": "Docker Container Scripting, CI/CD Pipelines, BATS Unittesting und Master DevOps Monitoring Suite.",
        "certificateKey": "bash_master",
        "chapters": [
          {
            "folder": "13_docker_und_container_scripting",
            "title": "Bash 13: Docker & Container Lifecycle Scripting",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "14_ci_cd_und_github_actions_shell",
            "title": "Bash 14: CI/CD Workflows & GitHub Actions",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "15_bats_automatisiertes_unit_testing",
            "title": "Bash 15: BATS Automatisiertes Unit-Testing",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "16_master_abschlussprojekt_devops_suite",
            "title": "Master 16: DevOps Multi-Server Automation Suite",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          }
        ]
      }
    ]
  },
  "cpp": {
    "id": "cpp",
    "title": "C & Modernes C++20 Systems Engineering",
    "language": "cpp",
    "icon": "⚙️",
    "runner": "cpp",
    "description": "Von C Pointern & manuellem Speichermanagement (malloc/free) über RAII, Smart Pointer (unique_ptr) & STL bis zu GoogleTest & 2D Physics Simulation Master.",
    "tracks": [
      {
        "id": "track_1_c_basics",
        "title": "🌱 Lehrpfad 1: C Fundamente & Manuelles Memory Management",
        "description": "C-Syntax, Pointer & Adressoperatoren (&/*), Pointer-Arithmetik, Stack vs. Heap, malloc/free & Header-Dateien (.h/.c).",
        "certificateKey": "cpp_c_grundlagen",
        "chapters": [
          {
            "folder": "01_c_syntax_datentypen_und_io",
            "title": "C 01: C Syntax, Datentypen & printf/scanf",
            "taskFile": "aufgabe.c",
            "testFile": "test_aufgabe.cpp"
          },
          {
            "folder": "02_pointer_und_speicheradressen",
            "title": "C 02: Pointer, Adressen (&/*) & Arithmetik",
            "taskFile": "aufgabe.c",
            "testFile": "test_aufgabe.cpp"
          },
          {
            "folder": "03_arrays_strings_und_manuelle_speicherallokation",
            "title": "C 03: Strings, Stack vs. Heap & malloc/free",
            "taskFile": "aufgabe.c",
            "testFile": "test_aufgabe.cpp"
          },
          {
            "folder": "04_structs_und_header_dateien",
            "title": "C 04: Structs, typedef & Header-Architektur",
            "taskFile": "aufgabe.c",
            "testFile": "test_aufgabe.cpp"
          }
        ]
      },
      {
        "id": "track_2_cpp_oop",
        "title": "🏗️ Lehrpfad 2: Modern C++ Einstieg, RAII & OOP",
        "description": "std::cout, Referenzen, Klassen, Konstruktoren/Destruktoren, RAII-Prinzip, virtual Methoden & Operator-Overloading.",
        "certificateKey": "cpp_oop",
        "chapters": [
          {
            "folder": "05_einstieg_cpp_und_namespaces",
            "title": "C++ 05: Einstieg C++, Namespaces & Referenzen (&)",
            "taskFile": "aufgabe.cpp",
            "testFile": "test_aufgabe.cpp"
          },
          {
            "folder": "06_klassen_konstruktoren_und_raii",
            "title": "C++ 06: Klassen, Destruktoren & RAII-Prinzip",
            "taskFile": "aufgabe.cpp",
            "testFile": "test_aufgabe.cpp"
          },
          {
            "folder": "07_vererbung_und_virtuelle_methoden",
            "title": "C++ 07: Vererbung, Virtual & Polymorphismus",
            "taskFile": "aufgabe.cpp",
            "testFile": "test_aufgabe.cpp"
          },
          {
            "folder": "08_operator_overloading",
            "title": "C++ 08: Operator Overloading & Rule of Five",
            "taskFile": "aufgabe.cpp",
            "testFile": "test_aufgabe.cpp"
          }
        ]
      },
      {
        "id": "track_3_smart_pointers_stl",
        "title": "⚡ Lehrpfad 3: Modern C++20: Smart Pointer & STL",
        "description": "Templates, Smart Pointer (std::unique_ptr, std::shared_ptr), STL-Container (vector/map), Algorithmen, Lambdas & Structured Binding.",
        "certificateKey": "cpp_modern",
        "chapters": [
          {
            "folder": "09_templates_und_generische_programmierung",
            "title": "C++ 09: Function & Class Templates",
            "taskFile": "aufgabe.cpp",
            "testFile": "test_aufgabe.cpp"
          },
          {
            "folder": "10_smart_pointer_und_speichersicherheit",
            "title": "C++ 10: Smart Pointer (unique_ptr, shared_ptr)",
            "taskFile": "aufgabe.cpp",
            "testFile": "test_aufgabe.cpp"
          },
          {
            "folder": "11_standard_template_library_stl",
            "title": "C++ 11: STL Container (vector/map) & Algorithmen",
            "taskFile": "aufgabe.cpp",
            "testFile": "test_aufgabe.cpp"
          },
          {
            "folder": "12_lambdas_und_moderne_cpp20_features",
            "title": "C++ 12: C++ Lambdas, auto & Structured Binding",
            "taskFile": "aufgabe.cpp",
            "testFile": "test_aufgabe.cpp"
          }
        ]
      },
      {
        "id": "track_4_concurrency_master",
        "title": "💎 Lehrpfad 4: Concurrency, GoogleTest & Systems Master",
        "description": "std::thread, std::mutex, Streams & Binärdateien, GoogleTest (gtest) Suite & High-Performance 2D Physics Engine Master.",
        "certificateKey": "cpp_master",
        "chapters": [
          {
            "folder": "13_multithreading_mit_std_thread",
            "title": "C++ 13: Multithreading (std::thread & std::mutex)",
            "taskFile": "aufgabe.cpp",
            "testFile": "test_aufgabe.cpp"
          },
          {
            "folder": "14_dateiverarbeitung_und_streams",
            "title": "C++ 14: Dateiverarbeitung & Binäre Streams",
            "taskFile": "aufgabe.cpp",
            "testFile": "test_aufgabe.cpp"
          },
          {
            "folder": "15_googletest_gtest_unittesting",
            "title": "C++ 15: GoogleTest (gtest) & Assertions",
            "taskFile": "aufgabe.cpp",
            "testFile": "test_aufgabe.cpp"
          },
          {
            "folder": "16_master_abschlussprojekt_high_performance_engine",
            "title": "Master 16: High-Performance 2D Physics Simulation",
            "taskFile": "aufgabe.cpp",
            "testFile": "test_aufgabe.cpp"
          }
        ]
      }
    ]
  },
  "csharp": {
    "id": "csharp",
    "title": "C# 12 & Modernes .NET 8+ Enterprise",
    "language": "csharp",
    "icon": "💜",
    "runner": "csharp",
    "description": "Von C# 12 Top-Level Statements über Records, LINQ-Pipelines & Async/Await bis zu xUnit Testing & der Enterprise Order Processing Engine.",
    "tracks": [
      {
        "id": "track_1_csharp_basics",
        "title": "🌱 Lehrpfad 1: C# 12 Essentials & Moderne Syntax",
        "description": "Top-Level Statements, Nullable Reference Types, moderne Switch-Expressions, Collections und C# Tupel.",
        "certificateKey": "csharp_grundlagen",
        "chapters": [
          {
            "folder": "01_syntax_datentypen_und_top_level_statements",
            "title": "C# 01: Syntax, Top-Level Statements & Nullables",
            "taskFile": "Aufgabe.cs",
            "testFile": "TestAufgabe.cs"
          },
          {
            "folder": "02_kontrollfluss_und_pattern_matching",
            "title": "C# 02: Switch-Expressions & Pattern Matching",
            "taskFile": "Aufgabe.cs",
            "testFile": "TestAufgabe.cs"
          },
          {
            "folder": "03_arrays_listen_und_collections",
            "title": "C# 03: Arrays, List<T> & Collection Expressions",
            "taskFile": "Aufgabe.cs",
            "testFile": "TestAufgabe.cs"
          },
          {
            "folder": "04_methoden_parameter_und_tuples",
            "title": "C# 04: Methoden, Out/Ref & Tupel",
            "taskFile": "Aufgabe.cs",
            "testFile": "TestAufgabe.cs"
          }
        ]
      },
      {
        "id": "track_2_modern_oop",
        "title": "🏗️ Lehrpfad 2: Modernes OOP, Records & Interfaces",
        "description": "Primary Constructors, Records mit with-Expressions, Vererbung & Polymorphismus, Interfaces & Dependency Injection.",
        "certificateKey": "csharp_oop",
        "chapters": [
          {
            "folder": "05_klassen_objekte_und_primary_constructors",
            "title": "C# 05: Klassen, Properties & Primary Constructors",
            "taskFile": "Aufgabe.cs",
            "testFile": "TestAufgabe.cs"
          },
          {
            "folder": "06_records_und_immutability",
            "title": "C# 06: Records, Immutability & with-Expressions",
            "taskFile": "Aufgabe.cs",
            "testFile": "TestAufgabe.cs"
          },
          {
            "folder": "07_vererbung_polymorphismus_und_abstract",
            "title": "C# 07: Vererbung, Virtual/Override & Abstract",
            "taskFile": "Aufgabe.cs",
            "testFile": "TestAufgabe.cs"
          },
          {
            "folder": "08_interfaces_und_dependency_injection",
            "title": "C# 08: Interfaces & Dependency Injection",
            "taskFile": "Aufgabe.cs",
            "testFile": "TestAufgabe.cs"
          }
        ]
      },
      {
        "id": "track_3_linq_async",
        "title": "⚡ Lehrpfad 3: LINQ, Generics & Async/Await Tasks",
        "description": "Generics mit Constraints, LINQ-Pipelines (.Where/.Select/.GroupBy), asynchrone Tasks (async/await) und using-Disposal.",
        "certificateKey": "csharp_linq",
        "chapters": [
          {
            "folder": "09_generics_und_constraints",
            "title": "C# 09: Generics & Generic Constraints",
            "taskFile": "Aufgabe.cs",
            "testFile": "TestAufgabe.cs"
          },
          {
            "folder": "10_linq_funktionale_datenabfragen",
            "title": "C# 10: LINQ Datenabfragen & Fluent Chaining",
            "taskFile": "Aufgabe.cs",
            "testFile": "TestAufgabe.cs"
          },
          {
            "folder": "11_asynchrone_programmierung_mit_async_await",
            "title": "C# 11: Async/Await & Task.WhenAll Pipelines",
            "taskFile": "Aufgabe.cs",
            "testFile": "TestAufgabe.cs"
          },
          {
            "folder": "12_exception_handling_und_ressourcen",
            "title": "C# 12: Exceptions & using-Statements (IDisposable)",
            "taskFile": "Aufgabe.cs",
            "testFile": "TestAufgabe.cs"
          }
        ]
      },
      {
        "id": "track_4_enterprise_master",
        "title": "💎 Lehrpfad 4: Architektur, xUnit & Cloud Master",
        "description": "System.Text.Json, Events & Delegates, xUnit Unit-Testing ([Fact]/[Theory]) & Enterprise Order Processing Engine.",
        "certificateKey": "csharp_master",
        "chapters": [
          {
            "folder": "13_json_serialisierung_und_dateien",
            "title": "C# 13: System.Text.Json & Asynchrone Dateien",
            "taskFile": "Aufgabe.cs",
            "testFile": "TestAufgabe.cs"
          },
          {
            "folder": "14_events_delegates_und_lambdas",
            "title": "C# 14: Delegates, Action/Func & Events",
            "taskFile": "Aufgabe.cs",
            "testFile": "TestAufgabe.cs"
          },
          {
            "folder": "15_xunit_automatisiertes_unit_testing",
            "title": "C# 15: xUnit Tests, Data-Theories & Assertions",
            "taskFile": "Aufgabe.cs",
            "testFile": "TestAufgabe.cs"
          },
          {
            "folder": "16_master_abschlussprojekt_enterprise_order_engine",
            "title": "Master 16: Enterprise Order Processing & Analytics",
            "taskFile": "Aufgabe.cs",
            "testFile": "TestAufgabe.cs"
          }
        ]
      }
    ]
  },
  "go": {
    "id": "go",
    "title": "Go (Golang) Cloud Microservices & Systems",
    "language": "go",
    "icon": "⚡",
    "runner": "go",
    "description": "Vom statischen Typensystem über Structs & Interfaces, Goroutines & Channels bis zu net/http REST-APIs und dem Cloud Microservice Master.",
    "tracks": [
      {
        "id": "track_1_go_basics",
        "title": "🌱 Lehrpfad 1: Go Syntax, Typensystem & Kontrollfluss",
        "description": "Variablen, Typen, Type Inference (:=), Slices, Arrays, Maps, Schleifen (for/range) und Verzweigungen (if/switch).",
        "certificateKey": "go_grundlagen",
        "chapters": [
          {
            "folder": "01_syntax_variablen_und_typen",
            "title": "Go 01: Go Syntax, Variablen & Typensystem",
            "taskFile": "aufgabe.go",
            "testFile": "test_aufgabe.go"
          },
          {
            "folder": "02_slices_arrays_und_maps",
            "title": "Go 02: Slices, Dynamische Arrays & Maps",
            "taskFile": "aufgabe.go",
            "testFile": "test_aufgabe.go"
          },
          {
            "folder": "03_kontrollfluss_und_schleifen",
            "title": "Go 03: Kontrollfluss, for-Loops & switch",
            "taskFile": "aufgabe.go",
            "testFile": "test_aufgabe.go"
          },
          {
            "folder": "04_funktionen_und_multiple_returns",
            "title": "Go 04: Funktionen & Mehrfache Rückgabewerte",
            "taskFile": "aufgabe.go",
            "testFile": "test_aufgabe.go"
          }
        ]
      },
      {
        "id": "track_2_structs_interfaces",
        "title": "🏗️ Lehrpfad 2: Idiomatisches Go: Structs & Interfaces",
        "description": "Structs, Methoden mit Pointer-Receivern, Interfaces & Duck Typing, Explizites Error-Handling (if err != nil) & Defer/Panic/Recover.",
        "certificateKey": "go_oop",
        "chapters": [
          {
            "folder": "05_structs_und_methoden",
            "title": "Go 05: Structs, Instanziierung & Pointer-Methoden",
            "taskFile": "aufgabe.go",
            "testFile": "test_aufgabe.go"
          },
          {
            "folder": "06_interfaces_und_polymorphie",
            "title": "Go 06: Interfaces, Duck Typing & Polymorphie",
            "taskFile": "aufgabe.go",
            "testFile": "test_aufgabe.go"
          },
          {
            "folder": "07_explizites_error_handling",
            "title": "Go 07: Idiomatisches Error-Handling (if err != nil)",
            "taskFile": "aufgabe.go",
            "testFile": "test_aufgabe.go"
          },
          {
            "folder": "08_defer_panic_und_recover",
            "title": "Go 08: Ressourcensicherheit mit defer & Recover",
            "taskFile": "aufgabe.go",
            "testFile": "test_aufgabe.go"
          }
        ]
      },
      {
        "id": "track_3_concurrency",
        "title": "🚀 Lehrpfad 3: Concurrency: Goroutines & Channels",
        "description": "Leichtgewichtige Goroutines (go fn()), Unbuffered & Buffered Channels, select Multiplexing, sync.WaitGroup und sync.Mutex.",
        "certificateKey": "go_concurrency",
        "chapters": [
          {
            "folder": "09_goroutines_und_waitgroups",
            "title": "Go 09: Goroutines (go worker) & sync.WaitGroup",
            "taskFile": "aufgabe.go",
            "testFile": "test_aufgabe.go"
          },
          {
            "folder": "10_channels_und_datenfluss",
            "title": "Go 10: Buffered & Unbuffered Channels (<-)",
            "taskFile": "aufgabe.go",
            "testFile": "test_aufgabe.go"
          },
          {
            "folder": "11_select_und_timeouts",
            "title": "Go 11: select Multiplexing, Context & Timeouts",
            "taskFile": "aufgabe.go",
            "testFile": "test_aufgabe.go"
          },
          {
            "folder": "12_mutex_und_thread_safety",
            "title": "Go 12: Race Conditions vermeiden mit sync.Mutex",
            "taskFile": "aufgabe.go",
            "testFile": "test_aufgabe.go"
          }
        ]
      },
      {
        "id": "track_4_microservices_master",
        "title": "💎 Lehrpfad 4: REST-APIs, Microservices & Master",
        "description": "Standardbibliothek net/http, JSON Encoding/Decoding, Middleware-Pattern, automatisierte Unit-Tests mit testing Package & Cloud API Master.",
        "certificateKey": "go_master",
        "chapters": [
          {
            "folder": "13_http_server_und_routing",
            "title": "Go 13: HTTP Web Server & net/http Routing",
            "taskFile": "aufgabe.go",
            "testFile": "test_aufgabe.go"
          },
          {
            "folder": "14_json_apis_und_middleware",
            "title": "Go 14: REST JSON APIs & Chained Middleware",
            "taskFile": "aufgabe.go",
            "testFile": "test_aufgabe.go"
          },
          {
            "folder": "15_unit_testing_und_benchmarks",
            "title": "Go 15: Automatisiertes Testing & Benchmarks",
            "taskFile": "aufgabe.go",
            "testFile": "test_aufgabe.go"
          },
          {
            "folder": "16_master_abschlussprojekt_microservice",
            "title": "Master 16: High-Concurrency Microservice API",
            "taskFile": "aufgabe.go",
            "testFile": "test_aufgabe.go"
          }
        ]
      }
    ]
  },
  "html_css": {
    "id": "html_css",
    "title": "HTML5, Modern CSS3 & Responsive UI",
    "language": "html_css",
    "icon": "🎨",
    "runner": "html_css",
    "description": "Vom semantischen HTML5-Dokument über modernes CSS3 Box Model, Flexbox, CSS Grid Matrix bis zu Themes (Dark Mode) & SaaS Portfolio Master.",
    "tracks": [
      {
        "id": "track_1_html_basics",
        "title": "🌱 Lehrpfad 1: Semantisches HTML5 & Barrierefreiheit",
        "description": "Dokumentenstruktur, semantische Tags (header/main/footer/article), interaktive Formulare, Validierung & Accessibility (A11y/ARIA).",
        "certificateKey": "html_grundlagen",
        "chapters": [
          {
            "folder": "01_semantisches_html_und_struktur",
            "title": "HTML 01: Semantik & Dokumentenstruktur",
            "taskFile": "aufgabe.html",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "02_texte_listen_und_medien",
            "title": "HTML 02: Texte, Listen, Bilder & Videos",
            "taskFile": "aufgabe.html",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "03_formulare_und_validierung",
            "title": "HTML 03: Formulare & HTML5-Validierung",
            "taskFile": "aufgabe.html",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "04_barrierefreiheit_und_aria",
            "title": "HTML 04: Accessibility (A11y) & ARIA-Attribute",
            "taskFile": "aufgabe.html",
            "testFile": "test_aufgabe.js"
          }
        ]
      },
      {
        "id": "track_2_css_styling",
        "title": "🎨 Lehrpfad 2: Modern CSS3 Styling & Box Model",
        "description": "CSS-Selektoren, Kaskade, Spezifität, Box-Modell (Margin/Padding/Border), Custom Properties (CSS-Variablen) und Typografie.",
        "certificateKey": "css_styling",
        "chapters": [
          {
            "folder": "05_css_selektoren_und_kaskade",
            "title": "CSS 05: Selektoren, Kaskade & Spezifität",
            "taskFile": "aufgabe.html",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "06_box_modell_und_abstaende",
            "title": "CSS 06: Box-Modell, Padding, Margin & Border",
            "taskFile": "aufgabe.html",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "07_css_variablen_und_farbwelten",
            "title": "CSS 07: CSS Custom Properties & Farbsysteme",
            "taskFile": "aufgabe.html",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "08_typografie_und_webfonts",
            "title": "CSS 08: Web-Typografie, Schriftarten & Text-Effekte",
            "taskFile": "aufgabe.html",
            "testFile": "test_aufgabe.js"
          }
        ]
      },
      {
        "id": "track_3_layouts_and_responsive",
        "title": "📱 Lehrpfad 3: Responsive Layouts: Flexbox & Grid",
        "description": "Flexbox 1D-Layouts, CSS Grid 2D-Matrix, Media Queries (@media) für Mobile-First Design, Keyframe-Animationen & Transitions.",
        "certificateKey": "css_responsive",
        "chapters": [
          {
            "folder": "09_flexbox_achsen_und_alignment",
            "title": "CSS 09: Flexbox Achsen, Justify & Align",
            "taskFile": "aufgabe.html",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "10_css_grid_und_areas",
            "title": "CSS 10: CSS Grid 2D-Matrix & Template Areas",
            "taskFile": "aufgabe.html",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "11_media_queries_und_mobile_first",
            "title": "CSS 11: Media Queries & Mobile-First Design",
            "taskFile": "aufgabe.html",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "12_transitions_und_animationen",
            "title": "CSS 12: Transitions, Transforms & Keyframes",
            "taskFile": "aufgabe.html",
            "testFile": "test_aufgabe.js"
          }
        ]
      },
      {
        "id": "track_4_modern_ui_and_master",
        "title": "💎 Lehrpfad 4: CSS-Architektur, Themes & UI Master",
        "description": "BEM-Methodik, Dark/Light Themes (prefers-color-scheme), moderne UI-Komponenten (Glassmorphism/Cards) & SaaS Landingpage Master.",
        "certificateKey": "html_css_master",
        "chapters": [
          {
            "folder": "13_bem_methodik_und_modularitaet",
            "title": "CSS 13: BEM-Methodik & Modulare CSS-Architektur",
            "taskFile": "aufgabe.html",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "14_dark_mode_und_themes",
            "title": "CSS 14: Dark/Light Mode & System-Themes",
            "taskFile": "aufgabe.html",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "15_moderne_ui_komponenten",
            "title": "CSS 15: Moderne UI-Komponenten & Glassmorphism",
            "taskFile": "aufgabe.html",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "16_master_abschlussprojekt_saas_landingpage",
            "title": "Master 16: Responsive SaaS Landingpage & Portfolio",
            "taskFile": "aufgabe.html",
            "testFile": "test_aufgabe.js"
          }
        ]
      }
    ]
  },
  "ihk_ap1": {
    "id": "ihk_ap1",
    "title": "IHK AP1 Crashkurs: IT-Arbeitsplatz & Programmierung",
    "language": "ihk_ap1",
    "icon": "📘",
    "runner": "none",
    "description": "Lückenlose Vorbereitung auf die IHK-Abschlussprüfung Teil 1. Alle Lernfelder (LF 1 bis LF 8) mit interaktiven Übungen, 150-Fragen-Pool & 90-Minuten Probeprüfung.",
    "tracks": [
      {
        "id": "track_1_it_systeme",
        "title": "🌱 Lehrpfad 1: Basissysteme & Sicherheit (LF 1–4)",
        "description": "Unternehmen & Rolle im Betrieb, Hardware & Ergonomie, Subnetting & Netzwerke, Schutzbedarfsanalyse & DSGVO.",
        "certificateKey": "ihk_ap1_systeme",
        "chapters": [
          {
            "folder": "01_lf1_unternehmen_und_arbeitsplatz",
            "title": "LF 1: Unternehmen & Rolle im Betrieb (Organisation, Verträge, ITIL)",
            "taskFile": "README.md",
            "testFile": "index.html"
          },
          {
            "folder": "02_lf2_arbeitsplaetze_ausstatten",
            "title": "LF 2: Arbeitsplätze ausstatten (Hardware, Ergonomie, USV, NWA)",
            "taskFile": "README.md",
            "testFile": "index.html"
          },
          {
            "folder": "03_lf3_clients_in_netzwerke_einbinden",
            "title": "LF 3: Clients in Netzwerke einbinden (Subnetting, IPv6, LWL)",
            "taskFile": "README.md",
            "testFile": "index.html"
          },
          {
            "folder": "04_lf4_schutzbedarfsanalyse_und_cybersicherheit",
            "title": "LF 4: Schutzbedarfsanalyse & Cyber-Sicherheit (CIA, Backup, TOMs)",
            "taskFile": "README.md",
            "testFile": "index.html"
          }
        ]
      },
      {
        "id": "track_2_programmierung_und_datenbanken",
        "title": "💻 Lehrpfad 2: Software, CPS & Schnittstellen (LF 5–8)",
        "description": "Algorithmen & SQL-Datenbanken, Cyber-physische Systeme, Instandhaltung & Fehlerdiagnose, REST-Schnittstellen.",
        "certificateKey": "ihk_ap1_programmierung",
        "chapters": [
          {
            "folder": "05_lf5_software_zur_datenverwaltung",
            "title": "LF 5: Software zur Datenverwaltung anpassen (Trace, UML, SQL)",
            "taskFile": "README.md",
            "testFile": "index.html"
          },
          {
            "folder": "06_lf6_cyber_physische_systeme_iot",
            "title": "LF 6: Das Cyber-Physische System ergänzen (Sensoren, Aktoren, MQTT)",
            "taskFile": "README.md",
            "testFile": "index.html"
          },
          {
            "folder": "07_lf7_instandhaltung_und_fehlerdiagnose",
            "title": "LF 7: Cyber-Physische Systeme instand halten (Diagnose, ESD, Messen)",
            "taskFile": "README.md",
            "testFile": "index.html"
          },
          {
            "folder": "08_lf8_datenfluesse_und_schnittstellen",
            "title": "LF 8: Datenflüsse optimieren & Schnittstellen anpassen (REST, JSON, JWT)",
            "taskFile": "README.md",
            "testFile": "index.html"
          }
        ]
      },
      {
        "id": "track_3_praxis_drills",
        "title": "⚡ Lehrpfad 3: Interaktive Praxis-Drills & Labore",
        "description": "Trace-Tabellen-Trainer mit zeilenweiser Prüfung, Relationales SQL-Labor & Subnetting-Drill Master.",
        "certificateKey": "ihk_ap1_prozesse",
        "chapters": [
          {
            "folder": "09_trace_tabellen_trainer",
            "title": "Drill 1: Interaktiver Trace-Tabellen-Trainer (LF 5)",
            "taskFile": "README.md",
            "testFile": "index.html"
          },
          {
            "folder": "10_sql_datenbank_labor",
            "title": "Drill 2: Relationale Datenbanken & Live-SQL Labor (LF 5)",
            "taskFile": "README.md",
            "testFile": "index.html"
          },
          {
            "folder": "11_subnetting_drill_master",
            "title": "Drill 3: Endlos Subnetting-Drill Generator (LF 3)",
            "taskFile": "README.md",
            "testFile": "index.html"
          }
        ]
      },
      {
        "id": "track_4_probepruefung",
        "title": "🏆 Lehrpfad 4: Offizielle AP1 Probeprüfung & Notenrechner",
        "description": "90-Minuten Realtime Prüfungsmodus mit Countdown, 100 Punkten, Zufallsgenerator aus 150 Fragen & Erwartungshorizont.",
        "certificateKey": "ihk_ap1_master",
        "chapters": [
          {
            "folder": "12_ap1_probepruefung_simulation",
            "title": "Probeprüfung AP1: 90 Min. Realtime Simulation (100 Pkt.)",
            "taskFile": "README.md",
            "testFile": "index.html"
          }
        ]
      }
    ]
  },
  "ihk_ap2_fisi": {
    "id": "ihk_ap2_fisi",
    "title": "IHK AP2 Crashkurs: Fachinformatiker Systemintegration",
    "language": "ihk_ap2_fisi",
    "icon": "📕",
    "runner": "none",
    "description": "Vollständige Prüfungsvorbereitung für FISI (LF 9–12, WiSo, 40h-Projekt). VLANs, OSPF, Active Directory, RAID-Simulator, Cloud & 3 vollständige Probeprüfungen.",
    "tracks": [
      {
        "id": "track_1_netzwerke_und_server",
        "title": "🌱 Lehrpfad 1: Enterprise Netzwerke & Serverdienste (LF 9 & 10)",
        "description": "VLANs (802.1Q), LACP, Spanning Tree, OSPF, BGP, Active Directory, Gruppenrichtlinien, PKI & Ansible.",
        "certificateKey": "ihk_ap2_netzwerke",
        "chapters": [
          {
            "folder": "01_lf9_netzwerke_und_dienste",
            "title": "LF 9: Netzwerke & Dienste bereitstellen (VLAN, Routing, Firewalls)",
            "taskFile": "README.md",
            "testFile": "index.html"
          },
          {
            "folder": "02_lf10_serverdienste_und_automation",
            "title": "LF 10: Serverdienste & Automation bereitstellen (AD DS, DNS, Ansible)",
            "taskFile": "README.md",
            "testFile": "index.html"
          }
        ]
      },
      {
        "id": "track_2_storage_und_cloud",
        "title": "🛡️ Lehrpfad 2: Storage, Hochverfügbarkeit & Cloud (LF 11 & 12)",
        "description": "RAID 0/1/5/6/10, SAN/NAS, HA-Cluster, Quorum, STONITH, ZFS, Hypervisoren, Docker, Kubernetes & Prometheus.",
        "certificateKey": "ihk_ap2_sicherheit",
        "chapters": [
          {
            "folder": "03_lf11_speicher_und_hochverfuegbarkeit",
            "title": "LF 11: Speicher- & Hochverfügbarkeitssysteme (RAID, SAN, Cluster)",
            "taskFile": "README.md",
            "testFile": "index.html"
          },
          {
            "folder": "04_lf12_virtualisierung_und_cloud",
            "title": "LF 12: Virtualisierung, Cloud & Automation (Docker, K8s, IaC)",
            "taskFile": "README.md",
            "testFile": "index.html"
          }
        ]
      },
      {
        "id": "track_3_wiso_und_projekt",
        "title": "☁️ Lehrpfad 3: WiSo & 40h-Betriebliche Projektarbeit",
        "description": "Wirtschafts- & Sozialkunde (Arbeitsrecht, KSchG, Sozialversicherung) & Leitfaden zur 40h-Projektarbeit samt Fachgespräch.",
        "certificateKey": "ihk_ap2_wiso_projekt",
        "chapters": [
          {
            "folder": "05_wiso_arbeitsrecht_und_wirtschaft",
            "title": "WiSo: Wirtschafts- & Sozialkunde Prüfungs-Fit (BGB, KSchG, BetrVG)",
            "taskFile": "README.md",
            "testFile": "index.html"
          },
          {
            "folder": "06_betriebliche_projektarbeit_guide",
            "title": "Projekt: Betriebliche Projektarbeit (40h) & Fachgespräch-Guide",
            "taskFile": "README.md",
            "testFile": "index.html"
          }
        ]
      },
      {
        "id": "track_4_probepruefungen",
        "title": "🏆 Lehrpfad 4: Offizielle AP2 Probeprüfungen & Simulationen",
        "description": "Die 3 schriftlichen IHK-Prüfungsteile unter Realbedingungen (Teil 1: 90 Min., Teil 2: 90 Min., WiSo: 60 Min.) mit 150-Fragen-Zufallsgenerator.",
        "certificateKey": "ihk_ap2_fisi_master",
        "chapters": [
          {
            "folder": "07_ap2_teil_1_probepruefung",
            "title": "Probeprüfung AP2 Teil 1: Planen & Umsetzen (90 Min. / 100 Pkt.)",
            "taskFile": "README.md",
            "testFile": "index.html"
          },
          {
            "folder": "08_ap2_teil_2_probepruefung",
            "title": "Probeprüfung AP2 Teil 2: Administration & Netzanalyse (90 Min. / 100 Pkt.)",
            "taskFile": "README.md",
            "testFile": "index.html"
          },
          {
            "folder": "09_ap2_wiso_probepruefung",
            "title": "Probeprüfung AP2 WiSo: Wirtschafts- & Sozialkunde (60 Min. / 100 Pkt.)",
            "taskFile": "README.md",
            "testFile": "index.html"
          }
        ]
      }
    ]
  },
  "java": {
    "id": "java",
    "title": "Java 21+ Enterprise & IHK/Uni Standard",
    "language": "java",
    "icon": "☕",
    "runner": "java",
    "description": "Vom statischen Typensystem über reine OOP, Kapselung & Records bis zu Generics, Streams API, Virtual Threads Loom & JUnit 5 Banking Master.",
    "tracks": [
      {
        "id": "track_1_java_basics",
        "title": "🌱 Lehrpfad 1: Java Syntax, Typen & Kontrollfluss",
        "description": "Primitive Typen, main()-Einstieg, moderne switch-Expressions (->), Schleifen, Arrays und Methodenüberladung.",
        "certificateKey": "java_grundlagen",
        "chapters": [
          {
            "folder": "01_java_syntax_und_primitive_typen",
            "title": "Java 01: Java Syntax & Primitive Datentypen",
            "taskFile": "Aufgabe.java",
            "testFile": "TestAufgabe.java"
          },
          {
            "folder": "02_kontrollfluss_und_verzweigungen",
            "title": "Java 02: Kontrollfluss & Switch-Expressions",
            "taskFile": "Aufgabe.java",
            "testFile": "TestAufgabe.java"
          },
          {
            "folder": "03_schleifen_und_arrays",
            "title": "Java 03: Schleifen, For-Each & Arrays",
            "taskFile": "Aufgabe.java",
            "testFile": "TestAufgabe.java"
          },
          {
            "folder": "04_methoden_und_parameter",
            "title": "Java 04: Methoden, Static & Overloading",
            "taskFile": "Aufgabe.java",
            "testFile": "TestAufgabe.java"
          }
        ]
      },
      {
        "id": "track_2_pure_oop",
        "title": "🏗️ Lehrpfad 2: Reine Objektorientierung & Kapselung",
        "description": "Klassen, Konstruktoren, Kapselung, Immutability & Java 17+ Records, Vererbung (extends), Polymorphie & Interfaces.",
        "certificateKey": "java_oop",
        "chapters": [
          {
            "folder": "05_klassen_objekte_und_konstruktoren",
            "title": "Java 05: Klassen, Objekte & Konstruktoren",
            "taskFile": "Aufgabe.java",
            "testFile": "TestAufgabe.java"
          },
          {
            "folder": "06_kapselung_und_records",
            "title": "Java 06: Kapselung, Immutability & Records",
            "taskFile": "Aufgabe.java",
            "testFile": "TestAufgabe.java"
          },
          {
            "folder": "07_vererbung_polymorphie_und_super",
            "title": "Java 07: Vererbung, Polymorphie & Abstract Classes",
            "taskFile": "Aufgabe.java",
            "testFile": "TestAufgabe.java"
          },
          {
            "folder": "08_interfaces_und_default_methods",
            "title": "Java 08: Interfaces, Default Methods & Kopplung",
            "taskFile": "Aufgabe.java",
            "testFile": "TestAufgabe.java"
          }
        ]
      },
      {
        "id": "track_3_collections_streams",
        "title": "⚡ Lehrpfad 3: Generics, Collections & Modern Streams",
        "description": "Generics <T>, Java Collections Framework (List/Set/Map), Exception-Hierarchien, try-with-resources, Streams API & Optional.",
        "certificateKey": "java_streams",
        "chapters": [
          {
            "folder": "09_generics_und_type_safety",
            "title": "Java 09: Generics <T> & Type Safety",
            "taskFile": "Aufgabe.java",
            "testFile": "TestAufgabe.java"
          },
          {
            "folder": "10_collections_framework_list_set_map",
            "title": "Java 10: Collections (ArrayList, HashSet, HashMap)",
            "taskFile": "Aufgabe.java",
            "testFile": "TestAufgabe.java"
          },
          {
            "folder": "11_exceptions_und_ressourcenmanagement",
            "title": "Java 11: Exceptions & Try-with-Resources",
            "taskFile": "Aufgabe.java",
            "testFile": "TestAufgabe.java"
          },
          {
            "folder": "12_lambdas_streams_api_und_optional",
            "title": "Java 12: Lambdas, Streams API & Optional",
            "taskFile": "Aufgabe.java",
            "testFile": "TestAufgabe.java"
          }
        ]
      },
      {
        "id": "track_4_enterprise_master",
        "title": "💎 Lehrpfad 4: Enterprise Architekturen & Masterprojekt",
        "description": "NIO.2 Dateiverarbeitung, Java 21 Virtual Threads (Loom), JUnit 5 Unittesting & Enterprise Banking Core Master.",
        "certificateKey": "java_master",
        "chapters": [
          {
            "folder": "13_dateien_json_und_persistenz",
            "title": "Java 13: Modernes Dateihandling (NIO.2) & JSON",
            "taskFile": "Aufgabe.java",
            "testFile": "TestAufgabe.java"
          },
          {
            "folder": "14_multithreading_und_virtual_threads",
            "title": "Java 14: Virtual Threads (Loom) & Concurrency",
            "taskFile": "Aufgabe.java",
            "testFile": "TestAufgabe.java"
          },
          {
            "folder": "15_junit_5_automatisiertes_unit_testing",
            "title": "Java 15: JUnit 5 Testsuites & Assertions",
            "taskFile": "Aufgabe.java",
            "testFile": "TestAufgabe.java"
          },
          {
            "folder": "16_master_abschlussprojekt_banking_system",
            "title": "Master 16: Enterprise Banking Core & Transactions",
            "taskFile": "Aufgabe.java",
            "testFile": "TestAufgabe.java"
          }
        ]
      }
    ]
  },
  "javascript": {
    "id": "javascript",
    "title": "JavaScript & Moderne Web-Entwicklung",
    "language": "javascript",
    "icon": "🌐",
    "runner": "javascript",
    "description": "Vom Einsteiger über moderne ES6+-Features, OOP, Reguläre Ausdrücke, Asynchronität bis hin zu TypeScript und dem Master-Abschlussprojekt.",
    "tracks": [
      {
        "id": "track_1_grundlagen",
        "title": "🌱 Lehrpfad 1: JavaScript Grundlagen & ES6",
        "description": "Variablen, Kontrollfluss, Funktionen, Scopes, Arrays, Sets, Maps, Objekte & Destructuring.",
        "certificateKey": "js_grundlagen",
        "chapters": [
          {
            "folder": "01_erste_schritte_variablen",
            "title": "JS 01: Variablen, Typen & Template-Strings",
            "taskFile": "aufgabe.js",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "02_kontrollfluss_und_schleifen",
            "title": "JS 02: Kontrollfluss & Schleifen",
            "taskFile": "aufgabe.js",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "03_funktionen_und_scope",
            "title": "JS 03: Funktionen, Arrow Functions & Scope",
            "taskFile": "aufgabe.js",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "04_arrays_sets_und_maps",
            "title": "JS 04: Arrays, Sets & Maps",
            "taskFile": "aufgabe.js",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "05_objekte_und_destructuring",
            "title": "JS 05: Objekte, Destructuring & Rest/Spread",
            "taskFile": "aufgabe.js",
            "testFile": "test_aufgabe.js"
          }
        ]
      },
      {
        "id": "track_2_oop_und_daten",
        "title": "🏗️ Lehrpfad 2: Moderne Datenmodelle & OOP",
        "description": "Objektorientierung mit ES6-Klassen, Reguläre Ausdrücke (RegExp) & strukturierte Fehlerbehandlung mit Error-Klassen.",
        "certificateKey": "js_oop",
        "chapters": [
          {
            "folder": "06_klassen_und_oop",
            "title": "JS 06: Klassen & Objektorientierung (OOP)",
            "taskFile": "aufgabe.js",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "07_regex_und_textverarbeitung",
            "title": "JS 07: Reguläre Ausdrücke & Textverarbeitung",
            "taskFile": "aufgabe.js",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "08_fehlerbehandlung_und_debugging",
            "title": "JS 08: Fehlerbehandlung & Debugging",
            "taskFile": "aufgabe.js",
            "testFile": "test_aufgabe.js"
          }
        ]
      },
      {
        "id": "track_3_web_und_async",
        "title": "⚡ Lehrpfad 3: Web-APIs, DOM & Asynchronität",
        "description": "DOM-Manipulation, Web Storage, Callbacks, Promises, Async/Await und REST-APIs (Fetch).",
        "certificateKey": "js_async",
        "chapters": [
          {
            "folder": "09_dom_und_events",
            "title": "JS 09: DOM-Manipulation & Events",
            "taskFile": "aufgabe.js",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "10_web_storage_und_json",
            "title": "JS 10: Web Storage & JSON",
            "taskFile": "aufgabe.js",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "11_callbacks_und_promises",
            "title": "JS 11: Callbacks, Event Loop & Promises",
            "taskFile": "aufgabe.js",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "12_async_await_und_fetch",
            "title": "JS 12: Async/Await & REST-APIs (Fetch)",
            "taskFile": "aufgabe.js",
            "testFile": "test_aufgabe.js"
          }
        ]
      },
      {
        "id": "track_4_typescript_und_master",
        "title": "🛡️ Lehrpfad 4: Architektur, TypeScript & Masterprojekt",
        "description": "ES-Module, statische Typsicherheit mit TypeScript, Interfaces, Generics und vollwertige MVC-Applikation.",
        "certificateKey": "js_master",
        "chapters": [
          {
            "folder": "13_es_module_und_architektur",
            "title": "JS 13: ES-Module & Clean Architecture",
            "taskFile": "aufgabe.js",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "14_einstieg_typescript",
            "title": "TS 14: TypeScript Type Safety & Interfaces",
            "taskFile": "aufgabe.js",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "15_typescript_fortgeschritten",
            "title": "TS 15: TypeScript Generics & Advanced Types",
            "taskFile": "aufgabe.js",
            "testFile": "test_aufgabe.js"
          },
          {
            "folder": "16_master_abschlussprojekt_web_app",
            "title": "Master 16: Interaktive Task-App (MVC)",
            "taskFile": "aufgabe.js",
            "testFile": "test_aufgabe.js"
          }
        ]
      }
    ]
  },
  "powershell": {
    "id": "powershell",
    "title": "Modern PowerShell 7+ Core & Cloud Automation",
    "language": "powershell",
    "icon": "🔷",
    "runner": "powershell",
    "description": "Vom Cmdlet-Einsteiger über .NET-Objekt-Pipelines, Multithreading (ForEach-Object -Parallel), REST-APIs bis zu Pester v5 Unittests & Cloud Engineering.",
    "tracks": [
      {
        "id": "track_1_ps7_essentials",
        "title": "🌱 Lehrpfad 1: PowerShell 7+ Essentials & Objekt-Pipeline",
        "description": "Verb-Noun Cmdlets, die .NET-Objekt-Pipeline, Where-Object Filterung, Select-Object Projektion und PSCustomObjects.",
        "certificateKey": "ps_grundlagen",
        "chapters": [
          {
            "folder": "01_powershell_konsole_und_cmdlet_architektur",
            "title": "PS 01: Cmdlet-Architektur & Verb-Noun Syntax",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "02_die_objekt_pipeline_und_get_member",
            "title": "PS 02: Die Objekt-Pipeline & Get-Member",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "03_filterung_sortierung_und_projektion",
            "title": "PS 03: Where-Object, Select & Calculated Properties",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "04_variablen_datentypen_und_pscustomobject",
            "title": "PS 04: Typisierung, Hashtables & PSCustomObject",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          }
        ]
      },
      {
        "id": "track_2_skripting_und_errorhandling",
        "title": "⚡ Lehrpfad 2: Skripting, Kontrollfluss & Error-Handling",
        "description": "Moderne Operatoren (Ternary, Null-Coalescing), Schleifen, erweiterte Cmdlet-Funktionen mit [CmdletBinding()] und Try/Catch.",
        "certificateKey": "ps_scripting",
        "chapters": [
          {
            "folder": "05_kontrollfluss_und_moderne_operatoren",
            "title": "PS 05: Kontrollfluss & Moderne PS7 Operatoren",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "06_schleifen_und_pipeline_durchlaeufe",
            "title": "PS 06: Schleifen (foreach, while & Pipeline)",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "07_erweiterte_funktionen_und_parameter",
            "title": "PS 07: Eigene Cmdlets [CmdletBinding()] & Validierung",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "08_robustes_error_handling_und_try_catch",
            "title": "PS 08: Robustes Error-Handling (Try/Catch/Finally)",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          }
        ]
      },
      {
        "id": "track_3_parallelisierung_und_rest",
        "title": "🚀 Lehrpfad 3: Parallelisierung, REST-APIs & Datenformate",
        "description": "Multithreading mit ForEach-Object -Parallel, Start-ThreadJob, REST-APIs mit Invoke-RestMethod, PSDrives und SecretManagement.",
        "certificateKey": "ps_performance",
        "chapters": [
          {
            "folder": "09_multithreading_mit_foreach_object_parallel",
            "title": "PS 09: Multithreading mit ForEach-Object -Parallel",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "10_json_csv_xml_und_rest_apis",
            "title": "PS 10: REST-APIs & JSON-Pipelines (Invoke-RestMethod)",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "11_dateisystem_registry_und_psprovider",
            "title": "PS 11: Dateisystem, PSDrives (Env/Cert) & Hashes",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "12_sicherheit_und_credentials_management",
            "title": "PS 12: Sicherheit, Execution Policies & Secrets",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          }
        ]
      },
      {
        "id": "track_4_enterprise_und_cloud_master",
        "title": "💎 Lehrpfad 4: Enterprise Modules, Pester Testing & Masterprojekt",
        "description": "Modul-Entwicklung (.psm1/.psd1), Pester v5 Unittests, Cloud-Automatisierung und Cloud Ops Masterprojekt.",
        "certificateKey": "ps_master",
        "chapters": [
          {
            "folder": "13_modul_entwicklung_und_manifeste",
            "title": "PS 13: Enterprise Module & Manifeste (.psd1)",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "14_pester_automatisierte_unit_tests",
            "title": "PS 14: Pester v5 Automatisiertes Testing & Mocking",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "15_cloud_und_cross_platform_automatisierung",
            "title": "PS 15: Cross-Platform Cloud Automation (Az & AWS)",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "16_master_abschlussprojekt_cloud_ops_engine",
            "title": "Master 16: Multi-Threaded Cloud & Server Ops Engine",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          }
        ]
      }
    ]
  },
  "python": {
    "id": "python",
    "title": "Python Software Engineering",
    "language": "python",
    "icon": "🐍",
    "runner": "python",
    "description": "Vom Einsteiger über professionelle Objektorientierung bis hin zu Data Engineering und Desktop-Apps in 33 Modulen.",
    "tracks": [
      {
        "id": "lehrpfad_1_grundlagen",
        "title": "🌱 Lehrpfad 1: Grundlagen der Programmierung",
        "description": "Zahlen, Variablen, Bedingungen, Schleifen, Funktionen, Listen, Strings, Dicts & Sets.",
        "certificateKey": "lehrpfad_1",
        "chapters": [
          {
            "folder": "01_erste_schritte_taschenrechner",
            "title": "G01: Python als Taschenrechner",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "02_variablen_und_datentypen",
            "title": "G02: Variablen & Datentypen",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "03_ein_und_ausgabe",
            "title": "G03: Interaktive Ein- & Ausgabe",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "04_verzweigungen_und_bedingungen",
            "title": "G04: Verzweigungen & Bedingungen",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "05_schleifen_und_wiederholungen",
            "title": "G05: Schleifen & Wiederholungen",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "06_funktionen_und_module",
            "title": "G06: Eigene Funktionen & Module",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "07_listen_und_sequenzen",
            "title": "G07: Listen & Sequenzen",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "08_textverarbeitung_und_strings",
            "title": "G08: Textverarbeitung & Strings",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "09_dictionaries_und_sets",
            "title": "G09: Dictionaries & Sets",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "10_comprehensions_datum_algorithmen",
            "title": "G10: Comprehensions & Algorithmen",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          }
        ]
      },
      {
        "id": "lehrpfad_2_oop_einstieg",
        "title": "🏗️ Lehrpfad 2: Einstieg in die Objektorientierung (OOP)",
        "description": "Klassen, Konstruktor, self, Methoden, Tools (VS Code & Git) und Tamagotchi-Projekt.",
        "certificateKey": "lehrpfad_2",
        "chapters": [
          {
            "folder": "00_fehlersuche_und_grundlagen",
            "title": "OOP 00: Python-Fehlersuche",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "01_einstieg_klassen",
            "title": "OOP 01: Erste Klassen & Instanzen",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "02_init_und_self",
            "title": "OOP 02: Konstruktor __init__ & self",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "03_methoden_und_verhalten",
            "title": "OOP 03: Methoden & Verhalten",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "04_str_und_darstellung",
            "title": "OOP 04: __str__ & String-Darstellung",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "04b_umstieg_vscode",
            "title": "Tooling 04b: Umstieg auf VS Code",
            "taskFile": "vscode_test.py",
            "testFile": ""
          },
          {
            "folder": "04c_git_und_versionskontrolle",
            "title": "Tooling 04c: Git & Versionskontrolle",
            "taskFile": "git_uebung.py",
            "testFile": ""
          },
          {
            "folder": "05_objekte_kombinieren",
            "title": "OOP 05: Objekte kombinieren",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "06_abschlussprojekt_tamagotchi",
            "title": "Projekt 06: Virtuelles Haustier (Tamagotchi)",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          }
        ]
      },
      {
        "id": "lehrpfad_3_fortgeschrittenes_oop",
        "title": "🚀 Lehrpfad 3: Fortgeschrittenes OOP & GUIs",
        "description": "Speicher-Referenzen, Dunder-Methoden, TDD, Vererbung, Polymorphie, Exceptions, JSON/CSV, Tkinter & Masterprojekt.",
        "certificateKey": "lehrpfad_3",
        "chapters": [
          {
            "folder": "07_referenzen_und_speicher",
            "title": "Adv 07: Referenzen & Speicher",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "08_operator_overloading_dunder",
            "title": "Adv 08: Operator Overloading & Dunder",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "09_eigene_unit_tests_schreiben",
            "title": "Adv 09: Eigene Unit Tests & TDD",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "10_vererbung_und_super",
            "title": "Adv 10: Vererbung & super()",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "11_polymorphie_und_interfaces",
            "title": "Adv 11: Polymorphie & Interfaces",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "12_exceptions_und_fehlerbehandlung",
            "title": "Adv 12: Exceptions & Fehlerbehandlung",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "13_persistenz_json_und_csv",
            "title": "Adv 13: Datei-Persistenz (JSON & CSV)",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "14_gui_mit_tkinter",
            "title": "Adv 14: Desktop-GUIs mit Tkinter",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "15_parameter_und_container",
            "title": "Adv 15: Parameter & Eigene Container",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "16_master_abschlussprojekt",
            "title": "Master 16: Master-Abschlussprojekt",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          }
        ]
      },
      {
        "id": "lehrpfad_4_professional_data_engineering",
        "title": "🌟 Lehrpfad 4: Python Professional & Data Engineering",
        "description": "Reguläre Ausdrücke (re), funktionale Idiome, Generatoren, Dataclasses, Type Hints, SQLite & REST-APIs.",
        "certificateKey": "lehrpfad_4",
        "chapters": [
          {
            "folder": "17_regulaere_ausdruecke_re",
            "title": "Pro 17: Reguläre Ausdrücke (re)",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "18_funktionale_programmierung_lambda",
            "title": "Pro 18: Funktionale Programmierung (lambda)",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "19_generatoren_und_itertools",
            "title": "Pro 19: Generatoren & itertools (yield)",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "20_dataclasses_und_typehints",
            "title": "Pro 20: Dataclasses & Type Hints",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "21_datenbanken_und_sqlite",
            "title": "Pro 21: Relationale Datenbanken & SQLite",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          },
          {
            "folder": "22_web_apis_und_json_feeds",
            "title": "Pro 22: Web-APIs & JSON-Feeds",
            "taskFile": "aufgabe.py",
            "testFile": "test_aufgabe.py"
          }
        ]
      }
    ]
  },
  "rust": {
    "id": "rust",
    "title": "Rust Modern Systems & WebAssembly",
    "language": "rust",
    "icon": "🦀",
    "runner": "rust",
    "description": "Vom revolutionären Ownership- & Borrowing-System über Structs, Enums, Option/Result bis zu Traits, Fearless Concurrency & LRU Cache Master.",
    "tracks": [
      {
        "id": "track_1_rust_basics",
        "title": "🌱 Lehrpfad 1: Rust Grundlagen & Ownership-System",
        "description": "Variablen, Typen, Mutabilität, Move-Semantik, Stack vs. Heap, Referenzen &mut, Slices und Pattern Matching.",
        "certificateKey": "rust_grundlagen",
        "chapters": [
          {
            "folder": "01_variablen_mutabilitaet_und_typen",
            "title": "Rust 01: Variablen, Mutabilität & Typensystem",
            "taskFile": "aufgabe.rs",
            "testFile": "test_aufgabe.rs"
          },
          {
            "folder": "02_das_ownership_und_borrowing_system",
            "title": "Rust 02: Ownership, Move & Borrowing (&/&mut)",
            "taskFile": "aufgabe.rs",
            "testFile": "test_aufgabe.rs"
          },
          {
            "folder": "03_slices_und_lifetimes_grundlagen",
            "title": "Rust 03: Slices (&str/&[T]) & Lifetimes ('a)",
            "taskFile": "aufgabe.rs",
            "testFile": "test_aufgabe.rs"
          },
          {
            "folder": "04_kontrollfluss_und_pattern_matching",
            "title": "Rust 04: Kontrollfluss & match Pattern Matching",
            "taskFile": "aufgabe.rs",
            "testFile": "test_aufgabe.rs"
          }
        ]
      },
      {
        "id": "track_2_structs_enums",
        "title": "🏗️ Lehrpfad 2: Structs, Enums & Error-Handling",
        "description": "Structs, impl-Methodenblöcke, Option<T> Monade, Result<T, E> mit ?-Operator und Cargo Multi-File Modul-Architektur.",
        "certificateKey": "rust_structs",
        "chapters": [
          {
            "folder": "05_structs_und_impl_methoden",
            "title": "Rust 05: Structs, impl-Methoden & Konstruktoren",
            "taskFile": "aufgabe.rs",
            "testFile": "test_aufgabe.rs"
          },
          {
            "folder": "06_enums_und_option_monade",
            "title": "Rust 06: Enums, Option<T> & if let",
            "taskFile": "aufgabe.rs",
            "testFile": "test_aufgabe.rs"
          },
          {
            "folder": "07_robustes_error_handling_mit_result",
            "title": "Rust 07: Result<T, E> & der ?-Operator",
            "taskFile": "aufgabe.rs",
            "testFile": "test_aufgabe.rs"
          },
          {
            "folder": "08_packages_crates_und_module",
            "title": "Rust 08: Packages, Crates & Multi-File Module",
            "taskFile": "aufgabe.rs",
            "testFile": "test_aufgabe.rs"
          }
        ]
      },
      {
        "id": "track_3_traits_generics",
        "title": "⚡ Lehrpfad 3: Traits, Generics & Smart Pointer",
        "description": "Traits, Trait Bounds, Monomorphisierung vs. Trait Objects (dyn Trait), Closures, Iterator-Pipelines & Smart Pointer (Box/Rc/RefCell).",
        "certificateKey": "rust_traits",
        "chapters": [
          {
            "folder": "09_traits_und_shared_behavior",
            "title": "Rust 09: Traits & Shared Behavior",
            "taskFile": "aufgabe.rs",
            "testFile": "test_aufgabe.rs"
          },
          {
            "folder": "10_generics_und_dynamischer_dispatch",
            "title": "Rust 10: Generics & Trait Objects (dyn Trait)",
            "taskFile": "aufgabe.rs",
            "testFile": "test_aufgabe.rs"
          },
          {
            "folder": "11_iteratoren_und_closures",
            "title": "Rust 11: Closures & Iterator Pipelines",
            "taskFile": "aufgabe.rs",
            "testFile": "test_aufgabe.rs"
          },
          {
            "folder": "12_smart_pointer_und_speichersicherheit",
            "title": "Rust 12: Smart Pointer (Box<T>, Rc<T>, RefCell<T>)",
            "taskFile": "aufgabe.rs",
            "testFile": "test_aufgabe.rs"
          }
        ]
      },
      {
        "id": "track_4_concurrency_master",
        "title": "💎 Lehrpfad 4: Fearless Concurrency & Systems Master",
        "description": "Thread Spawning, MPSC Channels, Send & Sync Traits, Arc<Mutex<T>>, Cargo Testsuite & High-Speed In-Memory LRU Cache Master.",
        "certificateKey": "rust_master",
        "chapters": [
          {
            "folder": "13_fearless_concurrency_threads_und_channels",
            "title": "Rust 13: Threads & MPSC Channels",
            "taskFile": "aufgabe.rs",
            "testFile": "test_aufgabe.rs"
          },
          {
            "folder": "14_shared_state_concurrency",
            "title": "Rust 14: Shared State Concurrency (Arc<Mutex<T>>)",
            "taskFile": "aufgabe.rs",
            "testFile": "test_aufgabe.rs"
          },
          {
            "folder": "15_automatisiertes_testing_mit_cargo_test",
            "title": "Rust 15: Automatisierte Tests mit cargo test",
            "taskFile": "aufgabe.rs",
            "testFile": "test_aufgabe.rs"
          },
          {
            "folder": "16_master_abschlussprojekt_high_speed_cache",
            "title": "Master 16: High-Speed In-Memory LRU Cache Engine",
            "taskFile": "aufgabe.rs",
            "testFile": "test_aufgabe.rs"
          }
        ]
      }
    ]
  },
  "sql": {
    "id": "sql",
    "title": "SQL & Relationale Datenbanken",
    "language": "sql",
    "icon": "🗄️",
    "runner": "sql",
    "description": "Vom ersten SELECT über relationale Joins, Normalisierung (1NF-3NF) bis zu CTEs, Window Functions (OVER) und dem Analytics Data Warehouse Master.",
    "tracks": [
      {
        "id": "track_1_grundlagen",
        "title": "🌱 Lehrpfad 1: SQL-Grundlagen & CRUD-Operationen",
        "description": "Tabellen anlegen, Datentypen, Constraints, Filterung mit WHERE, Daten einfügen, aktualisieren und löschen.",
        "certificateKey": "sql_grundlagen",
        "chapters": [
          {
            "folder": "01_tabellen_und_select",
            "title": "SQL 01: Tabellen anlegen & SELECT",
            "taskFile": "aufgabe.sql",
            "testFile": "test_aufgabe.sql"
          },
          {
            "folder": "02_filterung_und_logische_operatoren",
            "title": "SQL 02: Filterung mit WHERE, LIKE & BETWEEN",
            "taskFile": "aufgabe.sql",
            "testFile": "test_aufgabe.sql"
          },
          {
            "folder": "03_daten_aktualisieren_und_loeschen",
            "title": "SQL 03: UPDATE, DELETE & ALTER TABLE",
            "taskFile": "aufgabe.sql",
            "testFile": "test_aufgabe.sql"
          },
          {
            "folder": "04_datentypen_und_constraints",
            "title": "SQL 04: Datentypen & Constraints (CHECK/UNIQUE)",
            "taskFile": "aufgabe.sql",
            "testFile": "test_aufgabe.sql"
          }
        ]
      },
      {
        "id": "track_2_joins_und_design",
        "title": "🏗️ Lehrpfad 2: Relationale Joins & Datenbank-Design",
        "description": "Fremdschlüssel, Relationen (1:1, 1:n, n:m), INNER & OUTER JOINs, Datenbank-Normalisierung (1NF bis 3NF) und Junction Tables.",
        "certificateKey": "sql_joins",
        "chapters": [
          {
            "folder": "05_foreign_keys_und_relationen",
            "title": "SQL 05: Foreign Keys & Relationen (1:n)",
            "taskFile": "aufgabe.sql",
            "testFile": "test_aufgabe.sql"
          },
          {
            "folder": "06_inner_und_outer_joins",
            "title": "SQL 06: INNER JOIN & LEFT/RIGHT JOIN",
            "taskFile": "aufgabe.sql",
            "testFile": "test_aufgabe.sql"
          },
          {
            "folder": "07_datenbank_normalisierung_1nf_bis_3nf",
            "title": "SQL 07: Datenbank-Normalisierung (1NF–3NF)",
            "taskFile": "aufgabe.sql",
            "testFile": "test_aufgabe.sql"
          },
          {
            "folder": "08_m_zu_n_verknuepfungstabellen",
            "title": "SQL 08: n:m Beziehungen & Junction Tables",
            "taskFile": "aufgabe.sql",
            "testFile": "test_aufgabe.sql"
          }
        ]
      },
      {
        "id": "track_3_aggregation_und_analytics",
        "title": "⚡ Lehrpfad 3: Aggregationen, CTEs & Window Functions",
        "description": "GROUP BY, HAVING, Aggregate, Subqueries, Common Table Expressions (WITH ...) und moderne Window Functions (ROW_NUMBER, OVER).",
        "certificateKey": "sql_analytics",
        "chapters": [
          {
            "folder": "09_aggregate_und_group_by",
            "title": "SQL 09: Aggregationen (COUNT/SUM) & GROUP BY",
            "taskFile": "aufgabe.sql",
            "testFile": "test_aufgabe.sql"
          },
          {
            "folder": "10_subqueries_und_mengenoperationen",
            "title": "SQL 10: Subqueries & UNION / INTERSECT",
            "taskFile": "aufgabe.sql",
            "testFile": "test_aufgabe.sql"
          },
          {
            "folder": "11_common_table_expressions_cte",
            "title": "SQL 11: Common Table Expressions (WITH CTE)",
            "taskFile": "aufgabe.sql",
            "testFile": "test_aufgabe.sql"
          },
          {
            "folder": "12_window_functions_over_partition",
            "title": "SQL 12: Window Functions (ROW_NUMBER, OVER)",
            "taskFile": "aufgabe.sql",
            "testFile": "test_aufgabe.sql"
          }
        ]
      },
      {
        "id": "track_4_performance_und_master",
        "title": "💎 Lehrpfad 4: Performance, Transaktionen & Analytics Master",
        "description": "B-Tree Indizes, EXPLAIN Query Plans, ACID Transaktionen (COMMIT/ROLLBACK), Views und E-Commerce Data Warehouse Master.",
        "certificateKey": "sql_master",
        "chapters": [
          {
            "folder": "13_indizes_und_query_optimierung",
            "title": "SQL 13: B-Tree Indizes & EXPLAIN QUERY PLAN",
            "taskFile": "aufgabe.sql",
            "testFile": "test_aufgabe.sql"
          },
          {
            "folder": "14_transaktionen_acid_und_locking",
            "title": "SQL 14: ACID Transaktionen (BEGIN/COMMIT)",
            "taskFile": "aufgabe.sql",
            "testFile": "test_aufgabe.sql"
          },
          {
            "folder": "15_views_und_gespeicherte_logik",
            "title": "SQL 15: Virtuelle Views & Trigger",
            "taskFile": "aufgabe.sql",
            "testFile": "test_aufgabe.sql"
          },
          {
            "folder": "16_master_abschlussprojekt_data_warehouse",
            "title": "Master 16: E-Commerce Analytics Data Warehouse",
            "taskFile": "aufgabe.sql",
            "testFile": "test_aufgabe.sql"
          }
        ]
      }
    ]
  },
  "active_directory": {
    "id": "active_directory",
    "title": "Active Directory & Windows Server Administration",
    "language": "powershell",
    "icon": "🏛️",
    "runner": "powershell",
    "description": "Praxis-Masterkurs für Fachinformatiker: AD DS Gesamtstruktur, FSMO-Rollen, OU-Design, Sites & Replikation, AGDLP-Berechtigungskonzept, Gruppenrichtlinien (GPOs) & Enterprise PowerShell Automation.",
    "tracks": [
      {
        "id": "track_1_ad_architektur",
        "title": "🏛️ Lehrpfad 1: AD DS Architektur & Organisationseinheiten (OUs)",
        "description": "AD DS Gesamtstruktur, Trees, Domänen, DNS-Abhängigkeit (_msdcs), Kerberos & LDAP, die 5 FSMO-Rollen, OU-Hierarchien und Standorte & Replikation.",
        "certificateKey": "ad_architektur",
        "chapters": [
          {
            "folder": "01_ad_architektur_und_wald_baum_domaene",
            "title": "AD 01: AD DS Architektur & Wald, Baum, Domäne",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "02_domaenencontroller_und_fsmo_rollen",
            "title": "AD 02: Domänencontroller & FSMO-Rollen",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "03_organisationseinheiten_und_struktur",
            "title": "AD 03: Organisationseinheiten & Struktur",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "04_standorte_subnetze_und_replikation",
            "title": "AD 04: Standorte, Subnetze & Replikation",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          }
        ]
      },
      {
        "id": "track_2_identitaet_agdlp",
        "title": "🛡️ Lehrpfad 2: Identitätsmanagement & das AGDLP-Prinzip",
        "description": "Benutzerkonten, UPN & SAM-Account, UAC-Flags, Computerkonten, Secure Channel, djoin.exe, Sicherheitsgruppenbereiche und das AGDLP-Prinzip.",
        "certificateKey": "ad_identitaet",
        "chapters": [
          {
            "folder": "05_benutzerkonten_und_attribute",
            "title": "AD 05: Benutzerkonten & LDAP-Attribute",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "06_computerkonten_und_domaenenbeitritt",
            "title": "AD 06: Computerkonten & Domänenbeitritt",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "07_sicherheitsgruppen_und_bereichstypen",
            "title": "AD 07: Sicherheitsgruppen & Bereichstypen",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "08_das_agdlp_prinzip_in_der_praxis",
            "title": "AD 08: Das AGDLP-Prinzip in der Praxis",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          }
        ]
      },
      {
        "id": "track_3_gpo_design",
        "title": "📜 Lehrpfad 3: Gruppenrichtlinien (GPOs) & Richtlinien-Design",
        "description": "LSDOU-Abarbeitung, Vererbung und Enforced, Computerkonfiguration vs. Benutzerkonfiguration, Loopback Merge/Replace, WMI-Filter und GPO-Troubleshooting.",
        "certificateKey": "ad_gpo",
        "chapters": [
          {
            "folder": "09_gpo_grundlagen_und_lsdous",
            "title": "AD 09: GPO-Grundlagen & LSDOU-Hierarchie",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "10_computerkonfiguration_vs_benutzerkonfiguration",
            "title": "AD 10: Computer- vs. Benutzerkonfiguration & Loopback",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "11_sicherheitsfilterung_und_wmi_filter",
            "title": "AD 11: Sicherheitsfilterung & WMI-Filter",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "12_gpo_troubleshooting_gpupdate_und_gpresult",
            "title": "AD 12: GPO Troubleshooting: gpupdate & gpresult",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          }
        ]
      },
      {
        "id": "track_4_ad_automation",
        "title": "⚡ Lehrpfad 4: PowerShell AD-Automation & Enterprise Security",
        "description": "Microsoft ActiveDirectory Modul, Filter-Syntax, CSV-Massenprovisioning mit Kollisionsauflösung, NTFS- & Share-ACLs und Master-Abschlussprojekt.",
        "certificateKey": "ad_automation",
        "chapters": [
          {
            "folder": "13_powershell_activedirectory_modul_basics",
            "title": "AD 13: PowerShell ActiveDirectory-Modul Basics",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "14_csv_bulk_import_und_provisioning",
            "title": "AD 14: CSV Bulk-Import & Provisioning",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "15_ntfs_und_share_berechtigungssteuerung",
            "title": "AD 15: NTFS- & Share-Berechtigungssteuerung",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          },
          {
            "folder": "16_master_abschlussprojekt_ad_automation_suite",
            "title": "Master 16: Enterprise AD Automation & Security Suite",
            "taskFile": "aufgabe.ps1",
            "testFile": "test_aufgabe.ps1"
          }
        ]
      }
    ]
  },
  "git": {
    "id": "git",
    "title": "Git Versionskontrolle, Branching & DevOps Workflows",
    "language": "bash",
    "icon": "🔀",
    "runner": "bash",
    "description": "Vom ersten Commit über Branching, Merge-Konfliktlösung, Remotes & Tags bis zu interaktivem Rebase, Pre-Commit Hooks und professionellem Git-Flow.",
    "tracks": [
      {
        "id": "track_1_git_basics",
        "title": "🌱 Lehrpfad 1: Git Grundlagen & Lokale Repositories",
        "description": "Initialisierung, die 3 logischen Bereiche, Staging, atomare Commits, Historie und .gitignore.",
        "certificateKey": "git_basics",
        "chapters": [
          {
            "folder": "01_git_init_und_repo_basics",
            "title": "Git 01: Repository-Initialisierung & 3 Bereiche",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "02_staging_commits_und_historie",
            "title": "Git 02: Staging Area, Commits & Historie",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "03_aenderungen_vergleichen_mit_git_diff",
            "title": "Git 03: Diff-Analysen & Änderungen untersuchen",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "04_dateien_ignorieren_und_gitignore",
            "title": "Git 04: .gitignore & Ausschlussregeln",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          }
        ]
      },
      {
        "id": "track_2_branching_merging",
        "title": "⚡ Lehrpfad 2: Branching, Merging & Konflikte",
        "description": "Paralleles Arbeiten auf Branches, Fast-Forward vs. 3-Way-Merge, Konfliktlösung und Stash.",
        "certificateKey": "git_branching",
        "chapters": [
          {
            "folder": "05_branching_und_switch",
            "title": "Git 05: Branch-Management & HEAD-Pointer",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "06_fast_forward_und_3way_merge",
            "title": "Git 06: Fast-Forward & 3-Way-Merge Strategien",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "07_merge_konflikte_verstehen_und_loesen",
            "title": "Git 07: Merge-Konflikte analysieren & lösen",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "08_temporaere_aenderungen_mit_git_stash",
            "title": "Git 08: Zwischenspeichern mit Git Stash",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          }
        ]
      },
      {
        "id": "track_3_remotes_collaboration",
        "title": "🚀 Lehrpfad 3: Remote Repositories & Team-Collaboration",
        "description": "Origin-Remotes, push/pull, Fetch vs. Pull, SemVer Tags und selektives Cherry-Picking.",
        "certificateKey": "git_collaboration",
        "chapters": [
          {
            "folder": "09_remotes_verbinden_und_git_push",
            "title": "Git 09: Remote Repositories & Upstream Tracking",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "10_git_fetch_vs_git_pull",
            "title": "Git 10: Git Fetch vs. Git Pull & Rebase",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "11_git_tags_und_releases",
            "title": "Git 11: Release-Tags & Semantische Versionierung",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "12_cherry_picking_und_selektive_commits",
            "title": "Git 12: Selektive Commits mit Git Cherry-Pick",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          }
        ]
      },
      {
        "id": "track_4_advanced_workflows",
        "title": "💎 Lehrpfad 4: Fortgeschrittene Workflows & Master-Projekt",
        "description": "Rebase, Interaktives Squashing, Git Hooks und Master-Abschlussprojekt Git-Flow.",
        "certificateKey": "git_master",
        "chapters": [
          {
            "folder": "13_rebase_fuer_saubere_historie",
            "title": "Git 13: Lineare Historie mit Git Rebase",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "14_interaktives_rebase_squash_und_fixup",
            "title": "Git 14: Interaktives Rebase (Squash & Fixup)",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "15_git_hooks_und_automatisierte_checks",
            "title": "Git 15: Pre-Commit Hooks & Automatisierung",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "16_master_abschlussprojekt_git_flow_und_release",
            "title": "Master 16: Enterprise Git-Flow & Release Suite",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          }
        ]
      }
    ]
  },
  "dns_records": {
    "id": "dns_records",
    "title": "DNS-Records, Domain Name System & E-Mail-Sicherheit",
    "language": "bash",
    "icon": "🌐",
    "runner": "bash",
    "description": "Vom DNS-Baum über A/AAAA, CNAME, MX und SOA bis zu moderner E-Mail-Sicherheit (SPF, DKIM, DMARC), Active Directory SRV-Records und DNSSEC.",
    "tracks": [
      {
        "id": "track_1_dns_architektur",
        "title": "🌐 Lehrpfad 1: DNS-Architektur & Namensauflösung",
        "description": "DNS-Hierarchie, Root-Zone (.), rekursive vs. iterative Abfragen, UDP/TCP Port 53 und TTL Caching.",
        "certificateKey": "dns_architektur",
        "chapters": [
          {
            "folder": "01_dns_hierarchie_und_root_server",
            "title": "DNS 01: DNS-Hierarchie & Root-Server",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "02_rekursive_vs_iterative_abfragen",
            "title": "DNS 02: Rekursive vs. Iterative Abfragen",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "03_ports_udp_tcp_und_dns_paketaufbau",
            "title": "DNS 03: UDP vs. TCP Port 53 & EDNS0",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "04_ttl_und_dns_propagation",
            "title": "DNS 04: TTL & DNS-Propagation",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          }
        ]
      },
      {
        "id": "track_2_core_records",
        "title": "⚡ Lehrpfad 2: Kern-Resource-Records & Zonen",
        "description": "A & AAAA Records, CNAME Alias-Regeln, SOA-Header mit Serial und NS/PTR Reverse-Lookups.",
        "certificateKey": "dns_records_core",
        "chapters": [
          {
            "folder": "05_a_und_aaaa_records",
            "title": "DNS 05: A & AAAA Records (IPv4 / IPv6)",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "06_cname_canonical_name_und_alias_regeln",
            "title": "DNS 06: CNAME Alias & das Apex-Problem",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "07_soa_start_of_authority_und_serial",
            "title": "DNS 07: SOA Start of Authority & Serial",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "08_ns_und_ptr_reverse_dns_lookups",
            "title": "DNS 08: NS Delegation & PTR Reverse DNS",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          }
        ]
      },
      {
        "id": "track_3_email_security",
        "title": "🛡️ Lehrpfad 3: E-Mail-Sicherheit & Security Records",
        "description": "MX Prioritäten, SPF-Einträge, DKIM-Kryptosignaturen und DMARC Schutz vor Phishing & Spoofing.",
        "certificateKey": "dns_email_security",
        "chapters": [
          {
            "folder": "09_mx_mail_exchange_und_prioritaeten",
            "title": "DNS 09: MX Records & Mail-Prioritäten",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "10_txt_records_und_spf_sender_policy_framework",
            "title": "DNS 10: SPF Sender Policy Framework (TXT)",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "11_dkim_domainkeys_identified_mail",
            "title": "DNS 11: DKIM Kryptografische E-Mail-Signatur",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "12_dmarc_und_email_security_suite",
            "title": "DNS 12: DMARC Policy & Phishing-Abwehr",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          }
        ]
      },
      {
        "id": "track_4_advanced_dns",
        "title": "🚀 Lehrpfad 4: Erweiterte Records, DNSSEC & Auditing",
        "description": "SRV Records für Active Directory, CAA, DNSSEC Vertrauenskette, dig-Troubleshooting & Master Auditor.",
        "certificateKey": "dns_master",
        "chapters": [
          {
            "folder": "13_srv_service_records_fuer_ad_und_sip",
            "title": "DNS 13: SRV Service Records (Active Directory & SIP)",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "14_caa_und_dnssec_sicherheit",
            "title": "DNS 14: CAA Records & DNSSEC Vertrauenskette",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "15_dns_troubleshooting_mit_dig_und_nslookup",
            "title": "DNS 15: DNS-Troubleshooting mit dig & nslookup",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          },
          {
            "folder": "16_master_abschlussprojekt_dns_zone_auditor",
            "title": "Master 16: Enterprise DNS Zone & Security Auditor",
            "taskFile": "aufgabe.sh",
            "testFile": "test_aufgabe.sh"
          }
        ]
      }
    ]
  }
};
