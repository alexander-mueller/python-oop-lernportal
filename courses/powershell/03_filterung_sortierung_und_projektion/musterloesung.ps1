<#
.SYNOPSIS
    PS 03: Where-Object, Select & Calculated Properties (Musterlösung)
#>

# 🎯 TEILZIEL 1 (TODO 1): Filter-ActiveServices - Running Services filtern
function Filter-ActiveServices {
    param(
        [array]$Services
    )
    if ($null -eq $Services -or $Services.Count -eq 0) {
        return @()
    }
    return @($Services | Where-Object { $_.Status -eq 'Running' })
}

# 🎯 TEILZIEL 2 (TODO 2): Select-ProcessSummary - Projektion & Calculated Property
function Select-ProcessSummary {
    param(
        [array]$Processes
    )
    if ($null -eq $Processes -or $Processes.Count -eq 0) {
        return @()
    }
    return @($Processes | Select-Object -Property Id, Name, @{
        Name       = 'MemoryMB'
        Expression = { [Math]::Round($_.WorkingSet / 1MB, 2) }
    })
}

# 🎯 TEILZIEL 3 (TODO 3): Sort-EmployeeList - Mehrstufige Sortierung
function Sort-EmployeeList {
    param(
        [array]$Employees
    )
    if ($null -eq $Employees -or $Employees.Count -eq 0) {
        return @()
    }
    return @($Employees | Sort-Object -Property @{ Expression = 'Salary'; Descending = $true }, 'LastName')
}

# 🎯 TEILZIEL 4 (TODO 4): Group-LogEntriesBySeverity - Gruppierung und Zählung
function Group-LogEntriesBySeverity {
    param(
        [array]$LogEntries
    )
    $result = @{}
    if ($null -eq $LogEntries -or $LogEntries.Count -eq 0) {
        return $result
    }

    $grouped = $LogEntries | Group-Object -Property Severity
    foreach ($g in $grouped) {
        $result[$g.Name] = $g.Count
    }
    return $result
}
