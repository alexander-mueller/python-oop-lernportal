<#
.SYNOPSIS
    PS 04: Typisierung, Hashtables & PSCustomObject (Musterlösung)
#>

# 🎯 TEILZIEL 1 (TODO 1): New-ServerInventoryObject - PSCustomObject erstellen
function New-ServerInventoryObject {
    param(
        [string]$Hostname,
        [string]$IPAddress,
        [int]$CPUCount,
        [bool]$IsActive,
        [datetime]$CreatedAt
    )
    if ($CreatedAt -eq [DateTime]::MinValue -or $null -eq $CreatedAt) {
        $CreatedAt = [DateTime]::UtcNow
    }

    return [PSCustomObject]@{
        Hostname  = $Hostname
        IPAddress = $IPAddress
        CPUCount  = $CPUCount
        IsActive  = $IsActive
        CreatedAt = $CreatedAt
    }
}

# 🎯 TEILZIEL 2 (TODO 2): Convert-HashtableToCustomObject - Hashtable konvertieren
function Convert-HashtableToCustomObject {
    param(
        [hashtable]$HashTable
    )
    if ($null -eq $HashTable -or $HashTable.Count -eq 0) {
        return [PSCustomObject]@{}
    }
    return [PSCustomObject]$HashTable
}

# 🎯 TEILZIEL 3 (TODO 3): Get-ArrayStatistics - Array-Metriken berechnen
function Get-ArrayStatistics {
    param(
        [double[]]$Numbers
    )
    if ($null -eq $Numbers -or $Numbers.Length -eq 0) {
        return [PSCustomObject]@{
            Sum     = 0.0
            Average = 0.0
            Min     = 0.0
            Max     = 0.0
        }
    }

    $sum = 0.0
    $min = $Numbers[0]
    $max = $Numbers[0]

    foreach ($n in $Numbers) {
        $sum += $n
        if ($n -lt $min) { $min = $n }
        if ($n -gt $max) { $max = $n }
    }

    $avg = $sum / $Numbers.Length
    $roundedAvg = [Math]::Round($avg, 2)

    return [PSCustomObject]@{
        Sum     = $sum
        Average = $roundedAvg
        Min     = $min
        Max     = $max
    }
}

# 🎯 TEILZIEL 4 (TODO 4): Merge-Hashtables - Hashtables verschmelzen
function Merge-Hashtables {
    param(
        [hashtable]$Primary,
        [hashtable]$Secondary
    )
    $result = @{}

    if ($null -ne $Primary) {
        foreach ($key in $Primary.Keys) {
            $result[$key] = $Primary[$key]
        }
    }

    if ($null -ne $Secondary) {
        foreach ($key in $Secondary.Keys) {
            $result[$key] = $Secondary[$key]
        }
    }

    return $result
}
