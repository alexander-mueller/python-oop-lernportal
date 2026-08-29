# Kapitel 11: Polymorphie & Interfaces 🎭📐

Willkommen zu Kapitel 11! In diesem Kapitel lernst du das Konzept der **Polymorphie (Vielgestaltigkeit)** und **Interfaces (abstrakte Basisklassen)** in Python kennen.

---

## 🎯 Was du lernst

1. **Was bedeutet Polymorphie?**
   - Aus dem Griechischen: *poly* = viel, *morph* = Gestalt &rarr; "Vielgestaltigkeit".
   - Verschiedene Klassen stellen Methoden mit demselben Namen und denselben Parametern bereit (`flaeche()`, `umfang()`, `info()`), berechnen ihr Ergebnis aber völlig unterschiedlich!
2. **Didaktische Analogie: Die Universalfernbedienung &amp; Mediaplayer:**
   - Wenn du auf der Fernbedienung auf "Power" drückst, schaltet sich der Fernseher, die Soundbar oder die Spielkonsole ein – jedes Gerät auf seine Art.
   - Ein Mediaplayer drückt einfach auf `medium.abspielen()` – egal ob MP3, MP4, FLAC oder Stream.
3. **Abstrakte Basisklassen &amp; Interfaces (`abc.ABC`):**
   - Mit `from abc import ABC, abstractmethod` zwingst du abgeleitete Klassen dazu, bestimmte Methoden zu implementieren.
   - Wird eine abstrakte Methode nicht implementiert, verhindert Python das Erstellen von Objekten mit einem `TypeError`.
4. **Duck Typing in Python:**
   - *"If it walks like a duck and quacks like a duck, it is a duck."*
   - In Python zählt das Verhalten eines Objekts: Solange ein Objekt eine Methode `flaeche()` besitzt, kann es in polymorphen Berechnungen verwendet werden.
5. **Polymorphe Sammlungen (Manager-Klassen):**
   - Eine Liste mit vielen unterschiedlichen Objekten (`[Rechteck, Kreis, Dreieck]`) durchlaufen und einheitlich `form.flaeche()` aufrufen – ohne eine einzige `if isinstance(...)` Abfrage!

---

## 📊 UML-Klassendiagramm

```
              ┌───────────────────────────────────────────────┐
              │             «abstract» Form                   │
              ├───────────────────────────────────────────────┤
              │ - farbe: str                                  │
              ├───────────────────────────────────────────────┤
              │ + __init__(farbe: str = "schwarz")            │
              │ + {abstract} flaeche() -> float               │
              │ + {abstract} umfang() -> float                │
              │ + info() -> str                               │
              └───────────────────────▲───────────────────────┘
                                      │
              ┌───────────────────────┼───────────────────────┐
              │                       │                       │
  ┌───────────┴───────────┐ ┌─────────┴─────────┐ ┌───────────┴───────────┐
  │       Rechteck        │ │       Kreis       │ │        Dreieck        │
  ├───────────────────────┤ ├───────────────────┤ ├───────────────────────┤
  │ - breite: float       │ │ - radius: float   │ │ - seite_a: float      │
  │ - hoehe: float        │ ├───────────────────┤ │ - seite_b: float      │
  ├───────────────────────┤ │ + flaeche()       │ ├───────────────────────┤
  │ + flaeche()           │ │ + umfang()        │ │ + hypotenuse()        │
  │ + umfang()            │ │ + info()          │ │ + flaeche()           │
  │ + info()              │ └───────────────────┘ │ + umfang()            │
  └───────────────────────┘                       │ + info()              │
                                                  └───────────────────────┘

  ┌───────────────────────────────────────────────────────────┐
  │                      Zeichenflaeche                       │
  ├───────────────────────────────────────────────────────────┤
  │ - name: str                                               │
  │ - formen: list[Form]                                      │
  ├───────────────────────────────────────────────────────────┤
  │ + hinzufuegen(form: Form) -> None                         │
  │ + anzahl_formen() -> int                                  │
  │ + gesamte_flaeche() -> float   <-- ruft form.flaeche() auf│
  │ + gesamter_umfang() -> float   <-- ruft form.umfang() auf │
  │ + formen_nach_farbe(farbe) -> list[Form]                  │
  │ + groesste_form() -> Form | None                          │
  │ + report() -> list[str]                                   │
  └───────────────────────────────────────────────────────────┘
```

---

## 📁 Die Dateien in diesem Ordner

- **`index.html`**: Die interaktive Lernseite mit visuellen Erklärungen, Analogien, UML-Diagrammen und Lösungstipps.
- **`aufgabe.py`**: Dein Arbeitsblatt mit den Klassen `Form`, `Rechteck`, `Kreis`, `Dreieck` und `Zeichenflaeche`.
- **`test_aufgabe.py`**: Automatische Tests (`python3 test_aufgabe.py`).
- **`musterloesung.py`**: Vollständig ausprogrammierte Beispiellösung.

---

## 🚀 Schnellstart

```bash
# 1. Bearbeite aufgabe.py
# 2. Teste deine Lösung:
python3 test_aufgabe.py
```
