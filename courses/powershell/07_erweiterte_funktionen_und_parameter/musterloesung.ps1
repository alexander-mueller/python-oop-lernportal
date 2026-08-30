<#
.SYNOPSIS
    PS 07: Eigene Cmdlets [CmdletBinding()] & Validierung (Musterlösung)
#>

# 🎯 TEILZIEL 1 (TODO 1): Get-EnvironmentConfig - Cmdlet mit Parameter-Validierung
function Get-EnvironmentConfig {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [ValidateSet('Development', 'Staging', 'Production')]
        [string]$Environment,

        [Parameter(Mandatory = $false, Position = 1)]
        [ValidateRange(1, 65535)]
        [int]$Port = 8080
    )

    return [PSCustomObject]@{
        Environment  = $Environment
        Port         = $Port
        IsProduction = ($Environment -eq 'Production')
    }
}

# 🎯 TEILZIEL 2 (TODO 2): Restart-AppService - SupportsShouldProcess & WhatIf
function Restart-AppService {
    [CmdletBinding(SupportsShouldProcess = $true)]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [ValidateNotNullOrEmpty()]
        [string]$ServiceName
    )

    $executed = $false
    if ($PSCmdlet.ShouldProcess($ServiceName, "Restart Service")) {
        $executed = $true
    }

    return [PSCustomObject]@{
        ServiceName = $ServiceName
        Action      = "Restarted"
        Executed    = $executed
    }
}

# 🎯 TEILZIEL 3 (TODO 3): New-UserAccount - Pipeline-Input & Regex-Validierung
function New-UserAccount {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, ValueFromPipeline = $true, Position = 0)]
        [ValidatePattern('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')]
        [string]$Email,

        [Parameter(Mandatory = $false, Position = 1)]
        [ValidateSet('User', 'Admin', 'Auditor')]
        [string]$Role = 'User'
    )

    process {
        $username = ($Email -split '@')[0]
        return [PSCustomObject]@{
            Username = $username
            Email    = $Email
            Role     = $Role
        }
    }
}

# 🎯 TEILZIEL 4 (TODO 4): Get-SystemReport - Switch-Parameter & Non-Empty Check
function Get-SystemReport {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [ValidateNotNullOrEmpty()]
        [string]$Title,

        [Parameter(Mandatory = $false)]
        [switch]$Detailed
    )

    return [PSCustomObject]@{
        Title       = $Title
        IsDetailed  = [bool]$Detailed
        ReportDate  = [DateTime]::UtcNow
    }
}
