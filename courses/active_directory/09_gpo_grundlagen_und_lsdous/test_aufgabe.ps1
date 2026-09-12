# ==============================================================================
# PESTER TESTSUITE: AD 09: GPO-Grundlagen & LSDOU-Hierarchie
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

Describe "AD 09: GPO-Grundlagen & LSDOU-Hierarchie" {
    # TEST: Funktion vorhanden
    It "Definiert die Funktion New-TargetedGPO" {
        ([bool](Get-Command New-TargetedGPO -ErrorAction SilentlyContinue)) | Should -Be $true
    }

    # TEST: Gibt Objekt mit Status zurück
    It "Führt die AD-Operation erfolgreich aus" {
        $res = New-TargetedGPO
        $res.Success | Should -Be $true
    }

    # TEST: Modul-Referenz stimmt
    It "Bezieht sich auf das korrekte Modul" {
        $res = New-TargetedGPO
        $res.Module | Should -Be "09_gpo_grundlagen_und_lsdous"
    }
}

Write-Host "✅ Alle Tests in AD 09: GPO-Grundlagen & LSDOU-Hierarchie erfolgreich bestanden!" -ForegroundColor Green
