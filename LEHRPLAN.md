# 📚 Didaktischer Lehrplan & Abgleich mit dem Schulskriptum

Dieses Dokument dient als didaktischer Leitfaden für die Python-Nachhilfe.
Es gleicht die Übungsreihe mit dem offiziellen Lehrplan und Skriptum des Lehrers (**`rradlbauer/python_skriptum`**) ab.

---

## 🎯 Didaktische Leitlinien für die Nachhilfe

1. **Type Hints als Standard:** Da der Lehrer in Teil 2 strikt Typ-Annotationen verwendet (`name: str`, `def alter(self) -> int:`), führen wir diese ab den Klassen sauber ein.
2. **UML-Klassendiagramme:** Das Skriptum fordert UML-Diagramme (`22.1_UML.md`). Jedes Kapitel enthält visuelle UML-Karten.
3. **Echte Entwickler-Werkzeuge früh erlernen:** Nach den ersten OOP-Kapiteln folgen **VS Code (04b)** und **Git Versionskontrolle (04c)**, damit die Schülerin ab Kapitel 05 jedes gelöste Kapitel selbstständig versioniert und committet.
4. **Eigene Unit Tests schreiben:** Ab Kapitel 09 lernt die Schülerin, wie man mit `unittest` eigene Testsuiten und Test-Driven Development (TDD) praktiziert.
5. **Praxisnahe Analogien:** Statt trockener Theorie nutzen wir greifbare Alltagsbeispiele (Fahrrad-Verleih, Spotify-Playlists, Stammbäume, Geldautomaten).
6. **Automatische Tests & Sofort-Feedback:** Jedes Kapitel hat ein Testskript (`test_aufgabe.py`), das bei `python3 test_aufgabe.py` oder `python3 test_all.py` sofort anzeigt, was schon klappt.
7. **Autonomes Lernen:** Die Schülerin kann alle Kapitel über die modernen, interaktiven HTML-Seiten im Browser selbstständig durcharbeiten.

---

## 🗺️ Der Gesamtlehrplan im Überblick (Kapitel 00 bis 16)

```
PHASE 1: GRUNDLAGEN DER OBJEKTORIENTIERUNG (OOP) & TOOLING
  ├── Kapitel 00: Fehlersuche & Python-Debugging (Warm-up)
  ├── Kapitel 01: Erste Klasse & Baupläne (Lehrer 22.0 / 21.0 Type Hints)
  ├── Kapitel 02: Konstruktor __init__, self & UML (Lehrer 22.0 / 22.1)
  ├── Kapitel 03: Methoden & Objekt-Interaktion (Lehrer 22.0)
  ├── Kapitel 04: Schöne Textausgabe mit __str__ (Lehrer 28.0)
  ├── Kapitel 04b: Umstieg & Installation von VS Code (Lehrer 20.1)
  ├── Kapitel 04c: Git & Versionskontrolle (VS Code & Terminal) 🌿
  ├── Kapitel 05: Assoziation & Aggregation: Spotify Playlists (Lehrer 23.0)
  └── Kapitel 06: Mini-Abschlussprojekt: Tamagotchi Terminal-Game

PHASE 2: FORTGESCHRITTENES OOP, TESTING & SPEICHER
  ├── Kapitel 07: Referenzen, Speicher & Stammbäume (Lehrer 24.0) 🧠
  ├── Kapitel 08: Operator Overloading & Dunder-Methoden (Lehrer 28.0) ➕
  ├── Kapitel 09: Eigene Unit Tests schreiben & TDD (unittest) 🧪
  ├── Kapitel 10: Vererbung (Inheritance) & super() (Lehrer 25.0) 🧬
  ├── Kapitel 11: Polymorphie & Duck Typing (Lehrer 25.1) 🎭
  ├── Kapitel 12: Exceptions & Robuste Fehlerbehandlung (Lehrer 26.0) 🛡️
  └── Kapitel 13: Speichern & Laden: JSON & CSV Persistenz (Lehrer 14.0) 💾

PHASE 3: GRAFISCHE OBERFLÄCHEN & PROFESSIONS-MODULE
  ├── Kapitel 14: Grafische Oberflächen mit Tkinter / CustomTkinter (Lehrer 27.0) 🖥️
  ├── Kapitel 15: Erweiterte Parameter (*args, **kwargs) & Container (Lehrer 29/30) 📦
  └── Kapitel 16: Master-Abschlussprojekt: Grafische Desktop-App mit Savegame 🏆
```

