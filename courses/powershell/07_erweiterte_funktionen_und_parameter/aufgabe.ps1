<#
.SYNOPSIS
    PS 07: Eigene Cmdlets [CmdletBinding()] & Validierung
.DESCRIPTION
    Advanced Functions, Parameter-Attribute, Validierung und SupportsShouldProcess.
#>

# 🎯 TEILZIEL 1 (TODO 1): Get-EnvironmentConfig - Cmdlet mit Parameter-Validierung
# Erstelle eine Advanced Function mit [CmdletBinding()]:
# Parameter:
# - $Environment: [Parameter(Mandatory = $true)] [ValidateSet('Development', 'Staging', 'Production')] [string]
# - $Port: [Parameter(Mandatory = $false)] [ValidateRange(1, 65535)] [int] = 8080
# Rückgabe: Ein [PSCustomObject] mit { Environment = $Environment; Port = $Port; IsProduction = ($Environment -eq 'Production') }
function Get-EnvironmentConfig {
    [CmdletBinding()]
    param(
        # TODO: Parameter mit Mandatory, ValidateSet und ValidateRange definieren
        [string]$Environment,
        [int]$Port = 8080
    )
    # TODO: Rückgabe-Objekt erstellen
    return $null
}

# 🎯 TEILZIEL 2 (TODO 2): Restart-AppService - SupportsShouldProcess & WhatIf
# Erstelle eine Advanced Function mit [CmdletBinding(SupportsShouldProcess = $true)]:
# Parameter:
# - $ServiceName: [Parameter(Mandatory = $true)] [string]
# Logik:
# - Prüfe mit if ($PSCmdlet.ShouldProcess($ServiceName, "Restart Service")):
#   - Falls wahr: Setze $executed = $true
#   - Falls falsch (z.B. bei -WhatIf): Setze $executed = $false
# Rückgabe: [PSCustomObject]@{ ServiceName = $ServiceName; Action = "Restarted"; Executed = $executed }
function Restart-AppService {
    [CmdletBinding(SupportsShouldProcess = $true)]
    param(
        [Parameter(Mandatory = $true)]
        [string]$ServiceName
    )
    # TODO: Nutze $PSCmdlet.ShouldProcess
    $executed = $false
    return [PSCustomObject]@{
        ServiceName = $ServiceName
        Action      = "Restarted"
        Executed    = $executed
    }
}

# 🎯 TEILZIEL 3 (TODO 3): New-UserAccount - Pipeline-Input & Regex-Validierung
# Erstelle ein Cmdlet zur Benutzererstellung:
# Parameter:
# - $Email: [Parameter(Mandatory = $true, ValueFromPipeline = $true)]
#           [ValidatePattern('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')]
#           [string]
# - $Role: [Parameter(Mandatory = $false)] [ValidateSet('User', 'Admin', 'Auditor')] [string] = 'User'
# Logik:
# - Extrahiere den Benutzernamen (den Teil vor dem '@') aus der E-Mail.
# Rückgabe: [PSCustomObject]@{ Username = $username; Email = $Email; Role = $Role }
function New-UserAccount {
    [CmdletBinding()]
    param(
        # TODO: Parameter mit Pipeline-Support und Regex-Muster
        [string]$Email,
        [string]$Role = 'User'
    )
    # TODO: Benutzername ermitteln und Objekt zurückgeben
    return $null
}

# 🎯 TEILZIEL 4 (TODO 4): Get-SystemReport - Switch-Parameter & Non-Empty Check
# Erstelle ein Report-Cmdlet:
# Parameter:
# - $Title: [Parameter(Mandatory = $true)] [ValidateNotNullOrEmpty()] [string]
# - $Detailed: [Parameter(Mandatory = $false)] [switch]
# Rückgabe: [PSCustomObject]@{ Title = $Title; IsDetailed = [bool]$Detailed; ReportDate = [DateTime]::UtcNow }
function Get-SystemReport {
    [CmdletBinding()]
    param(
        # TODO: Switch-Parameter und ValidateNotNullOrEmpty
        [string]$Title,
        [switch]$Detailed
    )
    # TODO: Report-Objekt zurückgeben
    return $null
}
