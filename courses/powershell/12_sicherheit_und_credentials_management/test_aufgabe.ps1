# 🧪 PS 12: Pester v5 Test-Suite für Sicherheit & Credentials Management

Describe 'PS 12: Security & Credentials Management' {
    BeforeAll {
        . $PSScriptRoot/aufgabe.ps1
    }

    Context 'TODO 1: New-SecureCredentials' {
        # TEST: 1.1 PSCredential Erstellung mit SecureString
        It 'Sollte ein PSCredential-Objekt mit verschlüsseltem Passwort erstellen' {
            $cred = New-SecureCredentials -UserName 'cloudadmin' -PlainTextPassword 'SuperSecretPass123!'
            
            $cred | Should -Not -BeNullOrEmpty
            $cred.UserName | Should -Be 'cloudadmin'
            $cred.Password | Should -BeOfType [System.Security.SecureString]
            $cred.GetNetworkCredential().Password | Should -Be 'SuperSecretPass123!'
        }
    }

    Context 'TODO 2: Protect-SensitiveString & Unprotect-SensitiveString' {
        # TEST: 2.1 Roundtrip-Verschlüsselung
        It 'Sollte einen String verschlüsseln und verlustfrei wieder entschlüsseln' {
            $originalText = "ApiToken_Prod_9988776655"
            $encrypted = Protect-SensitiveString -PlainText $originalText
            
            $encrypted | Should -Not -BeNullOrEmpty
            $encrypted | Should -Not -Be $originalText
            
            $decrypted = Unprotect-SensitiveString -EncryptedString $encrypted
            $decrypted | Should -Be $originalText
        }
    }

    Context 'TODO 3: Get-SecurityAuditReport' {
        # TEST: 3.1 Sicherheits-Audit Report
        It 'Sollte LanguageMode, Policy und SecurityScore im Audit-Report liefern' {
            $report = Get-SecurityAuditReport
            
            $report | Should -Not -BeNullOrEmpty
            $report.LanguageMode | Should -Not -BeNullOrEmpty
            $report.ExecutionPolicy | Should -Not -BeNullOrEmpty
            $report.SecurityScore | Should -BeGreaterOrEqual 0
            $report.SecurityScore | Should -BeLessOrEqual 100
        }
    }

    Context 'TODO 4: Invoke-SecretVaultSimulation' {
        # TEST: 4.1 Secret Vault Lifecycle (Set, List, Get, Remove)
        It 'Sollte Secrets verschlüsselt speichern (Set), listen, abrufen und löschen' {
            $vault = @{}

            # 1. Set
            $setRes = Invoke-SecretVaultSimulation -Action 'Set' -SecretName 'DbPassword' -SecretValue 'P@ssword99!' -VaultStorage $vault
            $setRes | Should -BeTrue
            # Der gespeicherte Wert im Storage darf nicht Klartext sein
            $vault['DbPassword'] | Should -Not -Be 'P@ssword99!'

            # 2. List
            $keys = Invoke-SecretVaultSimulation -Action 'List' -VaultStorage $vault
            $keys | Should -Contain 'DbPassword'

            # 3. Get
            $val = Invoke-SecretVaultSimulation -Action 'Get' -SecretName 'DbPassword' -VaultStorage $vault
            $val | Should -Be 'P@ssword99!'

            # 4. Remove
            $remRes = Invoke-SecretVaultSimulation -Action 'Remove' -SecretName 'DbPassword' -VaultStorage $vault
            $remRes | Should -BeTrue
            $vault.ContainsKey('DbPassword') | Should -BeFalse
        }
    }
}
