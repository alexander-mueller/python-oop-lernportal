# PS 02: Die Objekt-Pipeline & Get-Member 🔷

Willkommen zu **Modul 02** des PowerShell 7+ Core Kurses!

In diesem Modul erforschst du das Kernstück von PowerShell: Die **.NET-Objekt-Pipeline**. Statt mit instabilen Text-Streams zu kämpfen, arbeitest du mit vollwertigen Objekten inklusive Typensicherheit, Eigenschaften und Methoden.

---

## 💡 1. Das Wichtigste auf einen Blick

### Objekte statt Text
- Jeder Befehl in PowerShell gibt strukturierte .NET-Objekte zurück.
- Mit `$Object.PropertyName` greifst du direkt auf Datenfelder zu.
- Mit `$Object.MethodName()` rufst du Funktionen des Objekts auf.

### `Get-Member` & Typ-Inspektion
- `Get-Member` (Alias: `gm`) zeigt alle Methoden und Eigenschaften eines Pipeline-Objekts an.
- Mit `$obj.GetType().FullName` ermittelst du die zugrundeliegende .NET-Klasse.

### Statische .NET-Klassen & Multiplikatoren
- Aufruf statischer Methoden mit `[KlassenName]::MethodenName()` (z.B. `[Math]::Round(...)`).
- PowerShell stellt integrierte Speicher-Multiplikatoren bereit: `1KB`, `1MB`, `1GB`, `1TB`.

---

## 🎯 Aufgabenübersicht in `aufgabe.ps1`

1. **Get-ObjectPropertyNames**: Extrahiert alle Property-Namen eines Objekts als String-Array.
2. **Invoke-StringSanitization**: Führt Methodenverkettung (`.Trim()`, `.ToUpper()`, `.Replace()`) auf einem String aus.
3. **Get-ProcessMemoryInMB**: Berechnet Megabyte aus Byte-Angaben mit Rundung auf 2 Dezimalstellen.
4. **Get-DotNetTypeInfo**: Ermittelt Typ-Informationen über `.GetType()`.
