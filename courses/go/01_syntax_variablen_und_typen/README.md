# Go 01: Go Syntax, Variablen & Typensystem ⚡

Willkommen zu **Modul 01** des Go (Golang) Kurses!

In diesem Modul lernst du das fundamentale statische Typensystem von Go kennen: Deklarationen mit `var` und `:=`, Basistypen (`int`, `float64`, `string`, `bool`), Zero Values, Konstanten (`const` mit `iota`) und explizite Typkonvertierung.

---

## 💡 1. Das Wichtigste in Kürze

### `var` vs. `:=` (Short Variable Declaration)
- `var x int = 10`: Klassische Deklaration. Funktioniert auf Paket-Ebene (außerhalb von Funktionen) und lokal.
- `x := 10`: Kurzschreibweise mit **Type Inference**. Funktioniert **nur innerhalb von Funktionen**.

### Zero Values
In Go gibt es kein `undefined` oder uninitialisierten Speicher. Variablen ohne Zuweisung erhalten automatisch ihren Zero Value:
- `int` / `float64`: `0` / `0.0`
- `string`: `""` (leerer String)
- `bool`: `false`
- Pointer / Slices / Maps / Interfaces: `nil`

### Explizite Typkonvertierung
Go erzwingt strikte Typtreue. Es gibt **keine automatische Typumwandlung**:
```go
var a int = 42
var b float64 = float64(a) // Explizite Konvertierung nötig!
```

### Konstanten und `iota`
Mit `iota` lassen sich fortlaufende Zähler (Enums) elegant deklarieren:
```go
const (
    StatusOffline = iota // 0
    StatusOnline         // 1
    StatusBusy           // 2
)
```

---

## 🎯 Teilziele in `aufgabe.go`

1. **TODO 1:** `GetServerConfig()` implementieren (`"localhost"`, `8080`, `1000`, `true`).
2. **TODO 2:** `BerechneDurchschnitt(summe int, anzahl int) float64` mit expliziter Typkonvertierung implementieren.
3. **TODO 3:** `FormatiereServerStatus(name string, port int, online bool) string` mit `fmt.Sprintf` umsetzen.
4. **TODO 4:** `iota` Konstanten für `StatusStopped`, `StatusStarting`, `StatusRunning` definieren und `GetStatusName(status int) string` implementieren.
