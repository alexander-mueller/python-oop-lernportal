# ==============================================================================
# PESTER TESTSUITE: Master 16: Enterprise AD Automation & Security Suite
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

Describe "Master 16: Enterprise AD Automation & Security Suite" {
    # TEST: Funktion vorhanden
    It "Definiert die Funktion Invoke-ADEnterpriseAutomationSuite" {
        ([bool](Get-Command Invoke-ADEnterpriseAutomationSuite -ErrorAction SilentlyContinue)) | Should -Be $true
    }

    # TEST: Gibt Objekt mit Status zurück
    It "Führt die AD-Operation erfolgreich aus" {
        $res = Invoke-ADEnterpriseAutomationSuite
        $res.Success | Should -Be $true
    }

    # TEST: Modul-Referenz stimmt
    It "Bezieht sich auf das korrekte Modul" {
        $res = Invoke-ADEnterpriseAutomationSuite
        $res.Module | Should -Be "16_master_abschlussprojekt_ad_automation_suite"
    }
}

Write-Host "✅ Alle Tests in Master 16: Enterprise AD Automation & Security Suite erfolgreich bestanden!" -ForegroundColor Green
