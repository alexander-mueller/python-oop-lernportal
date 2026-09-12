# AD 03: Organisationseinheiten & Struktur

Willkommen zum Kurs **Active Directory & Windows Server Administration** im IT-Praxisportal!

## 💡 Das Wichtigste in Kürze
- **Ziel:** Hierarchisches OU-Design nach Standorten oder Abteilungen, Schutz vor versehentlichem Löschen und Delegierung.
- **Wichtigste Cmdlets / Tools:** `New-ADStructureOU`, `Get-ADUser`, `Get-ADGroup`, `New-ADOrganizationalUnit`

## 🎯 Deine Aufgaben (Checkliste)
1. **Teilziel 1:** Strukturierte OU-Hierarchie (OU=Produktion, OU=Verwaltung) mit New-ADOrganizationalUnit anlegen
2. **Teilziel 2:** ProtectedFromAccidentalDeletion aktivieren
3. **Teilziel 3:** Verwaltungsrechte auf Helpdesk-Gruppe delegieren
4. **Teilziel 4:** OU-Objekte mit Get-ADOrganizationalUnit auflisten und filtern

## 🧪 Tests ausführen
```powershell
pwsh test_aufgabe.ps1
```
