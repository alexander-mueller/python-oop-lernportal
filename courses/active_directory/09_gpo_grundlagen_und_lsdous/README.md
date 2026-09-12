# AD 09: GPO-Grundlagen & LSDOU-Hierarchie

Willkommen zum Kurs **Active Directory & Windows Server Administration** im IT-Praxisportal!

## 💡 Das Wichtigste in Kürze
- **Ziel:** Gruppenrichtlinienarchitektur, LSDOU-Reihenfolge (Local, Site, Domain, OU), Vererbung und Enforced.
- **Wichtigste Cmdlets / Tools:** `New-TargetedGPO`, `Get-ADUser`, `Get-ADGroup`, `New-ADOrganizationalUnit`

## 🎯 Deine Aufgaben (Checkliste)
1. **Teilziel 1:** Neues Gruppenrichtlinienobjekt mit New-GPO erstellen
2. **Teilziel 2:** GPO an die passende Organisationseinheit verknüpfen (New-GPLink)
3. **Teilziel 3:** GPO-Vererbung blockieren (Set-GPInheritance) und Enforced testen
4. **Teilziel 4:** GPO-Reihenfolge und Vorrang analysieren

## 🧪 Tests ausführen
```powershell
pwsh test_aufgabe.ps1
```
