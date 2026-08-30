# PS 12: Sicherheit, Execution Policies & SecretManagement 🛡️

Willkommen zu **Modul 12** des PowerShell 7+ DevOps-Kurses!

In Enterprise- und Cloud-Umgebungen ist die Sicherheit von Zugangsdaten, API-Schlüsseln und Skriptausführungen oberste Priorität. PowerShell bietet mit `[SecureString]`, `[PSCredential]` und dem modernen Modul **Microsoft.PowerShell.SecretManagement** ein robustes Fundament gegen Credential Leaks und unsichere Klartext-Passwörter im Code.

---

## 💡 1. Das Wichtigste in Kürze

### A. Execution Policies (Ausführungsrichtlinien)
Execution Policies sind eine Schutzplanke (*Safety Guardrail*), um versehentliches Ausführen ungetesteter Skripte zu verhindern:

| Richtlinie | Bedeutung |
|---|---|
| `Restricted` | Keine Skripte erlaubt, nur interaktive Befehle. |
| `RemoteSigned` | Lokale Skripte erlaubt; aus dem Internet heruntergeladene Skripte müssen digital signiert sein. |
| `AllSigned` | Alle Skripte müssen von einem vertrauenswürdigen Herausgeber signiert sein. |
| `Bypass` / `Unrestricted` | Keine Blockaden (nur für CI/CD-Pipelines und kontrollierte Container!). |

---

### B. `[SecureString]` & `[PSCredential]`
Passwörter dürfen **niemals als Klartext-Strings** im Speicher oder in Skriptdateien liegen. Ein `[SecureString]` wird im Arbeitsspeicher verschlüsselt gehalten:

```powershell
# Passwort sicher erfassen oder konvertieren:
$secPass = ConvertTo-SecureString "MeinGeheimesPasswort123!" -AsPlainText -Force

# Typensicheres PSCredential erzeugen:
$cred = [PSCredential]::new("admin@cloudcorp.de", $secPass)

# Sicher an Cloud-Cmdlets übergeben:
Connect-AzAccount -Credential $cred
```

---

### C. Modernes `SecretManagement` (Microsoft.PowerShell.SecretManagement)
Das moderne SecretManagement-Ökosystem abstrahiert Secrets: Skripte greifen über `Get-Secret` und `Set-Secret` auf Passwörter zu, unabhängig davon, ob im Hintergrund Azure Key Vault, HashiCorp Vault, KeePass oder der lokale Windows Credential Manager verwendet wird:

```powershell
# Standardisierter Secret-Zugriff:
$dbKey = Get-Secret -Name "ProductionDbToken" -AsPlainText
```

---

## 🎼 Die didaktische Analogie: "Der gepanzerte Geldtransporter"

- **Klartext-Passwort im Code:**  
  Bargeld liegt offen auf dem Beifahrersitz eines Cabrios – jeder, der durch das Skriptfenster (oder Git-Repository) schaut, kann es sofort stehlen.
- **`[SecureString]`:**  
  Das Geld wird sofort in einen versiegelten Stahlkoffer gepackt. Es ist unlesbar, bis der autorisierte Empfänger es mit dem Schlüssel öffnet.
- **`SecretVault`:**  
  Ein unterirdischer Banktresor. Du musst dir nur noch den Namen des Schließfachs (`"DbPassword"`) merken, nicht die Zahlenkombination des Schlosses.

---

## 🎯 Aufgaben & Teilziele in `aufgabe.ps1`

1. **TODO 1: `New-SecureCredentials`**  
   Erzeuge ein sicheres `[PSCredential]`-Objekt aus Benutzername und Passwort mit `ConvertTo-SecureString`.
2. **TODO 2: `Protect-SensitiveString` & `Unprotect-SensitiveString`**  
   Verschlüssele sensible Strings mit `ConvertFrom-SecureString` und entschlüssele sie über `[System.Net.NetworkCredential]`.
3. **TODO 3: `Get-SecurityAuditReport`**  
   Prüfe LanguageMode, ExecutionPolicy und Admin-Rechte und berechne einen Security-Score.
4. **TODO 4: `Invoke-SecretVaultSimulation`**  
   Implementiere einen modularen Secret-Store mit Aktionen `Set`, `Get`, `Remove` und `List`.

---

## 🧪 Tests ausführen

```powershell
Invoke-Pester ./test_aufgabe.ps1
```
