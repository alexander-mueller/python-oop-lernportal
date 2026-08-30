# 🧪 PS 13: Pester v5 Test-Suite für Modul-Entwicklung & Manifeste

Describe 'PS 13: Enterprise Modules & Manifests' {
    BeforeAll {
        . $PSScriptRoot/aufgabe.ps1
        
        $tempModBase = Join-Path $TestDrive "ps13_modules_test"
        if (-not (Test-Path $tempModBase)) {
            New-Item -ItemType Directory -Path $tempModBase -Force | Out-Null
        }
    }

    Context 'TODO 1: New-ModuleStructure' {
        # TEST: 1.1 Modul-Ordnerstruktur anlegen
        It 'Sollte die Standard-Ordnerstruktur und Manifest-Dateien anlegen' {
            $modRes = New-ModuleStructure -DestinationPath $tempModBase -ModuleName 'CloudToolkit'
            
            $modRes | Should -Not -BeNullOrEmpty
            $modRes.HasPublic | Should -BeTrue
            $modRes.HasPrivate | Should -BeTrue
            $modRes.HasTests | Should -BeTrue
            Test-Path (Join-Path $modRes.ModulePath "CloudToolkit.psm1") | Should -BeTrue
            Test-Path (Join-Path $modRes.ModulePath "CloudToolkit.psd1") | Should -BeTrue
        }
    }

    Context 'TODO 2: Build-ModuleManifestContent' {
        # TEST: 2.1 PSD1 Manifest String Generierung
        It 'Sollte ein valides PowerShell .psd1 Manifest mit Metadaten generieren' {
            $psd1 = Build-ModuleManifestContent -ModuleName 'AzHelper' -Version '2.1.0' -Author 'Lead DevOps' -FunctionsToExport @('Get-AzAudit', 'Set-AzTag')
            
            $psd1 | Should -Match "RootModule\s*=\s*'AzHelper.psm1'"
            $psd1 | Should -Match "ModuleVersion\s*=\s*'2.1.0'"
            $psd1 | Should -Match "Author\s*=\s*'Lead DevOps'"
            $psd1 | Should -Match "Get-AzAudit"
            $psd1 | Should -Match "GUID\s*=\s*'[a-f0-9\-]+'"
        }
    }

    Context 'TODO 3: Invoke-ModuleLoader' {
        # TEST: 3.1 Dynamischer Modul-Loader
        It 'Sollte Public und Private Skripte laden und nur Public exportieren' {
            $loaderTestDir = Join-Path $tempModBase "LoaderTestModule"
            $null = New-ModuleStructure -DestinationPath $tempModBase -ModuleName "LoaderTestModule"
            
            # Private Skript anlegen
            $privFile = Join-Path $loaderTestDir "Private/Format-InternalKey.ps1"
            Set-Content -Path $privFile -Value 'function Format-InternalKey { "InternalKey" }'

            # Public Skript anlegen
            $pubFile = Join-Path $loaderTestDir "Public/Get-PublicStatus.ps1"
            Set-Content -Path $pubFile -Value 'function Get-PublicStatus { Format-InternalKey }'

            $exported = Invoke-ModuleLoader -ModuleRootPath $loaderTestDir
            $exported | Should -Contain "Get-PublicStatus"
            $exported | Should -Not -Contain "Format-InternalKey"
        }
    }

    Context 'TODO 4: Test-ModuleCompliance' {
        # TEST: 4.1 Compliance Prüfung für vollständiges Modul
        It 'Sollte ein vollständiges Modul als IsCompliant=$true einstufen' {
            $compTestDir = Join-Path $tempModBase "CompliantMod"
            $null = New-ModuleStructure -DestinationPath $tempModBase -ModuleName "CompliantMod"
            
            $psd1Path = Join-Path $compTestDir "CompliantMod.psd1"
            Set-Content -Path $psd1Path -Value "@{ ModuleVersion = '3.0.0' }"

            $check = Test-ModuleCompliance -ModulePath $compTestDir
            $check.IsCompliant | Should -BeTrue
            $check.MissingItems.Count | Should -Be 0
            $check.Version | Should -Be '3.0.0'
        }

        # TEST: 4.2 Fehlererkennung bei unvollständigem Modul
        It 'Sollte fehlende Elemente präzise in MissingItems auflisten' {
            $brokenDir = Join-Path $tempModBase "BrokenMod"
            New-Item -ItemType Directory -Path $brokenDir -Force | Out-Null
            
            $checkBroken = Test-ModuleCompliance -ModulePath $brokenDir
            $checkBroken.IsCompliant | Should -BeFalse
            $checkBroken.MissingItems.Count | Should -BeGreaterThan 0
        }
    }
}
