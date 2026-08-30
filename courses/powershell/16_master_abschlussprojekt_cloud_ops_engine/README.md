# Master 16: Multi-Threaded Cloud Ops & Auditing Engine 🏆

Herzlichen Glückwunsch zum Erreichen des **Master-Abschlussprojekts** im modernen PowerShell 7+ DevOps-Kurs!

In diesem Meisterstück verbindest du alle fortgeschrittenen Disziplinen zu einer voll funktionsfähigen, mandantenfähigen **Cloud & Server Operations Engine**:
1. **Lehrpfad 1 & 2:** Typisierte Objekte, Pipeline-Streaming, erweitertes Error-Handling.
2. **Lehrpfad 3:** Paralleles Multithreading (`ForEach-Object -Parallel`), REST-APIs, SHA256-Prüfsummen und Secret-Management.
3. **Lehrpfad 4:** Enterprise-Architektur, Testbarkeit mit Pester v5 und Multi-Cloud Governance.

---

## 🏛️ Die Systemarchitektur der Cloud Ops Engine

```
                                [ Cloud Ops Engine Orchestrator ]
                                               │
               ┌───────────────────────────────┼───────────────────────────────┐
               ▼                               ▼                               ▼
    [ Azure Worker Nodes ]           [ AWS EC2 Instances ]          [ On-Premises Linux Hosts ]
               │                               │                               │
               └───────────────────────────────┼───────────────────────────────┘
                                               │
                                               ▼
                         ┌───────────────────────────────────────────┐
                         │  Invoke-NodeAuditParallel                 │
                         │  (ForEach-Object -Parallel, Throttle = 8) │
                         └───────────────────────────────────────────┘
                                               │
                                               ▼
                         ┌───────────────────────────────────────────┐
                         │  New-CloudOpsReport                       │
                         │  (Aggregation, Compliance-Score, Metrics) │
                         └───────────────────────────────────────────┘
                                               │
                        ┌──────────────────────┴──────────────────────┐
                        ▼                                             ▼
          [ Export-CloudOpsJsonReport ]                 [ Send-CloudOpsAlertWebhook ]
          (JSON -Depth 10 + SHA256 Hash)                (Slack/Teams/Discord Webhook Alert)
```

---

## 🎯 Aufgaben & Teilziele in `aufgabe.ps1`

1. **TODO 1: `New-CloudOpsNode`**  
   Node-Factory für Server- und Cloud-Knoten mit individuellen CPU-/Memory-Schwellenwerten.
2. **TODO 2: `Invoke-NodeAuditParallel`**  
   Parallele Abfrage von Ping, CPU, Memory und HealthStatus (`Healthy`, `Warning`, `Critical`) mit `ForEach-Object -Parallel`.
3. **TODO 3: `New-CloudOpsReport`**  
   Aggregieren aller Findings in einen Master-Report mit berechnetem `ComplianceScore` in %.
4. **TODO 4: `Export-CloudOpsJsonReport`**  
   Verlustfreier JSON-Export (`-Depth 10`) mit kryptografischem SHA256-Integritätsnachweis.
5. **TODO 5: `Send-CloudOpsAlertWebhook`**  
   Formatieren und Versenden von Alert-Payloads an Monitoring-Webhooks via `Invoke-RestMethod`.

---

## 🧪 Tests ausführen

```powershell
Invoke-Pester ./test_aufgabe.ps1
```
