# Go 15: Automatisiertes Testing, Table-Driven Tests & Benchmarks 🧪

Willkommen zu **Modul 15** des Go Cloud & Concurrency Lehrpfads!

In diesem Modul professionalisierst du deine Testpraxis mit Gos Standard-Tooling. Du schreibst wartbare Table-Driven Tests, führst Subtests aus und analysierst Speicherallokationen mit Gos Benchmark-Runner.

---

## 💡 1. Das Wichtigste in Kürze

### Table-Driven Test Pattern
```go
func TestSlugify(t *testing.T) {
    tests := []struct {
        name    string
        input   string
        want    string
        wantErr bool
    }{
        {"Normaler Text", "Hello World", "hello-world", false},
        {"Sonderzeichen", "Go 1.22 & Cloud!", "go-122-cloud", false},
        {"Leerer String", "", "", true},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got, err := Slugify(tt.input)
            if (err != nil) != tt.wantErr {
                t.Fatalf("Slugify() error = %v, wantErr %v", err, tt.wantErr)
            }
            if got != tt.want {
                t.Errorf("Slugify() = %v, want %v", got, tt.want)
            }
        })
    }
}
```

### Benchmarks & Allokationen
```go
func BenchmarkFastStringJoin(b *testing.B) {
    parts := []string{"apple", "banana", "cherry", "date"}
    b.ReportAllocs()
    b.ResetTimer()
    for i := 0; i < b.N; i++ {
        _ = FastStringJoin(parts, ", ")
    }
}
```

---

## 🎯 Aufgaben in `aufgabe.go`

1. **TODO 1 (`Slugify`)**:
   - Wandelt einen String in einen URL-Slug um:
     - Kleinschreibung (`strings.ToLower`)
     - Ersetzt Leerzeichen, Punkte und Sonderzeichen durch Bindestriche (`-`)
     - Entfernt doppelte Bindestriche (`--` -> `-`)
     - Trimmt Bindestriche am Anfang und Ende
   - Gibt einen Fehler zurück, falls der Eingabestring leer ist (`errors.New("input string cannot be empty")`).
2. **TODO 2 (`ValidateEmail`)**:
   - Prüft Email-Format:
     - Enthält genau ein `@`
     - Text vor `@` (Username) darf nicht leer sein
     - Domain nach `@` darf nicht leer sein und muss mindestens einen Punkt `.` enthalten (nicht als erstes/letztes Zeichen).
3. **TODO 3 (`FastStringJoin`)**:
   - Verbindet einen String-Slice mit einem Trennzeichen unter Verwendung von `strings.Builder`.
4. **TODO 4 (`RunTableDrivenTests`)**:
   - Führt eine strukturierte Testtabelle über `Slugify` und `ValidateEmail` aus.

---

## 🧪 Tests & Benchmarks ausführen

```bash
go test -v -bench=. -benchmem ./...
```
