# Kapitel 16: Master-Abschlussprojekt – PetCare & Tierheim-Manager 🐾🏥🖥️

Herzlichen Glückwunsch! Du bist am **großen Finale der gesamten Python OOP-Übungsreihe** angekommen.
Hier führst du alles zusammen, was du in den drei Lehrpfaden gelernt hast – von Datentypen und Schleifen über Vererbung, Polymorphie, Exceptions und JSON-Persistenz bis hin zur interaktiven **Tkinter Desktop-Applikation** mit professioneller **Model-View-Controller (MVC)** Architektur.

---

## 🧭 Die 3 Lehrpfade im Masterprojekt vereint

```
                     [ 🏆 KAPITEL 16: MEISTERSTÜCK ]
                                    │
    ┌───────────────────────────────┼──────────────────────────────┐
    ▼                               ▼                              ▼
[ 🛣️ LEHRPFAD 1: GRUNDLAGEN ]  [ 🛣️ LEHRPFAD 2: OOP & TOOLS ] [ 🛣️ LEHRPFAD 3: SOFTWARETECHNIK ]
 • Datentypen, Strings & Mathe   • Klassen, __init__, self      • Vererbung & super()
 • Schleifen, Listen & Dicts     • Methoden & Interaktionen     • Polymorphie & Interfaces
 • Typsichere Validierung        • __str__ & Repräsentation     • Eigene Exception-Klassen
 • CSV-Tabellenexport            • Modularer Aufbau             • JSON Savegame-Persistenz
                                                               • Tkinter Desktop-GUI (MVC)
                                                               • 100% TDD / Unittest-Suite
```

---

## 🏛️ Die Architektur: Model-View-Controller (MVC)

In professioneller Software wird die **Geschäftslogik (Model)** strikt von der **grafischen Oberfläche (View & Controller)** getrennt.
Dadurch kann die gesamte Fachlogik zu 100% in automatischen Unittests ohne Bildschirm/Fenster getestet werden!

```
 ┌────────────────────────────────────────────────────────────────────────┐
 │                              BENUTZER                                  │
 └──────────────────┬─────────────────────────────────▲───────────────────┘
                    │ 1. Klickt Button / gibt Text ein│ 4. Sieht Update
                    ▼                                 │
 ┌────────────────────────────────────────────────────┴───────────────────┐
 │                     VIEW & CONTROLLER (TierheimApp)                    │
 │  • Tkinter-Fenster, Formular, Listbox, Aktionsbuttons, Statusleiste    │
 │  • Liest Formulareingaben aus & fängt ValidierungsFehler ab            │
 └──────────────────┬─────────────────────────────────▲───────────────────┘
                    │ 2. Ruft Methoden auf            │ 3. Liefert Daten
                    ▼                                 │
 ┌────────────────────────────────────────────────────┴───────────────────┐
 │                             MODEL (Tierheim)                           │
 │  • Verwaltet Tierbestand (Hund, Katze, Vogel)                          │
 │  • Filter (Art, ungeimpft, hungrig) & Statistiken (Ø Alter, Gewicht)   │
 │  • Persistenz: JSON Speichern/Laden & CSV-Export                       │
 └────────────────────────────────────────────────────────────────────────┘
```

---

## 📊 UML-Klassendiagramm

```
           ┌──────────────────────────────────────────────┐
           │             Exception: TierheimFehler        │
           └──────────────────────▲───────────────────────┘
                                  │
         ┌────────────────────────┼────────────────────────┐
         │                        │                        │
┌────────┴─────────────┐ ┌────────┴────────────┐ ┌─────────┴───────────────┐
│ ValidierungsFehler   │ │TierNichtGefunden    │ │KapazitaetUeberschritten │
└──────────────────────┘ └─────────────────────┘ └─────────────────────────┘

                                  ┌───────────────────────────────┐
                                  │            «class»            │
                                  │             Tier              │
                                  ├───────────────────────────────┤
                                  │ + name: str                   │
                                  │ + alter: int                  │
                                  │ + gewicht: float              │
                                  │ + geimpft: bool               │
                                  │ + hunger: int (0..100)        │
                                  ├───────────────────────────────┤
                                  │ + fuettern(menge_g: int): str │
                                  │ + impfen(): bool              │
                                  │ + mache_laut(): str           │
                                  │ + get_details(): str          │
                                  │ + to_dict(): dict             │
                                  │ + from_dict(data: dict): Tier │
                                  └───────────────▲───────────────┘
                                                  │ (Vererbung)
                ┌─────────────────────────────────┼─────────────────────────────────┐
                │                                 │                                 │
 ┌──────────────┴──────────────┐   ┌──────────────┴──────────────┐   ┌──────────────┴──────────────┐
 │            Hund             │   │            Katze            │   │            Vogel            │
 ├─────────────────────────────┤   ├─────────────────────────────┤   ├─────────────────────────────┤
 │ + rasse: str                │   │ + stubenrein: bool          │   │ + spannweite_cm: float      │
 │ + gassigegangen: bool       │   │ + kratzbaum_benutzt: bool   │   │ + kann_sprechen: bool       │
 ├─────────────────────────────┤   ├─────────────────────────────┤   ├─────────────────────────────┤
 │ + gassi_gehen(minuten): str │   │ + kratzen(): str            │   │ + fliegen(runden): str      │
 │ + mache_laut(): str (Wuff!) │   │ + mache_laut(): str (Miau!) │   │ + mache_laut(): str (Tsch!) │
 └─────────────────────────────┘   └─────────────────────────────┘   └─────────────────────────────┘
                                                  ▲
                                                  │ 1:n Komposition
 ┌────────────────────────────────────────────────┴────────────────────────┐
 │                                Tierheim                                 │
 ├─────────────────────────────────────────────────────────────────────────┤
 │ + name: str                                                             │
 │ + max_kapazitaet: int                                                   │
 │ + tiere: List[Tier]                                                     │
 ├─────────────────────────────────────────────────────────────────────────┤
 │ + tier_aufnehmen(tier: Tier): None                                      │
 │ + tier_entlassen(name: str): Tier                                       │
 │ + finde_tier(name: str): Optional[Tier]                                 │
 │ + filtriere_nach_art(art: str): List[Tier]                              │
 │ + ungeimpfte_tiere(): List[Tier]                                        │
 │ + hungrige_tiere(schwellenwert: int): List[Tier]                        │
 │ + durchschnittsalter(): float                                           │
 │ + gesamtgewicht(): float                                                │
 │ + alle_fuettern(menge: int): dict                                       │
 │ + alle_impfen(): int                                                    │
 │ + speichern_json(pfad: str): None                                       │
 │ + laden_json(pfad: str): None                                           │
 │ + exportiere_csv(pfad: str): None                                       │
 └─────────────────────────────────────────────────────────────────────────┘
```

