<#
.SYNOPSIS
    PS 01: Cmdlet-Architektur & Verb-Noun Syntax
.DESCRIPTION
    Lerne die Anatomie moderner PowerShell Cmdlets, Verb-Noun Zerlegung und Validierung.
#>

# Liste der wichtigsten Microsoft Approved Verbs zur Validierung:
$Global:ApprovedVerbsList = @(
    'Get', 'Set', 'New', 'Remove', 'Start', 'Stop', 'Restart',
    'Test', 'Find', 'Invoke', 'Select', 'Group', 'Export', 'Import'
)

# 🎯 TEILZIEL 1 (TODO 1): Get-FormattedCommandInfo - Cmdlet-Name zerlegen
# Zerlege einen Cmdlet-Namen (z.B. "Get-Process" oder "Start-Service") anhand des Bindestrichs '-'.
# Gib ein Hashtable zurück mit folgenden Schlüsseln:
# - Verb: Der Verb-Teil vor dem Bindestrich (z.B. "Get")
# - Noun: Der Noun-Teil nach dem Bindestrich (z.B. "Process")
# - IsValidVerb: $true, wenn das Verb in $Global:ApprovedVerbsList enthalten ist, sonst $false.
# Falls der Name keinen Bindestrich enthält oder leer ist, gib @{ Verb = ""; Noun = ""; IsValidVerb = $false } zurück.
function Get-FormattedCommandInfo {
    param(
        [string]$CommandName
    )
    # TODO: Zerlege $CommandName und gib das formatierte Hashtable zurück
    return @{
        Verb        = ""
        Noun        = ""
        IsValidVerb = $false
    }
}

# 🎯 TEILZIEL 2 (TODO 2): Format-CmdletName - Verb und Noun zusammensetzen
# Nimm zwei Parameter ($Verb und $Noun) und setze sie im Format "$Verb-$Noun" zusammen.
# Beide Teile sollen getrimmt werden (keine führenden/nachfolgenden Leerzeichen).
# Wenn einer der beiden Teile leer oder $null ist, gib eine leere Zeichenkette "" zurück.
function Format-CmdletName {
    param(
        [string]$Verb,
        [string]$Noun
    )
    # TODO: Kombiniere Verb und Noun zum Standard-Format
    return ""
}

# 🎯 TEILZIEL 3 (TODO 3): Test-ApprovedVerb - Genehmigtes Verb validieren
# Prüfe, ob das übergebene $Verb (Groß-/Kleinschreibung soll ignoriert werden)
# in der Liste $Global:ApprovedVerbsList enthalten ist.
# Gib $true zurück, wenn es genehmigt ist, sonst $false.
function Test-ApprovedVerb {
    param(
        [string]$Verb
    )
    # TODO: Prüfe, ob $Verb in $Global:ApprovedVerbsList enthalten ist
    return $false
}

# 🎯 TEILZIEL 4 (TODO 4): Get-CommandSummary - Formatierte Zusammenfassung erzeugen
# Erzeuge einen String im exakten Format:
# "Cmdlet: <Verb-Noun> | Kategorie: <Category>"
# Beispiel: Für $CmdletName = "Get-Process" und $Category = "Diagnostic"
# -> "Cmdlet: Get-Process | Kategorie: Diagnostic"
function Get-CommandSummary {
    param(
        [string]$CmdletName,
        [string]$Category
    )
    # TODO: Erzeuge den formatierten Ausgabe-String
    return ""
}
