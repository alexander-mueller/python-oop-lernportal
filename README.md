# 🐍 Python Lernportal: Vom Einsteiger zum Software-Entwickler

Willkommen zum interaktiven **Python Lernportal**! 🎉

Dieses Portal ist didaktisch aufbereitet, voll **abgeglichen mit dem Informatik-Schulunterricht** ([`LEHRPLAN.md`](./LEHRPLAN.md)) und gliedert sich in **3 strukturierte Lehrpfade**:

---

## 🧭 Die 3 Lehrpfade

### 🛣️ Lehrpfad 1: Grundlagen der Programmierung (Prozedural & Datenstrukturen)
| Modul | Titel | Themenschwerpunkte |
| :--- | :--- | :--- |
| **[G01. Taschenrechner](./g01_erste_schritte_taschenrechner/)** | **Python als Rechner** | Zahlenarten (`int`, `float`), Grundrechenarten, `//`, `%`, `**`, Rangfolge & `print()` |
| **[G02. Variablen & Typen](./g02_variablen_und_datentypen/)** | **Datentypen** | Speicherboxen, `int`, `float`, `str`, `bool`, Type Casting & Type Hints |
| **[G03. Ein- & Ausgabe](./g03_ein_und_ausgabe/)** | **Interaktion** | Tastatureingaben mit `input()`, f-Strings mit Formatierungs-Codes (`{preis:.2f} €`) |
| **[G04. Bedingungen](./g04_verzweigungen_und_bedingungen/)** | **Entscheidungen** | `if`, `elif`, `else`, Vergleichsoperatoren & Logik (`and`, `or`, `not`) |
| **[G05. Schleifen](./g05_schleifen_und_wiederholungen/)** | **Wiederholungen** | Zählschleifen mit `for in range()`, Bedingungsschleifen mit `while`, `break`/`continue` |
| **[G06. Funktionen](./g06_funktionen_und_module/)** | **Modularität** | `def`, `return`, Parameter, Scope & Module (`math`, `random`) |
| **[G07. Listen & Sequenzen](./g07_listen_und_sequenzen/)** | **Datenstrukturen 1** | Listen erstellen, Indexing, Slicing `[1:4]`, Methoden (`append`, `pop`) & `sum/min/max` |
| **[G08. Textverarbeitung](./g08_textverarbeitung_und_strings/)** | **String-Methoden** | Unveränderlichkeit, `.strip()`, `.replace()`, `.split()`, `", ".join()` & Textanalyse |
| **[G09. Dictionaries & Sets](./g09_dictionaries_und_sets/)** | **Datenstrukturen 2** | Key-Value Paare (`{key: val}`), sicheres `.get()`, Mengen (`set`) ohne Duplikate |
| **[G10. Comprehensions & Datum](./g10_comprehensions_datum_algorithmen/)** | **Vertiefung** | List Comprehensions `[x for x in ...]`, `datetime` & Such-/Sortier-Algorithmen |

---

### 🛣️ Lehrpfad 2: Einstieg in die Objektorientierung (OOP) & Entwickler-Tools
| Modul | Titel | Themenschwerpunkte |
| :--- | :--- | :--- |
| **[00. Fehlersuche](./00_fehlersuche_und_grundlagen/)** | **Warm-up & Debugging** | Tracebacks von unten lesen, `IndentationError`, `SyntaxError`, `TypeError` |
| **[01. Einstieg in Klassen](./01_einstieg_klassen/)** | **Bauplan vs. Objekt** | Klassen definieren, Instanziierung, Punktnotation & Type Hints (`Fahrrad`) |
| **[02. Konstruktor & self](./02_init_und_self/)** | **Initialisierung & UML** | `__init__`, `self`, Startwerte & UML-Klassendiagramme (`Bankkonto`, `Smartphone`) |
| **[03. Methoden & Verhalten](./03_methoden_und_verhalten/)** | **Objekt-Interaktion** | Methoden definieren, Rückgabewerte & Duell zweier Objekte (`Rennauto`) |
| **[04. Schöne Textausgabe](./04_str_und_darstellung/)** | **`__str__` Dunder** | Lesbare `print()`-Ausgabe von Objekten, Kassenzettel (`Warenkorb`) |
| **[04b. VS Code Installation](./04b_umstieg_vscode/)** | **IDE-Setup** | Installation (Win/Mac/Linux), Plugins (Error Lens, Python), Shortcuts |
| **[04c. Git & Versionskontrolle](./04c_git_und_versionskontrolle/)** | **Git-Tooling** | Spielstände (Commits) sichern, VS Code Git-Tab, Terminal & Remote Push |
| **[05. Objekte kombinieren](./05_objekte_kombinieren/)** | **Komposition** | 1:1 und 1:n Beziehungen zwischen Objekten (`Spotify Playlist-Manager`) |
| **[06. Mini-Projekt OOP 1](./06_abschlussprojekt_tamagotchi/)** | **Tamagotchi Game** | Voll spielbares, interaktives Haustierspiel im Terminal |

