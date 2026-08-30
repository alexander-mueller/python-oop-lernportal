# 🧪 Pester v5 Testsuite: PS 02 - Die Objekt-Pipeline & Get-Member

Describe "PS 02: Die Objekt-Pipeline & Get-Member" {
    # TEST: Get-ObjectPropertyNames mit PSCustomObject
    It "Get-ObjectPropertyNames extrahiert alle Namen aus einem PSCustomObject" {
        $sampleObj = [PSCustomObject]@{
            Id   = 101
            Name = "WebService"
            Port = 8080
        }
        $names = Get-ObjectPropertyNames -InputObject $sampleObj
        $names | Should -Contain "Id"
        $names | Should -Contain "Name"
        $names | Should -Contain "Port"
    }

    # TEST: Get-ObjectPropertyNames mit Null
    It "Get-ObjectPropertyNames gibt bei Null ein leeres Array zurück" {
        $names = Get-ObjectPropertyNames -InputObject $null
        $names.Count | Should -Be 0
    }

    # TEST: Invoke-StringSanitization
    It "Invoke-StringSanitization bereinigt Strings korrekt mit Methodenverkettung" {
        $result = Invoke-StringSanitization -RawString "   azure virtual machine   "
        $result | Should -Be "AZURE-VIRTUAL-MACHINE"
    }

    # TEST: Invoke-StringSanitization mit Leerstring
    It "Invoke-StringSanitization liefert Leerstring bei leerer Eingabe" {
        $result = Invoke-StringSanitization -RawString ""
        $result | Should -Be ""
    }

    # TEST: Get-ProcessMemoryInMB
    It "Get-ProcessMemoryInMB rechnet 104857600 Bytes korrekt in 100.0 MB um" {
        $mb = Get-ProcessMemoryInMB -Bytes 104857600
        $mb | Should -Be 100.0
    }

    # TEST: Get-ProcessMemoryInMB mit Rundung
    It "Get-ProcessMemoryInMB rundet auf 2 Nachkommastellen" {
        $mb = Get-ProcessMemoryInMB -Bytes 157286400
        $mb | Should -Be 150.0
        
        $mbKrumm = Get-ProcessMemoryInMB -Bytes 123456789
        $mbKrumm | Should -Be 117.74
    }

    # TEST: Get-DotNetTypeInfo
    It "Get-DotNetTypeInfo liefert Typ-Metadaten für Strings" {
        $info = Get-DotNetTypeInfo -TargetObject "TestString"
        $info.TypeName | Should -Be "System.String"
        $info.IsValueType | Should -Be $false
        $info.BaseType | Should -Be "Object"
    }

    # TEST: Get-DotNetTypeInfo für ValueType (Int32)
    It "Get-DotNetTypeInfo erkennt Integer als ValueType" {
        $info = Get-DotNetTypeInfo -TargetObject 42
        $info.TypeName | Should -Be "System.Int32"
        $info.IsValueType | Should -Be $true
    }
}

Write-Host "✅ Alle Tests in PS 02 erfolgreich bestanden!" -ForegroundColor Green
