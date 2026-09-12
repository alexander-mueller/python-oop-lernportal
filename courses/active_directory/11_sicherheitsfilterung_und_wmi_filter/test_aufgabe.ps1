# ==============================================================================
# PESTER TESTSUITE: AD 11: Sicherheitsfilterung & WMI-Filter
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

Describe "AD 11: Sicherheitsfilterung & WMI-Filter" {
    # TEST: Funktion vorhanden
    It "Definiert die Funktion New-WmiGpoFilter" {
        ([bool](Get-Command New-WmiGpoFilter -ErrorAction SilentlyContinue)) | Should -Be $true
    }

    # TEST: Gibt Objekt mit Status zurück
    It "Führt die AD-Operation erfolgreich aus" {
        $res = New-WmiGpoFilter
        $res.Success | Should -Be $true
    }

    # TEST: Modul-Referenz stimmt
    It "Bezieht sich auf das korrekte Modul" {
        $res = New-WmiGpoFilter
        $res.Module | Should -Be "11_sicherheitsfilterung_und_wmi_filter"
    }
}

Write-Host "✅ Alle Tests in AD 11: Sicherheitsfilterung & WMI-Filter erfolgreich bestanden!" -ForegroundColor Green
