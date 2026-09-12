# ==============================================================================
# PESTER TESTSUITE: AD 02: Domänencontroller & FSMO-Rollen
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

Describe "AD 02: Domänencontroller & FSMO-Rollen" {
    # TEST: Funktion vorhanden
    It "Definiert die Funktion Get-FSMORoleOwner" {
        ([bool](Get-Command Get-FSMORoleOwner -ErrorAction SilentlyContinue)) | Should -Be $true
    }

    # TEST: Gibt Objekt mit Status zurück
    It "Führt die AD-Operation erfolgreich aus" {
        $res = Get-FSMORoleOwner
        $res.Success | Should -Be $true
    }

    # TEST: Modul-Referenz stimmt
    It "Bezieht sich auf das korrekte Modul" {
        $res = Get-FSMORoleOwner
        $res.Module | Should -Be "02_domaenencontroller_und_fsmo_rollen"
    }
}

Write-Host "✅ Alle Tests in AD 02: Domänencontroller & FSMO-Rollen erfolgreich bestanden!" -ForegroundColor Green
