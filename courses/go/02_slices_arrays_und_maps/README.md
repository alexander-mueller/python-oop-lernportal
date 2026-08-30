# Go 02: Slices, Arrays & Maps ⚡

Willkommen zu **Modul 02** des Go (Golang) Kurses!

In diesem Modul meisterst du die grundlegenden Sammlungs-Datentypen in Go: Arrays fester Größe, dynamische Slices (`make`, `append`, Reslicing) und Assoziative Maps (`delete`, Comma-OK Idiom).

---

## 💡 1. Das Wichtigste in Kürze

### Array vs. Slice
- **Array (`[5]int`)**: Feste Länge zur Compile-Zeit. Werttyp: Übergabe an Funktionen kopiert das gesamte Array.
- **Slice (`[]int`)**: Dynamischer View auf ein Underlyings Array. Enthält Pointer, Länge (`len`) und Kapazität (`cap`).
- **`make([]T, len, cap)`**: Erstellt ein Slice mit vorallokiertem Speicher, um wiederholte Speicher-Reallokationen bei vielen `append`-Aufrufen zu vermeiden.

### Slicing Syntax
- `s[start:ende]`: Elemente von Index `start` bis `ende-1`.
- `s[:ende]`: Ab Beginn bis `ende-1`.
- `s[start:]`: Ab Index `start` bis zum Ende.

### Maps in Go
Maps bilden Schlüssel eindeutig auf Werte ab:
```go
m := make(map[string]int)
m["cpu"] = 4
delete(m, "cpu") // Entfernt den Schlüssel

// Comma-OK Idiom:
wert, existiert := m["ram"]
if !existiert {
    // Schlüssel fehlt
}
```

---

## 🎯 Teilziele in `aufgabe.go`

1. **TODO 1:** `FiltereGeradeZahlen(zahlen []int) []int` implementieren.
2. **TODO 2:** `ErweitereProtokolle(logs []string, neueEintraege ...string) []string` umsetzen.
3. **TODO 3:** `ZaehleWortHaeufigkeit(text string) map[string]int` schreiben.
4. **TODO 4:** `SichereBenutzerAbfrage` und `LoescheBenutzer` mit Comma-OK Idiom implementieren.
