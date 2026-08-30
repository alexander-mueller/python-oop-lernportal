# PS 08: Robustes Error-Handling (Try/Catch/Finally) ⚡

Willkommen zu **Modul 08** des PowerShell 7+ Core Kurses!

In diesem Modul lernst du professionelles Error-Handling in Enterprise-PowerShell-Skripten. Du verstehst die Unterscheidung zwischen terminierenden und nicht-terminierenden Fehlern und setzt `try`, `catch`, `finally` sowie `$ErrorActionPreference` zielsicher ein.

---

## 💡 1. Das Wichtigste auf einen Blick

### Nicht-terminierend vs. Terminierend
- Standard-Cmdlets lösen oft nur *nicht-terminierende* Fehler aus.
- Um Fehler mit `try/catch` abzufangen, setze `-ErrorAction Stop` oder `$ErrorActionPreference = 'Stop'`.

### Die `try / catch / finally` Syntax
```powershell
try {
    # Riskanter Code:
    $data = Get-Content -Path $filePath -ErrorAction Stop
}
catch [System.IO.FileNotFoundException] {
    Write-Warning "Datei nicht gefunden!"
}
catch {
    Write-Error "Allgemeiner Fehler: $($_.Exception.Message)"
}
finally {
    # Wird IMMER ausgeführt (z.B. Verbindung schließen):
    Write-Verbose "Cleanup beendet."
}
```

---

## 🎯 Aufgabenübersicht in `aufgabe.ps1`

1. **Read-SafeConfiguration**: Sicheres Einlesen von Dateien mit Fallback bei Fehlern.
2. **Invoke-SafeDivision**: Abfangen von Division durch 0 mit `throw` und `try/catch`.
3. **Invoke-TransactionalTask**: Garantierte Bereinigung von Sperren im `finally`-Block.
4. **Format-DetailedErrorRecord**: Strukturierte Aufbereitung von Ausnahme-Details.
