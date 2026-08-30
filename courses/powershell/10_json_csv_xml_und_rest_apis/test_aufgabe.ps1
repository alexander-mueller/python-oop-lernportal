# 🧪 PS 10: Pester v5 Test-Suite für JSON, CSV, XML & REST APIs

Describe 'PS 10: REST APIs & Data Pipelines' {
    BeforeAll {
        . $PSScriptRoot/aufgabe.ps1
    }

    Context 'TODO 1: Get-RestApiData' {
        # TEST: 1.1 REST Request mit Mocking
        It 'Sollte Invoke-RestMethod mit URI und Bearer-Header aufrufen' {
            Mock Invoke-RestMethod {
                return [PSCustomObject]@{
                    status  = 'success'
                    nodeCount = 5
                }
            } -ParameterFilter { $Uri -eq 'https://api.cloudops.internal/v1/nodes' -and $Headers['Authorization'] -eq 'Bearer secret-token-123' }

            $res = Get-RestApiData -Uri 'https://api.cloudops.internal/v1/nodes' -BearerToken 'secret-token-123'
            $res.status | Should -Be 'success'
            $res.nodeCount | Should -Be 5
        }
    }

    Context 'TODO 2: Convert-JsonToCsvReport' {
        # TEST: 2.1 JSON zu CSV Transformation
        It 'Sollte JSON in CSV ohne Typinformationen und mit Delimiter konvertieren' {
            $jsonInput = @'
[
  {"Host": "srv01", "IP": "10.0.0.1", "Role": "Web"},
  {"Host": "srv02", "IP": "10.0.0.2", "Role": "DB"}
]
'@
            $csv = Convert-JsonToCsvReport -JsonString $jsonInput -SelectedProperties @('Host', 'IP') -Delimiter ';'

            $csv | Should -Not -BeNullOrEmpty
            # Keine #TYPE Header-Zeile
            ($csv | Where-Object { $_ -match '^#TYPE' }) | Should -BeNullOrEmpty
            # Enthält Header mit Delimiter
            $csv[0] | Should -Match 'Host;IP'
            # Enthält Datenzeilen
            $csv[1] | Should -Match 'srv01;10.0.0.1'
        }
    }

    Context 'TODO 3: Format-DeepNestedConfig' {
        # TEST: 3.1 Tiefe JSON Serialisierung mit -Depth
        It 'Sollte tief verschachtelte Strukturen mit -Depth serialisieren und validieren' {
            $deepObject = @{
                cluster = @{
                    name = "K8s-Prod"
                    network = @{
                        subnet = @{
                            cidr = "10.244.0.0/16"
                            gateway = @{
                                ip = "10.244.0.1"
                                dns = @{
                                    primary = "1.1.1.1"
                                    secondary = "8.8.8.8"
                                }
                            }
                        }
                    }
                }
            }

            $result = Format-DeepNestedConfig -ConfigObject $deepObject -Depth 10
            $result | Should -Not -BeNullOrEmpty
            $result.IsValid | Should -BeTrue
            $result.JsonString | Should -Match 'primary'
            $result.ParsedBack.cluster.network.subnet.gateway.dns.primary | Should -Be '1.1.1.1'
        }
    }

    Context 'TODO 4: Parse-XmlServerManifest' {
        # TEST: 4.1 XML Parsing von Server-Manifesten
        It 'Sollte XML-Serverdefinitionen in strukturierte PSCustomObjects parsen' {
            $xmlSample = @'
<infrastructure environment="production">
  <servers>
    <server name="app-node-01" role="Frontend"><port>443</port></server>
    <server name="db-primary" role="Database"><port>5432</port></server>
  </servers>
</infrastructure>
'@
            $servers = Parse-XmlServerManifest -XmlContent $xmlSample
            $servers.Count | Should -Be 2
            $servers[0].Name | Should -Be 'app-node-01'
            $servers[0].Role | Should -Be 'Frontend'
            $servers[0].Port | Should -Be 443
            $servers[0].Environment | Should -Be 'production'
            $servers[1].Name | Should -Be 'db-primary'
            $servers[1].Port | Should -Be 5432
        }
    }
}
