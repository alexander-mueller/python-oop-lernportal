# Kapitel 20: Dataclasses, Type Hints & Decorators (Moderne Python-Architektur) 🏷️✨

Willkommen zu **Kapitel 20** im Lehrpfad 4 (*Professional Data Engineering*)!
In diesem Modul lernst du die Kernbausteine moderner, robuster Python-Architekturen kennen:
1. **Dataclasses (`@dataclass`)**: Schluss mit endlosem Boilerplate-Code für `__init__`, `__repr__` und `__eq__`!
2. **Fortgeschrittene Type Hints**: Statische Typsicherheit mit `Optional`, `Union`, `Callable` und `Dict`.
3. **Eigene Decorators**: Funktionserweiterungen wie Logging, Zeitmessung und Zugriffskontrollen als wiederverwendbare Hüllen.
4. **Standard-Decorators**: `@property`, `@classmethod` und `@staticmethod`.

---

## 🧭 Didaktische Analogien

### A) Das Fertighaus / Die Gussform (`@dataclass`)
Statt jeden Ziegelstein für den Konstruktor (`def __init__(self, a, b, c): self.a = a...`), den String-Druck (`def __repr__`) und Vergleiche (`def __eq__`) von Hand zu mauern, gibst du Python einfach die **Gussform** (die Feld-Typen). Python gießt das gesamte Klassenfundament automatisch in Millisekunden!

### B) Die Geschenkverpackung / Schutzhülle (Decorators)
Ein Decorator nimmt eine existierende Funktion, wickelt eine schützende Hülle (den Wrapper) darum und gibt das eingepackte Geschenk zurück. Die ursprüngliche Funktion bleibt unverändert, erhält aber Superkräfte (z.B. Zeitmessung oder Aufrufzählung)!

```
                ┌────────────────────────────────────────────────────────┐
                │ 🎁 DECORATOR WRAPPER                                   │
                │                                                        │
                │   [1. Vorher]  ⏱️ Startzeit erfassen / Zähler +1      │
                │   [2. Kern]    ▶️ Originalfunktion ausführen          │
                │   [3. Nachher] 📊 Dauer berechnen & loggen            │
                │                                                        │
                └────────────────────────────────────────────────────────┘
```

---

## 📦 1. Dataclasses: Schluss mit Boilerplate-Code

### Vor Python 3.7 (Klassischer Boilerplate):
```python
class ArtikelKlassisch:
    def __init__(self, name: str, preis: float, kategorie: str = "Allgemein"):
        self.name = name
        self.preis = preis
        self.kategorie = kategorie

    def __repr__(self):
        return f"ArtikelKlassisch(name='{self.name}', preis={self.preis}, kategorie='{self.kategorie}')"

    def __eq__(self, other):
        if not isinstance(other, ArtikelKlassisch):
            return False
        return (self.name, self.preis, self.kategorie) == (other.name, other.preis, other.kategorie)
```

### Modern mit `@dataclass`:
```python
from dataclasses import dataclass, field

@dataclass
class Artikel:
    name: str
    preis: float
    kategorie: str = "Allgemein"
```
Python erzeugt `__init__`, `__repr__` und `__eq__` vollautomatisch!

### ⚠️ Wichtig: Veränderliche Standardwerte mit `field(default_factory=...)`
Listen oder Dictionaries dürfen in Dataclasses niemals als `artikel: list = []` definiert werden (da alle Instanzen sonst dieselbe Liste teilen würden). Nutze stattdessen immer `field(default_factory=list)`:

```python
@dataclass
class Warenkorb:
    kunde: str
    artikel_liste: list[Artikel] = field(default_factory=list)
```

---

## 🏷️ 2. Fortgeschrittene Type Hints

Pythons `typing`-Modul macht deinen Code selbsterklärend und schützt vor bösen Überraschungen:

| Type Hint | Bedeutung | Beispiel |
| :--- | :--- | :--- |
| `Optional[T]` | Wert vom Typ `T` oder `None` (`Union[T, None]`) | `Optional[str]` (z.B. `"Max"` oder `None`) |
| `Union[A, B]` | Wert kann entweder Typ `A` oder Typ `B` sein | `Union[int, float]` |
| `Callable[[Arg1, Arg2], ReturnType]` | Eine Funktion als Argument oder Rückgabe | `Callable[[int, int], bool]` |
| `List[T]`, `Dict[K, V]` | Typisierte Listen und Key-Value-Mappings | `Dict[str, Union[str, int]]` |

---

## 🎨 3. Eigene Decorators schreiben

Ein Decorator ist eine Funktion höherer Ordnung, die eine Funktion entgegennimmt und eine neue Wrapper-Funktion zurückliefert. Nutze immer `@functools.wraps(func)`, um den ursprünglichen Namen und Docstring zu erhalten:

```python
import functools
import time

def zeitmessung(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        ergebnis = func(*args, **kwargs)
        dauer = time.perf_counter() - start
        print(f"[⏱️] {func.__name__} dauerte {dauer:.4f}s")
        return ergebnis
    return wrapper

@zeitmessung
def berechne_daten():
    time.sleep(0.1)
    return 42
```

---

## ⚙️ 4. Standard-Decorators im Überblick

- **`@property`**: Ermöglicht den Aufruf einer Methode wie ein Attribut (`auto.geschwindigkeit` statt `auto.get_geschwindigkeit()`).
- **`@classmethod`**: Erhält die Klasse `cls` als ersten Parameter; ideal für alternative Konstruktoren (Factory Methods wie `Artikel.aus_csv_zeile(zeile)`).
- **`@staticmethod`**: Reine Hilfsfunktion innerhalb des Klassen-Namespaces ohne Zugriff auf `self` oder `cls`.

---

## 📁 Die Dateien in diesem Ordner

- **`index.html`**: Interaktive Web-Lernseite mit visuellen Ablaufdiagrammen, Vorher-Nachher-Vergleichen, Cheat-Sheets und Checkliste.
- **`aufgabe.py`**: Dein Arbeitsblatt mit Type Hints und didaktischen TODOs für Dataclasses, Warenkorb, Decorators und Typprüfung.
- **`test_aufgabe.py`**: Automatische Unittest-Suite zur Überprüfung aller Anforderungen.
- **`musterloesung.py`**: Vollständig ausprogrammierte Referenzlösung.

---

## 🚀 Schnellstart

```bash
# 1. Bearbeite aufgabe.py
# 2. Führe die automatischen Tests aus:
python3 test_aufgabe.py

# 3. Oder starte das interaktive Skript:
python3 aufgabe.py
```
