<#
.SYNOPSIS
    PS 06: Schleifen (foreach, while & Pipeline) (Musterlösung)
#>

# 🎯 TEILZIEL 1 (TODO 1): Get-FilteredEvenSquares - Quadrate gerader Zahlen
function Get-FilteredEvenSquares {
    param(
        [int[]]$Numbers
    )
    if ($null -eq $Numbers -or $Numbers.Length -eq 0) {
        return @()
    }

    $results = [System.Collections.Generic.List[int]]::new()
    foreach ($n in $Numbers) {
        if ($n % 2 -ne 0) {
            continue
        }
        $results.Add($n * $n)
    }
    return @($results)
}

# 🎯 TEILZIEL 2 (TODO 2): Invoke-StreamingPipelineMetrics - Pipeline-Lifecycle Blöcke
function Invoke-StreamingPipelineMetrics {
    param(
        [double[]]$DataStream
    )
    if ($null -eq $DataStream -or $DataStream.Length -eq 0) {
        return [PSCustomObject]@{
            Count    = 0
            TotalSum = 0.0
            Average  = 0.0
        }
    }

    $result = $DataStream | ForEach-Object -Begin {
        $count = 0
        $sum = 0.0
    } -Process {
        $count++
        $sum += $_
    } -End {
        $avg = if ($count -gt 0) { [Math]::Round($sum / $count, 2) } else { 0.0 }
        [PSCustomObject]@{
            Count    = $count
            TotalSum = $sum
            Average  = $avg
        }
    }

    return $result
}

# 🎯 TEILZIEL 3 (TODO 3): Invoke-RetryOperation - Wiederholungsschleife
function Invoke-RetryOperation {
    param(
        [int]$MaxAttempts,
        [int]$SuccessOnAttempt
    )
    $attempts = 0
    $isSuccess = $false

    do {
        $attempts++
        if ($attempts -eq $SuccessOnAttempt) {
            $isSuccess = $true
        }
    } until ($isSuccess -or $attempts -ge $MaxAttempts)

    return @{
        Attempts  = $attempts
        IsSuccess = $isSuccess
    }
}

# 🎯 TEILZIEL 4 (TODO 4): Find-FirstMatchingServer - Vorzeitiger Abbruch mit break
function Find-FirstMatchingServer {
    param(
        [string[]]$Servers,
        [string]$Prefix
    )
    if ($null -eq $Servers -or $Servers.Length -eq 0) {
        return $null
    }

    $found = $null
    foreach ($srv in $Servers) {
        if ($srv.StartsWith($Prefix, [System.StringComparison]::OrdinalIgnoreCase)) {
            $found = $srv
            break
        }
    }
    return $found
}
