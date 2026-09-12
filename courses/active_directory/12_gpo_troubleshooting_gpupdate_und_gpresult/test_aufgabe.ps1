# ==============================================================================
# PESTER TESTSUITE: AD 12: GPO Troubleshooting: gpupdate & gpresult
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

Describe "AD 12: GPO Troubleshooting: gpupdate & gpresult" {
    # TEST: Funktion vorhanden
    It "Definiert die Funktion Invoke-GPODiagnostics" {
        ([bool](Get-Command Invoke-GPODiagnostics -ErrorAction SilentlyContinue)) | Should -Be $true
    }

    # TEST: Gibt Objekt mit Status zurück
    It "Führt die AD-Operation erfolgreich aus" {
        $res = Invoke-GPODiagnostics
        $res.Success | Should -Be $true
    }

    # TEST: Modul-Referenz stimmt
    It "Bezieht sich auf das korrekte Modul" {
        $res = Invoke-GPODiagnostics
        $res.Module | Should -Be "12_gpo_troubleshooting_gpupdate_und_gpresult"
    }
}

Write-Host "✅ Alle Tests in AD 12: GPO Troubleshooting: gpupdate & gpresult erfolgreich bestanden!" -ForegroundColor Green
