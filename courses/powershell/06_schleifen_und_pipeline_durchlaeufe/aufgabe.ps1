<#
.SYNOPSIS
    PS 06: Schleifen (foreach, while & Pipeline)
.DESCRIPTION
    Schleifen-Statements, Pipeline-Streaming mit ForEach-Object, Retry-Muster und Steuerung.
#>

# 🎯 TEILZIEL 1 (TODO 1): Get-FilteredEvenSquares - Quadrate gerader Zahlen
# Nimm ein Array von ganzen Zahlen $Numbers ([int[]]).
# Durchlaufe das Array mit einer 'foreach'-Schleife:
# - Überspringe ungerade Zahlen ($n % 2 -ne 0) mit dem 'continue'-Befehl.
# - Quadriere jede gerade Zahl ($n * $n) und sammle das Ergebnis.
# Gib das Array der quadrierten geraden Zahlen zurück.
# Falls $Numbers leer oder $null ist, gib @() zurück.
function Get-FilteredEvenSquares {
    param(
        [int[]]$Numbers
    )
    # TODO: foreach-Schleife mit continue für ungerade Zahlen
    return @()
}

# 🎯 TEILZIEL 2 (TODO 2): Invoke-StreamingPipelineMetrics - Pipeline-Lifecycle Blöcke
# Nimm ein Array von Zahlen $DataStream ([double[]]).
# Verarbeite die Zahlen mittels Pipeline und ForEach-Object mit -Begin, -Process und -End:
# - Begin: Initialisiere $count = 0 und $sum = 0.0
# - Process: Erhöhe $count um 1 und addiere $_ zu $sum
# - End: Berechne den Durchschnitt ($sum / $count) gerundet auf 2 Dezimalstellen
# Gib ein [PSCustomObject] mit { Count = $count; TotalSum = $sum; Average = $avg } zurück.
# Falls $DataStream leer ist, gib Count=0, TotalSum=0, Average=0 zurück.
function Invoke-StreamingPipelineMetrics {
    param(
        [double[]]$DataStream
    )
    # TODO: Pipeline-Verarbeitung mit ForEach-Object
    return [PSCustomObject]@{
        Count    = 0
        TotalSum = 0.0
        Average  = 0.0
    }
}

# 🎯 TEILZIEL 3 (TODO 3): Invoke-RetryOperation - Wiederholungsschleife
# Simuliere einen Retry-Vorgang mit einer 'do { ... } until (...)'-Schleife:
# Parameter:
# - $MaxAttempts: Maximale Anzahl von Versuchen ([int], z.B. 3)
# - $SuccessOnAttempt: Bei welchem Versuch die Operation erfolgreich ist ([int], z.B. 2)
# Die Schleife soll in jedem Durchlauf $attempts um 1 erhöhen.
# Wenn $attempts gleich $SuccessOnAttempt ist, setze $isSuccess = $true.
# Die Schleife endet, wenn $isSuccess $true ist ODER $attempts >= $MaxAttempts erreicht ist.
# Gib ein Hashtable @{ Attempts = $attempts; IsSuccess = $isSuccess } zurück.
function Invoke-RetryOperation {
    param(
        [int]$MaxAttempts,
        [int]$SuccessOnAttempt
    )
    # TODO: do..until Schleife implementieren
    return @{
        Attempts  = 0
        IsSuccess = $false
    }
}

# 🎯 TEILZIEL 4 (TODO 4): Find-FirstMatchingServer - Vorzeitiger Abbruch mit break
# Nimm ein Array von Server-Namen $Servers ([string[]]) und einen Präfix-String $Prefix.
# Durchlaufe die Serverliste mit 'foreach':
# - Sobald ein Servername mit $Prefix beginnt (z.B. $server.StartsWith($Prefix) oder $server -like "$Prefix*"),
#   speichere diesen Server und beende die Schleife SOFORT mit 'break'.
# Gib den gefundenen Servernamen zurück (oder $null, falls kein Server passte oder die Liste leer ist).
function Find-FirstMatchingServer {
    param(
        [string[]]$Servers,
        [string]$Prefix
    )
    # TODO: foreach mit break beim ersten Treffer
    return $null
}