---

### 🛣️ Lehrpfad 3: Fortgeschrittenes OOP, Softwarequalität & Desktop-GUIs
| Modul | Titel | Themenschwerpunkte |
| :--- | :--- | :--- |
| **[07. Referenzen & Speicher](./07_referenzen_und_speicher/)** | **RAM & Zeiger** | Referenzen im RAM, Aliasing (`b = a`), `is` vs. `==` & Familienstammbaum (`Person`) |
| **[08. Operator Overloading](./08_operator_overloading_dunder/)** | **Dunder-Methoden** | Eigene Klassen rechenbar machen mit `__add__`, `__mul__`, `__eq__` (2D-Vektoren) |
| **[09. Eigene Unit Tests & TDD](./09_eigene_unit_tests_schreiben/)** | **Softwarequalität** | Testsuiten schreiben mit `unittest`, `assertEqual`, `assertRaises` & TDD |
| **[10. Vererbung & `super()`](./10_vererbung_und_super/)** | **Inheritance** | Basis- & Kindklassen, DRY-Prinzip, `super().__init__()` & Fahrzeugflotte |
| **[11. Polymorphie & Interfaces](./11_polymorphie_und_interfaces/)** | **Polymorphism** | Duck Typing, abstrakte Basisklassen (`ABC`) & Geometrie-Engine |
| **[12. Exceptions & Fehler](./12_exceptions_und_fehlerbehandlung/)** | **Robustes Coding** | `try-except-else-finally`, `raise`, eigene Exception-Klassen im Banking |
| **[13. Datei-Persistenz](./13_persistenz_json_und_csv/)** | **JSON & CSV** | Dauerhaftes Speichern & Laden: Savegames & Tabellen-Export |
| **[14. Desktop-GUIs mit Tkinter](./14_gui_mit_tkinter/)** | **Tkinter Desktop-Apps** | Echte Fenster, Buttons, Labels, Grid-Layout & MVC-Architektur |
| **[15. Parameter & Container](./15_parameter_und_container/)** | **Dunder-Container** | Variable Argumente (`*args`, `**kwargs`), Unpacking & Container (`len`, `[]`, `in`, `iter`) |
| **[16. Master-Abschlussprojekt](./16_master_abschlussprojekt/)** | **🏆 Meisterstück: PetCare** | Vollständige Desktop-App: MVC, Vererbung, Polymorphie, JSON-Savegames & Tkinter GUI |

---

## 🧪 Wie benutze ich die automatischen Tests?

In jedem Kapitelordner liegt eine Datei namens `test_aufgabe.py`. Sie enthält automatische **Unit Tests**, die überprüfen, ob deine Lösung alle Anforderungen erfüllt.

### 1. Einzelnes Kapitel testen
Öffne das Terminal in VS Code (`Strg + \``) und führe den Test im jeweiligen Ordner aus:
```bash
# Beispiel für Grundlagen G01:
cd g01_erste_schritte_taschenrechner
python3 test_aufgabe.py
```

### 2. Testausgabe richtig lesen:
- ✅ **`OK`**: Perfekt! Alle Tests sind grün und bestanden. Du kannst mit dem nächsten Kapitel weitermachen.
- ❌ **`FAIL` (AssertionError)**: Dein Code läuft, liefert aber einen falschen Wert zurück (z.B. Rechenfehler oder falsche Bedingung). Lies die letzte Zeile der Fehlermeldung!
- 💥 **`ERROR` (Syntax / AttributeError)**: Dein Code hat einen Absturz (z.B. Tippfehler im Funktionsnamen).

### 3. Gesamten Fortschritt aller 27 Kapitel prüfen:
Führe im Hauptordner folgenden Befehl aus:
```bash
python3 test_all.py
```
Dieser Befehl zeigt dir eine Übersicht über alle Kapitel mit `✅` (bestanden) und `⏳` (noch offen).

---

## 💡 3 Wichtige Regeln für die Aufgaben

1. **`return` statt `print()`:** Tests prüfen das, was eine Funktion/Methode mit `return` zurückliefert. Ein reines `print()` genügt dem Test nicht!
2. **Exakte Namen:** Die Namen der Funktionen, Methoden und Attribute müssen exakt der Aufgabenstellung entsprechen (`addieren`, nicht `Addieren`).
3. **Fehlermeldungen von unten nach oben lesen:** Ganz unten im Traceback steht immer die genaue Ursache.
