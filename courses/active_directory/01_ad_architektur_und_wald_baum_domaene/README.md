# AD 01: AD DS Architektur & Wald, Baum, Domäne

Willkommen zum Kurs **Active Directory & Windows Server Administration** im IT-Praxisportal!

## 💡 Das Wichtigste in Kürze
- **Ziel:** AD DS Gesamtstruktur (Forest), Trees, Domänen, Vertrauensstellungen, DNS-SRV-Records (_ldap._tcp) und Kerberos.
- **Wichtigste Cmdlets / Tools:** `Get-ADDomainArchitecture`, `Get-ADUser`, `Get-ADGroup`, `New-ADOrganizationalUnit`

## 🎯 Deine Aufgaben (Checkliste)
1. **Teilziel 1:** Gesamtstruktur-Funktionsebene mit Get-ADForest analysieren
2. **Teilziel 2:** DNS-SRV-Einträge für Domänencontroller abfragen
3. **Teilziel 3:** Kerberos Ticket-Vergabe und LDAP-Ports (389/636) prüfen
4. **Teilziel 4:** Vertrauensstellung (Trust) zwischen Domänen validieren

## 🧪 Tests ausführen
```powershell
pwsh test_aufgabe.ps1
```
