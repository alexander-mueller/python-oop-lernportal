# PS 01: Cmdlet-Architektur & Verb-Noun Syntax 🔷

Willkommen zu **Modul 01** des PowerShell 7+ Core Kurses!

In diesem Modul lernst du die fundamentale Architektur von PowerShell-Cmdlets kennen. Anders als in traditionellen Shells basieren alle PowerShell-Befehle auf einem strengen Standard: dem **Verb-Noun Paradigma**.

---

## 💡 1. Das Wichtigste auf einen Blick

### Verb-Noun Grammatik
- Jedes Cmdlet besteht aus einem genehmigten **Verb** (Aktion) und einem **Noun** (Singular-Substantiv des Objekts).
- Getrennt werden beide Teile durch einen Bindestrich: `Verb-Noun`.
- Beispiele:
  - `Get-Process` (Prozesse abfragen)
  - `Stop-Service` (Dienst anhalten)
  - `New-Item` (Datei/Ordner erstellen)
  - `Restart-Computer` (Rechner neustarten)

### Discovery-Werkzeuge
1. `Get-Command`: Durchsucht alle verfügbaren Module nach Befehlen (`Get-Command *Service*`).
2. `Get-Help`: Zeigt die vollständige Hilfe, Syntaxvarianten und Praxisbeispiele (`Get-Help Get-Process -Examples`).
3. `Get-Verb`: Listet alle von Microsoft standardisierten Verben auf (`Get-Verb`).

---

## 🎯 Aufgabenübersicht in `aufgabe.ps1`

1. **Get-FormattedCommandInfo**: Zerlegt einen Cmdlet-String (z.B. `"Get-Process"`) und liefert ein Hashtable mit `Verb`, `Noun` und `IsValidVerb` zurück.
2. **Format-CmdletName**: Verbindet ein Verb und ein Noun zu einem wohlgeformten `Verb-Noun` String.
3. **Test-ApprovedVerb**: Prüft, ob ein Verb in der Liste genehmigter PowerShell-Verben enthalten ist.
4. **Get-CommandSummary**: Erzeugt eine formatierte Übersicht als String.
