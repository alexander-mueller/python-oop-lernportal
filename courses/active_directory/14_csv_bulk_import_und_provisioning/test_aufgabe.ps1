# ==============================================================================
# PESTER TESTSUITE: AD 14: CSV Bulk-Import & Provisioning
# ==============================================================================

# Pester Compatibility Shim falls Pester v5 Modul nicht geladen ist
if (-not (Get-Command Describe -ErrorAction SilentlyContinue)) {
    function Describe ($Name, $Script) { & $Script }
    function It ($Name, $Script) { & $Script }
    function Should {
        [CmdletBinding()]
        param(
            [Parameter(ValueFromPipeline=$true)] $ActualValue,
            [Parameter(Position=0)] $ExpectedValue,
            [switch]$Be
        )
        process {
            if ($Be -and ($ActualValue -ne $ExpectedValue)) {
                throw "Assertion failed: Expected '$ExpectedValue' but got '$ActualValue'"
            }
        }
    }
}

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
. "$ScriptDir/aufgabe.ps1"

Describe "AD 14: CSV Bulk-Import & Provisioning" {
    # TEST: Funktion vorhanden
    It "Definiert die Funktion Import-ADUsersFromCSV" {
        ([bool](Get-Command Import-ADUsersFromCSV -ErrorAction SilentlyContinue)) | Should -Be $true
    }

    # TEST: Gibt Objekt mit Status zurück
    It "Führt die AD-Operation erfolgreich aus" {
        $res = Import-ADUsersFromCSV
        $res.Success | Should -Be $true
    }

    # TEST: Modul-Referenz stimmt
    It "Bezieht sich auf das korrekte Modul" {
        $res = Import-ADUsersFromCSV
        $res.Module | Should -Be "14_csv_bulk_import_und_provisioning"
    }
}

Write-Host "✅ Alle Tests in AD 14: CSV Bulk-Import & Provisioning erfolgreich bestanden!" -ForegroundColor Green
