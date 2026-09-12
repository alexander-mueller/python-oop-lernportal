# AD 14: CSV Bulk-Import & Provisioning

Willkommen zum Kurs **Active Directory & Windows Server Administration** im IT-Praxisportal!

## 💡 Das Wichtigste in Kürze
- **Ziel:** Automatisierter Massenimport neuer Mitarbeiter aus CSV-Dateien mit robuster Fehlerbehandlung.
- **Wichtigste Cmdlets / Tools:** `Import-ADUsersFromCSV`, `Get-ADUser`, `Get-ADGroup`, `New-ADOrganizationalUnit`

## 🎯 Deine Aufgaben (Checkliste)
1. **Teilziel 1:** CSV-Mitarbeiterdaten einlesen (Import-Csv)
2. **Teilziel 2:** Eindeutige Benutzernamen (SAM-Account) automatisch generieren
3. **Teilziel 3:** Automatische OU- und Gruppen-Zuweisung je nach Abteilung durchführen
4. **Teilziel 4:** Erfolgs- und Fehlerprotokoll als Transaktions-Log schreiben

## 🧪 Tests ausführen
```powershell
pwsh test_aufgabe.ps1
```
