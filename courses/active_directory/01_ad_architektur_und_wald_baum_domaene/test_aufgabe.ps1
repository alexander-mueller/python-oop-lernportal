# ==============================================================================
# PESTER TESTSUITE: AD 01: AD DS Architektur & Wald, Baum, Domäne
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

Describe "AD 01: AD DS Architektur & Wald, Baum, Domäne" {
    # TEST: Funktion vorhanden
    It "Definiert die Funktion Get-ADDomainArchitecture" {
        ([bool](Get-Command Get-ADDomainArchitecture -ErrorAction SilentlyContinue)) | Should -Be $true
    }

    # TEST: Gibt Objekt mit Status zurück
    It "Führt die AD-Operation erfolgreich aus" {
        $res = Get-ADDomainArchitecture
        $res.Success | Should -Be $true
    }

    # TEST: Modul-Referenz stimmt
    It "Bezieht sich auf das korrekte Modul" {
        $res = Get-ADDomainArchitecture
        $res.Module | Should -Be "01_ad_architektur_und_wald_baum_domaene"
    }
}

Write-Host "✅ Alle Tests in AD 01: AD DS Architektur & Wald, Baum, Domäne erfolgreich bestanden!" -ForegroundColor Green
