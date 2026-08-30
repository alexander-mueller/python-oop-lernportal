# 🧪 PS 14: Pester v5 Test-Suite für Automatisiertes Testing & Mocking

Describe 'PS 14: Pester v5 Testing Framework' {
    BeforeAll {
        . $PSScriptRoot/aufgabe.ps1
    }

    Context 'TODO 1: Get-ServerHealthStatus mit Mocking' {
        # TEST: 1.1 Gesunder Server Zustand
        It 'Sollte Operational und Code 200 liefern, wenn Dienst und Ping erfolgreich sind' {
            Mock Get-Service { [PSCustomObject]@{ Status = 'Running'; Name = 'AppService' } }
            Mock Test-Connection { $true }

            $status = Get-ServerHealthStatus -ServerName 'srv-web01' -ServiceName 'AppService'
            $status.IsHealthy | Should -BeTrue
            $status.Status | Should -Be 'Operational'
            $status.Code | Should -Be 200
        }

        # TEST: 1.2 Gestörter Server Zustand
        It 'Sollte Degraded und Code 500 liefern, wenn Dienst gestoppt ist' {
            Mock Get-Service { [PSCustomObject]@{ Status = 'Stopped'; Name = 'AppService' } }
            Mock Test-Connection { $true }

            $status = Get-ServerHealthStatus -ServerName 'srv-web01' -ServiceName 'AppService'
            $status.IsHealthy | Should -BeFalse
            $status.Status | Should -Be 'Degraded'
            $status.Code | Should -Be 500
        }
    }

    Context 'TODO 2: Restart-FailedService mit Retry & Exception Handling' {
        # TEST: 2.1 Bereits laufender Dienst
        It 'Sollte 0 Versuche benötigen, wenn Dienst bereits läuft' {
            Mock Get-Service { [PSCustomObject]@{ Status = 'Running'; Name = 'SqlService' } }
            
            $res = Restart-FailedService -ServiceName 'SqlService'
            $res.Success | Should -BeTrue
            $res.Attempts | Should -Be 0
        }

        # TEST: 2.2 Erfolgreicher Neustart nach Versuch
        It 'Sollte Restart-Service ausführen und Erfolg melden' {
            $state = [System.Collections.Generic.List[string]]::new(@('Stopped', 'Running'))
            Mock Get-Service {
                $cur = if ($state.Count -gt 0) { $state[0] } else { 'Running' }
                if ($state.Count -gt 0) { $state.RemoveAt(0) }
                [PSCustomObject]@{ Status = $cur; Name = 'TestSvc' }
            }
            Mock Restart-Service {}

            $res = Restart-FailedService -ServiceName 'TestSvc' -MaxRetries 3
            $res.Success | Should -BeTrue
            $res.Attempts | Should -Be 1
        }

        # TEST: 2.3 Exception nach MaxRetries
        It 'Sollte werfen, wenn Dienst nach MaxRetries nicht startet' {
            Mock Get-Service { [PSCustomObject]@{ Status = 'Stopped'; Name = 'DeadSvc' } }
            Mock Restart-Service {}

            { Restart-FailedService -ServiceName 'DeadSvc' -MaxRetries 2 } | Should -Throw
        }
    }

    Context 'TODO 3: Test-PesterResultAnalyzer' {
        # TEST: 3.1 100% Erfolgreiche Testsuite
        It 'Sollte PassRate 100% und IsProductionReady=$true berechnen' {
            $mockResult = [PSCustomObject]@{
                TotalCount  = 20
                PassedCount = 20
                FailedCount = 0
                Duration    = [TimeSpan]::FromSeconds(2.5)
            }

            $analysis = Test-PesterResultAnalyzer -PesterResult $mockResult
            $analysis.Total | Should -Be 20
            $analysis.Passed | Should -Be 20
            $analysis.PassRate | Should -Be 100.0
            $analysis.Status | Should -Be 'Passed'
            $analysis.IsProductionReady | Should -BeTrue
        }

        # TEST: 3.2 Testsuite mit Fehlern
        It 'Sollte Status Failed und IsProductionReady=$false bei Fehlern setzen' {
            $mockFailResult = [PSCustomObject]@{
                TotalCount  = 10
                PassedCount = 8
                FailedCount = 2
                Duration    = [TimeSpan]::FromSeconds(1.2)
            }

            $analysis = Test-PesterResultAnalyzer -PesterResult $mockFailResult
            $analysis.PassRate | Should -Be 80.0
            $analysis.Status | Should -Be 'Failed'
            $analysis.IsProductionReady | Should -BeFalse
        }
    }

    Context 'TODO 4: Invoke-MockableApiAudit' {
        # TEST: 4.1 API Audit mit Mocking
        It 'Sollte PayloadValid=$true für eine erfolgreiche API-Antwort ermitteln' {
            Mock Invoke-RestMethod {
                [PSCustomObject]@{ status = 'healthy'; version = '1.0.4' }
            }

            $audit = Invoke-MockableApiAudit -EndpointUrl 'https://api.internal/health'
            $audit.ResponseCode | Should -Be 200
            $audit.PayloadValid | Should -BeTrue
            $audit.AuditTime | Should -Not -BeNullOrEmpty
        }
    }
}
