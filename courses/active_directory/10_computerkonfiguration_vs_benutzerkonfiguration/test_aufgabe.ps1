# ==============================================================================
# PESTER TESTSUITE: AD 10: Computer- vs. Benutzerkonfiguration & Loopback
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

Describe "AD 10: Computer- vs. Benutzerkonfiguration & Loopback" {
    # TEST: Funktion vorhanden
    It "Definiert die Funktion Set-GPOLoopbackPolicy" {
        ([bool](Get-Command Set-GPOLoopbackPolicy -ErrorAction SilentlyContinue)) | Should -Be $true
    }

    # TEST: Gibt Objekt mit Status zurück
    It "Führt die AD-Operation erfolgreich aus" {
        $res = Set-GPOLoopbackPolicy
        $res.Success | Should -Be $true
    }

    # TEST: Modul-Referenz stimmt
    It "Bezieht sich auf das korrekte Modul" {
        $res = Set-GPOLoopbackPolicy
        $res.Module | Should -Be "10_computerkonfiguration_vs_benutzerkonfiguration"
    }
}

Write-Host "✅ Alle Tests in AD 10: Computer- vs. Benutzerkonfiguration & Loopback erfolgreich bestanden!" -ForegroundColor Green
