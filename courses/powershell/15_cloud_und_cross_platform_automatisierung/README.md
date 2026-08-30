# PS 15: Cross-Platform Cloud Automation (Azure Az & AWS CLI) ☁️

Willkommen zu **Modul 15** des PowerShell 7+ DevOps-Kurses!

PowerShell ist längst kein reines Windows-Admin-Tool mehr: Als **PowerShell 7+ (Core)** läuft es nativ auf Linux, macOS, in Docker-Containern und Kubernetes Pods. In modernen Hybrid-Cloud-Architekturen steuert PowerShell sowohl Microsoft Azure (`Az`-Modul) als auch AWS (`AWS CLI` / `AWS.Tools`) und Google Cloud (`GoogleCloudPlatform`).

---

## 💡 1. Das Wichtigste in Kürze

### A. Cross-Platform Besonderheiten in PowerShell 7+
- **Automatische Plattform-Variablen:** `$IsLinux`, `$IsWindows`, `$IsMacOS`.
- **Dateipfade:** Verwende immer `Join-Path` oder `[System.IO.Path]::Combine()`, um plattformunabhängige Pfade (`/` vs `\`) zu garantieren.
- **Case-Sensitivity:** Auf Linux/Docker sind Dateinamen und Pfade strikt *case-sensitive* (`config.json` != `Config.json`)!

```powershell
if ($IsLinux) {
    Write-Host "Läuft in einer Linux/Container-Umgebung."
}
```

---

### B. Cloud Governance: Idempotenz & Tagging
In Infrastructure as Code (IaC) müssen Konfigurationen **idempotent** sein: Mehrfaches Ausführen führt immer zum gleichen fehlerfreien Zustand, ohne Duplikate zu erzeugen. Zudem sind strukturierte Tags Pflicht:

```powershell
$tags = @{
    Environment = "Production"
    ManagedBy   = "PowerShellAutomation"
    CostCenter  = "DevOps-Core"
    CreatedDate = (Get-Date -Format "yyyy-MM-dd")
}
```

---

### C. AWS CLI & Multi-Cloud Parsing
Während das Azure `Az`-Modul native PowerShell-Objekte liefert, gibt das AWS CLI rohes JSON aus. Mit `ConvertFrom-Json` binden wir AWS-Outputs nahtlos in PowerShell-Pipelines ein:

```powershell
# AWS CLI Ausgabe direkt in PowerShell-Objekte wandeln:
$ec2Json = aws ec2 describe-instances --output json
$instances = ($ec2Json | ConvertFrom-Json).Reservations.Instances

$instances | Where-Object { $_.State.Name -eq 'running' } | Select-Object InstanceId, InstanceType
```

---

## 🎼 Die didaktische Analogie: "Der universelle Cloud-Dirigent"

- **Das Orchester der Cloud-Provider:**  
  Azure, AWS und lokale Linux-Server sprechen unterschiedliche Sprachen und Dialekte.
- **PowerShell 7+ (Der Dirigent):**  
  Steht plattformunabhängig im Zentrum. Er liest die Noten (JSON-Manifeste), hebt den Taktstock und steuert alle Musiker harmonisch über eine einheitliche Objekt-Pipeline!

---

## 🎯 Aufgaben & Teilziele in `aufgabe.ps1`

1. **TODO 1: `Get-PlatformDiagnostics`**  
   Ermittle Betriebssystem, Pfadtrennzeichen und CoreCLR-Status für Cross-Platform-Skripte.
2. **TODO 2: `New-IdempotentResourceConfig`**  
   Erzeuge eine Azure-Ressourcenkonfiguration mit Pflicht-Tags (`Environment`, `ManagedBy`, `CreatedDate`).
3. **TODO 3: `Convert-AwsCliOutputToPsObject`**  
   Parse und normalisiere rohe JSON-Ausgaben von AWS CLI-Befehlen (EC2 / S3).
4. **TODO 4: `Audit-CloudResourceCompliance`**  
   Führe ein automatisches Governance-Audit über Cloud-Ressourcen durch (Prüfung von Pflicht-Tags und Regionen).

---

## 🧪 Tests ausführen

```powershell
Invoke-Pester ./test_aufgabe.ps1
```
