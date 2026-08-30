<#
.SYNOPSIS
    PS 08: Robustes Error-Handling (Try/Catch/Finally) (Musterlösung)
#>

$Global:ResourceLocked = $false

# 🎯 TEILZIEL 1 (TODO 1): Read-SafeConfiguration - Sicheres Datei-Einlesen
function Read-SafeConfiguration {
    param(
        [string]$Path
    )
    try {
        $content = Get-Content -Path $Path -Raw -ErrorAction Stop
        return @{
            Success      = $true
            Content      = $content
            ErrorMessage = ""
        }
    }
    catch {
        return @{
            Success      = $false
            Content      = ""
            ErrorMessage = $_.Exception.Message
        }
    }
}

# 🎯 TEILZIEL 2 (TODO 2): Invoke-SafeDivision - Fehler werfen & abfangen
function Invoke-SafeDivision {
    param(
        [double]$Numerator,
        [double]$Denominator
    )
    $result = 0.0
    $hasError = $false
    $errorMessage = ""

    try {
        if ($Denominator -eq 0) {
            throw "Division by zero is not allowed"
        }
        $result = $Numerator / $Denominator
    }
    catch {
        $hasError = $true
        $errorMessage = $_.Exception.Message
    }

    return [PSCustomObject]@{
        Result       = $result
        HasError     = $hasError
        ErrorMessage = $errorMessage
    }
}

# 🎯 TEILZIEL 3 (TODO 3): Invoke-TransactionalTask - Garantierter Cleanup im finally-Block
function Invoke-TransactionalTask {
    param(
        [bool]$ShouldFail
    )
    $completed = $false

    try {
        $Global:ResourceLocked = $true
        if ($ShouldFail) {
            throw "Transaction failed"
        }
        $completed = $true
    }
    catch {
        $completed = $false
    }
    finally {
        $Global:ResourceLocked = $false
    }

    return @{
        Completed   = $completed
        CleanupDone = (-not $Global:ResourceLocked)
    }
}

# 🎯 TEILZIEL 4 (TODO 4): Format-DetailedErrorRecord - Strukturierter Fehlerbericht
function Format-DetailedErrorRecord {
    param(
        [System.Exception]$ExceptionObj
    )
    if ($null -eq $ExceptionObj) {
        $ExceptionObj = [System.Exception]::new("Unknown error")
    }

    return [PSCustomObject]@{
        ErrorMessage  = $ExceptionObj.Message
        ExceptionType = $ExceptionObj.GetType().FullName
        Timestamp     = [DateTime]::UtcNow
        Success       = $false
    }
}
