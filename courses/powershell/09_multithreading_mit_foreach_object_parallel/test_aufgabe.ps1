# 🧪 PS 09: Pester v5 Test-Suite für Multithreading mit ForEach-Object -Parallel

Describe 'PS 09: Multithreading & Concurrency' {
    BeforeAll {
        . $PSScriptRoot/aufgabe.ps1
    }

    Context 'TODO 1: Invoke-ParallelPing' {
        # TEST: 1.1 Parallel Ping auf mehrere Hosts
        It 'Sollte ein Array von Objekten für alle übergebenen Hosts zurückgeben' {
            $hosts = @('srv-app01', 'srv-db01', 'srv-backup')
            $result = Invoke-ParallelPing -ComputerNames $hosts -ThrottleLimit 3
            
            $result.Count | Should -Be 3
            $result[0].ComputerName | Should -Be 'srv-app01'
        }

        # TEST: 1.2 Status und Timestamp Prüfung
        It 'Sollte für erreichbare Hosts Status Online und Timestamp liefern' {
            $result = Invoke-ParallelPing -ComputerNames @('srv-web01') -TimeoutMs 500
            
            $result[0].Status | Should -Be 'Online'
            $result[0].ResponseTimeMs | Should -BeGreaterThan 0
            $result[0].Timestamp | Should -Not -BeNullOrEmpty
        }

        # TEST: 1.3 Offline-Erkennung
        It 'Sollte für offline Hosts den Status Offline erkennen' {
            $result = Invoke-ParallelPing -ComputerNames @('srv-down-node') -TimeoutMs 200
            
            $result[0].Status | Should -Be 'Offline'
            $result[0].ResponseTimeMs | Should -Be -1
        }
    }

    Context 'TODO 2: Start-AsyncServerTask' {
        # TEST: 2.1 Starten eines asynchronen Tasks
        It 'Sollte einen Thread-Job erfolgreich starten und ein Job-Objekt liefern' {
            $job = Start-AsyncServerTask -TaskName 'TestJob1' -ScriptBlock {
                param($val)
                Start-Sleep -Milliseconds 100
                "JobOutput: $val"
            } -ArgumentList @('HelloWorld')

            $job | Should -Not -BeNullOrEmpty
            $job.Name | Should -Be 'TestJob1'
            $job.Id | Should -BeGreaterThan 0

            # Cleanup
            $null = Wait-Job -Job $job -Timeout 5 -ErrorAction SilentlyContinue
            $null = Receive-Job -Job $job -ErrorAction SilentlyContinue
            Remove-Job -Job $job -Force -ErrorAction SilentlyContinue
        }
    }

    Context 'TODO 3: Wait-AndCollectThreadJobs' {
        # TEST: 3.1 Jobs einsammeln und bereinigen
        It 'Sollte Job-Ergebnisse einsammeln und Jobs sauber entfernen' {
            $job1 = Start-Job -Name 'CollectTest1' -ScriptBlock { 'Result-A' }
            $job2 = Start-Job -Name 'CollectTest2' -ScriptBlock { 'Result-B' }

            $results = Wait-AndCollectThreadJobs -Jobs @($job1, $job2) -TimeoutSeconds 5

            $results | Should -Contain 'Result-A'
            $results | Should -Contain 'Result-B'

            # Überprüfen ob Job entfernt wurde
            $leftover = Get-Job -Name 'CollectTest1' -ErrorAction SilentlyContinue
            $leftover | Should -BeNullOrEmpty
        }
    }

    Context 'TODO 4: Invoke-ThrottledBatchProcessing' {
        # TEST: 4.1 Batchverarbeitung mit Drosselung und Metriken
        It 'Sollte TotalItems, ProcessedItems und SuccessCount korrekt berechnen' {
            $items = @(1, 2, 3, 4)
            $batch = Invoke-ThrottledBatchProcessing -Items $items -ThrottleLimit 2 -ProcessBlock {
                param($num)
                [PSCustomObject]@{
                    Item    = $num
                    Success = ($num % 2 -eq 0)
                    Status  = if ($num % 2 -eq 0) { 'OK' } else { 'Fail' }
                }
            }

            $batch | Should -Not -BeNullOrEmpty
            $batch.TotalItems | Should -Be 4
            $batch.ProcessedItems.Count | Should -Be 4
            $batch.SuccessCount | Should -Be 2
            $batch.DurationMs | Should -BeGreaterOrEqual 0
        }
    }
}
