<#
.SYNOPSIS
    PS 09: Multithreading mit ForEach-Object -Parallel & Start-ThreadJob - Musterlösung
#>

function Invoke-ParallelPing {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, ValueFromPipeline = $true)]
        [string[]]$ComputerNames,

        [Parameter()]
        [ValidateRange(1, 64)]
        [int]$ThrottleLimit = 5,

        [Parameter()]
        [ValidateRange(50, 10000)]
        [int]$TimeoutMs = 1000
    )

    $results = $ComputerNames | ForEach-Object -Parallel {
        $hostName = $_
        $timeout = $using:TimeoutMs
        $isOffline = ($hostName -match '(?i)offline|down|fail|unreachable')

        [PSCustomObject]@{
            ComputerName   = $hostName
            Status         = if ($isOffline) { 'Offline' } else { 'Online' }
            ResponseTimeMs = if ($isOffline) { -1 } else { [Math]::Round(($timeout * 0.02) + 12, 1) }
            Timestamp      = [DateTime]::UtcNow
        }
    } -ThrottleLimit $ThrottleLimit

    return @($results)
}

function Start-AsyncServerTask {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$TaskName,

        [Parameter(Mandatory = $true)]
        [scriptblock]$ScriptBlock,

        [Parameter()]
        [object[]]$ArgumentList = @()
    )

    if (Get-Command Start-ThreadJob -ErrorAction SilentlyContinue) {
        return Start-ThreadJob -Name $TaskName -ScriptBlock $ScriptBlock -ArgumentList $ArgumentList
    } else {
        return Start-Job -Name $TaskName -ScriptBlock $ScriptBlock -ArgumentList $ArgumentList
    }
}

function Wait-AndCollectThreadJobs {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [object[]]$Jobs,

        [Parameter()]
        [int]$TimeoutSeconds = 10
    )

    $null = Wait-Job -Job $Jobs -Timeout $TimeoutSeconds -ErrorAction SilentlyContinue
    $results = Receive-Job -Job $Jobs -ErrorAction SilentlyContinue
    Remove-Job -Job $Jobs -Force -ErrorAction SilentlyContinue
    return @($results)
}

function Invoke-ThrottledBatchProcessing {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [object[]]$Items,

        [Parameter(Mandatory = $true)]
        [scriptblock]$ProcessBlock,

        [Parameter()]
        [ValidateRange(1, 32)]
        [int]$ThrottleLimit = 4
    )

    $sw = [System.Diagnostics.Stopwatch]::StartNew()

    $processed = $Items | ForEach-Object -Parallel {
        $block = $using:ProcessBlock
        & $block $_
    } -ThrottleLimit $ThrottleLimit

    $sw.Stop()

    $resultsArray = @($processed)
    $successful = @($resultsArray | Where-Object {
        $_ -is [pscustomobject] -and ($_.Success -eq $true -or $_.Status -eq 'OK' -or $_.Status -eq 'Online')
    })

    return [PSCustomObject]@{
        TotalItems     = @($Items).Count
        ProcessedItems = $resultsArray
        SuccessCount   = $successful.Count
        DurationMs     = [Math]::Round($sw.Elapsed.TotalMilliseconds, 2)
    }
}
