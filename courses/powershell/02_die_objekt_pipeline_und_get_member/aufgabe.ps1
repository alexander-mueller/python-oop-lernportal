<#
.SYNOPSIS
    PS 02: Die Objekt-Pipeline & Get-Member
.DESCRIPTION
    Arbeiten mit .NET-Objekten, Eigenschaften, Methodenaufrufen und Typ-Inspektion.
#>

# 🎯 TEILZIEL 1 (TODO 1): Get-ObjectPropertyNames - Eigenschaftsnamen extrahieren
# Nimm ein beliebiges Eingabeobjekt $InputObject (z.B. ein [PSCustomObject] oder Hashtable).
# Ermittle alle Namen der Eigenschaften über $InputObject.PSObject.Properties.Name
# und gib sie als Array von Strings ([string[]]) zurück.
# Falls das Objekt $null ist oder keine Properties besitzt, gib ein leeres Array @() zurück.
function Get-ObjectPropertyNames {
    param(
        $InputObject
    )
    # TODO: Extrahiere die Eigenschaftsnamen als [string[]]
    return @()
}

# 🎯 TEILZIEL 2 (TODO 2): Invoke-StringSanitization - .NET-Methodenverkettung
# Bereinige den übergebenen Parameter $RawString durch Verkettung von .NET String-Methoden:
# 1. Entferne führende und nachfolgende Leerzeichen (.Trim()).
# 2. Wandle alle Buchstaben in Großbuchstaben um (.ToUpper()).
# 3. Ersetze jedes Leerzeichen (" ") durch einen Bindestrich ("-") (.Replace(" ", "-")).
# Falls $RawString $null oder leer ist, gib "" zurück.
function Invoke-StringSanitization {
    param(
        [string]$RawString
    )
    # TODO: Führe die Methodenverkettung aus
    return ""
}

# 🎯 TEILZIEL 3 (TODO 3): Get-ProcessMemoryInMB - Megabyte berechnen und runden
# Nimm eine Speichergröße in Bytes ($Bytes) als [int64] bzw. [double].
# Rechne diesen Wert in Megabyte (MB) um (unter Nutzung des PowerShell-Multiplikators 1MB).
# Runde das Ergebnis mit [Math]::Round auf genau 2 Nachkommastellen.
# Wenn $Bytes kleiner oder gleich 0 ist, gib 0.0 zurück.
function Get-ProcessMemoryInMB {
    param(
        [double]$Bytes
    )
    # TODO: Berechne den Megabyte-Wert gerundet auf 2 Dezimalstellen
    return 0.0
}

# 🎯 TEILZIEL 4 (TODO 4): Get-DotNetTypeInfo - Typ-Informationen analysieren
# Ermittle über die Methode $TargetObject.GetType() die Typ-Informationen des übergebenen Objekts.
# Gib ein Hashtable mit folgenden Schlüsseln zurück:
# - TypeName: Vollständiger Typname (z.B. "System.String" oder "System.Int32") via .FullName
# - IsValueType: Boolescher Wert ($true / $false) via .IsValueType
# - BaseType: Name des Basistyps (z.B. "Object" oder "ValueType") via .BaseType.Name (oder "" falls kein BaseType existiert)
# Falls $TargetObject $null ist, gib @{ TypeName = "Null"; IsValueType = $false; BaseType = "" } zurück.
function Get-DotNetTypeInfo {
    param(
        $TargetObject
    )
    # TODO: Ermittle Typ-Informationen und gib das Hashtable zurück
    return @{
        TypeName    = ""
        IsValueType = $false
        BaseType    = ""
    }
}
