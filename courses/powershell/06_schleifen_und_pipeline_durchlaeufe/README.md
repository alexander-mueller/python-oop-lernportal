# PS 06: Schleifen & Pipeline-Durchläufe ⚡

Willkommen zu **Modul 06** des PowerShell 7+ Core Kurses!

In diesem Modul lernst du die verschiedenen Schleifenkonstrukte in PowerShell und ihre Anwendungsbereiche kennen:
1. `foreach ($item in $list)` für blitzschnelle Berechnungen im Arbeitsspeicher
2. `ForEach-Object` (mit `-Begin`, `-Process`, `-End`) für speicherschonendes Pipeline-Streaming
3. `do..until` und `while` für dynamische Wiederholungs- und Retry-Muster
4. Schleifensteuerung mit `continue` und `break`

---

## 💡 1. Das Wichtigste auf einen Blick

### `foreach` vs. `ForEach-Object`
- `foreach`: Schneller Statement-Block für Arrays.
- `ForEach-Object`: Cmdlet für Streaming über die Pipeline.

### Lifecycle-Blöcke
```powershell
1..5 | ForEach-Object -Begin {
    $sum = 0
} -Process {
    $sum += $_
} -End {
    $sum
}
```

### `do..until` für Retry-Muster
```powershell
do {
    $tries++
} until ($success -or $tries -ge $maxTries)
```

---

## 🎯 Aufgabenübersicht in `aufgabe.ps1`

1. **Get-FilteredEvenSquares**: Berechnet Quadrate gerader Zahlen mit `foreach` und `continue`.
2. **Invoke-StreamingPipelineMetrics**: Berechnet Kennzahlen mit `ForEach-Object -Begin/-Process/-End`.
3. **Invoke-RetryOperation**: Wiederholungsmechanismus mit `do..until`.
4. **Find-FirstMatchingServer**: Durchsucht eine Liste und bricht vorzeitig mit `break` ab.
