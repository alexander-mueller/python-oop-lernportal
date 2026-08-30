# 🧪 Pester v5 Testsuite: PS 04 - Typisierung, Hashtables & PSCustomObject

Describe "PS 04: Typisierung, Hashtables & PSCustomObject" {
    # TEST: New-ServerInventoryObject
    It "New-ServerInventoryObject erzeugt ein vollständiges PSCustomObject" {
        $testDate = [DateTime]::new(2026, 1, 1, 12, 0, 0)
        $server = New-ServerInventoryObject -Hostname "srv-prod01" -IPAddress "10.0.0.15" -CPUCount 16 -IsActive $true -CreatedAt $testDate
        
        $server.Hostname | Should -Be "srv-prod01"
        $server.IPAddress | Should -Be "10.0.0.15"
        $server.CPUCount | Should -Be 16
        $server.IsActive | Should -Be $true
        $server.CreatedAt | Should -Be $testDate
    }

    # TEST: Convert-HashtableToCustomObject
    It "Convert-HashtableToCustomObject wandelt ein Hashtable in ein PSCustomObject um" {
        $hash = @{
            AppId       = 42
            AppName     = "CloudOps"
            Environment = "Production"
        }
        $obj = Convert-HashtableToCustomObject -HashTable $hash
        $obj.AppId | Should -Be 42
        $obj.AppName | Should -Be "CloudOps"
        $obj.Environment | Should -Be "Production"
    }

    # TEST: Get-ArrayStatistics
    It "Get-ArrayStatistics berechnet Summe, Durchschnitt, Min und Max korrekt" {
        $stats = Get-ArrayStatistics -Numbers @(10.0, 20.0, 30.0, 40.0, 50.0)
        $stats.Sum | Should -Be 150.0
        $stats.Average | Should -Be 30.0
        $stats.Min | Should -Be 10.0
        $stats.Max | Should -Be 50.0
    }

    # TEST: Get-ArrayStatistics mit Rundung
    It "Get-ArrayStatistics rundet den Durchschnitt sauber auf 2 Dezimalstellen" {
        $stats = Get-ArrayStatistics -Numbers @(10.0, 20.0, 25.0)
        $stats.Sum | Should -Be 55.0
        $stats.Average | Should -Be 18.33
        $stats.Min | Should -Be 10.0
        $stats.Max | Should -Be 25.0
    }

    # TEST: Merge-Hashtables
    It "Merge-Hashtables verschmilzt zwei Hashtables und überschreibt Duplikate" {
        $baseConfig = @{
            Port    = 80
            Host    = "localhost"
            Timeout = 30
        }
        $overrideConfig = @{
            Port = 443
            SSL  = $true
        }
        $merged = Merge-Hashtables -Primary $baseConfig -Secondary $overrideConfig
        $merged["Port"] | Should -Be 443
        $merged["Host"] | Should -Be "localhost"
        $merged["Timeout"] | Should -Be 30
        $merged["SSL"] | Should -Be $true
    }
}

Write-Host "✅ Alle Tests in PS 04 erfolgreich bestanden!" -ForegroundColor Green
