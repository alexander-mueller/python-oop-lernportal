<#
.SYNOPSIS
    PS 15: Cross-Platform Cloud Automation (Azure Az & AWS CLI) - Musterlösung
#>

function Get-PlatformDiagnostics {
    [CmdletBinding()]
    param()

    $platform = if ($IsLinux) {
        'Linux'
    } elseif ($IsMacOS) {
        'macOS'
    } elseif ($IsWindows) {
        'Windows'
    } else {
        'Linux'
    }

    return [PSCustomObject]@{
        Platform      = $platform
        OS            = try { [string]$PSVersionTable.OS } catch { $platform }
        PathSeparator = [System.IO.Path]::DirectorySeparatorChar.ToString()
        PSVersion     = $PSVersionTable.PSVersion.ToString()
        IsCoreCLR     = ($PSVersionTable.PSEdition -eq 'Core')
    }
}

function New-IdempotentResourceConfig {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$ResourceName,

        [Parameter(Mandatory = $true)]
        [string]$ResourceType,

        [Parameter()]
        [string]$Location = 'westeurope',

        [Parameter()]
        [hashtable]$CustomTags = @{}
    )

    $tags = @{
        'Environment' = 'Production'
        'ManagedBy'   = 'PowerShellAutomation'
        'CreatedDate' = (Get-Date -Format 'yyyy-MM-dd')
    }

    foreach ($key in $CustomTags.Keys) {
        $tags[$key] = $CustomTags[$key]
    }

    return [PSCustomObject]@{
        Name       = $ResourceName
        Type       = $ResourceType
        Location   = $Location
        Tags       = $tags
        ResourceId = "/subscriptions/simulated-sub/resourceGroups/rg-prod/providers/$ResourceType/$ResourceName"
    }
}

function Convert-AwsCliOutputToPsObject {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$AwsJsonOutput
    )

    $parsed = $AwsJsonOutput | ConvertFrom-Json
    $results = [System.Collections.Generic.List[object]]::new()

    if ($parsed.Reservations) {
        foreach ($res in $parsed.Reservations) {
            foreach ($inst in $res.Instances) {
                $stateVal = if ($inst.State) { $inst.State.Name } else { 'unknown' }
                $results.Add([PSCustomObject]@{
                    Id    = $inst.InstanceId
                    Type  = $inst.InstanceType
                    State = $stateVal
                    Tags  = $inst.Tags
                })
            }
        }
    } elseif ($parsed.Buckets) {
        foreach ($b in $parsed.Buckets) {
            $results.Add([PSCustomObject]@{
                Name         = $b.Name
                CreationDate = $b.CreationDate
            })
        }
    }

    return @($results)
}

function Audit-CloudResourceCompliance {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [object[]]$Resources,

        [Parameter()]
        [string[]]$MandatoryTags = @('Environment', 'ManagedBy'),

        [Parameter()]
        [string[]]$AllowedLocations = @('westeurope', 'germanywestcentral', 'eu-central-1')
    )

    $violations = [System.Collections.Generic.List[object]]::new()
    $compliantCount = 0

    foreach ($res in $Resources) {
        $hasViolations = $false

        # 1. Mandatory Tags Check
        foreach ($tag in $MandatoryTags) {
            $hasTag = $false
            if ($res.Tags -is [hashtable] -and $res.Tags.ContainsKey($tag)) {
                $hasTag = $true
            } elseif ($res.Tags -and ($res.Tags | Get-Member -Name $tag)) {
                $hasTag = $true
            }

            if (-not $hasTag) {
                $violations.Add([PSCustomObject]@{
                    ResourceName = $res.Name
                    Rule         = "MissingTag:$tag"
                    Severity     = "High"
                })
                $hasViolations = $true
            }
        }

        # 2. Location Check
        $locStr = [string]$res.Location
        if ($AllowedLocations -and ($AllowedLocations -notcontains $locStr.ToLower())) {
            $violations.Add([PSCustomObject]@{
                ResourceName = $res.Name
                Rule         = "InvalidLocation:$($res.Location)"
                Severity     = "Critical"
            })
            $hasViolations = $true
        }

        if (-not $hasViolations) {
            $compliantCount++
        }
    }

    $total = @($Resources).Count
    return [PSCustomObject]@{
        TotalAudited      = $total
        CompliantCount    = $compliantCount
        NonCompliantCount = $total - $compliantCount
        Violations        = @($violations)
    }
}
