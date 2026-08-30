<#
.SYNOPSIS
    PS 05: Kontrollfluss & Moderne PS7 Operatoren (Musterlösung)
#>

# 🎯 TEILZIEL 1 (TODO 1): Get-AccessDecision - Rollen & Status bewerten
function Get-AccessDecision {
    param(
        [string]$Role,
        [bool]$IsActive
    )
    if (-not $IsActive) {
        return "Denied"
    }

    switch ($Role) {
        "Admin"  { return "FullAccess" }
        "Editor" { return "WriteAccess" }
        "Viewer" { return "ReadOnly" }
        default  { return "Denied" }
    }
}

# 🎯 TEILZIEL 2 (TODO 2): Get-ConfigWithFallback - 3-Stufen Null-Coalescing Kaskade
function Get-ConfigWithFallback {
    param(
        [string]$UserOverride,
        [string]$EnvSetting,
        [string]$DefaultSetting
    )
    if (-not [string]::IsNullOrEmpty($UserOverride)) {
        return $UserOverride
    }
    if (-not [string]::IsNullOrEmpty($EnvSetting)) {
        return $EnvSetting
    }
    return $DefaultSetting
}

# 🎯 TEILZIEL 3 (TODO 3): Classify-LogMessage - Log-Nachrichten klassifizieren
function Classify-LogMessage {
    param(
        [string]$Message
    )
    if ([string]::IsNullOrWhiteSpace($Message)) {
        return "Unknown"
    }

    switch -Regex ($Message) {
        '^ERR-\d+'  { return "CriticalError" }
        '^WARN-\d+' { return "Warning" }
        '^OK-'      { return "Success" }
        default     { return "Unknown" }
    }
}

# 🎯 TEILZIEL 4 (TODO 4): Test-NetworkPort - Port-Bereich überprüfen
function Test-NetworkPort {
    param(
        [int]$Port
    )
    return ($Port -ge 1024 -and $Port -le 49151)
}
