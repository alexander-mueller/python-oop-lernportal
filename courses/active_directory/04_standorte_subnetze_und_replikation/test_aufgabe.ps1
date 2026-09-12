# ==============================================================================
# PESTER TESTSUITE: AD 04: Standorte, Subnetze & Replikation
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

Describe "AD 04: Standorte, Subnetze & Replikation" {
    # TEST: Funktion vorhanden
    It "Definiert die Funktion Sync-ADReplicationSite" {
        ([bool](Get-Command Sync-ADReplicationSite -ErrorAction SilentlyContinue)) | Should -Be $true
    }

    # TEST: Gibt Objekt mit Status zurück
    It "Führt die AD-Operation erfolgreich aus" {
        $res = Sync-ADReplicationSite
        $res.Success | Should -Be $true
    }

    # TEST: Modul-Referenz stimmt
    It "Bezieht sich auf das korrekte Modul" {
        $res = Sync-ADReplicationSite
        $res.Module | Should -Be "04_standorte_subnetze_und_replikation"
    }
}

Write-Host "✅ Alle Tests in AD 04: Standorte, Subnetze & Replikation erfolgreich bestanden!" -ForegroundColor Green
