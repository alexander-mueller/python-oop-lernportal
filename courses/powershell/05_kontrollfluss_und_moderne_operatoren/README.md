# PS 05: Kontrollfluss & Moderne PS7 Operatoren ⚡

Willkommen zu **Modul 05** und **Lehrpfad 2: Skripting, Kontrollfluss & Error-Handling**!

In diesem Modul hebst du deine PowerShell-Skripting-Fähigkeiten auf Profi-Niveau. Du lernst nicht nur die klassischen Vergleichs- und Verzweigungskonstrukte kennen, sondern auch die modernen Operatoren von **PowerShell 7+ Core** wie Ternary `?:`, Null-Coalescing `??` und Chaining `&&` / `||`.

---

## 💡 1. Das Wichtigste auf einen Blick

### Vergleichsoperatoren
- `-eq`, `-ne`, `-gt`, `-ge`, `-lt`, `-le`
- `-and`, `-or`, `-not` (oder `!`)
- `-match` für Reguläre Ausdrücke

### Moderne PowerShell 7 Operatoren
```powershell
# Ternary Operator:
$ergebnis = $isAdmin ? "Vollzugriff" : "Eingeschränkt"

# Null-Coalescing Operator:
$wert = $customVal ?? $defaultVal

# Pipeline-Chaining:
Start-Task && Write-Host "Erfolg" || Write-Host "Fehler"
```

### `switch -Regex`
```powershell
switch -Regex ($inputString) {
    "^ERR-(\d+)"  { "Fehler $Matches[1]" }
    "^WARN"       { "Warnung" }
    default       { "Unbekannt" }
}
```

---

## 🎯 Aufgabenübersicht in `aufgabe.ps1`

1. **Get-AccessDecision**: Berechtigungsentscheidung mit Rolle und Aktiv-Status.
2. **Get-ConfigWithFallback**: 3-Stufen Null-Coalescing Fallback (`??`).
3. **Classify-LogMessage**: Einstufung von Logmeldungen mittels `switch -Regex`.
4. **Test-NetworkPort**: Validierung von Portnummern mit Vergleichsoperatoren.
