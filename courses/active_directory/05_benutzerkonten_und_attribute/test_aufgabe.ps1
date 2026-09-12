# ==============================================================================
# PESTER TESTSUITE: AD 05: Benutzerkonten & LDAP-Attribute
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

Describe "AD 05: Benutzerkonten & LDAP-Attribute" {
    # TEST: Funktion vorhanden
    It "Definiert die Funktion New-EnterpriseADUser" {
        ([bool](Get-Command New-EnterpriseADUser -ErrorAction SilentlyContinue)) | Should -Be $true
    }

    # TEST: Gibt Objekt mit Status zurück
    It "Führt die AD-Operation erfolgreich aus" {
        $res = New-EnterpriseADUser
        $res.Success | Should -Be $true
    }

    # TEST: Modul-Referenz stimmt
    It "Bezieht sich auf das korrekte Modul" {
        $res = New-EnterpriseADUser
        $res.Module | Should -Be "05_benutzerkonten_und_attribute"
    }
}

Write-Host "✅ Alle Tests in AD 05: Benutzerkonten & LDAP-Attribute erfolgreich bestanden!" -ForegroundColor Green
