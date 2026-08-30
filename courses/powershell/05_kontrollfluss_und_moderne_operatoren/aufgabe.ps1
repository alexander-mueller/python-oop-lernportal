<#
.SYNOPSIS
    PS 05: Kontrollfluss & Moderne PS7 Operatoren
.DESCRIPTION
    Verzweigungen, switch mit Regex und PowerShell 7+ Operatoren (Ternary, Null-Coalescing).
#>

# 🎯 TEILZIEL 1 (TODO 1): Get-AccessDecision - Rollen & Status bewerten
# Bewerte die Zugriffsrechte anhand von $Role (string) und $IsActive (bool):
# - Falls $IsActive $false ist -> gib IMMER "Denied" zurück.
# - Falls $IsActive $true ist:
#   - $Role -eq "Admin"  -> "FullAccess"
#   - $Role -eq "Editor" -> "WriteAccess"
#   - $Role -eq "Viewer" -> "ReadOnly"
#   - Alle anderen Rollen -> "Denied"
# Nutze if/else oder switch bzw. den ternären Operator.
function Get-AccessDecision {
    param(
        [string]$Role,
        [bool]$IsActive
    )
    # TODO: Ermittle die Zugriffsstufe
    return "Denied"
}

# 🎯 TEILZIEL 2 (TODO 2): Get-ConfigWithFallback - 3-Stufen Null-Coalescing Kaskade
# Nimm drei Parameter: $UserOverride, $EnvSetting, $DefaultSetting.
# Gib den ersten Wert zurück, der weder $null noch ein Leerstring "" ist:
# 1. $UserOverride (höchste Priorität)
# 2. $EnvSetting (mittlere Priorität)
# 3. $DefaultSetting (Fallback)
# Tipp: Nutze den Null-Coalescing Operator '??' bzw. Validierung auf nicht-leer.
function Get-ConfigWithFallback {
    param(
        [string]$UserOverride,
        [string]$EnvSetting,
        [string]$DefaultSetting
    )
    # TODO: Werte mit Fallback-Kaskade ermitteln
    return ""
}

# 🎯 TEILZIEL 3 (TODO 3): Classify-LogMessage - Log-Nachrichten klassifizieren
# Klassifiziere die übergebene $Message (string) mittels 'switch -Regex':
# - Beginnt mit "ERR-" gefolgt von Ziffern (z.B. "ERR-500: Server down") -> "CriticalError"
# - Beginnt mit "WARN-" gefolgt von Ziffern (z.B. "WARN-101: Memory low") -> "Warning"
# - Beginnt mit "OK-" (z.B. "OK-200: Healthy") -> "Success"
# - Für alle anderen Nachrichten -> "Unknown"
function Classify-LogMessage {
    param(
        [string]$Message
    )
    # TODO: Nutze switch -Regex ($Message)
    return "Unknown"
}

# 🎯 TEILZIEL 4 (TODO 4): Test-NetworkPort - Port-Bereich überprüfen
# Prüfe, ob $Port ([int]) im gültigen User/Registered-Portbereich liegt:
# - Mindestens 1024 ($Port -ge 1024)
# - Höchstens 49151 ($Port -le 49151)
# Gib $true zurück, wenn beide Bedingungen erfüllt sind, sonst $false.
function Test-NetworkPort {
    param(
        [int]$Port
    )
    # TODO: Prüfe den Portbereich mit -ge, -le und -and
    return $false
}
