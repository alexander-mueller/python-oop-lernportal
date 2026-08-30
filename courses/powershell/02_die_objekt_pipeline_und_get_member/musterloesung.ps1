<#
.SYNOPSIS
    PS 02: Die Objekt-Pipeline & Get-Member (Musterlösung)
#>

# 🎯 TEILZIEL 1 (TODO 1): Get-ObjectPropertyNames - Eigenschaftsnamen extrahieren
function Get-ObjectPropertyNames {
    param(
        $InputObject
    )
    if ($null -eq $InputObject) {
        return @()
    }
    
    $props = $InputObject.PSObject.Properties.Name
    if ($null -eq $props) {
        return @()
    }
    return [string[]]@($props)
}

# 🎯 TEILZIEL 2 (TODO 2): Invoke-StringSanitization - .NET-Methodenverkettung
function Invoke-StringSanitization {
    param(
        [string]$RawString
    )
    if ([string]::IsNullOrEmpty($RawString)) {
        return ""
    }
    return $RawString.Trim().ToUpper().Replace(" ", "-")
}

# 🎯 TEILZIEL 3 (TODO 3): Get-ProcessMemoryInMB - Megabyte berechnen und runden
function Get-ProcessMemoryInMB {
    param(
        [double]$Bytes
    )
    if ($Bytes -le 0) {
        return 0.0
    }
    $mb = $Bytes / 1MB
    return [Math]::Round($mb, 2)
}

# 🎯 TEILZIEL 4 (TODO 4): Get-DotNetTypeInfo - Typ-Informationen analysieren
function Get-DotNetTypeInfo {
    param(
        $TargetObject
    )
    if ($null -eq $TargetObject) {
        return @{
            TypeName    = "Null"
            IsValueType = $false
            BaseType    = ""
        }
    }

    $type = $TargetObject.GetType()
    $baseName = if ($type.BaseType) { $type.BaseType.Name } else { "" }

    return @{
        TypeName    = $type.FullName
        IsValueType = $type.IsValueType
        BaseType    = $baseName
    }
}
