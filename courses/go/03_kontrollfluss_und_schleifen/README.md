# Go 03: Kontrollfluss, for-Loops & switch ⚡

Willkommen zu **Modul 03** des Go (Golang) Kurses!

In diesem Modul lernst du, wie Go Kontrollstrukturen handhabt: Die einzige Schleife `for` (inkl. `range` und `while`-Ersatz), `if` mit Initialisierung zur Begrenzung von Variablen-Scopes und mächtige `switch`-Anweisungen.

---

## 💡 1. Das Wichtigste in Kürze

### Die 4 Gesichter der `for`-Schleife
1. **Klassisch:** `for i := 0; i < 10; i++`
2. **Bedingt (`while`):** `for bedingung`
3. **Endlos:** `for { ... }`
4. **Iterator (`range`):** `for i, v := range slice` oder `for k, v := range myMap`

### `if` mit Initialisierungs-Statement
Ermöglicht saubere Scope-Begrenzung von Hilfsvariablen:
```go
if val, ok := cache[key]; ok {
    // val existiert nur in diesem Block
}
```

### `switch` in Go
- Kein automatisches Durchfallen (kein `break` erforderlich).
- Erlaubt mehrere Werte pro Case (`case 200, 201:`).
- Tagless `switch`: Ersetzt verschachtelte `if/else`-Blöcke.

---

## 🎯 Teilziele in `aufgabe.go`

1. **TODO 1:** `SummiereBereich(start, ende int) int` mit klassischer `for`-Schleife.
2. **TODO 2:** `BerechneFakultaet(n int) (int, bool)` mit while-artiger `for`-Schleife.
3. **TODO 3:** `FindeMaxUndMin(werte []int) (int, int, bool)` mit `for ... range`.
4. **TODO 4:** `HTTPStatusKategorie(statusCode int) string` mit `switch`.
