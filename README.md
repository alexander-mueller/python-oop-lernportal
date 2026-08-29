# 🐍 Python OOP Übungsreihe: Der Einstieg in Klassen & Objekte

Willkommen zu deiner Übungsreihe für **Objektorientierte Programmierung (OOP)** in Python! 🎉

Diese Übungsreihe ist didaktisch aufbereitet und **1:1 mit dem offiziellen Lehrplan des Informatik-Unterrichts** ([`LEHRPLAN.md`](./LEHRPLAN.md)) abgeglichen.

---

## 🗺️ Der Lernpfad

### 🌱 Phase 1: Grundlagen OOP & Werkzeuge
| Kapitel | Thema | Was du lernst |
| :--- | :--- | :--- |
| **[00. Fehlersuche & Grundlagen](./00_fehlersuche_und_grundlagen/)** | Warm-up & Debugging | Tracebacks lesen, Einrückungen (`IndentationError`), Typfehler & Detektiv-Aufgabe |
| **[01. Einstieg in Klassen](./01_einstieg_klassen/)** | Warum Klassen? | Bauplan vs. Objekt, Instanziierung, Punktnotation & Type Hints |
| **[02. Konstruktor & self](./02_init_und_self/)** | `__init__`, `self` & UML | Objekte sauber initialisieren und erste UML-Klassendiagramme |
| **[03. Methoden & Verhalten](./03_methoden_und_verhalten/)** | Methoden & Interaktion | Objekte können handeln & miteinander im Duell interagieren |
| **[04. Schöne Textausgabe](./04_str_und_darstellung/)** | `__str__` Dunder-Methode | Wie Objekte lesbar mit `print()` ausgegeben werden (Warenkorb & Bon) |
| **[04b. Umstieg & Installation VS Code](./04b_umstieg_vscode/)** | **Exkurs: IDE-Wechsel** | **Installation (Win/Mac/Linux), Plugins (Error Lens, Python), Shortcuts & Terminal** |
| **[04c. Git & Versionskontrolle](./04c_git_und_versionskontrolle/)** | **Exkurs: Git-Tooling** | **Spielstände (Commits) sichern, VS Code Git-Tab, Terminal-Befehle & Remote Push** |
| **[05. Objekte kombinieren](./05_objekte_kombinieren/)** | Assoziation & Komposition | Listen von Objekten & Spotify-Playlists filtern und berechnen |
| **[06. Abschlussprojekt OOP 1](./06_abschlussprojekt_tamagotchi/)** | Mini-Projekt: Tamagotchi | Ein interaktives Konsolenspiel mit allem Gelernten |

### 🧠 Phase 2: Fortgeschrittenes OOP, Testing & Persistenz
| Kapitel | Thema | Was du lernst |
| :--- | :--- | :--- |
| **[07. Referenzen, Speicher & Stammbäume](./07_referenzen_und_speicher/)** | **Speicher & RAM** | **Referenzen, Aliasing (`b = a`), Mutable vs. Immutable, `is` vs. `==` & Familienstammbaum** |
| **[08. Operator Overloading](./08_operator_overloading_dunder/)** | **Dunder-Methoden** | **`__add__`, `__mul__`, `__eq__`, `__lt__` (2D-Vektoren & Wegstrecken)** |
| **[09. Eigene Unit Tests & TDD](./09_eigene_unit_tests_schreiben/)** | **Softwarequalität** | **Testsuiten schreiben mit `unittest`, `assertEqual`, `assertTrue`, `assertRaises`** |
| **[10. Vererbung & `super()`](./10_vererbung_und_super/)** | **Inheritance** | **Basisklassen, Kindklassen, DRY-Prinzip & `super().__init__()` (Fahrzeugflotte)** |
| **[11. Polymorphie & Interfaces](./11_polymorphie_und_interfaces/)** | **Polymorphism** | **Vielgestaltigkeit, Duck Typing, abstrakte Basisklassen (`ABC`) & Geometrie-Engine** |
| **[12. Exceptions & Fehler](./12_exceptions_und_fehlerbehandlung/)** | **Robustes Coding** | **`try/except/else/finally`, `raise`, eigene Exception-Klassen (Bankkonto)** |
| **[13. JSON & CSV Speichern](./13_persistenz_json_und_csv/)** | **Persistenz** | **Spielstände dauerhaft mit JSON/CSV auf der Festplatte sichern** |
| **[14. Desktop-GUIs mit Tkinter](./14_gui_mit_tkinter/)** | **Grafische Oberflächen** | **Fenster, Buttons, Labels, Grid-Layout & MVC-Architektur** |

*(Den vollständigen didaktischen Masterplan für alle Kapitel bis 16 findest du in [`LEHRPLAN.md`](./LEHRPLAN.md).)*

---

## 🧪 Wie benutze ich die automatischen Tests?

In jedem Kapitelordner liegt eine Datei namens `test_aufgabe.py`. Sie enthält automatische **Unit Tests**, die überprüfen, ob deine Lösung alle Anforderungen erfüllt.

### 1. Einzelnes Kapitel testen
Öffne das Terminal in VS Code (`Strg + \``) und führe den Test im jeweiligen Ordner aus:
```bash
# Beispiel für Kapitel 01:
cd 01_einstieg_klassen
python3 test_aufgabe.py
```

### 2. Testausgabe richtig lesen:
- ✅ **`OK`**: Perfekt! Alle Tests sind grün und bestanden. Du kannst mit dem nächsten Kapitel weitermachen.
- ❌ **`FAIL` (AssertionError)**: Dein Code läuft, liefert aber einen falschen Wert zurück (z.B. Rechenfehler oder falsche Bedingung). Lies die letzte Zeile der Fehlermeldung!
- 💥 **`ERROR` (Syntax / AttributeError)**: Dein Code hat einen Absturz (z.B. Tippfehler im Methodennamen oder `self` im Methodenkopf vergessen).

### 3. Gesamten Fortschritt aller Kapitel prüfen:
Führe im Hauptordner folgenden Befehl aus:
```bash
python3 test_all.py
```
Dieser Befehl zeigt dir eine Übersicht über alle Kapitel mit `✅` (bestanden) und `⏳` (noch offen).

---

## 💡 3 Wichtige Regeln für die Aufgaben

1. **`return` statt `print()`:** Tests prüfen das, was eine Methode mit `return` zurückliefert. Ein reines `print()` genügt dem Test nicht!
2. **Exakte Namen:** Die Namen der Methoden und Attribute müssen exakt der Aufgabenstellung entsprechen (`mutter_setzen`, nicht `MutterSetzen`).
3. **Immer `self` als erster Methoden-Parameter:** Jede Methode in einer Klasse muss `def meine_methode(self, ...):` geschrieben werden.
