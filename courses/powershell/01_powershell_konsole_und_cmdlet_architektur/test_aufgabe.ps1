# 🧪 Pester v5 Testsuite: PS 01 - Cmdlet-Architektur & Verb-Noun Syntax

Describe "PS 01: Cmdlet-Architektur & Verb-Noun Syntax" {
    # TEST: Get-FormattedCommandInfo
    It "Get-FormattedCommandInfo zerlegt 'Get-Process' korrekt" {
        $info = Get-FormattedCommandInfo -CommandName "Get-Process"
        $info.Verb | Should -Be "Get"
        $info.Noun | Should -Be "Process"
        $info.IsValidVerb | Should -Be $true
    }

    # TEST: Get-FormattedCommandInfo mit ungültigem Verb
    It "Get-FormattedCommandInfo erkennt ungenehmigte Verben wie 'Fetch-Process'" {
        $info = Get-FormattedCommandInfo -CommandName "Fetch-Process"
        $info.Verb | Should -Be "Fetch"
        $info.Noun | Should -Be "Process"
        $info.IsValidVerb | Should -Be $false
    }

    # TEST: Get-FormattedCommandInfo mit ungültigem Format
    It "Get-FormattedCommandInfo behandelt Namen ohne Bindestrich sicher" {
        $info = Get-FormattedCommandInfo -CommandName "InvalidName"
        $info.IsValidVerb | Should -Be $false
        $info.Verb | Should -Be ""
        $info.Noun | Should -Be ""
    }

    # TEST: Format-CmdletName
    It "Format-CmdletName verbindet Verb und Noun korrekt" {
        $result = Format-CmdletName -Verb "Start" -Noun "Service"
        $result | Should -Be "Start-Service"
    }

    # TEST: Format-CmdletName mit Leerzeichen
    It "Format-CmdletName trimmt führende und nachfolgende Leerzeichen" {
        $result = Format-CmdletName -Verb "  Stop  " -Noun " Process "
        $result | Should -Be "Stop-Process"
    }

    # TEST: Format-CmdletName mit fehlenden Parametern
    It "Format-CmdletName liefert Leerstring bei unvollständigen Eingaben" {
        $result = Format-CmdletName -Verb "Get" -Noun ""
        $result | Should -Be ""
    }

    # TEST: Test-ApprovedVerb
    It "Test-ApprovedVerb validiert genehmigte Verben unabhängig von Groß/Kleinschreibung" {
        (Test-ApprovedVerb -Verb "get") | Should -Be $true
        (Test-ApprovedVerb -Verb "RESTART") | Should -Be $true
        (Test-ApprovedVerb -Verb "Delete") | Should -Be $false
    }

    # TEST: Get-CommandSummary
    It "Get-CommandSummary erzeugt das vorgegebene Format" {
        $summary = Get-CommandSummary -CmdletName "Get-Service" -Category "Management"
        $summary | Should -Be "Cmdlet: Get-Service | Kategorie: Management"
    }
}

Write-Host "✅ Alle Tests in PS 01 erfolgreich bestanden!" -ForegroundColor Green
