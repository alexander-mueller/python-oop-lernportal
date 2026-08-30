# 🧪 Master 16: Pester v5 Test-Suite für Multi-Threaded Cloud Ops Engine

Describe 'Master 16: Cloud Ops Engine' {
    BeforeAll {
        . $PSScriptRoot/aufgabe.ps1
        
        $testExportDir = Join-Path $TestDrive "ps16_engine_reports"
        if (-not (Test-Path $testExportDir)) {
            New-Item -ItemType Directory -Path $testExportDir -Force | Out-Null
        }
    }

    Context 'TODO 1: New-CloudOpsNode' {
        # TEST: 1.1 Node Factory
        It 'Sollte ein valides Node-Objekt mit Thresholds initialisieren' {
            $node = New-CloudOpsNode -Name 'az-app-01' -IpAddress '10.2.0.4' -Role 'Backend' -Provider 'Azure' -CpuThreshold 75 -MemoryThreshold 80
            
            $node | Should -Not -BeNullOrEmpty
            $node.Name | Should -Be 'az-app-01'
            $node.IpAddress | Should -Be '10.2.0.4'
            $node.Role | Should -Be 'Backend'
            $node.Provider | Should -Be 'Azure'
            $node.CpuThreshold | Should -Be 75
            $node.MemoryThreshold | Should -Be 80
        }
    }

    Context 'TODO 2: Invoke-NodeAuditParallel' {
        # TEST: 2.1 Paralleles Audit über mehrere Knoten
        It 'Sollte parallele Audits durchführen und Gesundheitsstatus ermitteln' {
            $nodes = @(
                (New-CloudOpsNode -Name 'node-ok-01' -IpAddress '10.0.1.1' -Role 'Web'),
                (New-CloudOpsNode -Name 'node-high-cpu-02' -IpAddress '10.0.1.2' -Role 'Worker' -CpuThreshold 70),
                (New-CloudOpsNode -Name 'node-down-03' -IpAddress '10.0.1.3' -Role 'DB')
            )

            $results = Invoke-NodeAuditParallel -Nodes $nodes -ThrottleLimit 3
            
            $results.Count | Should -Be 3
            ($results | Where-Object { $_.NodeName -eq 'node-ok-01' }).HealthStatus | Should -Be 'Healthy'
            ($results | Where-Object { $_.NodeName -eq 'node-high-cpu-02' }).HealthStatus | Should -Be 'Warning'
            ($results | Where-Object { $_.NodeName -eq 'node-down-03' }).HealthStatus | Should -Be 'Critical'
        }
    }

    Context 'TODO 3: New-CloudOpsReport' {
        # TEST: 3.1 Aggregation in Master Report
        It 'Sollte Gesamtmetriken und ComplianceScore präzise berechnen' {
            $mockAuditResults = @(
                [PSCustomObject]@{ NodeName = 'n1'; HealthStatus = 'Healthy' },
                [PSCustomObject]@{ NodeName = 'n2'; HealthStatus = 'Healthy' },
                [PSCustomObject]@{ NodeName = 'n3'; HealthStatus = 'Warning' },
                [PSCustomObject]@{ NodeName = 'n4'; HealthStatus = 'Critical' }
            )

            $report = New-CloudOpsReport -AuditResults $mockAuditResults
            
            $report.TotalNodes | Should -Be 4
            $report.HealthyNodes | Should -Be 2
            $report.WarningNodes | Should -Be 1
            $report.CriticalNodes | Should -Be 1
            $report.ComplianceScore | Should -Be 50.0
            $report.GeneratedAt | Should -Not -BeNullOrEmpty
            $report.Findings.Count | Should -Be 4
        }
    }

    Context 'TODO 4: Export-CloudOpsJsonReport' {
        # TEST: 4.1 JSON Export mit SHA256 Signatur
        It 'Sollte den Report als JSON speichern und mit SHA256 signieren' {
            $sampleReport = [PSCustomObject]@{
                Title           = 'Weekly Cloud Ops Audit'
                ComplianceScore = 95.5
                CriticalNodes   = 0
            }
            $outFile = Join-Path $testExportDir "audit_report.json"

            $exportRes = Export-CloudOpsJsonReport -Report $sampleReport -OutputPath $outFile
            
            $exportRes | Should -Not -BeNullOrEmpty
            Test-Path $exportRes.FilePath | Should -BeTrue
            $exportRes.SizeBytes | Should -BeGreaterThan 0
            $exportRes.Sha256 | Should -Match '^[A-F0-9]{64}$'
        }
    }

    Context 'TODO 5: Send-CloudOpsAlertWebhook' {
        # TEST: 5.1 Webhook Dispatch
        It 'Sollte Webhook-Payload formatieren und Dispatched Status zurückgeben' {
            $sampleReport = [PSCustomObject]@{ ComplianceScore = 60.0; CriticalNodes = 2; WarningNodes = 1 }
            
            Mock Invoke-RestMethod { [PSCustomObject]@{ status = 'received' } }

            $dispatch = Send-CloudOpsAlertWebhook -WebhookUrl 'https://hooks.slack.com/services/test' -Report $sampleReport
            
            $dispatch.Success | Should -BeTrue
            $dispatch.Status | Should -Be 'Dispatched'
            $dispatch.WebhookUrl | Should -Be 'https://hooks.slack.com/services/test'
        }
    }
}
