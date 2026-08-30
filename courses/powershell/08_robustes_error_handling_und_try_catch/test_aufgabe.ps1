# 🧪 Pester v5 Testsuite: PS 08 - Robustes Error-Handling (Try/Catch/Finally)

Describe "PS 08: Robustes Error-Handling (Try/Catch/Finally)" {
    # TEST: Read-SafeConfiguration bei nicht existierender Datei
    It "Read-SafeConfiguration fängt Fehler bei fehlenden Dateien sicher ab" {
        $result = Read-SafeConfiguration -Path "non_existing_file_998877.txt"
        $result.Success | Should -Be $false
        $result.ErrorMessage | Should -Not -BeNullOrEmpty
        $result.Content | Should -Be ""
    }

    # TEST: Invoke-SafeDivision bei normaler Berechnung
    It "Invoke-SafeDivision führt gültige Divisionen korrekt aus" {
        $div = Invoke-SafeDivision -Numerator 100 -Denominator 4
        $div.Result | Should -Be 25.0
        $div.HasError | Should -Be $false
        $div.ErrorMessage | Should -Be ""
    }

    # TEST: Invoke-SafeDivision bei Division durch 0
    It "Invoke-SafeDivision fängt Division durch 0 mit sauberer Fehlermeldung ab" {
        $div0 = Invoke-SafeDivision -Numerator 50 -Denominator 0
        $div0.HasError | Should -Be $true
        $div0.ErrorMessage | Should -Contain "Division by zero"
    }

    # TEST: Invoke-TransactionalTask Erfolgsfall
    It "Invoke-TransactionalTask schließt erfolgreich ab und gibt Ressource frei" {
        $task1 = Invoke-TransactionalTask -ShouldFail $false
        $task1.Completed | Should -Be $true
        $task1.CleanupDone | Should -Be $true
        $Global:ResourceLocked | Should -Be $false
    }

    # TEST: Invoke-TransactionalTask Fehlerfall mit Cleanup
    It "Invoke-TransactionalTask gibt Ressource im Finally-Block auch bei Fehler frei" {
        $task2 = Invoke-TransactionalTask -ShouldFail $true
        $task2.Completed | Should -Be $false
        $task2.CleanupDone | Should -Be $true
        $Global:ResourceLocked | Should -Be $false
    }

    # TEST: Format-DetailedErrorRecord
    It "Format-DetailedErrorRecord erzeugt einen strukturierten Fehlerbericht" {
        $ex = [System.InvalidOperationException]::new("Ungültiger Vorgang")
        $report = Format-DetailedErrorRecord -ExceptionObj $ex
        $report.ErrorMessage | Should -Be "Ungültiger Vorgang"
        $report.ExceptionType | Should -Be "System.InvalidOperationException"
        $report.Success | Should -Be $false
        $report.Timestamp | Should -Not -BeNullOrEmpty
    }
}

Write-Host "✅ Alle Tests in PS 08 erfolgreich bestanden!" -ForegroundColor Green
