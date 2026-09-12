# AD 05: Benutzerkonten & LDAP-Attribute

Willkommen zum Kurs **Active Directory & Windows Server Administration** im IT-Praxisportal!

## 💡 Das Wichtigste in Kürze
- **Ziel:** SAM-Account-Name, UPN (User Principal Name), LDAP-Attribute (mail, department) und UserAccountControl Flags.
- **Wichtigste Cmdlets / Tools:** `New-EnterpriseADUser`, `Get-ADUser`, `Get-ADGroup`, `New-ADOrganizationalUnit`

## 🎯 Deine Aufgaben (Checkliste)
1. **Teilziel 1:** Neues Benutzerkonto mit New-ADUser und SecureString-Kennwort erstellen
2. **Teilziel 2:** UPN, Mailadresse, Telefonnummer und Abteilung pflegen
3. **Teilziel 3:** Passwortrichtlinien (PasswordNeverExpires, MustChangePassword) steuern
4. **Teilziel 4:** Inaktive Benutzerkonten mit Search-ADAccount aufspüren

## 🧪 Tests ausführen
```powershell
pwsh test_aufgabe.ps1
```
