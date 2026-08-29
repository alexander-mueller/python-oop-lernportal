# Kapitel 19: Generatoren, Iteratoren & itertools (Memory Efficiency & Streaming) 🌊⚡

Willkommen zu **Kapitel 19** im Lehrpfad 4 (*Professional Data Engineering*)!
In diesem Modul lernst du, wie professionelle Software-Entwickler riesige Datenmengen speichereffizient im RAM verarbeiten. Statt Gigabytes an Daten auf einmal in eine Liste zu laden und dein System zum Absturz zu bringen, streamst du Werte **on-demand** Tropfen für Tropfen mit **Generatoren** und dem mächtigen **`itertools`**-Modul.

---

## 🧭 Didaktischer Hintergrund

In Data Pipelines, Web-Servern und Big-Data-Anwendungen stößt klassisches Laden von Daten schnell an physikalische RAM-Grenzen:
- **Speicherüberlauf (Out of Memory):** Eine Liste mit 50 Millionen Objekten belegt mehrere Gigabytes Arbeitsspeicher.
- **Lazy Evaluation (Verzögerte Auswertung):** Werte werden erst in dem exakten Mikrosekunden-Moment berechnet, in dem sie gebraucht werden.
- **Null RAM-Verschwendung:** Ein Generator verbraucht unabhängig davon, ob er 10 oder 10 Milliarden Elemente liefert, immer nur eine winzige, konstante Speichermenge (ca. 100 Bytes)!

---

## 🚰 1. Die Badewannen- vs. Wasserhahn-Analogie

```
🔴 DIE BADEWANNE (Klassische Listen & Arrays)
┌────────────────────────────────────────────────────────┐
│  [Wert 1, Wert 2, Wert 3, ..., Wert 10.000.000]        │
│  -> 800 MB RAM belegt! Alles muss VORHER im RAM sein! │
└────────────────────────────────────────────────────────┘

🟢 DER WASSERHAHN (Generatoren & Streams mit yield)
┌────────────────────────────────────────────────────────┐
│  [Wasserhahn]  ── Tropfen 1 ──> [Verarbeitung]         │
│                ── Tropfen 2 ──> [Verarbeitung]         │
│                ── Tropfen 3 ──> [Verarbeitung]         │
│  -> ~100 Bytes RAM! Jeder Wert wird nach Gebrauch     │
│     wieder verworfen oder weitergeleitet.             │
└────────────────────────────────────────────────────────┘
```

---

## 🔄 2. Iterables vs. Iterators (`iter()`, `next()`, `StopIteration`)

In Python gibt es einen fundamentalen Unterschied:

| Begriff | Was ist das? | Wie wird es erzeugt? | Typische Beispiele |
| :--- | :--- | :--- | :--- |
| **Iterable** | Eine Sammlung, über die man iterieren kann (besitzt `__iter__()`). | Listen, Tupel, Strings, Dicts | `[1, 2, 3]`, `"Hallo"` |
| **Iterator** | Das Zustandsobjekt, das den aktuellen Zeiger hält und mit `next()` den nächsten Wert liefert (besitzt `__next__()`). | `it = iter(iterable)` | `iter([1, 2, 3])` |

### Was passiert bei `for x in sammlung:` unter der Haube?
1. Python ruft `it = iter(sammlung)` auf, um einen Iterator zu erhalten.
2. In jeder Schleifenrunde wird `x = next(it)` aufgerufen.
3. Wenn keine Elemente mehr vorhanden sind, löst Python intern die `StopIteration`-Exception aus und beendet die Schleife sauber.

```python
daten = [10, 20, 30]
it = iter(daten)

print(next(it))  # -> 10
print(next(it))  # -> 20
print(next(it))  # -> 30
# print(next(it))  # -> Löst StopIteration aus!
```

---

## 🪄 3. Eigene Generatoren mit `yield`

