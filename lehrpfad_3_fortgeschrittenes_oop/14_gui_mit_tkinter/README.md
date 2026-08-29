# Kapitel 14: Desktop-GUIs mit Tkinter & OOP 🖥️✨

Bisher liefen alle unsere Python-Programme im Terminal (der Konsole) ab: Text eingeben mit `input()`, Text ausgeben mit `print()`. Das ist super für den Einstieg, aber echte moderne Desktop-Programme haben grafische Benutzeroberflächen (**GUI = Graphical User Interface**) mit Fenstern, Buttons, Eingabefeldern und Maus-Klicks!

In diesem Kapitel lernst du, wie du mit Pythons integriertem Modul **`tkinter`** und **Objektorientierter Programmierung (OOP)** professionelle Desktop-Programme baust.

---

## 📺 1. Vom Schwarz-Weiß-Fernseher zum Touchscreen (Event-Driven)

| Terminal (Konsole) | Grafische Oberfläche (Tkinter GUI) |
| :--- | :--- |
| **Linearer Ablauf:** Schritt 1 &rarr; Schritt 2 &rarr; `input()` &rarr; Ende | **Ereignisgesteuert (Event-Driven):** Das Fenster wartet in einer Dauerschleife (`mainloop`) auf Benutzeraktionen |
| Nur reiner Text | Buttons, Eingabefelder, Farben, Fenster |
| Programm beendet sich nach Ausführung | Programm bleibt geöffnet, bis das Fenster geschlossen wird |

### Der Event-Loop (`root.mainloop()`):
Ein GUI-Programm läuft nicht einfach von oben nach unten durch. Sobald das Fenster aufgebaut ist, übergibt Python die Kontrolle an den **Event-Loop**:
```python
root.mainloop()  # Wartet geduldig auf Klicks, Tastaturanschläge oder Fenster-Schließen
```

---

## 🧱 2. Die wichtigsten Tkinter-Widgets

Ein **Widget** (Window Gadget) ist ein grafisches Bauelement:

| Widget | Klasse | Zweck | Wichtigste Optionen / Methoden |
| :--- | :--- | :--- | :--- |
| **Hauptfenster** | `tk.Tk()` | Das Betriebssystem-Fenster | `.title("Titel")`, `.geometry("400x300")`, `.mainloop()` |
| **Textanzeige** | `tk.Label` | Zeigt Text oder Zahlen an | `text="Hallo"`, `font=("Arial", 14)`, `fg="blue"`, `bg="white"` |
| **Schaltfläche** | `tk.Button` | Klickbarer Knopf | `text="Klick"`, `command=self.methode` |
| **Eingabefeld** | `tk.Entry` | Einzeilige Texteingabe | `.get()`, `.insert(0, "Start")`, `.delete(0, "end")` |
| **Container** | `tk.Frame` | Gruppiert mehrere Widgets | Hilft beim sauberen Verschachteln von Layouts |

---

## 📐 3. Das Grid-Layout-System (Raster)

Um Elemente auf dem Bildschirm auszurichten, nutzen wir den **Grid-Layout-Manager**. Er funktioniert wie eine Tabelle oder ein Schachbrett:

```
               Spalte 0               Spalte 1
         ┌──────────────────────┬──────────────────────┐
Zeile 0  │  🔢 Überschrift (columnspan=2)              │
         ├──────────────────────┼──────────────────────┤
Zeile 1  │  Große Zähleranzeige: "0" (columnspan=2)    │
         ├──────────────────────┼──────────────────────┤
Zeile 2  │  Status: "Klicks: 0" (columnspan=2)         │
         ├──────────────────────┬──────────────────────┤
Zeile 3  │  ➕ Erhöhen          │  ➖ Verringern        │
         ├──────────────────────┴──────────────────────┤
Zeile 4  │  ↺ Zurücksetzen (columnspan=2)              │
         └─────────────────────────────────────────────┘
```

### Die wichtigsten Parameter bei `.grid()`:
- `row=0, column=1`: Bestimmt Zeile und Spalte.
- `columnspan=2`: Lässt das Element über 2 Spalten spannen.
- `padx=10, pady=5`: Äußerer Abstand (Padding) in Pixeln.
- `sticky="ew"`: Dehnt das Element nach Osten und Westen (links & rechts) aus.

> ⚠️ **Goldene Regel:** Mische niemals `.pack()` und `.grid()` im selben Eltern-Container! Verwende innerhalb eines Fensters oder Frames konsistent einen Layout-Manager.

---

## ⚙️ 4. Event-Driven Programming: Was passiert beim Klick?

Wenn ein Button geklickt wird, führt Tkinter die bei `command` hinterlegte Methode aus:

```python
# RICHTIG: Referenz auf die Methode übergeben (ohne Klammern!)
self.btn_plus = tk.Button(self.root, text="+", command=self.klick_plus)

# FALSCH: Würde die Methode SOFORT beim Start aufrufen, statt erst beim Klick!
self.btn_plus = tk.Button(self.root, text="+", command=self.klick_plus())
```

---

## 🏛️ 5. Clean Architecture: Model-View-Controller (MVC)

Warum packen wir nicht alles in eine einzige Datei/Funktion? Weil professioneller Code modular und automatisiert testbar sein muss!

```
┌────────────────────────────────┐         ┌────────────────────────────────┐
│   Model (ZaehlerLogik)         │         │   View/Controller (ZaehlerApp) │
│   - wert: int                  │         │   - root: tk.Tk                │
│   - schrittweite: int          │ ◄────── │   - label_anzeige: tk.Label    │
│   - erhoehen() -> int          │         │   - btn_plus: tk.Button        │
│   - verringern() -> int        │         │   - klick_plus()               │
│   (100% reines Python, keine GUI) │         │   (Tkinter-Widgets & Ereignisse)│
└────────────────────────────────┘         └────────────────────────────────┘
```

1. **`ZaehlerLogik` (Model):** Verwaltet die Daten (Zahlen, Grenzen, Schrittweiten). Es weiß nichts von Fenstern oder Buttons und kann in Unittests in Millisekunden geprüft werden.
2. **`ZaehlerApp` (View & Controller):** Erstellt die Oberfläche und ruft bei Klicks die Methoden von `self.logik` auf.

---

## 🎯 6. Deine Aufgaben in `aufgabe.py`

Öffne `14_gui_mit_tkinter/aufgabe.py` und vervollständige die Klassen:

1. **TODO 1:** `ZaehlerLogik.__init__` mit `startwert`, `min_wert`, `max_wert`, `schrittweite=1`, `klick_anzahl=0`.
2. **TODO 2:** `erhoehen()`, `verringern()` (mit Clamping an Min/Max) und `zuruecksetzen()`.
3. **TODO 3:** `setze_schrittweite()`, `ist_gerade()` und `__str__()`.
4. **TODO 4:** `ZaehlerApp.__init__` (Fenster-Konfiguration, Widgets anlegen und im Grid platzieren).
5. **TODO 5:** Event-Handler `klick_plus()`, `klick_minus()`, `klick_reset()`, `klick_schritt_setzen()`.
6. **TODO 6:** `aktualisiere_anzeige()` (Labels synchronisieren und farblich hervorheben).

---

## 🧪 7. Testen & Ausführen

### Automatische Tests ausführen:
```bash
python3 test_aufgabe.py
```

### Startbare grafische Applikation ausprobieren:
```bash
python3 gui_app.py
```
*(Hinweis: Die grafische Oberfläche benötigt eine Desktop-Umgebung mit Display)*
