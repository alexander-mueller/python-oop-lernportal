<#
.SYNOPSIS
    PS 11: Dateisystem, PSDrives (Env/Cert/Registry) & Hashes - Musterlösung
#>

function Get-EnvironmentReport {
    [CmdletBinding()]
    param(
        [Parameter()]
        [string[]]$FilterPatterns = @('*')
    )

    $allEnv = Get-ChildItem Env:
    $results = foreach ($pattern in $FilterPatterns) {
        $allEnv | Where-Object { $_.Name -like $pattern } | ForEach-Object {
            $val = [string]$_.Value
            [PSCustomObject]@{
                VariableName = [string]$_.Name
                Value        = $val
                Length       = $val.Length
            }
        }
    }
    return @($results | Sort-Object VariableName -Unique)
}

function Get-DirectoryFileInventory {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path,

        [Parameter()]
        [string[]]$Extensions = @('*'),

        [Parameter()]
        [bool]$CalculateHash = $true
    )

    if (-not (Test-Path -Path $Path)) {
        return @()
    }

    $files = Get-ChildItem -Path $Path -File -Recurse -ErrorAction SilentlyContinue
    $filtered = if ($Extensions -contains '*' -or $Extensions -contains '*.*') {
        $files
    } else {
        $files | Where-Object {
            $ext = $_.Extension.TrimStart('.')
            $Extensions -contains $ext -or $Extensions -contains $_.Extension
        }
    }

    $inventory = foreach ($f in $filtered) {
        $hashVal = $null
        if ($CalculateHash) {
            try {
                $hashObj = Get-FileHash -Path $f.FullName -Algorithm SHA256 -ErrorAction SilentlyContinue
                $hashVal = $hashObj.Hash
            } catch {
                $hashVal = "Error: $_"
            }
        }

        [PSCustomObject]@{
            Name         = $f.Name
            FullPath     = $f.FullName
            Extension    = $f.Extension
            SizeKB       = [Math]::Round($f.Length / 1KB, 2)
            LastModified = $f.LastWriteTime
            SHA256       = $hashVal
        }
    }

    return @($inventory)
}

function Test-FileIntegrity {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$FilePath,

        [Parameter(Mandatory = $true)]
        [string]$ExpectedHash,

        [Parameter()]
        [ValidateSet('SHA256', 'SHA384', 'SHA512', 'MD5')]
        [string]$Algorithm = 'SHA256'
    )

    if (-not (Test-Path -Path $FilePath)) {
        throw "Datei nicht gefunden: $FilePath"
    }

    $fileHash = Get-FileHash -Path $FilePath -Algorithm $Algorithm
    $calculated = $fileHash.Hash.ToUpper()
    $expected = $ExpectedHash.Trim().ToUpper()

    return [PSCustomObject]@{
        FilePath       = (Resolve-Path $FilePath).Path
        IsValid        = ($calculated -eq $expected)
        CalculatedHash = $calculated
        ExpectedHash   = $expected
    }
}

function New-TemporaryMountDrive {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$DriveName,

        [Parameter(Mandatory = $true)]
        [string]$RootPath,

        [Parameter(Mandatory = $true)]
        [scriptblock]$Action
    )

    $drive = New-PSDrive -Name $DriveName -PSProvider FileSystem -Root $RootPath -ErrorAction Stop
    try {
        return & $Action $DriveName
    } finally {
        Remove-PSDrive -Name $DriveName -Force -ErrorAction SilentlyContinue
    }
}
