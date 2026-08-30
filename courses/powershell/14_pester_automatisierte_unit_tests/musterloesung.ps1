<#
.SYNOPSIS
    PS 14: Pester v5 Automatisiertes Testing & Mocking - Musterlösung
#>

function Get-ServerHealthStatus {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$ServerName,

        [Parameter()]
        [string]$ServiceName = 'AppService'
    )

    $svcStatus = try {
        (Get-Service -Name $ServiceName -ErrorAction Stop).Status
    } catch {
        'Stopped'
    }

    $pingOk = try {
        Test-Connection -TargetName $ServerName -Count 1 -Quiet -ErrorAction Stop
    } catch {
        $false
    }

    $isHealthy = ($svcStatus -eq 'Running' -and $pingOk -eq $true)

    return [PSCustomObject]@{
        ServerName = $ServerName
        IsHealthy  = $isHealthy
        Status     = if ($isHealthy) { 'Operational' } else { 'Degraded' }
        Code       = if ($isHealthy) { 200 } else { 500 }
    }
}

function Restart-FailedService {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$ServiceName,

        [Parameter()]
        [int]$MaxRetries = 3
    )

    $svc = try { Get-Service -Name $ServiceName -ErrorAction Stop } catch { throw $_ }
    if ($svc.Status -eq 'Running') {
        return [PSCustomObject]@{
            ServiceName = $ServiceName
            Success     = $true
            Attempts    = 0
        }
    }

    for ($i = 1; $i -le $MaxRetries; $i++) {
        Restart-Service -Name $ServiceName -ErrorAction SilentlyContinue
        $current = Get-Service -Name $ServiceName -ErrorAction SilentlyContinue
        if ($current.Status -eq 'Running') {
            return [PSCustomObject]@{
                ServiceName = $ServiceName
                Success     = $true
                Attempts    = $i
            }
        }
    }

    throw "Dienst $ServiceName konnte nicht gestartet werden."
}

function Test-PesterResultAnalyzer {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [PSCustomObject]$PesterResult
    )

    $total = [int]$PesterResult.TotalCount
    $passed = [int]$PesterResult.PassedCount
    $failed = [int]$PesterResult.FailedCount

    $passRate = if ($total -gt 0) { [Math]::Round(($passed / $total) * 100, 1) } else { 0.0 }
    $isOk = ($failed -eq 0 -and $total -gt 0)

    return [PSCustomObject]@{
        Total             = $total
        Passed            = $passed
        Failed            = $failed
        PassRate          = $passRate
        Status            = if ($isOk) { 'Passed' } else { 'Failed' }
        IsProductionReady = $isOk
    }
}

function Invoke-MockableApiAudit {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$EndpointUrl
    )

    try {
        $res = Invoke-RestMethod -Uri $EndpointUrl -Method GET -ErrorAction Stop
        $valid = ($null -ne $res -and ($null -ne $res.status -or $null -ne $res.Status))
        return [PSCustomObject]@{
            Url          = $EndpointUrl
            ResponseCode = 200
            PayloadValid = [bool]$valid
            AuditTime    = [DateTime]::UtcNow
        }
    } catch {
        return [PSCustomObject]@{
            Url          = $EndpointUrl
            ResponseCode = 500
            PayloadValid = $false
            AuditTime    = [DateTime]::UtcNow
        }
    }
}
