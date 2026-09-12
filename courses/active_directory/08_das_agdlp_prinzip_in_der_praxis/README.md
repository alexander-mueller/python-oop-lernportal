# AD 08: Das AGDLP-Prinzip in der Praxis

Willkommen zum Kurs **Active Directory & Windows Server Administration** im IT-Praxisportal!

## 💡 Das Wichtigste in Kürze
- **Ziel:** Best-Practice Berechtigungsarchitektur: Accounts -> Global Groups -> Domain Local Groups -> Permissions.
- **Wichtigste Cmdlets / Tools:** `Deploy-AGDLPFramework`, `Get-ADUser`, `Get-ADGroup`, `New-ADOrganizationalUnit`

## 🎯 Deine Aufgaben (Checkliste)
1. **Teilziel 1:** Benutzerkonten (A) erstellen und globalen Rollengruppen (G) zuordnen
2. **Teilziel 2:** Domänenlokale Zugriffsgruppen (DL) für Dateifreigaben erstellen
3. **Teilziel 3:** Globale Gruppen in die domänenlokalen Gruppen schachteln
4. **Teilziel 4:** NTFS-Berechtigungen (P) ausschließlich auf domänenlokale Gruppen vergeben

## 🧪 Tests ausführen
```powershell
pwsh test_aufgabe.ps1
```
