# 🧪 Pester v5 Testsuite: PS 03 - Where-Object, Select & Calculated Properties

Describe "PS 03: Where-Object, Select & Calculated Properties" {
    # TEST: Filter-ActiveServices
    It "Filter-ActiveServices filtert nur laufende Dienste heraus" {
        $services = @(
            [PSCustomObject]@{ Name = "wuauserv"; Status = "Stopped" },
            [PSCustomObject]@{ Name = "spooler"; Status = "Running" },
            [PSCustomObject]@{ Name = "sshd"; Status = "Running" }
        )
        $running = Filter-ActiveServices -Services $services
        $running.Count | Should -Be 2
        $running[0].Name | Should -Be "spooler"
        $running[1].Name | Should -Be "sshd"
    }

    # TEST: Filter-ActiveServices mit leerer Eingabe
    It "Filter-ActiveServices liefert leeres Array bei leerer Eingabe" {
        $running = Filter-ActiveServices -Services @()
        $running.Count | Should -Be 0
    }

    # TEST: Select-ProcessSummary mit Calculated Property
    It "Select-ProcessSummary projiziert Id, Name und berechneten MemoryMB-Wert" {
        $procs = @(
            [PSCustomObject]@{ Id = 1001; Name = "pwsh"; WorkingSet = 104857600 },
            [PSCustomObject]@{ Id = 1002; Name = "code"; WorkingSet = 209715200 }
        )
        $summary = Select-ProcessSummary -Processes $procs
        $summary.Count | Should -Be 2
        $summary[0].Id | Should -Be 1001
        $summary[0].Name | Should -Be "pwsh"
        $summary[0].MemoryMB | Should -Be 100.0
        $summary[1].MemoryMB | Should -Be 200.0
    }

    # TEST: Sort-EmployeeList mehrstufig
    It "Sort-EmployeeList sortiert primär absteigend nach Gehalt, sekundär nach Nachname" {
        $employees = @(
            [PSCustomObject]@{ FirstName = "Anna"; LastName = "Meier"; Salary = 50000 },
            [PSCustomObject]@{ FirstName = "Ben"; LastName = "Schmidt"; Salary = 80000 },
            [PSCustomObject]@{ FirstName = "Clara"; LastName = "Becker"; Salary = 80000 },
            [PSCustomObject]@{ FirstName = "David"; LastName = "Althaus"; Salary = 40000 }
        )
        $sorted = Sort-EmployeeList -Employees $employees
        $sorted[0].LastName | Should -Be "Becker"
        $sorted[0].Salary | Should -Be 80000
        $sorted[1].LastName | Should -Be "Schmidt"
        $sorted[1].Salary | Should -Be 80000
        $sorted[2].LastName | Should -Be "Meier"
        $sorted[3].LastName | Should -Be "Althaus"
    }

    # TEST: Group-LogEntriesBySeverity
    It "Group-LogEntriesBySeverity erzeugt korrekte Zählerstände im Hashtable" {
        $logs = @(
            [PSCustomObject]@{ Timestamp = "10:00"; Severity = "INFO"; Message = "Booted" },
            [PSCustomObject]@{ Timestamp = "10:01"; Severity = "WARN"; Message = "High CPU" },
            [PSCustomObject]@{ Timestamp = "10:02"; Severity = "INFO"; Message = "Heartbeat" },
            [PSCustomObject]@{ Timestamp = "10:03"; Severity = "ERROR"; Message = "Disk Full" },
            [PSCustomObject]@{ Timestamp = "10:04"; Severity = "INFO"; Message = "Done" }
        )
        $grouped = Group-LogEntriesBySeverity -LogEntries $logs
        $grouped["INFO"] | Should -Be 3
        $grouped["WARN"] | Should -Be 1
        $grouped["ERROR"] | Should -Be 1
    }
}

Write-Host "✅ Alle Tests in PS 03 erfolgreich bestanden!" -ForegroundColor Green
