<#
.SYNOPSIS
    PS 01: Cmdlet-Architektur & Verb-Noun Syntax (Musterlösung)
#>

$Global:ApprovedVerbsList = @(
    'Get', 'Set', 'New', 'Remove', 'Start', 'Stop', 'Restart',
    'Test', 'Find', 'Invoke', 'Select', 'Group', 'Export', 'Import'
)

# 🎯 TEILZIEL 1 (TODO 1): Get-FormattedCommandInfo - Cmdlet-Name zerlegen
function Get-FormattedCommandInfo {
    param(
        [string]$CommandName
    )
    if ([string]::IsNullOrWhiteSpace($CommandName) -or -not ($CommandName -match '-')) {
        return @{
            Verb        = ""
            Noun        = ""
            IsValidVerb = $false
        }
    }

    $parts = $CommandName -split '-', 2
    $verb = $parts[0].Trim()
    $noun = $parts[1].Trim()
    $isValid = $Global:ApprovedVerbsList -contains $verb

    return @{
        Verb        = $verb
        Noun        = $noun
        IsValidVerb = $isValid
    }
}

# 🎯 TEILZIEL 2 (TODO 2): Format-CmdletName - Verb und Noun zusammensetzen
function Format-CmdletName {
    param(
        [string]$Verb,
        [string]$Noun
    )
    if ([string]::IsNullOrWhiteSpace($Verb) -or [string]::IsNullOrWhiteSpace($Noun)) {
        return ""
    }
    return "$($Verb.Trim())-$($Noun.Trim())"
}

# 🎯 TEILZIEL 3 (TODO 3): Test-ApprovedVerb - Genehmigtes Verb validieren
function Test-ApprovedVerb {
    param(
        [string]$Verb
    )
    if ([string]::IsNullOrWhiteSpace($Verb)) {
        return $false
    }
    return $Global:ApprovedVerbsList -contains $Verb.Trim()
}

# 🎯 TEILZIEL 4 (TODO 4): Get-CommandSummary - Formatierte Zusammenfassung erzeugen
function Get-CommandSummary {
    param(
        [string]$CmdletName,
        [string]$Category
    )
    return "Cmdlet: $CmdletName | Kategorie: $Category"
}
