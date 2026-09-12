# ==============================================================================
# PESTER TESTSUITE: AD 07: Sicherheitsgruppen & Bereichstypen
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

Describe "AD 07: Sicherheitsgruppen & Bereichstypen" {
    # TEST: Funktion vorhanden
    It "Definiert die Funktion New-SecurityGroupHierarchy" {
        ([bool](Get-Command New-SecurityGroupHierarchy -ErrorAction SilentlyContinue)) | Should -Be $true
    }

    # TEST: Gibt Objekt mit Status zurück
    It "Führt die AD-Operation erfolgreich aus" {
        $res = New-SecurityGroupHierarchy
        $res.Success | Should -Be $true
    }

    # TEST: Modul-Referenz stimmt
    It "Bezieht sich auf das korrekte Modul" {
        $res = New-SecurityGroupHierarchy
        $res.Module | Should -Be "07_sicherheitsgruppen_und_bereichstypen"
    }
}

Write-Host "✅ Alle Tests in AD 07: Sicherheitsgruppen & Bereichstypen erfolgreich bestanden!" -ForegroundColor Green
