<#
.SYNOPSIS
    PS 12: Sicherheit, Execution Policies & Secrets Management - Musterlösung
#>

function New-SecureCredentials {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$UserName,

        [Parameter(Mandatory = $true)]
        [string]$PlainTextPassword
    )

    $secPass = ConvertTo-SecureString -String $PlainTextPassword -AsPlainText -Force
    return [PSCredential]::new($UserName, $secPass)
}

function Protect-SensitiveString {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$PlainText
    )

    $sec = ConvertTo-SecureString -String $PlainText -AsPlainText -Force
    return ConvertFrom-SecureString -SecureString $sec
}

function Unprotect-SensitiveString {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$EncryptedString
    )

    $sec = ConvertTo-SecureString -String $EncryptedString
    $cred = [System.Net.NetworkCredential]::new('', $sec)
    return $cred.Password
}

function Get-SecurityAuditReport {
    [CmdletBinding()]
    param()

    $langMode = [string]$ExecutionContext.SessionState.LanguageMode
    $policy = try { (Get-ExecutionPolicy).ToString() } catch { "RemoteSigned" }

    $isElevated = if ($IsWindows) {
        $currentPrincipal = [Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()
        $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
    } else {
        try { ((whoami) -eq 'root') } catch { $false }
    }

    $score = 100
    $recommendations = [System.Collections.Generic.List[string]]::new()

    if ($policy -in @('Unrestricted', 'Bypass')) {
        $score -= 30
        $recommendations.Add("Set-ExecutionPolicy auf 'RemoteSigned' oder 'AllSigned' beschränken.")
    }
    if ($langMode -eq 'FullLanguage' -and $isElevated) {
        $recommendations.Add("Prinzip der geringsten Rechte (Least Privilege) beachten: Nicht dauerhaft mit Root/Admin-Rechten arbeiten.")
    }

    return [PSCustomObject]@{
        LanguageMode    = $langMode
        ExecutionPolicy = $policy
        IsElevated      = [bool]$isElevated
        SecurityScore   = [Math]::Max(0, $score)
        Recommendations = @($recommendations)
    }
}

function Invoke-SecretVaultSimulation {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [ValidateSet('Set', 'Get', 'Remove', 'List')]
        [string]$Action,

        [Parameter()]
        [string]$SecretName,

        [Parameter()]
        [string]$SecretValue,

        [Parameter(Mandatory = $true)]
        [hashtable]$VaultStorage
    )

    switch ($Action) {
        'Set' {
            if (-not $SecretName) { throw "SecretName ist erforderlich für Set." }
            $VaultStorage[$SecretName] = Protect-SensitiveString -PlainText $SecretValue
            return $true
        }
        'Get' {
            if (-not $SecretName -or -not $VaultStorage.ContainsKey($SecretName)) {
                return $null
            }
            $enc = $VaultStorage[$SecretName]
            return Unprotect-SensitiveString -EncryptedString $enc
        }
        'Remove' {
            if ($VaultStorage.ContainsKey($SecretName)) {
                $VaultStorage.Remove($SecretName)
                return $true
            }
            return $false
        }
        'List' {
            return @($VaultStorage.Keys | Sort-Object)
        }
    }
}
