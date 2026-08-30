# PS 11: Dateisystem, Registry & PSProvider 📂

Willkommen zu **Modul 11** des PowerShell 7+ DevOps-Kurses!

Eine der elegantesten Kernarchitekturen von PowerShell ist das **Provider-Modell**. Anstatt für Umgebungsvariablen, Zertifikate, Registry-Einträge und Dateien jeweils völlig unterschiedliche APIs zu lernen, vereinheitlicht PowerShell diese Datenquellen als **PSDrives**.

---

## 💡 1. Das Wichtigste in Kürze

### A. PSProvider & PSDrives
Ein **PSProvider** übersetzt eine Datenquelle in eine hierarchische Ordner- und Dateistruktur:

| PSDrive | Provider | Beispiel-Befehl |
|---|---|---|
| `Env:` | `Environment` | `Get-ChildItem Env:PATH` |
| `Cert:` | `Certificate` | `Get-ChildItem Cert:\LocalMachine\Root` |
| `HKLM:` | `Registry` (Windows) | `Get-ItemProperty HKLM:\Software\...` |
| `Variable:` | `Variable` | `Get-ChildItem Variable:Host*` |
| `C:`, `/` | `FileSystem` | `Get-ChildItem -Path /var/log` |

```powershell
# Umgebungsvariablen wie ein Verzeichnis abfragen:
Get-ChildItem Env: | Where-Object Name -like "AZURE*"
```

---

### B. Dynamische PSDrives mounten (`New-PSDrive`)
Du kannst beliebige Verzeichnisse, Netzwerk-Freigaben oder benutzerdefinierte Provider als virtuelles Laufwerk mounten:

```powershell
# Projekt-Ordner als schnelles Laufwerk "Project:" mounten:
New-PSDrive -Name "Project" -PSProvider FileSystem -Root "/var/www/my-app"

# Verwenden wie ein normales Laufwerk:
Set-Location Project:
Get-ChildItem

# Wieder aufräumen:
Remove-PSDrive -Name "Project"
```

---

### C. Kryptografische Integritätsprüfung mit `Get-FileHash`
In CI/CD-Pipelines und Sicherheits-Audits ist der Nachweis unerlässlich, dass Build-Artefakte oder Konfigurationsdateien nicht manipuliert wurden:

```powershell
# SHA256-Prüfsumme ermitteln
$hashInfo = Get-FileHash -Path "./package.zip" -Algorithm SHA256
Write-Host "Kryptografischer Hash: $($hashInfo.Hash)"
```

---

## 🎼 Die didaktische Analogie: "Der universelle Reiseadapter"

- **Verschiedene Steckdosen der Welt (Datenquellen):**  
  Die Registry ist ein hierarchischer Binärbaum, Umgebungsvariablen sind ein flacher Speicherbereich, Zertifikate sind kryptografische X.509-Stores.
- **Der PSProvider (Der Universal-Adapter):**  
  Er sorgt dafür, dass jede dieser Steckdosen für deine Geräte (Cmdlets wie `Get-ChildItem`, `Get-Item`, `Set-Item`) wie ein normales Dateisystem aussieht!

---

## 🎯 Aufgaben & Teilziele in `aufgabe.ps1`

1. **TODO 1: `Get-EnvironmentReport`**  
   Lies Umgebungsvariablen über das `Env:`-Laufwerk aus und filtere nach Wildcard-Mustern.
2. **TODO 2: `Get-DirectoryFileInventory`**  
   Erstelle ein rekursives Dateiinventar mit Größe in KB und optionalem SHA256-Hash.
3. **TODO 3: `Test-FileIntegrity`**  
   Vergleiche den SHA256-Hash einer Datei mit einem Soll-Hashwert zur Manipulationserkennung.
4. **TODO 4: `New-TemporaryMountDrive`**  
   Mounte ein temporäres PSDrive, führe eine Aktion aus und stelle über `try/finally` sicher, dass das Laufwerk immer sauber entfernt wird.

---

## 🧪 Tests ausführen

```powershell
Invoke-Pester ./test_aufgabe.ps1
```