---

## 📝 Aufgabenstellung (Schritt für Schritt)

Öffne die Datei `aufgabe.py` und bearbeite die nummerierten Abschnitte:

### Schritt 1: Eigene Exceptions definieren
Erstelle die Exception-Klassen:
- `TierheimFehler(Exception)` als Basis
- `ValidierungsFehler(TierheimFehler)`
- `TierNichtGefundenFehler(TierheimFehler)`
- `KapazitaetUeberschrittenFehler(TierheimFehler)`

### Schritt 2: Basisklasse `Tier` implementieren
- Validiere im `__init__`: `name` darf nicht leer sein, `alter >= 0`, `gewicht > 0`.
- Implementiere `fuettern(futtermenge_gramm)`: Senkt Hunger um `futtermenge_gramm * 0.2` (Minimum 0).
- Implementiere `impfen()`: Setzt `geimpft = True` (gibt `True` bei Neugeimpften, `False` bei bereits Geimpften).
- Implementiere `to_dict()` und die Factory-Methode `from_dict(cls, data)` (stellt automatisch die korrekte Kindklasse wieder her!).

### Schritt 3: Spezialisierte Kindklassen `Hund`, `Katze`, `Vogel`
- Nutze `super().__init__(...)` für gemeinsame Attribute.
- Überschreibe `mache_laut()` polymorph (Hund bellt, Katze miaut/schnurrt, Vogel zwitschert/plappert).
- Implementiere artspezifische Methoden (`gassi_gehen()`, `kratzen()`, `fliegen()`).
- Erweitere `to_dict()` um die Kindklassen-Attribute.

### Schritt 4: Das Model `Tierheim`
- Aufnahme von Tieren mit Kapazitätsprüfung (`max_kapazitaet`).
- Entlassen von Tieren nach Name (mit Exception-Handling falls nicht gefunden).
- Filterfunktionen (`filtriere_nach_art`, `ungeimpfte_tiere`, `hungrige_tiere`).
- Statistiken: `durchschnittsalter()`, `gesamtgewicht()`.
- Massenaktionen: `alle_fuettern()`, `alle_impfen()`.
- Persistenz: `speichern_json()`, `laden_json()` und `exportiere_csv()`.

### Schritt 5: Die Desktop-GUI `TierheimApp` (Tkinter)
- Verknüpfe Buttons und Formularfelder mit den Model-Methoden.
- Fange Fehler (`ValidierungsFehler`, etc.) in `try-except`-Blöcken ab und gib Feedback in der dynamischen Statusleiste.
- Halte die Listbox und Kapazitätsanzeige synchron mit dem Datenmodell.

---

## 🧪 Tests ausführen & App starten

### 1. Automatische Unittests ausführen:
```bash
python3 test_aufgabe.py
```

### 2. Desktop-App mit grafischer Oberfläche starten:
```bash
python3 app.py
```

---

## 💡 Best Practices für dein Meisterstück
1. **Never trust user input:** Prüfe Datentypen und Grenzwerte frühzeitig im Konstruktor.
2. **Polymorphie nutzen:** Anstatt mit vielen `if/elif`-Abfragen nach dem Typ zu unterscheiden, rufe einfach `tier.mache_laut()` oder `tier.fuettern()` auf!
3. **Model & View trennen:** Halte Berechnungen und Daten im `Tierheim`-Objekt und nutze Tkinter nur zur Anzeige.
