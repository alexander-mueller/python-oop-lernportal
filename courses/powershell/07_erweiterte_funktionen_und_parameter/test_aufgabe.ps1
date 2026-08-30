# 🧪 Pester v5 Testsuite: PS 07 - Eigene Cmdlets [CmdletBinding()] & Validierung

Describe "PS 07: Eigene Cmdlets [CmdletBinding()] & Validierung" {
    # TEST: Get-EnvironmentConfig mit Standard-Port
    It "Get-EnvironmentConfig erzeugt ein korrektes Konfigurationsobjekt" {
        $cfg = Get-EnvironmentConfig -Environment "Production"
        $cfg.Environment | Should -Be "Production"
        $cfg.Port | Should -Be 8080
        $cfg.IsProduction | Should -Be $true
    }

    # TEST: Get-EnvironmentConfig mit benutzerdefiniertem Port
    It "Get-EnvironmentConfig akzeptiert benutzerdefinierten Port" {
        $cfg = Get-EnvironmentConfig -Environment "Development" -Port 3000
        $cfg.Environment | Should -Be "Development"
        $cfg.Port | Should -Be 3000
        $cfg.IsProduction | Should -Be $false
    }

    # TEST: Restart-AppService normale Ausführung
    It "Restart-AppService führt Operation aus wenn ShouldProcess bestätigt" {
        $res = Restart-AppService -ServiceName "nginx"
        $res.ServiceName | Should -Be "nginx"
        $res.Action | Should -Be "Restarted"
        $res.Executed | Should -Be $true
    }

    # TEST: New-UserAccount
    It "New-UserAccount extrahiert Username aus Email und setzt Rolle" {
        $user = New-UserAccount -Email "admin.devops@company.org" -Role "Admin"
        $user.Username | Should -Be "admin.devops"
        $user.Email | Should -Be "admin.devops@company.org"
        $user.Role | Should -Be "Admin"
    }

    # TEST: Get-SystemReport
    It "Get-SystemReport wertet Switch-Parameter [switch] präzise aus" {
        $rep1 = Get-SystemReport -Title "Daily Backup"
        $rep1.Title | Should -Be "Daily Backup"
        $rep1.IsDetailed | Should -Be $false

        $rep2 = Get-SystemReport -Title "Audit Log" -Detailed
        $rep2.Title | Should -Be "Audit Log"
        $rep2.IsDetailed | Should -Be $true
    }
}

Write-Host "✅ Alle Tests in PS 07 erfolgreich bestanden!" -ForegroundColor Green
