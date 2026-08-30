# Go 06: Interfaces, Duck Typing & Polymorphie ⚡

Willkommen zu **Modul 06** des Go (Golang) Kurses!

In diesem Modul lernst du das Interface-System von Go kennen: Implizite Schnittstellen-Erfüllung (Structural Typing), lose Kopplung bei Services, Type Assertions (`val.(Type)`) und Type Switches auf `any`.

---

## 💡 1. Das Wichtigste in Kürze

### Implizite Implementierung
In Go implementiert ein Datentyp ein Interface automatisch, ohne Schlüsselwörter wie `implements`. Sobald alle Methodensignaturen übereinstimmen, ist der Typ polymorph einsetzbar.

### Type Assertions
Mit `val.(ConcreteType)` prüfst du, ob ein Interface-Wert einen bestimmten konkreten Typ kapselt:
```go
if s, ok := i.(string); ok {
    fmt.Println("Es ist ein String:", s)
}
```

### Type Switches
Mit `switch v := i.(type)` unterscheidest du dynamisch zwischen verschiedenen Typen.

### Leeres Interface (`any` / `interface{}`)
Das leere Interface hat 0 Methoden und wird von jedem Typ in Go erfüllt.

---

## 🎯 Teilziele in `aufgabe.go`

1. **TODO 1:** Interface `Storage` mit `Save(key, val string) error`, `Get(key string) (string, bool)` und `Count() int` definieren.
2. **TODO 2:** Struct `MemoryStorage` implementieren, das `Storage` erfüllt.
3. **TODO 3:** Polymorphe Funktion `SyncData(source, target Storage, keys []string) (int, error)` schreiben.
4. **TODO 4:** Funktion `TypPruefung(val any) string` mit Type-Switch realisieren.
