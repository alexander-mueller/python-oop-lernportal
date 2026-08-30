<#
.SYNOPSIS
    PS 13: Enterprise Modul-Entwicklung & Manifeste (.psd1) - Musterlösung
#>

function New-ModuleStructure {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$DestinationPath,

        [Parameter(Mandatory = $true)]
        [string]$ModuleName
    )

    $modRoot = Join-Path $DestinationPath $ModuleName
    $publicDir = Join-Path $modRoot "Public"
    $privateDir = Join-Path $modRoot "Private"
    $testsDir = Join-Path $modRoot "Tests"

    New-Item -ItemType Directory -Path $publicDir -Force | Out-Null
    New-Item -ItemType Directory -Path $privateDir -Force | Out-Null
    New-Item -ItemType Directory -Path $testsDir -Force | Out-Null

    $psm1Path = Join-Path $modRoot "$ModuleName.psm1"
    $psd1Path = Join-Path $modRoot "$ModuleName.psd1"

    if (-not (Test-Path $psm1Path)) { Set-Content -Path $psm1Path -Value "# Root Module for $ModuleName" }
    if (-not (Test-Path $psd1Path)) { Set-Content -Path $psd1Path -Value "@{\n  ModuleVersion = '1.0.0'\n}" }

    return [PSCustomObject]@{
        ModulePath = $modRoot
        HasPublic  = (Test-Path $publicDir)
        HasPrivate = (Test-Path $privateDir)
        HasTests   = (Test-Path $testsDir)
    }
}

function Build-ModuleManifestContent {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$ModuleName,

        [Parameter()]
        [string]$Version = '1.0.0',

        [Parameter()]
        [string]$Author = 'DevOps Architect',

        [Parameter()]
        [string]$Description = 'PowerShell Enterprise Automation Module',

        [Parameter()]
        [string[]]$FunctionsToExport = @('*')
    )

    $guid = [Guid]::NewGuid().ToString()
    $funcsString = ($FunctionsToExport | ForEach-Object { "'$_'" }) -join ", "

    return @"
@{
    RootModule        = '$ModuleName.psm1'
    ModuleVersion     = '$Version'
    GUID              = '$guid'
    Author            = '$Author'
    CompanyName       = 'Cloud Operations'
    Copyright         = '(c) $([DateTime]::UtcNow.Year) $Author. All rights reserved.'
    Description       = '$Description'
    PowerShellVersion = '7.0'
    FunctionsToExport = @($funcsString)
    CmdletsToExport   = @()
    VariablesToExport = @()
    AliasesToExport   = @()
}
"@
}

function Invoke-ModuleLoader {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$ModuleRootPath
    )

    $privatePath = Join-Path $ModuleRootPath "Private"
    $publicPath = Join-Path $ModuleRootPath "Public"

    if (Test-Path $privatePath) {
        Get-ChildItem -Path $privatePath -Filter "*.ps1" -File | ForEach-Object {
            . $_.FullName
        }
    }

    $exportedFunctions = [System.Collections.Generic.List[string]]::new()
    if (Test-Path $publicPath) {
        Get-ChildItem -Path $publicPath -Filter "*.ps1" -File | ForEach-Object {
            . $_.FullName
            $exportedFunctions.Add($_.BaseName)
        }
    }

    if (Get-Command Export-ModuleMember -ErrorAction SilentlyContinue) {
        try {
            Export-ModuleMember -Function $exportedFunctions
        } catch {}
    }

    return @($exportedFunctions)
}

function Test-ModuleCompliance {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$ModulePath
    )

    $modItem = Get-Item -Path $ModulePath -ErrorAction Stop
    $modName = $modItem.Name

    $missing = [System.Collections.Generic.List[string]]::new()

    $publicDir = Join-Path $ModulePath "Public"
    $privateDir = Join-Path $ModulePath "Private"
    $psm1File = Join-Path $ModulePath "$modName.psm1"
    $psd1File = Join-Path $ModulePath "$modName.psd1"

    if (-not (Test-Path $publicDir)) { $missing.Add("Public-Ordner fehlt") }
    if (-not (Test-Path $privateDir)) { $missing.Add("Private-Ordner fehlt") }
    if (-not (Test-Path $psm1File)) { $missing.Add("$modName.psm1 fehlt") }
    if (-not (Test-Path $psd1File)) { $missing.Add("$modName.psd1 fehlt") }

    $version = "0.0.0"
    if (Test-Path $psd1File) {
        $content = Get-Content -Path $psd1File -Raw
        if ($content -match "ModuleVersion\s*=\s*['""]([^'""]+)['""]") {
            $version = $matches[1]
        }
    }

    return [PSCustomObject]@{
        ModuleName   = $modName
        IsCompliant  = ($missing.Count -eq 0)
        MissingItems = @($missing)
        Version      = $version
    }
}
