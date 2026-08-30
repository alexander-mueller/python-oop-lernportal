<#
.SYNOPSIS
    PS 08: Robustes Error-Handling (Try/Catch/Finally)
.DESCRIPTION
    Fehlerbehandlung, ErrorAction Stop, try/catch/finally und benutzerdefinierte Exceptions.
#>

$Global:ResourceLocked = $false

# 🎯 TEILZIEL 1 (TODO 1): Read-SafeConfiguration - Sicheres Datei-Einlesen
# Versuche eine Datei über $Path mit Get-Content und -ErrorAction Stop einzulesen.
# - Wenn die Datei existiert und gelesen werden kann:
#   Gib ein Hashtable @{ Success = $true; Content = $content; ErrorMessage = "" } zurück.
# - Wenn ein Fehler auftritt (abgefangen im catch-Block):
#   Gib ein Hashtable @{ Success = $false; Content = ""; ErrorMessage = $_.Exception.Message } zurück.
function Read-SafeConfiguration {
    param(
        [string]$Path
    )
    # TODO: try / catch mit Get-Content -ErrorAction Stop
    return @{
        Success      = $false
        Content      = ""
        ErrorMessage = ""
    }
}

# 🎯 TEILZIEL 2 (TODO 2): Invoke-SafeDivision - Fehler werfen & abfangen
# Führe eine Division $Numerator durch $Denominator ([double]) durch:
# - Prüfe im try-Block: Falls $Denominator -eq 0, wirf mit 'throw "Division by zero is not allowed"' einen terminierenden Fehler.
# - Falls kein Fehler: Berechne $result = $Numerator / $Denominator.
# - Fange im catch-Block den Fehler ab.
# Gib ein [PSCustomObject] mit { Result = $result; HasError = $hasError; ErrorMessage = $errorMessage } zurück.
function Invoke-SafeDivision {
    param(
        [double]$Numerator,
        [double]$Denominator
    )
    # TODO: try / catch mit throw bei 0
    return [PSCustomObject]@{
        Result       = 0.0
        HasError     = $false
        ErrorMessage = ""
    }
}

# 🎯 TEILZIEL 3 (TODO 3): Invoke-TransactionalTask - Garantierter Cleanup im finally-Block
# Simuliere eine transaktionale Sperre:
# 1. Setze im try-Block: $Global:ResourceLocked = $true
# 2. Falls $ShouldFail $true ist: wirf mit 'throw "Transaction failed"' einen Fehler.
# 3. Falls kein Fehler: setze $completed = $true
# 4. Im finally-Block: Setze GARANTIERT $Global:ResourceLocked = $false zurück!
# Gib ein Hashtable @{ Completed = $completed; CleanupDone = (-not $Global:ResourceLocked) } zurück.
function Invoke-TransactionalTask {
    param(
        [bool]$ShouldFail
    )
    # TODO: try / catch / finally mit Cleanup
    return @{
        Completed   = $false
        CleanupDone = $false
    }
}

# 🎯 TEILZIEL 4 (TODO 4): Format-DetailedErrorRecord - Strukturierter Fehlerbericht
# Nimm eine Exception $ExceptionObj (oder erzeuge aus $Message ein [Exception]-Objekt).
# Erzeuge ein [PSCustomObject] mit:
# - ErrorMessage: Die Nachricht der Exception ([string])
# - ExceptionType: Der FullName des Exception-Typs (z.B. "System.Exception")
# - Timestamp: Aktueller UTC-Zeitstempel ([DateTime]::UtcNow)
# - Success: $false
function Format-DetailedErrorRecord {
    param(
        [System.Exception]$ExceptionObj
    )
    # TODO: Erzeuge und gib das strukturierte Fehler-Objekt zurück
    return $null
}
