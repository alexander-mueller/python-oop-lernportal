# AD 06: Computerkonten & Domänenbeitritt

Willkommen zum Kurs **Active Directory & Windows Server Administration** im IT-Praxisportal!

## 💡 Das Wichtigste in Kürze
- **Ziel:** Maschinenkonten (sAMAccountName$), Secure Channel, Kennwortwechsel und Offline Domain Join mit djoin.exe.
- **Wichtigste Cmdlets / Tools:** `Add-DomainComputerAccount`, `Get-ADUser`, `Get-ADGroup`, `New-ADOrganizationalUnit`

## 🎯 Deine Aufgaben (Checkliste)
1. **Teilziel 1:** Computerkonto im passenden OU-Pfad anlegen
2. **Teilziel 2:** Secure Channel zwischen Client und DC mit Test-ComputerSecureChannel prüfen
3. **Teilziel 3:** Offline Domain Join Bereitstellungsdatei mit djoin.exe /provision erzeugen
4. **Teilziel 4:** Veraltete Computerkonten identifizieren und deaktivieren

## 🧪 Tests ausführen
```powershell
pwsh test_aufgabe.ps1
```
