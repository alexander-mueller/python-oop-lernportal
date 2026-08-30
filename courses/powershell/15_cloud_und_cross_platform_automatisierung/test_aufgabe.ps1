# 🧪 PS 15: Pester v5 Test-Suite für Cross-Platform Cloud Automation

Describe 'PS 15: Cloud & Cross-Platform Automation' {
    BeforeAll {
        . $PSScriptRoot/aufgabe.ps1
    }

    Context 'TODO 1: Get-PlatformDiagnostics' {
        # TEST: 1.1 Plattform-Diagnose
        It 'Sollte Plattform, Pfadtrennzeichen und CoreCLR ermitteln' {
            $diag = Get-PlatformDiagnostics
            
            $diag | Should -Not -BeNullOrEmpty
            $diag.Platform | Should -BeIn @('Linux', 'Windows', 'macOS')
            $diag.PathSeparator | Should -BeIn @('/', '\')
            $diag.PSVersion | Should -Not -BeNullOrEmpty
        }
    }

    Context 'TODO 2: New-IdempotentResourceConfig' {
        # TEST: 2.1 Governance-Tagging für Cloud-Ressourcen
        It 'Sollte Standard-Governance-Tags und ResourceId erstellen' {
            $cfg = New-IdempotentResourceConfig -ResourceName 'app-vm-01' -ResourceType 'Microsoft.Compute/virtualMachines' -Location 'westeurope' -CustomTags @{ CostCenter = 'DevOps-99' }
            
            $cfg.Name | Should -Be 'app-vm-01'
            $cfg.Location | Should -Be 'westeurope'
            $cfg.Tags['Environment'] | Should -Be 'Production'
            $cfg.Tags['ManagedBy'] | Should -Be 'PowerShellAutomation'
            $cfg.Tags['CostCenter'] | Should -Be 'DevOps-99'
            $cfg.ResourceId | Should -Match 'Microsoft.Compute/virtualMachines/app-vm-01'
        }
    }

    Context 'TODO 3: Convert-AwsCliOutputToPsObject' {
        # TEST: 3.1 EC2 Instanz-Parsing
        It 'Sollte EC2 AWS CLI JSON-Outputs in PowerShell-Objekte normalisieren' {
            $awsEc2Json = @'
{
  "Reservations": [
    {
      "Instances": [
        {
          "InstanceId": "i-0abcdef1234567890",
          "InstanceType": "t3.medium",
          "State": { "Name": "running" },
          "Tags": [{ "Key": "Name", "Value": "ProdWorker" }]
        }
      ]
    }
  ]
}
'@
            $parsed = Convert-AwsCliOutputToPsObject -AwsJsonOutput $awsEc2Json
            $parsed.Count | Should -Be 1
            $parsed[0].Id | Should -Be 'i-0abcdef1234567890'
            $parsed[0].Type | Should -Be 't3.medium'
            $parsed[0].State | Should -Be 'running'
        }
    }

    Context 'TODO 4: Audit-CloudResourceCompliance' {
        # TEST: 4.1 Cloud Compliance & Governance Audit
        It 'Sollte Compliance-Regeln prüfen und Verstöße erkennen' {
            $resources = @(
                [PSCustomObject]@{
                    Name     = 'compliant-vm'
                    Location = 'westeurope'
                    Tags     = @{ Environment = 'Production'; ManagedBy = 'PowerShellAutomation' }
                },
                [PSCustomObject]@{
                    Name     = 'rogue-storage'
                    Location = 'eastus' # Verbotene Region
                    Tags     = @{ Environment = 'Production' } # ManagedBy fehlt!
                }
            )

            $audit = Audit-CloudResourceCompliance -Resources $resources -MandatoryTags @('Environment', 'ManagedBy') -AllowedLocations @('westeurope', 'germanywestcentral')
            
            $audit.TotalAudited | Should -Be 2
            $audit.CompliantCount | Should -Be 1
            $audit.NonCompliantCount | Should -Be 1
            $audit.Violations.Count | Should -Be 2 # 1x MissingTag, 1x InvalidLocation
        }
    }
}