---

## 📑 Detaillierte Kapitel-Übersicht & Abgleich

| Kapitel | Titel / Thema | Lehrerskript-Referenz | Kerninhalte & Praxisaufgabe |
| :--- | :--- | :--- | :--- |
| **00** | **Fehlersuche & Debugging** | *04.1 & 07.1* | Tracebacks von unten lesen, `IndentationError`, `SyntaxError`, `TypeError`, Detektiv-Aufgabe |
| **01** | **Einstieg in Klassen** | *22.0 & 21.0* | Bauplan vs. Objekt, Instanziierung, Punktnotation, erste Type Hints (`Fahrrad`) |
| **02** | **Konstruktor & self** | *22.0 & 22.1* | `__init__`, `self`, Startwerte, erstes UML-Klassendiagramm (`Bankkonto` & `Smartphone`) |
| **03** | **Methoden & Verhalten** | *22.0* | Methoden definieren, Rückgabewerte, Interaktion zweier Objekte (`Rennauto` & RPG-Duell) |
| **04** | **`__str__` & Darstellung** | *28.0* | Dunder-Methode `__str__`, lesbare Ausgabe von Objekten, Kassenzettel (`Warenkorb`) |
| **04b** | **VS Code Umstieg** | *20.1* | Installation (Windows/Mac/Linux), Plugins (Error Lens, Python), Shortcuts, Projektordner |
| **04c** | **Git Versionskontrolle** | *Tooling* | Was ist Git? Spielstand-Analogie, `git add`, `git commit`, `git push`, VS Code Git-Tab |
| **05** | **Objekte kombinieren** | *23.0* | Assoziation & Aggregation (1:1 und 1:n), Listen von Objekten filtern (`Spotify Playlist`) |
| **06** | **Abschlussprojekt OOP 1** | *Konsolidierung* | Tamagotchi-Konsolenspiel (Lebenszyklus, Hunger, Müdigkeit, Zufallsevents) |
| **07** | **Referenzen & Speicher** | *24.0 Referenzen* | RAM-Visualisierung, Mutable vs. Immutable, `is` vs. `==`, Aliasing, `Stammbaum`-Projekt |
| **08** | **Operator Overloading** | *28.0 Spezielle Methoden*| `__add__`, `__sub__`, `__eq__`, `__lt__`, `__len__` (2D-Vektoren & Kartenspiel) |
| **09** | **Eigene Unit Tests & TDD**| *Softwarequalität* | Testsuiten schreiben mit `unittest`, `assertEqual`, `assertTrue`, `assertRaises` |
| **10** | **Vererbung & `super()`** | *25.0 Vererbung* | Basisklassen, Kindklassen, Vermeidung von Code-Duplikaten, `super().__init__()` (`Fahrzeuge`) |
| **11** | **Polymorphie & Interfaces**| *25.1 Polymorphie* | Methoden überschreiben, gemeinsames Interface, Geometrie- & Grafik-Engine (`Formen`) |
| **12** | **Exceptions & Fehler** | *26.0 Exceptions* | `try/except/else/finally`, `raise`, eigene Exception-Klassen (`Geldautomat`) |
| **13** | **JSON & CSV Speichern** | *14.0 CSV / Persistenz* | `with open()`, `json.dump`/`json.load`, Spielstände dauerhaft sichern (`Savegame`) |
| **14** | **Tkinter Desktop-GUI** | *27.0 Tkinter* | Fenster, Buttons, Labels, Eingabefelder, Event-Handling in OOP-Klassen |
| **15** | **Parameter & Container** | *29.0 & 30.0 Parameter*| `*args`, `**kwargs`, Dunder `__getitem__`, `__iter__` für eigene Listen-Container |
| **16** | **Master-Abschlussprojekt**| *Meisterstück* | Vollständige Desktop-App mit grafischer Oberfläche, Speichern & Laden |
