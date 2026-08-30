# PS 10: JSON, CSV, XML & REST-APIs (Invoke-RestMethod) 🌐

Willkommen zu **Modul 10** des PowerShell 7+ DevOps-Kurses!

In modernen Cloud- und DevOps-Architekturen sind **REST-APIs** und standardisierte Datenformate wie **JSON, CSV und XML** das Rückgrat der Systemintegration. PowerShell bietet mit Cmdlets wie `Invoke-RestMethod`, `ConvertFrom-Json` und dem `[xml]`-Typbeschleuniger erstklassige Werkzeuge zur Datenverarbeitung.

---

## 💡 1. Das Wichtigste in Kürze

### A. `Invoke-RestMethod` vs. `Invoke-WebRequest`
- **`Invoke-WebRequest`:** Liefert das rohe HTTP-Antwortobjekt inklusive HTML, Statuscode und Raw-Content zurück.
- **`Invoke-RestMethod`:** Erkennt automatisch JSON/XML-Antworten und wandelt den Payload direkt in native **`PSCustomObject`**-Hierarchien um!

```powershell
$headers = @{
    "Authorization" = "Bearer $env:API_TOKEN"
    "Content-Type"  = "application/json"
}

$response = Invoke-RestMethod -Uri "https://api.github.com/user/repos" -Headers $headers -Method GET
$response | Select-Object -Property name, stargazers_count, html_url
```

---

### B. Die gefährliche Falle: `ConvertTo-Json -Depth`
Standardmäßig serialisiert `ConvertTo-Json` Objekte nur bis zu einer Verschachtelungstiefe von **2 Ebenen**! Tiefere Objekte werden als String `System.Collections.Hashtable` abgeschnitten.

> ⚠️ **DevOps-Best-Practice:** Setze bei komplexen Datenstrukturen (z.B. Kubernetes-Configs oder Azure ARM Templates) immer explizit `-Depth 10` oder höher!

```powershell
$clusterConfig = @{
    cluster = @{
        network = @{
            subnets = @("10.0.1.0/24", "10.0.2.0/24")
        }
    }
}

# Falsch (Tiefe wird abgeschnitten):
$badJson = $clusterConfig | ConvertTo-Json

# Richtig (Verlustfreie Serialisierung):
$goodJson = $clusterConfig | ConvertTo-Json -Depth 10
```

---

### C. CSV-Export ohne Metadaten-Müll
Beim Exportieren von Objekten in CSV-Dateien für Excel oder Berichte sorgt der Schalter `-NoTypeInformation` dafür, dass die lästige Typzeile (`#TYPE System.Management.Automation.PSCustomObject`) entfällt:

```powershell
$servers | Select-Object Hostname, IP, Role | Export-Csv -Path "servers.csv" -Delimiter ";" -NoTypeInformation -Encoding utf8
```

---

### D. Schnelles XML-Parsing mit `[xml]`
Durch das Voranstellen von `[xml]` konvertiert PowerShell XML-Strings direkt in navigierbare .NET-Objekte:

```powershell
[xml]$manifest = Get-Content -Path "infrastructure.xml"
# Direkter Zugriff über Punktnotation oder XPath:
$allNodes = $manifest.SelectNodes("//server")
```

---

## 🎼 Die didaktische Analogie: "Der Zoll-Containerhafen"

- **Die REST-API:** Das Frachtschiff, das Waren über das Meer (HTTP/HTTPS) transportiert.
- **JSON / XML:** Die genormten Seecontainer – überall auf der Welt lesbar und maschinell verarbeitbar.
- **`Invoke-RestMethod`:** Der automatische Hafen-Kran, der den Container entlädt und die Ware sofort fix und fertig ausgepackt auf das Förderband legt.
- **`-Depth`:** Die Prüftiefe beim Zoll. Schaut man nur in die oberste Kiste (`-Depth 2`), übersieht man die wertvollen Teile ganz unten im Container!

---

## 🎯 Aufgaben & Teilziele in `aufgabe.ps1`

1. **TODO 1: `Get-RestApiData`**  
   Baue einen flexiblen REST-API-Client mit Bearer-Token-Unterstützung und `Invoke-RestMethod`.
2. **TODO 2: `Convert-JsonToCsvReport`**  
   Wandle einen JSON-String in ein sauberes CSV-Format ohne `#TYPE`-Kopfzeile und mit konfigurierbarem Trennzeichen um.
3. **TODO 3: `Format-DeepNestedConfig`**  
   Serialisiere tief verschachtelte Konfigurationen mit `ConvertTo-Json -Depth` und validiere die Rückumwandlung.
4. **TODO 4: `Parse-XmlServerManifest`**  
   Parse ein XML-Manifest mit dem `[xml]`-Beschleuniger und gib eine Liste strukturierter Server-Objekte zurück.

---

## 🧪 Tests ausführen

```powershell
Invoke-Pester ./test_aufgabe.ps1
```
