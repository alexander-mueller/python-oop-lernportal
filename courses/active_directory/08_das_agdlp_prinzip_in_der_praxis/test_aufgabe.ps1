# ==============================================================================
# PESTER TESTSUITE: AD 08: Das AGDLP-Prinzip in der Praxis
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

Describe "AD 08: Das AGDLP-Prinzip in der Praxis" {
    # TEST: Funktion vorhanden
    It "Definiert die Funktion Deploy-AGDLPFramework" {
        ([bool](Get-Command Deploy-AGDLPFramework -ErrorAction SilentlyContinue)) | Should -Be $true
    }

    # TEST: Gibt Objekt mit Status zurück
    It "Führt die AD-Operation erfolgreich aus" {
        $res = Deploy-AGDLPFramework
        $res.Success | Should -Be $true
    }

    # TEST: Modul-Referenz stimmt
    It "Bezieht sich auf das korrekte Modul" {
        $res = Deploy-AGDLPFramework
        $res.Module | Should -Be "08_das_agdlp_prinzip_in_der_praxis"
    }
}

Write-Host "✅ Alle Tests in AD 08: Das AGDLP-Prinzip in der Praxis erfolgreich bestanden!" -ForegroundColor Green
