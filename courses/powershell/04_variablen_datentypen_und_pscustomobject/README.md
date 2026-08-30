# PS 04: Typisierung, Hashtables & PSCustomObject 🔷

Willkommen zu **Modul 04** des PowerShell 7+ Core Kurses!

In diesem Modul lernst du, wie du strukturierte Datenmodelle in PowerShell definierst. Mit `[PSCustomObject]` erstellst du maßgeschneiderte Datenobjekte, die sich nahtlos in die Pipeline einfügen, als JSON exportiert oder in Tabellen dargestellt werden können.

---

## 💡 1. Das Wichtigste auf einen Blick

### Strikte Typisierung
```powershell
[int]$port = 443
[bool]$aktiv = $true
[datetime]$datum = [DateTime]::UtcNow
```

### Arrays & Hashtables
```powershell
# Array:
$server = @("srv01", "srv02")

# Hashtable:
$settings = @{
    Port    = 8080
    Verbose = $true
}
```

### `[PSCustomObject]`
```powershell
$obj = [PSCustomObject]@{
    Hostname  = "web01"
    IP        = "10.0.0.5"
    IsRunning = $true
}
```

---

## 🎯 Aufgabenübersicht in `aufgabe.ps1`

1. **New-ServerInventoryObject**: Erstellt ein standardisiertes `[PSCustomObject]` für Server-Inventare.
2. **Convert-HashtableToCustomObject**: Konvertiert eine Hashtable in ein `[PSCustomObject]`.
3. **Get-ArrayStatistics**: Berechnet Summe, Durchschnitt, Min und Max eines Zahlen-Arrays.
4. **Merge-Hashtables**: Führt zwei Hashtables mit Konfliktlösung zusammen.
