# Go 05: Structs & Methoden 🏗️

Willkommen zu **Modul 05** des Go (Golang) Kurses!

In diesem Modul lernst du, wie Go Datenstrukturen und Verhalten ohne traditionelle Klassen kapselt: Struct-Definitionen, Konstruktoren, Value-Receiver vs. Pointer-Receiver und Struct Embedding.

---

## 💡 1. Das Wichtigste in Kürze

### Structs & Konstruktor-Pattern
In Go deklarierst du Typen mit `type Name struct`. Konstruktoren werden als Funktionen nach dem Schema `NewName(...) *Name` realisiert.

### Value- vs. Pointer-Receiver
- **Value-Receiver (`func (u User) Info()`)**: Arbeitet auf einer Kopie. Das Original-Struct im Speicher wird nicht berührt.
- **Pointer-Receiver (`func (u *User) SetEmail(e string)`)**: Erhält die Speicheradresse des Objekts. Änderungen sind persistent.

### Struct Embedding (Komposition)
Felder und Methoden eines anonym eingebetteten Structs stehen dem übergeordneten Struct automatisch zur Verfügung:
```go
type Admin struct {
    User
    Superpower string
}
```

---

## 🎯 Teilziele in `aufgabe.go`

1. **TODO 1:** Struct `User` (ID int, Username string, Email string, Active bool) und Konstruktor `NewUser(...) *User` erstellen.
2. **TODO 2:** Value-Receiver Methode `(u User) Info() string` implementieren.
3. **TODO 3:** Pointer-Receiver Methoden `(u *User) Deactivate()` und `(u *User) UpdateEmail(newEmail string)` schreiben.
4. **TODO 4:** Struct `AdminUser` mit eingebettetem `User` und `(a *AdminUser) Permissions() []string` umsetzen.
