# PS 14: Pester v5 Automatisiertes Testing & Mocking 🧪

Willkommen zu **Modul 14** des PowerShell 7+ DevOps-Kurses!

**Pester** ist das De-facto-Standard-Framework für Behavior-Driven Development (BDD) und automatisierte Unittests in PowerShell. Mit Version 5 wurde Pester von Grund auf modernisiert und trennt die Test-Erkennungsphase (*Discovery Phase*) strikt von der eigentlichen Ausführung (*Run Phase*).

---

## 💡 1. Das Wichtigste in Kürze

### A. Pester v5 Syntax & Struktur
```powershell
Describe 'Server Health Monitoring Service' {
    BeforeAll {
        # Einmaliges Setup vor allen Tests
        $testHost = 'srv-app01'
    }

    Context 'Wenn alle Dienste online sind' {
        It 'Sollte den Server als Operational einstufen' {
            # Arrange: Mocks definieren
            Mock Get-Service { [PSCustomObject]@{ Status = 'Running' } }
            Mock Test-Connection { $true }

            # Act: Funktion ausführen
            $result = Get-ServerHealthStatus -ServerName $testHost

            # Assert: Überprüfungen
            $result.IsHealthy | Should -BeTrue
            $result.Code | Should -Be 200
        }
    }

    Context 'Fehlerbehandlung' {
        It 'Sollte werfen, wenn Dienst unrettbar ist' {
            Mock Get-Service { [PSCustomObject]@{ Status = 'Stopped' } }
            Mock Restart-Service {}

            { Restart-FailedService -ServiceName 'CriticalDB' -MaxRetries 1 } | Should -Throw
        }
    }
}
```

---

### B. Fluent Assertions mit `Should`
Pester bietet eine intuitive, lesbare Syntax für Zusicherungen:
- `$val | Should -Be $expected`
- `$val | Should -BeTrue` / `$val | Should -BeFalse`
- `$list | Should -HaveCount 3`
- `$list | Should -Contain "Entry"`
- `{ Invoke-DangerousCmdlet } | Should -Throw`

---

### C. Mocking (Isolierte Unittests)
Ein Mock ersetzt ein echtes PowerShell-Cmdlet (wie `Restart-Service` oder `Invoke-RestMethod`) während des Tests durch eine kontrollierte Attrappe. Dadurch zerstören Tests keine echten Produktivsysteme:

```powershell
# Echten Reboot simulieren:
Mock Restart-Computer {}

# Prüfen, ob der Mock genau 1x aufgerufen wurde:
Should -Invoke Restart-Computer -Times 1 -Exactly
```

---

## 🎼 Die didaktische Analogie: "Der Flugsimulator"

- **Das Flugzeug (Dein PowerShell-Code):**  
  Die Steuersoftware für echte Passagiermaschinen.
- **Der Flugsimulator (Pester v5 Framework):**  
  Eine kontrollierte Testumgebung, in der Turbulenzen, Blitzeinschläge und Triebwerksausfälle simuliert werden.
- **Die Mocks (`Mock Get-Service`):**  
  Die künstlichen Sensoren im Simulator. Sie melden "Triebwerk brennt", ohne dass echtes Kerosin brennen muss – und wir prüfen, ob die Notfall-Funktion blitzschnell und fehlerfrei reagiert!

---

## 🎯 Aufgaben & Teilziele in `aufgabe.ps1`

1. **TODO 1: `Get-ServerHealthStatus`**  
   Implementiere die Zustandsprüfung, die auf Mock-Aufrufe von `Get-Service` und `Test-Connection` reagiert.
2. **TODO 2: `Restart-FailedService`**  
   Baue eine Service-Restart-Schleife mit Retries und Exception-Handling bei anhaltendem Ausfall.
3. **TODO 3: `Test-PesterResultAnalyzer`**  
   Berechne Erfolgsquote (PassRate) und erstelle CI/CD Quality-Gate-Entscheidungen aus Testresultaten.
4. **TODO 4: `Invoke-MockableApiAudit`**  
   Führe einen REST-API-Audit durch und werte Status und Payload-Gültigkeit aus.

---

## 🧪 Tests ausführen

```powershell
Invoke-Pester ./test_aufgabe.ps1
```
