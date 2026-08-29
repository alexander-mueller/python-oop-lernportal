# Kapitel 10: Vererbung (Inheritance) & super() 🧬🚗

Willkommen zu Kapitel 10! In diesem Kapitel lernst du eines der mächtigsten Konzepte der Objektorientierten Programmierung kennen: **Vererbung**.

---

## 🎯 Was du lernst

1. **Was ist Vererbung?**
   - Basisklasse (Elternklasse / Superklasse) vs. abgeleitete Klasse (Kindklasse / Subklasse).
   - "Ist-ein"-Beziehung: Ein `Auto` *ist ein* `Fahrzeug`. Ein `ElektroAuto` *ist ein* `Auto`.
2. **Das DRY-Prinzip (Don't Repeat Yourself):**
   - Gemeinsame Attribute (`marke`, `modell`, `baujahr`, `grundpreis`, `kilometerstand`) und Methoden (`fahren()`, `berechne_restwert()`) müssen nur **einmal** in der Basisklasse `Fahrzeug` geschrieben werden.
3. **Syntax in Python:**
   ```python
   class KindKlasse(ElternKlasse):
       pass
   ```
4. **Der Konstruktor der Elternklasse: `super().__init__()`:**
   - Mit `super().__init__(...)` delegierst du die Initialisierung der geerbten Attribute an die Elternklasse.
5. **Methoden erweitern & überschreiben (Method Overriding):**
   - Eine Kindklasse kann Methoden der Elternklasse neu definieren oder mit `super().methode()` erweitern.
6. **Typ-Prüfung:**
   - `isinstance(mein_auto, Fahrzeug)` &rarr; `True`
   - `issubclass(ElektroAuto, Fahrzeug)` &rarr; `True`

---

## 📊 UML-Klassendiagramm

```
           ┌───────────────────────────────────────────────┐
           │                   Fahrzeug                    │
           ├───────────────────────────────────────────────┤
           │ - marke: str                                  │
           │ - modell: str                                 │
           │ - baujahr: int                                │
           │ - grundpreis: float                           │
           │ - kilometerstand: float                       │
           ├───────────────────────────────────────────────┤
           │ + __init__(marke, modell, baujahr, grundpreis)│
           │ + fahren(km: float) -> None                   │
           │ + berechne_restwert(aktuelles_jahr) -> float  │
           │ + info() -> str                               │
           └───────────────────────▲───────────────────────┘
                                   │
                   ┌───────────────┴───────────────┐
                   │                               │
       ┌───────────┴───────────────┐   ┌───────────┴───────────────┐
       │           Auto            │   │            Lkw            │
       ├───────────────────────────┤   ├───────────────────────────┤
       │ - sitzplaetze: int        │   │ - max_zuladung_kg: float  │
       │ - anzahl_tueren: int      │   │ - aktuelle_ladung_kg: floa│
       ├───────────────────────────┤   ├───────────────────────────┤
       │ + __init__(..., sitze, ...)│  │ + __init__(..., max_ladung)│
       │ + hupen() -> str          │   │ + beladen(kg) -> bool     │
       │ + info() -> str           │   │ + entladen(kg) -> float   │
       └───────────▲───────────────┘   │ + info() -> str           │
                   │                   └───────────────────────────┘
       ┌───────────┴───────────────┐
       │        ElektroAuto        │
       ├───────────────────────────┤
       │ - batterie_kapazitaet_kwh │
       │ - batterie_ladestand_kwh  │
       │ - verbrauch_pro_100km     │
       ├───────────────────────────┤
       │ + reichweite() -> float   │
       │ + fahren(km) -> bool      │
       │ + aufladen(kwh) -> float  │
       │ + info() -> str           │
       └───────────────────────────┘
```

---

## 📁 Die Dateien in diesem Ordner

- **`index.html`**: Die interaktive Lernseite mit visuellen Erklärungen, Analogien, Diagrammen und Lösungstipps.
- **`aufgabe.py`**: Dein Arbeitsblatt mit den Klassen `Fahrzeug`, `Auto`, `ElektroAuto` und `Lkw`.
- **`test_aufgabe.py`**: Automatische Tests (`python3 test_aufgabe.py`).
- **`musterloesung.py`**: Vollständig ausprogrammierte Beispiellösung.

---

## 🚀 Schnellstart

```bash
# 1. Bearbeite aufgabe.py
# 2. Teste deine Lösung:
python3 test_aufgabe.py
```
