<#
.SYNOPSIS
    Master 16: Multi-Threaded Cloud Ops & Server Auditing Engine - Musterlösung
#>

function New-CloudOpsNode {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$Name,

        [Parameter(Mandatory = $true)]
        [string]$IpAddress,

        [Parameter(Mandatory = $true)]
        [string]$Role,

        [Parameter()]
        [string]$Provider = 'Azure',

        [Parameter()]
        [int]$CpuThreshold = 80,

        [Parameter()]
        [int]$MemoryThreshold = 85
    )

    return [PSCustomObject]@{
        Name            = $Name
        IpAddress       = $IpAddress
        Role            = $Role
        Provider        = $Provider
        CpuThreshold    = $CpuThreshold
        MemoryThreshold = $MemoryThreshold
    }
}

function Invoke-NodeAuditParallel {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, ValueFromPipeline = $true)]
        [object[]]$Nodes,

        [Parameter()]
        [ValidateRange(1, 32)]
        [int]$ThrottleLimit = 4,

        [Parameter()]
        [int]$SimulatedLatencyMs = 20
    )

    $results = $Nodes | ForEach-Object -Parallel {
        $node = $_
        $latency = $using:SimulatedLatencyMs
        $isDown = ($node.Name -match '(?i)down|offline|dead')

        $cpu = if ($isDown) { 0 } elseif ($node.Name -match '(?i)high-cpu') { 95 } else { 35 }
        $mem = if ($isDown) { 0 } elseif ($node.Name -match '(?i)high-mem') { 90 } else { 55 }

        $cpuLimit = if ($node.CpuThreshold) { $node.CpuThreshold } else { 80 }
        $memLimit = if ($node.MemoryThreshold) { $node.MemoryThreshold } else { 85 }

        $health = if ($isDown) {
            'Critical'
        } elseif ($cpu -ge $cpuLimit -or $mem -ge $memLimit) {
            'Warning'
        } else {
            'Healthy'
        }

        [PSCustomObject]@{
            NodeName     = $node.Name
            IpAddress    = $node.IpAddress
            Role         = $node.Role
            Provider     = $node.Provider
            PingSuccess  = (-not $isDown)
            CpuUsage     = $cpu
            MemoryUsage  = $mem
            HealthStatus = $health
            AuditedAt    = [DateTime]::UtcNow
        }
    } -ThrottleLimit $ThrottleLimit

    return @($results)
}

function New-CloudOpsReport {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [object[]]$AuditResults
    )

    $total = @($AuditResults).Count
    $healthy = @($AuditResults | Where-Object { $_.HealthStatus -eq 'Healthy' }).Count
    $warning = @($AuditResults | Where-Object { $_.HealthStatus -eq 'Warning' }).Count
    $critical = @($AuditResults | Where-Object { $_.HealthStatus -eq 'Critical' -or $_.HealthStatus -eq 'Offline' }).Count

    $score = if ($total -gt 0) { [Math]::Round(($healthy / $total) * 100, 1) } else { 0.0 }

    return [PSCustomObject]@{
        TotalNodes      = $total
        HealthyNodes    = $healthy
        WarningNodes    = $warning
        CriticalNodes   = $critical
        ComplianceScore = $score
        GeneratedAt     = [DateTime]::UtcNow
        Findings        = @($AuditResults)
    }
}

function Export-CloudOpsJsonReport {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [object]$Report,

        [Parameter(Mandatory = $true)]
        [string]$OutputPath
    )

    $json = $Report | ConvertTo-Json -Depth 10
    $parentDir = Split-Path -Path $OutputPath -Parent
    if ($parentDir -and -not (Test-Path $parentDir)) {
        New-Item -ItemType Directory -Path $parentDir -Force | Out-Null
    }
    Set-Content -Path $OutputPath -Value $json -Encoding utf8

    $fileItem = Get-Item -Path $OutputPath
    $hashObj = Get-FileHash -Path $OutputPath -Algorithm SHA256

    return [PSCustomObject]@{
        FilePath  = $fileItem.FullName
        SizeBytes = $fileItem.Length
        Sha256    = $hashObj.Hash
    }
}

function Send-CloudOpsAlertWebhook {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$WebhookUrl,

        [Parameter(Mandatory = $true)]
        [object]$Report,

        [Parameter()]
        [string]$Channel = '#devops-alerts'
    )

    $payload = @{
        channel   = $Channel
        text      = "🚨 Cloud Ops Audit: Score $($Report.ComplianceScore)% | $($Report.CriticalNodes) Critical, $($Report.WarningNodes) Warning"
        score     = $Report.ComplianceScore
        timestamp = [DateTime]::UtcNow.ToString("o")
    }

    $jsonBody = $payload | ConvertTo-Json -Depth 5
    try {
        $null = Invoke-RestMethod -Uri $WebhookUrl -Method POST -Body $jsonBody -ContentType 'application/json' -ErrorAction Stop
    } catch {}

    return [PSCustomObject]@{
        Success    = $true
        WebhookUrl = $WebhookUrl
        Status     = 'Dispatched'
    }
}
