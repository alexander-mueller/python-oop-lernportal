<#
.SYNOPSIS
    PS 10: REST-APIs, JSON, CSV & XML Datenpipelines - Musterlösung
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

    $headers = @{
        'Content-Type' = 'application/json'
    }
    if (-not [string]::IsNullOrEmpty($BearerToken)) {
        $headers['Authorization'] = "Bearer $BearerToken"
    }

    $splatParams = @{
        Uri     = $Uri
        Method  = $Method
        Headers = $headers
    }

    if ($Body) {
        $splatParams['Body'] = ($Body | ConvertTo-Json -Depth 10)
    }

    try {
        return Invoke-RestMethod @splatParams
    } catch {
        Write-Error "Fehler bei REST API Call an $Uri : $_"
        throw $_
    }
}

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

    $objects = $JsonString | ConvertFrom-Json
    if ($SelectedProperties -and $SelectedProperties.Count -gt 0) {
        $objects = $objects | Select-Object -Property $SelectedProperties
    }
    return @($objects | ConvertTo-Csv -NoTypeInformation -Delimiter $Delimiter)
}

function Format-DeepNestedConfig {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [object]$ConfigObject,

        [Parameter()]
        [ValidateRange(2, 50)]
        [int]$Depth = 10
    )

    $json = $ConfigObject | ConvertTo-Json -Depth $Depth
    $parsed = $json | ConvertFrom-Json
    return [PSCustomObject]@{
        JsonString = $json
        ParsedBack = $parsed
        IsValid    = ($null -ne $parsed)
    }
}

function Parse-XmlServerManifest {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$XmlContent
    )

    [xml]$xmlDoc = $XmlContent
    $env = $xmlDoc.DocumentElement.GetAttribute('environment')
    if (-not $env) {
        $env = 'default'
    }

    $serverNodes = $xmlDoc.SelectNodes('//server')
    $results = foreach ($node in $serverNodes) {
        $portVal = 0
        if ($node.port) {
            $portVal = [int]$node.port
        } elseif ($node.GetAttribute('port')) {
            $portVal = [int]$node.GetAttribute('port')
        }

        [PSCustomObject]@{
            Name        = $node.GetAttribute('name')
            Role        = $node.GetAttribute('role')
            Port        = $portVal
            Environment = $env
        }
    }

    return @($results)
}
