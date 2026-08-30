# 🧪 Pester v5 Testsuite: PS 05 - Kontrollfluss & Moderne Operatoren

Describe "PS 05: Kontrollfluss & Moderne Operatoren" {
    # TEST: Get-AccessDecision
    It "Get-AccessDecision gewährt korrekte Rechte für aktive Benutzer" {
        (Get-AccessDecision -Role "Admin" -IsActive $true) | Should -Be "FullAccess"
        (Get-AccessDecision -Role "Editor" -IsActive $true) | Should -Be "WriteAccess"
        (Get-AccessDecision -Role "Viewer" -IsActive $true) | Should -Be "ReadOnly"
        (Get-AccessDecision -Role "Guest" -IsActive $true) | Should -Be "Denied"
    }

    # TEST: Get-AccessDecision für inaktive Benutzer
    It "Get-AccessDecision verweigert immer Zugriff für inaktive Benutzer" {
        (Get-AccessDecision -Role "Admin" -IsActive $false) | Should -Be "Denied"
        (Get-AccessDecision -Role "Editor" -IsActive $false) | Should -Be "Denied"
    }

    # TEST: Get-ConfigWithFallback
    It "Get-ConfigWithFallback respektiert die Prioritätsstufen" {
        $res1 = Get-ConfigWithFallback -UserOverride "CustomHost" -EnvSetting "EnvHost" -DefaultSetting "DefaultHost"
        $res1 | Should -Be "CustomHost"

        $res2 = Get-ConfigWithFallback -UserOverride "" -EnvSetting "EnvHost" -DefaultSetting "DefaultHost"
        $res2 | Should -Be "EnvHost"

        $res3 = Get-ConfigWithFallback -UserOverride "" -EnvSetting "" -DefaultSetting "DefaultHost"
        $res3 | Should -Be "DefaultHost"
    }

    # TEST: Classify-LogMessage
    It "Classify-LogMessage stuft Fehlermeldungen mit Regex korrekt ein" {
        (Classify-LogMessage -Message "ERR-500: Database timeout") | Should -Be "CriticalError"
        (Classify-LogMessage -Message "WARN-404: File missing") | Should -Be "Warning"
        (Classify-LogMessage -Message "OK-200: Service started") | Should -Be "Success"
        (Classify-LogMessage -Message "Random status message") | Should -Be "Unknown"
    }

    # TEST: Test-NetworkPort
    It "Test-NetworkPort prüft Port-Grenzen (1024 bis 49151) präzise" {
        (Test-NetworkPort -Port 1024) | Should -Be $true
        (Test-NetworkPort -Port 8080) | Should -Be $true
        (Test-NetworkPort -Port 49151) | Should -Be $true
        (Test-NetworkPort -Port 80) | Should -Be $false
        (Test-NetworkPort -Port 443) | Should -Be $false
        (Test-NetworkPort -Port 65535) | Should -Be $false
    }
}

Write-Host "✅ Alle Tests in PS 05 erfolgreich bestanden!" -ForegroundColor Green
