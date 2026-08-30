# PS 03: Where-Object, Select & Calculated Properties 🔷

Willkommen zu **Modul 03** des PowerShell 7+ Core Kurses!

In diesem Modul erlernst du die drei Arbeitspferde der PowerShell-Datenverarbeitung:
1. **Filterung** mit `Where-Object` (Alias `?`)
2. **Projektion & Transformation** mit `Select-Object` und **Calculated Properties**
3. **Sortierung & Aggregation** mit `Sort-Object` und `Group-Object`

---

## 💡 1. Das Wichtigste auf einen Blick

### `Where-Object`
Filtert Elemente im Datenstrom:
```powershell
$services | Where-Object { $_.Status -eq 'Running' }
```

### Calculated Properties in `Select-Object`
Erstellt berechnete Eigenschaften on-the-fly:
```powershell
$processes | Select-Object -Property Id, Name, @{
    Name       = 'MemoryMB'
    Expression = { [Math]::Round($_.WorkingSet / 1MB, 2) }
}
```

### Mehrstufiges Sortieren & Gruppieren
```powershell
# Absteigend nach Gehalt, Aufsteigend nach Nachname:
$users | Sort-Object -Property @{ Expression = "Salary"; Descending = $true }, "LastName"

# Gruppieren nach Schweregrad:
$logs | Group-Object -Property Severity
```

---

## 🎯 Aufgabenübersicht in `aufgabe.ps1`

1. **Filter-ActiveServices**: Filtert Service-Objekte mit Status `'Running'`.
2. **Select-ProcessSummary**: Projiziert `Id`, `Name` und `MemoryMB` (berechnet aus `WorkingSet`).
3. **Sort-EmployeeList**: Führt mehrstufige Sortierung (Gehalt absteigend, Name aufsteigend) durch.
4. **Group-LogEntriesBySeverity**: Erstellt eine Häufigkeitstabelle der Schweregrade.
