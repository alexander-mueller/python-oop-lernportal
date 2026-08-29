# 📚 Didaktischer Lehrplan: Das 3-Säulen-System

Dieses Dokument dient als didaktischer Leitfaden für die Python-Nachhilfe.
Es gleicht die gesamte Übungsreihe (Grundlagen &amp; Fortgeschrittene Objektorientierung) mit dem offiziellen Lehrplan und Skriptum des Lehrers (**`rradlbauer/python_skriptum`**) ab.

---

## 🧭 Die 3 Lehrpfade im Überblick

```
[ 🛣️ LEHRPFAD 1: GRUNDLAGEN DER PROGRAMMIERUNG (Prozedural & Datenstrukturen) ]
  ├── G01: Python als Taschenrechner (Zahlen, Operatoren, Rangfolge)       (Lehrer 02.1)
  ├── G02: Variablen & Datentypen (int, float, str, bool, Type Casting)    (Lehrer 03.0 & 03.1)
  ├── G03: Interaktive Ein- & Ausgabe (input, print, formatierte f-Strings) (Lehrer 07.0)
  ├── G04: Bedingungen & Verzweigungen (if, elif, else, and/or/not)        (Lehrer 08.0)
  ├── G05: Schleifen & Wiederholungen (for range, while, break, continue)  (Lehrer 09.1 & 09.2)
  ├── G06: Eigene Funktionen & Module (def, return, scope, math, random)   (Lehrer 05.0 & 05.1)
  ├── G07: Listen & Sequenzen (Indexing, Slicing, append/pop, sum/len/min) (Lehrer 09.0)
  ├── G08: Textverarbeitung & Strings (.strip, .replace, .split, .join)    (Lehrer 11.0)
  ├── G09: Dictionaries & Sets ({key: value}, .get(), Mengen ohne Duplikate) (Lehrer 15.0)
  └── G10: Comprehensions, Datum & Algorithmen ([x for x in ...], datetime) (Lehrer 13.0 & 15.1)

[ 🛣️ LEHRPFAD 2: EINSTIEG IN DIE OBJEKTORIENTIERUNG (OOP) & WERKZEUGE ]
  ├── 00: Fehlersuche & Python-Debugging (Warm-up & Tracebacks)            (Lehrer 04.1 & 07.1)
  ├── 01: Erste Klasse & Baupläne (Instanziierung, Punktnotation)          (Lehrer 22.0 & 21.0)
  ├── 02: Konstruktor __init__, self & UML-Klassendiagramme                (Lehrer 22.0 & 22.1)
  ├── 03: Methoden & Objekt-Interaktionen (Rennauto & Duell)               (Lehrer 22.0)
  ├── 04: Schöne Textausgabe mit __str__ (Warenkorb & Bon)                 (Lehrer 28.0)
  ├── 04b: Exkurs: Umstieg & Installation von VS Code                      (Lehrer 20.1)
  ├── 04c: Exkurs: Git & Versionskontrolle (VS Code & Terminal)            (Tooling)
  ├── 05: Assoziation & Komposition (Spotify Playlist-Manager)             (Lehrer 23.0)
  └── 06: Mini-Abschlussprojekt: Tamagotchi Terminal-Game                  (Konsolidierung)

[ 🛣️ LEHRPFAD 3: FORTGESCHRITTENES OOP, SOFTWAREQUALITÄT & GUIS ]
  ├── 07: Referenzen, RAM-Speicher & Familienstammbäume                    (Lehrer 24.0)
  ├── 08: Operator Overloading & Dunder-Methoden (__add__, __eq__, __lt__) (Lehrer 28.0)
  ├── 09: Eigene Unit Tests schreiben & TDD (unittest.TestCase)            (Testing & TDD)
  ├── 10: Vererbung (Inheritance) & super() (Fahrzeugflotte)               (Lehrer 25.0)
  ├── 11: Polymorphie & Interfaces (ABC, Geometrie & Zeichenfläche)        (Lehrer 25.1)
  ├── 12: Exceptions & Robuste Fehlerbehandlung (try-except, Bankkonto)    (Lehrer 26.0)
  ├── 13: Datei-Persistenz: JSON & CSV Speichern (Savegames)               (Lehrer 14.0)
  └── 14: Desktop-GUIs mit Tkinter & MVC-Architektur (Zähler & Rechner)    (Lehrer 27.0)
```

