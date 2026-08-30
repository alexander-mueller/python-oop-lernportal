# PS 09: Multithreading mit ForEach-Object -Parallel & Start-ThreadJob 🚀

Willkommen zu **Modul 09** des PowerShell 7+ DevOps-Kurses!

In früheren PowerShell-Versionen (Windows PowerShell 5.1) war echte Nebenläufigkeit teuer: `Start-Job` erzeugte für jeden Task einen komplett neuen `powershell.exe`-Betriebssystem-Prozess mit enormem RAM- und CPU-Overhead. Mit **PowerShell 7+** wurde echtes, leichtgewichtiges Multithreading eingeführt: `ForEach-Object -Parallel` und `Start-ThreadJob` führen Scriptblocks parallel in separaten Runspaces innerhalb desselben Prozesses aus – **bis zu 100x schneller!**

---

## 💡 1. Das Wichtigste in Kürze

### A. `ForEach-Object -Parallel`
Mit dem `-Parallel`-Switch verarbeitet PowerShell Elemente der Pipeline zeitgleich in separaten Threads:

```powershell
$servers = @("srv-app01", "srv-app02", "srv-db01", "srv-web01")

$servers | ForEach-Object -Parallel {
    Write-Host "Prüfe Server $_ auf Thread: $([System.Threading.Thread]::CurrentThread.ManagedThreadId)"
    Start-Sleep -Seconds 1
} -ThrottleLimit 4
```

- **`-ThrottleLimit <int>`**: Begrenzt die maximale Anzahl gleichzeitig aktiver Threads (Standardwert in PS7 ist 5).
- **Prozesse vs. Threads**: Runspaces teilen sich den Hauptprozess, was RAM und Startup-Latenz minimiert.

---

### B. Variablen-Scoping mit `$using:VariableName`
Weil jeder Thread in einem isolierten Runspace ausgeführt wird, haben parallele Blöcke standardmäßig keinen Zugriff auf lokale Variablen des Hauptskripts. Mit dem Präfix `$using:` reichst du Variablen thread-sicher hinein:

```powershell
$timeout = 2500
$logPrefix = "[PROD-CHECK]"

$servers | ForEach-Object -Parallel {
    $currentHost = $_
    $currentTimeout = $using:timeout
    $prefix = $using:logPrefix

    [PSCustomObject]@{
        Host      = $currentHost
        Timeout   = $currentTimeout
        LogTag    = "$prefix-$currentHost"
    }
} -ThrottleLimit 8
```

---

### C. Leichtgewichtige Asynchronität mit `Start-ThreadJob`
Für Hintergrundaufgaben, die nicht an eine Pipeline gebunden sind:

```powershell
# Asynchronen Thread-Job starten
$job = Start-ThreadJob -Name "BackupCheck" -ScriptBlock {
    param($folder)
    Get-ChildItem -Path $folder -Recurse | Measure-Object -Property Length -Sum
} -ArgumentList "C:\Logs"

# Status prüfen oder warten
$job | Wait-Job -Timeout 10
$ergebnis = $job | Receive-Job
$job | Remove-Job -Force
```

---

## 🎼 Die didaktische Analogie: "Die Autobahn-Mautstation"

- **Sequenzielle Schleife (`foreach ($s in $servers)`):**  
  Eine einzelne Mautstation mit nur einer Spur. Jedes Fahrzeug (Server-Request) muss warten, bis das vorherige komplett bezahlt hat und wegfährt.
- **Alter `Start-Job` (Prozess-basiert):**  
  Für jedes einzelne Auto wird eine komplett neue Mautstation auf der grünen Wiese gebaut, angelernt und nach 5 Sekunden wieder abgerissen – enorme Verschwendung!
- **`ForEach-Object -Parallel` (Thread-basiert):**  
  Eine 8-spurige Mautstation (`-ThrottleLimit 8`). Autos fahren parallel durch die Spuren. Alle Schilder und Preise (`$using:MautTarif`) sind für alle Spuren sofort sichtbar.

---

## 🎯 Aufgaben & Teilziele in `aufgabe.ps1`

Öffne `aufgabe.ps1` und implementiere die folgenden 4 Funktionen:

1. **TODO 1: `Invoke-ParallelPing`**  
   Prüfe Rechnernamen/IPs parallel mit `ForEach-Object -Parallel -ThrottleLimit $ThrottleLimit` und `$using:TimeoutMs`. Gib für jeden Host ein `[PSCustomObject]` zurück.
2. **TODO 2: `Start-AsyncServerTask`**  
   Starte einen asynchronen Task mit `Start-ThreadJob` und gib das Job-Objekt zurück.
3. **TODO 3: `Wait-AndCollectThreadJobs`**  
   Warte mit `Wait-Job -Timeout`, sammele Ergebnisse via `Receive-Job` ein und räume die Jobs sauber mit `Remove-Job -Force` auf.
4. **TODO 4: `Invoke-ThrottledBatchProcessing`**  
   Führe einen ScriptBlock parallel für Daten-Objekte aus, stoppe die Zeit mit `[System.Diagnostics.Stopwatch]::StartNew()` und gib aggregierte Metriken zurück.

---

## 🧪 Tests ausführen

Führe in PowerShell die Pester-Testsuite aus:
```powershell
Invoke-Pester ./test_aufgabe.ps1
```
Oder starte die Tests direkt in der Web-IDE!
