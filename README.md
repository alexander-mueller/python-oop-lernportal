# 🐍 Python OOP Übungsreihe: Der Einstieg in Klassen & Objekte

Willkommen zu deiner Übungsreihe für **Objektorientierte Programmierung (OOP)** in Python! 🎉

Diese Übungsreihe ist didaktisch aufbereitet und **1:1 mit dem offiziellen Lehrplan des Informatik-Unterrichts** ([`LEHRPLAN.md`](./LEHRPLAN.md)) abgeglichen.

---

## 🗺️ Der Lernpfad

### 🌱 Phase 1: Grundlagen OOP & Entwicklungsumgebung
| Kapitel | Thema | Was du lernst |
| :--- | :--- | :--- |
| **[00. Fehlersuche & Grundlagen](./00_fehlersuche_und_grundlagen/)** | Warm-up & Debugging | Tracebacks lesen, Einrückungen (`IndentationError`), Typfehler & Detektiv-Aufgabe |
| **[01. Einstieg in Klassen](./01_einstieg_klassen/)** | Warum Klassen? | Bauplan vs. Objekt, Instanziierung, Punktnotation & Type Hints |
| **[02. Konstruktor & self](./02_init_und_self/)** | `__init__`, `self` & UML | Objekte sauber initialisieren und erste UML-Klassendiagramme |
| **[03. Methoden & Verhalten](./03_methoden_und_verhalten/)** | Methoden & Interaktion | Objekte können handeln & miteinander im Duell interagieren |
| **[04. Schöne Textausgabe](./04_str_und_darstellung/)** | `__str__` Dunder-Methode | Wie Objekte lesbar mit `print()` ausgegeben werden (Warenkorb & Bon) |
| **[04b. Umstieg & Installation VS Code](./04b_umstieg_vscode/)** | **Exkurs: IDE-Wechsel** | **Installation (Win/Mac/Linux), Plugins (Error Lens, Python), Shortcuts & Terminal** |
| **[05. Objekte kombinieren](./05_objekte_kombinieren/)** | Assoziation & Komposition | Listen von Objekten & Spotify-Playlists filtern und berechnen |
| **[06. Abschlussprojekt OOP 1](./06_abschlussprojekt_tamagotchi/)** | Mini-Projekt: Tamagotchi | Ein interaktives Konsolenspiel mit allem Gelernten |

### 🧠 Phase 2: Fortgeschrittenes OOP, Speicher & Persistenz
| Kapitel | Thema | Was du lernst |
| :--- | :--- | :--- |
| **[07. Referenzen, Speicher & Stammbäume](./07_referenzen_und_speicher/)** | **Speicher & RAM** | **Referenzen, Aliasing (`b = a`), Mutable vs. Immutable, `is` vs. `==` & Familienstammbaum** |
| *08. Operator Overloading* | *Dunder-Methoden* | *`__add__`, `__eq__`, `__lt__` (2D-Vektoren & Kartenspiele)* |
| *09. Vererbung & `super()`* | *Inheritance* | *Basisklassen, Kindklassen & `super().__init__()` (Fahrzeuge & RPG-Helden)* |
| *10. Polymorphie & Interfaces* | *Polymorphism* | *Methoden überschreiben, Geometrie- & Grafik-Engine* |
| *11. Exceptions & Fehler* | *Robustes Coding* | *`try/except/else/finally`, `raise`, eigene Exception-Klassen* |
| *12. JSON & CSV Speichern* | *Persistenz* | *Spielstände dauerhaft mit JSON/CSV auf der Festplatte sichern* |

*(Den vollständigen didaktischen Masterplan für alle Kapitel bis 15 findest du in [`LEHRPLAN.md`](./LEHRPLAN.md).)*

---

## 📁 Aufbau eines Kapitels

In jedem Kapitelordner findest du:
1. **`index.html`**: Eine interaktive, schön gestaltete Webseite mit ausführlichen Erklärungen, Vollbeispielen und aufklappbaren Lösungshinweisen.
2. **`README.md`**: Die Erklärung im Markdown-Format.
3. **`aufgabe.py`**: Dein Arbeitsblatt! Hier steht der Starter-Code mit klaren `TODO`-Kommentaren.
4. **`test_aufgabe.py`**: Automatische Tests, mit denen du deine Lösung jederzeit überprüfen kannst.
5. **`musterloesung.py`**: Eine ausführlich kommentierte Beispiellösung.

---

## 🚀 Wie du vorgehst

1. Öffne den Ordner des aktuellen Kapitels (z.B. `07_referenzen_und_speicher`).
2. Öffne die `index.html` im Browser oder lies die `README.md`.
3. Öffne `aufgabe.py` und bearbeite die Aufgaben.
4. Führe die Tests aus, um deine Lösung zu prüfen:
   ```bash
   python3 test_aufgabe.py
   ```
5. Wenn alle Tests mit einem grünen `OK` durchlaufen: **Herzlichen Glückwunsch!** Du bist bereit für das nächste Kapitel! 🏆

---

## 💡 Gesamten Fortschritt prüfen
```bash
python3 test_all.py
```