---

## 📑 Detaillierte Themen-Abgleichstabelle

| Modul | Titel | Thema | Praxisbeispiel |
| :--- | :--- | :--- | :--- |
| **G01** | **Taschenrechner** | Grundrechenarten, `//`, `%`, `**`, Rangfolge | Rechner-Funktionen & Kreisflächen |
| **G02** | **Variablen & Typen** | Basisdatentypen, Type Casting, Type Hints | Typen-Erkenner & Preis-Formatierer |
| **G03** | **Ein- & Ausgabe** | `input()`, f-Strings mit Formatierungs-Codes | Steckbrief & Rechnungsposten |
| **G04** | **Verzweigungen** | `if`, `elif`, `else`, `and`, `or`, `not` | Kinokarten, Notenspiegel & Schaltjahr |
| **G05** | **Schleifen** | `for in range()`, `while`, `break`, `continue` | Fakultät, Primzahlen & Quersummen |
| **G06** | **Funktionen** | `def`, `return`, Scope, `math`, `random` | Hypotenuse, Zylindervolumen & Würfel |
| **G07** | **Listen & Slicing**| Indexing, Slicing `[1:4]`, Methoden wie `append`/`pop` | Notenschnitt ohne Ausreißer |
| **G08** | **Textverarbeitung**| String-Methoden (`.strip`, `.split`, `.replace`) | Palindrom-Prüfer & Kreditkarten-Maske |
| **G09** | **Dicts & Sets** | Key-Value Paare, `.get()`, Mengen ohne Duplikate | Häufigkeitszähler & Hobbys-Abgleich |
| **G10** | **Comprehensions** | `[x for x in ...]`, `datetime`, Sortier-Algorithmen | Countdown, Alters-Suche |
| **00** | **Fehlersuche** | Tracebacks von unten lesen, `IndentationError` | Code-Detektivin |
| **01** | **Erste Klasse** | Klassen als Baupläne, Punktnotation, Type Hints | Fahrrad-Verleih |
| **02** | **Konstruktor** | `__init__`, `self`, Startwerte, UML-Diagramme | Bankkonto & Smartphone |
| **03** | **Methoden** | Verhalten & Interaktion zweier Objekte | Rennauto-Duell |
| **04** | **`__str__`** | Lesbare Darstellung mit `print()`, Rechnungsdruck | Pizzeria-Warenkorb |
| **04b** | **VS Code** | Installation, Extensions (Error Lens, Python), Shortcuts | IDE-Praxis |
| **04c** | **Git** | Spielstand-Analogie, Commits, VS Code Git-Tab, Push | Versionskontrolle |
| **05** | **Komposition** | 1:1 und 1:n Beziehungen zwischen Objekten | Spotify Playlist-Manager |
| **06** | **Mini-Projekt**| Konsolidierung von OOP Teil 1 | Tamagotchi Konsolenspiel |
| **07** | **Referenzen** | RAM-Zeiger, Aliasing (`b = a`), `is` vs. `==` | Familienstammbaum (`Person`) |
| **08** | **Dunder** | Operator Overloading `__add__`, `__eq__`, `__len__` | 2D-Vektor & Wegstrecken |
| **09** | **Unit Testing**| Eigene Testsuiten schreiben, `assertEqual`, TDD | Taschenrechner & Bankkonto Tests |
| **10** | **Vererbung** | Basis- und Kindklassen, `super().__init__()`, DRY | Fahrzeugflotte (`ElektroAuto`, `Lkw`) |
| **11** | **Polymorphie** | Duck Typing, abstrakte Klassen (`ABC`), Overriding | Geometrie-Engine & Zeichenfläche |
| **12** | **Exceptions** | `try-except-else-finally`, `raise`, eigene Fehler | Bankkonto- & Geldautomat-Simulator |
| **13** | **Persistenz** | `with open()`, `json.dump`/`load`, CSV-Export | Savegames & Notenbuch |
| **14** | **Tkinter GUI** | Echte Desktop-Apps, Widgets, `grid()`, MVC-Muster | Interaktive Zähler- & Rechner-App |
