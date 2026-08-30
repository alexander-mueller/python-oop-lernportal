# PS 07: Eigene Cmdlets [CmdletBinding()] & Validierung ⚡

Willkommen zu **Modul 07** des PowerShell 7+ Core Kurses!

In diesem Modul entwickelst du echte Enterprise-fähige Cmdlets (Advanced Functions). Mit `[CmdletBinding()]` rüstest du Skripte mit professionellen Features wie `-WhatIf`, `-Confirm`, Parameter-Sets und Validierungs-Attributen aus.

---

## 💡 1. Das Wichtigste auf einen Blick

### `[CmdletBinding()]` & Parameter-Attribute
```powershell
function Get-ServerConfig {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [ValidateSet('Development', 'Staging', 'Production')]
        [string]$Environment,

        [Parameter(Mandatory = $false)]
        [ValidateRange(1, 65535)]
        [int]$Port = 8080
    )
    # Logik...
}
```

### `-WhatIf` und `$PSCmdlet.ShouldProcess`
```powershell
function Stop-Server {
    [CmdletBinding(SupportsShouldProcess = $true)]
    param([Parameter(Mandatory=$true)] [string]$ServerName)

    if ($PSCmdlet.ShouldProcess($ServerName, "Server stoppen")) {
        # Echte Ausführung...
    }
}
```

---

## 🎯 Aufgabenübersicht in `aufgabe.ps1`

1. **Get-EnvironmentConfig**: Konfigurations-Cmdlet mit `[ValidateSet()]` und `[ValidateRange()]`.
2. **Restart-AppService**: Destruktives Cmdlet mit `SupportsShouldProcess` und `$PSCmdlet.ShouldProcess`.
3. **New-UserAccount**: Pipeline-fähiges Cmdlet mit Regex-Email-Validierung `[ValidatePattern()]`.
4. **Get-SystemReport**: Report-Cmdlet mit Switch-Parameter `[switch]$Detailed`.
