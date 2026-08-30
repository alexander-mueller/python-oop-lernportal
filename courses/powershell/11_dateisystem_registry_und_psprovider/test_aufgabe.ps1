# 🧪 PS 11: Pester v5 Test-Suite für PSDrives, Dateisystem & Hashes

Describe 'PS 11: File System, PSDrives & Cryptographic Hashes' {
    BeforeAll {
        . $PSScriptRoot/aufgabe.ps1
        
        # Test-Verzeichnis vorbereiten
        $testDir = Join-Path $TestDrive "ps11_test_workspace"
        if (-not (Test-Path $testDir)) {
            New-Item -ItemType Directory -Path $testDir -Force | Out-Null
        }
        $testFileA = Join-Path $testDir "config.json"
        $testFileB = Join-Path $testDir "script.ps1"
        
        Set-Content -Path $testFileA -Value '{"status": "active"}'
        Set-Content -Path $testFileB -Value 'Write-Host "Hello PS11"'
    }

    Context 'TODO 1: Get-EnvironmentReport' {
        # TEST: 1.1 Abfrage des Env:-Laufwerks
        It 'Sollte Umgebungsvariablen aus dem Env: Provider abrufen' {
            $envReport = Get-EnvironmentReport -FilterPatterns @('PATH*', 'USER*')
            $envReport | Should -Not -BeNullOrEmpty
            $envReport[0].VariableName | Should -Not -BeNullOrEmpty
            $envReport[0].Length | Should -BeGreaterOrEqual 0
        }
    }

    Context 'TODO 2: Get-DirectoryFileInventory' {
        # TEST: 2.1 Rekursives Dateiinventar mit SHA256
        It 'Sollte Dateien auflisten und Metadaten sowie SHA256 berechnen' {
            $inventory = Get-DirectoryFileInventory -Path $testDir -Extensions @('json', 'ps1') -CalculateHash $true
            
            $inventory.Count | Should -Be 2
            $jsonFile = $inventory | Where-Object { $_.Name -eq 'config.json' }
            $jsonFile | Should -Not -BeNullOrEmpty
            $jsonFile.Extension | Should -Be '.json'
            $jsonFile.SHA256 | Should -Match '^[A-F0-9]{64}$'
            $jsonFile.SizeKB | Should -BeGreaterOrEqual 0
        }
    }

    Context 'TODO 3: Test-FileIntegrity' {
        # TEST: 3.1 Hashprüfung bei valider Datei
        It 'Sollte Integrität bei passendem Hash als IsValid=$true bestätigen' {
            $realHash = (Get-FileHash -Path $testFileA -Algorithm SHA256).Hash
            $result = Test-FileIntegrity -FilePath $testFileA -ExpectedHash $realHash
            
            $result | Should -Not -BeNullOrEmpty
            $result.IsValid | Should -BeTrue
            $result.CalculatedHash | Should -Be $realHash.ToUpper()
        }

        # TEST: 3.2 Manipulation erkennen
        It 'Sollte Manipulation bei abweichendem Hash als IsValid=$false erkennen' {
            $fakeHash = "0000000000000000000000000000000000000000000000000000000000000000"
            $result = Test-FileIntegrity -FilePath $testFileA -ExpectedHash $fakeHash
            
            $result.IsValid | Should -BeFalse
        }
    }

    Context 'TODO 4: New-TemporaryMountDrive' {
        # TEST: 4.1 Temporäres PSDrive erstellen und aufräumen
        It 'Sollte ein temporäres PSDrive mounten und im Finally-Block unmounten' {
            $driveName = "TempTestDrive"
            $res = New-TemporaryMountDrive -DriveName $driveName -RootPath $testDir -Action {
                param($drv)
                Test-Path "$($drv):\"
            }

            $res | Should -BeTrue

            # Überprüfen ob das PSDrive wieder sauber entfernt wurde
            $leftoverDrive = Get-PSDrive -Name $driveName -ErrorAction SilentlyContinue
            $leftoverDrive | Should -BeNullOrEmpty
        }
    }
}
