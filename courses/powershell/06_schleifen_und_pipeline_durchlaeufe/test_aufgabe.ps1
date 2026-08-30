# 🧪 Pester v5 Testsuite: PS 06 - Schleifen (foreach, while & Pipeline)

Describe "PS 06: Schleifen (foreach, while & Pipeline)" {
    # TEST: Get-FilteredEvenSquares
    It "Get-FilteredEvenSquares berechnet Quadrate nur für gerade Zahlen" {
        $result = Get-FilteredEvenSquares -Numbers @(1, 2, 3, 4, 5, 6)
        $result.Count | Should -Be 3
        $result[0] | Should -Be 4    # 2^2
        $result[1] | Should -Be 16   # 4^2
        $result[2] | Should -Be 36   # 6^2
    }

    # TEST: Get-FilteredEvenSquares mit leerem Array
    It "Get-FilteredEvenSquares liefert leeres Array bei leerer Eingabe" {
        $result = Get-FilteredEvenSquares -Numbers @()
        $result.Count | Should -Be 0
    }

    # TEST: Invoke-StreamingPipelineMetrics
    It "Invoke-StreamingPipelineMetrics ermittelt Count, Summe und Durchschnitt" {
        $metrics = Invoke-StreamingPipelineMetrics -DataStream @(10.0, 20.0, 30.0, 40.0)
        $metrics.Count | Should -Be 4
        $metrics.TotalSum | Should -Be 100.0
        $metrics.Average | Should -Be 25.0
    }

    # TEST: Invoke-RetryOperation erfolgreich
    It "Invoke-RetryOperation beendet bei Erfolg vorzeitig" {
        $retry1 = Invoke-RetryOperation -MaxAttempts 5 -SuccessOnAttempt 2
        $retry1.Attempts | Should -Be 2
        $retry1.IsSuccess | Should -Be $true
    }

    # TEST: Invoke-RetryOperation fehlgeschlagen
    It "Invoke-RetryOperation stoppt bei Erreichen des Maximums" {
        $retry2 = Invoke-RetryOperation -MaxAttempts 3 -SuccessOnAttempt 99
        $retry2.Attempts | Should -Be 3
        $retry2.IsSuccess | Should -Be $false
    }

    # TEST: Find-FirstMatchingServer
    It "Find-FirstMatchingServer findet den ersten passenden Server und bricht ab" {
        $servers = @("srv-web01", "srv-app01", "srv-db01", "srv-db02")
        $found = Find-FirstMatchingServer -Servers $servers -Prefix "srv-db"
        $found | Should -Be "srv-db01"
    }

    # TEST: Find-FirstMatchingServer ohne Treffer
    It "Find-FirstMatchingServer liefert Null wenn kein Server passt" {
        $servers = @("srv-web01", "srv-app01")
        $found = Find-FirstMatchingServer -Servers $servers -Prefix "srv-cloud"
        $found | Should -BeNullOrEmpty
    }
}

Write-Host "✅ Alle Tests in PS 06 erfolgreich bestanden!" -ForegroundColor Green
