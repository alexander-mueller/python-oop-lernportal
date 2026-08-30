# Go 04: Funktionen & Mehrfache Rückgabewerte ⚡

Willkommen zu **Modul 04** des Go (Golang) Kurses!

In diesem Modul lernst du das Funktionsmodell von Go im Detail kennen: Mehrfache Rückgabewerte (`(result, error)`), benannte Returns, variadische Parameter (`...`) und funktionale Closures.

---

## 💡 1. Das Wichtigste in Kürze

### Multiple Return Values
Go unterstützt native Tuple-Rückgaben ohne Wrapper-Klassen:
```go
func GetData(id string) (string, error) {
    if id == "" {
        return "", errors.New("id darf nicht leer sein")
    }
    return "Data for " + id, nil
}
```

### Benannte Rückgabewerte (Named Returns)
Rückgabeparameter können direkt in der Funktionssignatur benannt werden. Sie fungieren als lokale Variablen im Funktionskörper:
```go
func MinMax(a, b int) (min int, max int) {
    if a < b {
        min, max = a, b
    } else {
        min, max = b, a
    }
    return min, max
}
```

### Variadische Parameter (`...`)
Ein Parameter mit `...Typ` sammelt alle restlichen Argumente in einem Slice:
```go
func Sum(nums ...int) int {
    total := 0
    for _, n := range nums {
        total += n
    }
    return total
}
```

### Closures
Funktionen können als Rückgabewert dienen und Variablen ihres Entstehungskontexts binden.

---

## 🎯 Teilziele in `aufgabe.go`

1. **TODO 1:** `SichereDivision(a, b float64) (float64, error)` implementieren.
2. **TODO 2:** `BerechneStatistik(werte []int) (min int, max int, summe int, schnitt float64)` mit Named Returns.
3. **TODO 3:** `VariadischesSummieren(prefix string, zahlen ...int) string` mit `fmt.Sprintf`.
4. **TODO 4:** `ErstelleZaehler(start int) func() int` als Closure schreiben.
