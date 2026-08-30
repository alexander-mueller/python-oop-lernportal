# PS 13: Enterprise Modul-Entwicklung & Manifeste (.psd1) 📦

Willkommen zu **Modul 13** des PowerShell 7+ DevOps-Kurses!

Wer professionelle Automatisierungswerkzeuge für Teams und CI/CD-Pipelines baut, packt seinen Code nicht in unstrukturierte monolithische Skripte, sondern in **wiederverwendbare PowerShell-Module**. Ein professionelles Modul trennt interne Hilfsfunktionen (*Private*) von der offiziellen Nutzerschnittstelle (*Public*) und wird durch ein Modul-Manifest (`.psd1`) versioniert.

---

## 💡 1. Das Wichtigste in Kürze

### A. Das Standard-Modullayout
```
MyEnterpriseModule/
  ├── Public/                    # Exportierte Cmdlets für den Benutzer
  │     ├── Get-CloudResource.ps1
  │     └── New-CloudDeployment.ps1
  ├── Private/                   # Interne Hilfsfunktionen (nicht exportiert!)
  │     └── Format-AuthHeader.ps1
  ├── Tests/                     # Pester v5 Unit Tests
  │     └── MyEnterpriseModule.Tests.ps1
  ├── MyEnterpriseModule.psm1    # Der Modul-Code-Loader
  └── MyEnterpriseModule.psd1    # Das Modul-Manifest mit Metadaten
```

---

### B. Das Modul-Manifest (`.psd1`)
Das Manifest ist eine strukturierte PowerShell-Hashtable mit Metadaten über Autor, Version, GUID und exportierte Funktionen:

```powershell
@{
    RootModule        = 'MyEnterpriseModule.psm1'
    ModuleVersion     = '1.2.0'
    GUID              = '8e5d326c-d2c6-4b8f-8b9a-7c98e6a5d412'
    Author            = 'DevOps Cloud Team'
    Description       = 'Automatisierungs-Toolkit für Hybrid-Cloud Umgebungen'
    PowerShellVersion = '7.0'
    FunctionsToExport = @('Get-CloudResource', 'New-CloudDeployment')
    CmdletsToExport   = @()
}
```

---

### C. Der universelle `.psm1` Loader
Anstatt tausende Zeilen Code in eine einzige unübersichtliche `.psm1`-Datei zu schreiben, lädt der Loader alle Unterdateien dynamisch und exportiert gezielt nur die Public-Funktionen:

```powershell
# 1. Private Hilfsfunktionen dot-sourcen
Get-ChildItem "$PSScriptRoot/Private/*.ps1" | ForEach-Object { . $_.FullName }

# 2. Public Funktionen dot-sourcen und exportieren
$publicFunctions = Get-ChildItem "$PSScriptRoot/Public/*.ps1" | ForEach-Object {
    . $_.FullName
    $_.BaseName
}

Export-ModuleMember -Function $publicFunctions
```

---

## 🎼 Die didaktische Analogie: "Das Restaurant mit Showküche"

- **Der Gastraum (Public Functions):**  
  Die Speisekarte und die Kellner. Der Gast (Benutzer deines Moduls) sieht und bestellt nur die offiziellen Gerichte (z.B. `Invoke-CloudAudit`).
- **Die Küche im Hinterzimmer (Private Functions):**  
  Spülmaschine, Schneidebretter und geheime Gewürzmischungen. Extrem wichtig, aber für den Gast unsichtbar und geschützt vor versehentlicher Fehlbedienung.
- **Die Gewerbeanmeldung & Zertifikate (`.psd1`):**  
  Hygienepass, Inhabername, Versionsnummer und Öffnungszeiten.

---

## 🎯 Aufgaben & Teilziele in `aufgabe.ps1`

1. **TODO 1: `New-ModuleStructure`**  
   Erstelle das standardisierte Modul-Verzeichnislayout mit `Public/`, `Private/`, `Tests/` und den `.psm1`/`.psd1` Dateien.
2. **TODO 2: `Build-ModuleManifestContent`**  
   Generiere einen wohlgeformten `.psd1` Manifest-String mit Version, GUID und `FunctionsToExport`.
3. **TODO 3: `Invoke-ModuleLoader`**  
   Implementiere die Ladelogik, die Private/Public-Dateien einbindet und nur Public-Funktionen exportiert.
4. **TODO 4: `Test-ModuleCompliance`**  
   Schreibe einen automatisierten Compliance-Linter, der Modul-Ordner auf Vollständigkeit und Versionierung prüft.

---

## 🧪 Tests ausführen

```powershell
Invoke-Pester ./test_aufgabe.ps1
```
