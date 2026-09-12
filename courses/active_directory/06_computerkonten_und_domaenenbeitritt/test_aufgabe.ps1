# ==============================================================================
# PESTER TESTSUITE: AD 06: Computerkonten & Domänenbeitritt
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

Describe "AD 06: Computerkonten & Domänenbeitritt" {
    # TEST: Funktion vorhanden
    It "Definiert die Funktion Add-DomainComputerAccount" {
        ([bool](Get-Command Add-DomainComputerAccount -ErrorAction SilentlyContinue)) | Should -Be $true
    }

    # TEST: Gibt Objekt mit Status zurück
    It "Führt die AD-Operation erfolgreich aus" {
        $res = Add-DomainComputerAccount
        $res.Success | Should -Be $true
    }

    # TEST: Modul-Referenz stimmt
    It "Bezieht sich auf das korrekte Modul" {
        $res = Add-DomainComputerAccount
        $res.Module | Should -Be "06_computerkonten_und_domaenenbeitritt"
    }
}

Write-Host "✅ Alle Tests in AD 06: Computerkonten & Domänenbeitritt erfolgreich bestanden!" -ForegroundColor Green
