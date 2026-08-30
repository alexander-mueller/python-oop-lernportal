<#
.SYNOPSIS
    PS 10: REST-APIs, JSON, CSV & XML Datenpipelines
.DESCRIPTION
    Lerne moderne Datenverarbeitung und Web-APIs in PowerShell 7+:
    - Invoke-RestMethod mit Headern & Bearer-Authentifizierung
    - ConvertFrom-Json und ConvertTo-Json mit -Depth
    - Export-Csv / ConvertTo-Csv ohne Typ-Header
    - XML-Verarbeitung mit dem [xml]-Typbeschleuniger
#>

# 🎯 TEILZIEL 1 (TODO 1): Get-RestApiData
<#
.DESCRIPTION
    Führt einen REST-API Request mit `Invoke-RestMethod` aus.
    Unterstützt HTTP-Methoden (GET, POST, etc.) und optionale Bearer-Token Authentifizierung.
.OUTPUTS
    Das von Invoke-RestMethod deserialisierte Objekt
#>
function Get-RestApiData {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$Uri,

        [Parameter()]
        [ValidateSet('GET', 'POST', 'PUT', 'DELETE', 'PATCH')]
        [string]$Method = 'GET',

        [Parameter()]
        [string]$BearerToken = $null,

        [Parameter()]
        [hashtable]$Body = $null
    )

    # TODO:
    # 1. Erstelle eine Header-Hashtable mit 'Content-Type' = 'application/json'.
    # 2. Füge 'Authorization' = "Bearer $BearerToken" hinzu, falls $BearerToken gesetzt ist.
    # 3. Führe Invoke-RestMethod aus (mit -Body ($Body | ConvertTo-Json) falls $Body übergeben wurde).
    # 4. Gib das Ergebnis zurück.
    return $null
}

# 🎯 TEILZIEL 2 (TODO 2): Convert-JsonToCsvReport
<#
.DESCRIPTION
    Nimmt einen JSON-String entgegen, filtert bestimmte Eigenschaften und erzeugt
    einen wohlgeformten CSV-String (ohne #TYPE Metadaten-Zeile).
.OUTPUTS
    [string[]] Die CSV-Zeilen
#>
function Convert-JsonToCsvReport {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$JsonString,

        [Parameter()]
        [string[]]$SelectedProperties = @(),

        [Parameter()]
        [string]$Delimiter = ';'
    )

    # TODO:
    # 1. Konvertiere $JsonString mit ConvertFrom-Json in Objekte.
    # 2. Wähle mit Select-Object $SelectedProperties aus (falls übergeben).
    # 3. Konvertiere in CSV mit ConvertTo-Csv -NoTypeInformation -Delimiter $Delimiter.
    return @()
}

# 🎯 TEILZIEL 3 (TODO 3): Format-DeepNestedConfig
<#
.DESCRIPTION
    Konvertiert ein tief verschachteltes Konfigurationsobjekt verlustfrei in JSON
    unter expliziter Angabe von -Depth (verhindert das Abschneiden tiefer Ebenen).
.OUTPUTS
    [PSCustomObject]@{
        JsonString = [string]
        ParsedBack = [object]
        IsValid    = [bool]
    }
#>
function Format-DeepNestedConfig {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [object]$ConfigObject,

        [Parameter()]
        [ValidateRange(2, 50)]
        [int]$Depth = 10
    )

    # TODO:
    # 1. Serialisiere $ConfigObject zu JSON mit ConvertTo-Json -Depth $Depth.
    # 2. Deserialisiere den JSON-String wieder mit ConvertFrom-Json.
    # 3. Gib ein [PSCustomObject] mit JsonString, ParsedBack und IsValid ($true) zurück.
    return $null
}

# 🎯 TEILZIEL 4 (TODO 4): Parse-XmlServerManifest
<#
.DESCRIPTION
    Parst ein XML-Manifest mit Serverdefinitionen und extrahiert strukturierte PSCustomObjects.
    Beispiel XML:
    <infrastructure environment="production">
      <servers>
        <server name="web01" role="Frontend"><port>443</port></server>
        <server name="db01" role="Database"><port>5432</port></server>
      </servers>
    </infrastructure>
.OUTPUTS
    Array von [PSCustomObject] mit Eigenschaften: Name, Role, Port ([int]), Environment
#>
function Parse-XmlServerManifest {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$XmlContent
    )

    # TODO:
    # 1. Konvertiere $XmlContent in ein [xml]-Dokument.
    # 2. Ermittle das Environment-Attribut aus dem Root-Element.
    # 3. Iteriere über alle <server>-Knoten und erzeuge für jeden ein [PSCustomObject]@{
    #      Name = ...; Role = ...; Port = [int]...; Environment = ...
    #    }
    return @()
}
