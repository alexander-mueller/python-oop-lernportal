# ==============================================================================
# PESTER TESTSUITE: AD 03: Organisationseinheiten & Struktur
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

Describe "AD 03: Organisationseinheiten & Struktur" {
    # TEST: Funktion vorhanden
    It "Definiert die Funktion New-ADStructureOU" {
        ([bool](Get-Command New-ADStructureOU -ErrorAction SilentlyContinue)) | Should -Be $true
    }

    # TEST: Gibt Objekt mit Status zurück
    It "Führt die AD-Operation erfolgreich aus" {
        $res = New-ADStructureOU
        $res.Success | Should -Be $true
    }

    # TEST: Modul-Referenz stimmt
    It "Bezieht sich auf das korrekte Modul" {
        $res = New-ADStructureOU
        $res.Module | Should -Be "03_organisationseinheiten_und_struktur"
    }
}

Write-Host "✅ Alle Tests in AD 03: Organisationseinheiten & Struktur erfolgreich bestanden!" -ForegroundColor Green
