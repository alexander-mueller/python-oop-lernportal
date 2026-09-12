# AD 02: Domänencontroller & FSMO-Rollen

Willkommen zum Kurs **Active Directory & Windows Server Administration** im IT-Praxisportal!

## 💡 Das Wichtigste in Kürze
- **Ziel:** Die 5 FSMO-Rollen (Schema, Domain Naming, PDC Emulator, RID Pool, Infrastructure Master) und Global Catalog (GC).
- **Wichtigste Cmdlets / Tools:** `Get-FSMORoleOwner`, `Get-ADUser`, `Get-ADGroup`, `New-ADOrganizationalUnit`

## 🎯 Deine Aufgaben (Checkliste)
1. **Teilziel 1:** FSMO-Rolleninhaber mit Get-ADDomainController identifizieren
2. **Teilziel 2:** PDC Emulator Zeitsynchronisation (NTP) konfigurieren
3. **Teilziel 3:** RID-Pool Erschöpfung überwachen und diagnostizieren
4. **Teilziel 4:** Rollen-Transfer vs. Seizure (Beschlagnahmung) simulieren

## 🧪 Tests ausführen
```powershell
pwsh test_aufgabe.ps1
```