Das Schlüsselwort **`yield`** verwandelt eine gewöhnliche Funktion in eine Generator-Funktion.
- Ein `return` beendet die Funktion und vernichtet alle lokalen Variablen.
- Ein `yield` pausiert die Funktion, gibt den Zwischenwert zurück und merkt sich den exakten Programmzustand (Zeile, lokale Variablen), um beim nächsten `next()` genau dort weiterzumachen!

```python
def mein_generator():
    print("Starte Schritt 1...")
    yield "Erster Wert"
    print("Mache weiter bei Schritt 2...")
    yield "Zweiter Wert"
    print("Fertig!")

gen = mein_generator()  # Noch kein Code wird ausgeführt!
print(next(gen))        # Druckt: Starte Schritt 1... -> Erster Wert
print(next(gen))        # Druckt: Mache weiter... -> Zweiter Wert
```

### Unendliche Generatoren:
Mit `yield` sind unendliche Sequenzen möglich, ohne dass der Speicher überläuft:

```python
def endlos_zaehler(start=0, schritt=1):
    aktuell = start
    while True:
        yield aktuell
        aktuell += schritt
```

---

## ⚡ 4. Generator-Expressions: `(x**2 for x in ...)`

Genauso wie es List Comprehensions `[x for x in ...]` gibt, kannst du mit runden Klammern `(x for x in ...)` eine schlanke **Generator Expression** erzeugen:

```python
# 🔴 List Comprehension: Erzeugt 10 Mio. Zahlen sofort im RAM (ca. 80 MB!)
quadrate_liste = [x**2 for x in range(10_000_000)]

# 🟢 Generator Expression: Kostet ca. 100 Bytes RAM!
quadrate_gen = (x**2 for x in range(10_000_000))

print(next(quadrate_gen))  # 0
print(next(quadrate_gen))  # 1
print(next(quadrate_gen))  # 4
```

---

## 🧰 5. Das `itertools`-Modul (Die High-Performance Toolbox)

Pythons Standardbibliothek liefert mit `import itertools` hochgradig optimierte C-Iteratoren:

| Funktion | Erklärung | Code-Beispiel |
| :--- | :--- | :--- |
| `itertools.chain(*iterables)` | Hängt mehrere Iterables lückenlos hintereinander | `chain([1, 2], [3, 4])` $\rightarrow$ `1, 2, 3, 4` |
| `itertools.cycle(iterable)` | Wiederholt ein Iterable in einer Endlosschleife | `cycle(['A', 'B'])` $\rightarrow$ `A, B, A, B, A...` |
| `itertools.count(start, step)` | Unendlicher Zähler | `count(10, 2)` $\rightarrow$ `10, 12, 14, 16...` |
| `itertools.permutations(p, r)` | Alle geordneten Anordnungen der Länge $r$ | `permutations('AB', 2)` $\rightarrow$ `('A','B'), ('B','A')` |
| `itertools.combinations(p, r)` | Alle ungeordneten Kombinationen ohne Duplikate | `combinations('ABC', 2)` $\rightarrow$ `('A','B'), ('A','C'), ('B','C')` |
| `itertools.islice(iterable, n)`| Schneidet die ersten $n$ Elemente aus einem Stream | `islice(count(), 5)` $\rightarrow$ `0, 1, 2, 3, 4` |

---

## 📁 Die Dateien in diesem Ordner

- **`index.html`**: Interaktive Web-Lernseite mit visuellen Badewannen-Diagrammen, Code-Vergleichen, Cheat-Sheets und Checkliste.
- **`aufgabe.py`**: Dein Arbeitsblatt mit Type Hints und didaktischen TODOs für Generatoren, Filter und `itertools`.
- **`test_aufgabe.py`**: Automatische Unittest-Suite zur Überprüfung aller Anforderungen.
- **`musterloesung.py`**: Vollständig ausprogrammierte Referenzlösung.

---

## 🚀 Schnellstart

```bash
# 1. Bearbeite aufgabe.py
# 2. Führe die automatischen Tests aus:
python3 test_aufgabe.py

# 3. Oder starte das interaktive Benchmark-Skript:
python3 aufgabe.py
```
