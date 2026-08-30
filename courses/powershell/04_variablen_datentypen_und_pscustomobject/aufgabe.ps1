<#
.SYNOPSIS
    PS 04: Typisierung, Hashtables & PSCustomObject
.DESCRIPTION
    Arbeiten mit Datentypen, Arrays, Hashtables und Erstellung von [PSCustomObject].
#>

# 🎯 TEILZIEL 1 (TODO 1): New-ServerInventoryObject - PSCustomObject erstellen
# Erstelle ein [PSCustomObject] mit folgenden 5 Eigenschaften:
# - Hostname: [string]$Hostname
# - IPAddress: [string]$IPAddress
# - CPUCount: [int]$CPUCount
# - IsActive: [bool]$IsActive
# - CreatedAt: [datetime]$CreatedAt (falls $null oder nicht übergeben, nutze das aktuelle Datum [DateTime]::UtcNow)
# Gib das erstellte Objekt zurück.
function New-ServerInventoryObject {
    param(
        [string]$Hostname,
        [string]$IPAddress,
        [int]$CPUCount,
        [bool]$IsActive,
        [datetime]$CreatedAt
    )
    # TODO: Erzeuge und gib das [PSCustomObject] zurück
    return $null
}

# 🎯 TEILZIEL 2 (TODO 2): Convert-HashtableToCustomObject - Hashtable konvertieren
# Nimm ein beliebiges Hashtable $HashTable und konvertiere es in ein [PSCustomObject].
# Falls $HashTable $null oder leer ist, gib ein leeres [PSCustomObject]@{} zurück.
function Convert-HashtableToCustomObject {
    param(
        [hashtable]$HashTable
    )
    # TODO: Wandle das Hashtable in ein [PSCustomObject] um
    return $null
}

# 🎯 TEILZIEL 3 (TODO 3): Get-ArrayStatistics - Array-Metriken berechnen
# Nimm ein Array von Zahlen $Numbers ([double[]]).
# Berechne:
# - Sum: Die Summe aller Zahlen
# - Average: Der arithmetische Mittelwert (gerundet auf 2 Dezimalstellen mit [Math]::Round)
# - Min: Der kleinste Wert
# - Max: Der größte Wert
# Gib ein [PSCustomObject] mit den Eigenschaften Sum, Average, Min, Max zurück.
# Falls das Array leer oder $null ist, gib Sum=0, Average=0, Min=0, Max=0 zurück.
function Get-ArrayStatistics {
    param(
        [double[]]$Numbers
    )
    # TODO: Berechne die Statistiken und gib das Objekt zurück
    return [PSCustomObject]@{
        Sum     = 0.0
        Average = 0.0
        Min     = 0.0
        Max     = 0.0
    }
}

# 🎯 TEILZIEL 4 (TODO 4): Merge-Hashtables - Hashtables verschmelzen
# Führe zwei Hashtables ($Primary und $Secondary) zu einem neuen Hashtable zusammen.
# Alle Schlüssel/Werte aus $Primary sollen enthalten sein.
# Alle Schlüssel/Werte aus $Secondary sollen ebenfalls enthalten sein.
# Bei identischen Schlüsseln hat der Wert aus $Secondary Vorrang (überschreibt $Primary).
# Gib das neue resultierende Hashtable zurück.
function Merge-Hashtables {
    param(
        [hashtable]$Primary,
        [hashtable]$Secondary
    )
    # TODO: Führe die beiden Hashtables zusammen
    return @{}
}
