<#
.SYNOPSIS
    PS 03: Where-Object, Select & Calculated Properties
.DESCRIPTION
    Filtern, Projizieren, Berechnen, Sortieren und Gruppieren von Datenströmen.
#>

# 🎯 TEILZIEL 1 (TODO 1): Filter-ActiveServices - Running Services filtern
# Nimm ein Array von Service-Objekten oder Hashtables $Services.
# Filtere alle Services heraus, deren Eigenschaft 'Status' gleich 'Running' ist.
# Nutze Where-Object { $_.Status -eq 'Running' } und gib die gefilterte Liste zurück.
# Falls $Services $null oder leer ist, gib @() zurück.
function Filter-ActiveServices {
    param(
        [array]$Services
    )
    # TODO: Filtere mit Where-Object
    return @()
}

# 🎯 TEILZIEL 2 (TODO 2): Select-ProcessSummary - Projektion & Calculated Property
# Nimm ein Array von Prozess-Objekten $Processes (jedes besitzt 'Id', 'Name', 'WorkingSet' in Bytes).
# Nutze Select-Object, um ein neues Objekt mit folgenden 3 Eigenschaften zu erstellen:
# 1. Id
# 2. Name
# 3. MemoryMB (Calculated Property: [Math]::Round($_.WorkingSet / 1MB, 2))
# Gib das projizierte Array von Objekten zurück.
function Select-ProcessSummary {
    param(
        [array]$Processes
    )
    # TODO: Projiziere mit Select-Object und @{ Name='MemoryMB'; Expression={...} }
    return @()
}

# 🎯 TEILZIEL 3 (TODO 3): Sort-EmployeeList - Mehrstufige Sortierung
# Nimm ein Array von Mitarbeiter-Objekten $Employees (mit Feldern 'FirstName', 'LastName', 'Salary').
# Sortiere die Liste mit Sort-Object:
# 1. Primär: 'Salary' ABSTEIGEND (Descending)
# 2. Sekundär: 'LastName' AUFSTEIGEND (Ascending)
# Gib das sortierte Array zurück.
function Sort-EmployeeList {
    param(
        [array]$Employees
    )
    # TODO: Sortiere mit Sort-Object und @{ Expression='Salary'; Descending=$true }, 'LastName'
    return @()
}

# 🎯 TEILZIEL 4 (TODO 4): Group-LogEntriesBySeverity - Gruppierung und Zählung
# Nimm ein Array von Log-Objekten $LogEntries (jedes besitzt 'Severity', z.B. 'INFO', 'WARN', 'ERROR').
# Gruppiere die Einträge nach 'Severity' mit Group-Object.
# Gib ein Hashtable zurück, bei dem der Schlüssel der Severity-Name ist und der Wert die Anzahl (Count) der Einträge.
# Beispiel: @{ "INFO" = 5; "WARN" = 2; "ERROR" = 1 }
function Group-LogEntriesBySeverity {
    param(
        [array]$LogEntries
    )
    # TODO: Gruppiere mit Group-Object und erzeuge das Ergebnis-Hashtable
    return @{}
}
