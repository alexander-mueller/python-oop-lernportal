import os

BASE_DIR = "/root/uebungen_python/courses/csharp"

modules_data = [
    # =========================================================================
    # MODUL 01: Syntax, Datentypen, Top-Level Statements & Nullables
    # =========================================================================
    {
        "folder": "01_syntax_datentypen_und_top_level_statements",
        "title": "C# 01: Syntax, Top-Level Statements & Nullables",
        "track": "track_1_csharp_basics",
        "next_folder": "02_kontrollfluss_und_pattern_matching",
        "prev_folder": None,
        "badge": "💜 C# 12 & Modernes .NET 8",
        "header_title": "C# 01: Syntax, Top-Level Statements & Nullable Types",
        "header_desc": "Steige ein in modernes C# 12: Top-Level Statements, Value vs. Reference Types, Type Inference mit var, Nullable Reference Types und String-Interpolation.",
        "readme": """# C# 01: Syntax, Datentypen, Top-Level Statements & Nullables 💜

Willkommen zu **Modul 01** des C# 12 & .NET 8 Enterprise-Kurses!

In diesem Modul lernst du das moderne Fundament von C# kennen: Top-Level Statements, das statische Typsystem (Value vs. Reference Types), Type Inference mit `var`, Nullable Reference Types (`#nullable enable`) sowie mächtige String-Interpolation.

---

## 💡 1. Das Wichtigste in Kürze

### Top-Level Statements in C#
Seit C# 9/10 entfällt der historische Boilerplate-Code (`class Program { static void Main(string[] args) { ... } }`). Du kannst deinen Code direkt oben in der Datei schreiben:

```csharp
// Modernes C# (Top-Level Statement):
Console.WriteLine("Hallo .NET 8 Enterprise!");
```

### Wertetypen (Value Types) vs. Referenztypen (Reference Types)
- **Wertetypen (Stack):** `int`, `long`, `double`, `decimal`, `bool`, `char`, `struct`. Speichern den direkten Wert. Können per Default *nicht* `null` sein (außer als `Nullable<T>` bzw. `int?`).
- **Referenztypen (Heap):** `string`, `object`, `class`, `record`, `interface`. Speichern eine Referenz (Zeiger) auf das Objekt im verwalteten Heap-Speicher.

### Nullable Reference Types (`string?`)
C# schützt dich vor der gefürchteten `NullReferenceException`:
- `string text = "Hallo";` $\\rightarrow$ darf niemals `null` sein!
- `string? optionalerText = null;` $\\rightarrow$ signalisiert dem Compiler, dass der Wert fehlen kann.
- **Null-Coalescing Operator (`??`):** `string ausgabe = optionalerText ?? "Standardwert";`
- **Null-Conditional Operator (`?.`):** `int? laenge = optionalerText?.Length;`

### String Interpolation & Formatierung
```csharp
string name = "Cloud-Server";
int port = 443;
decimal preis = 49.99m;

// Moderne Interpolation mit Formatbezeichnern:
string info = $"{name}:{port} kostet {preis:F2} €";
```

---

## 🎯 Teilziele in `Aufgabe.cs`

1. **TODO 1:** `ErstelleServerInfo(string name, int port, double ramGb, bool isProduction)`:
   Liefert formatierte Server-Info: `"{name} (Port {port}) - {ramGb:F1} GB RAM [{PROD/DEV}]"`.
   Beispiel: `ErstelleServerInfo("AppHost", 8080, 16.0, true)` $\\rightarrow$ `"AppHost (Port 8080) - 16.0 GB RAM [PROD]"`.
2. **TODO 2:** `BerechneGesamtpreis(decimal einzelpreis, int anzahl, decimal? rabattProzent)`:
   Berechnet den Gesamtpreis mit Berücksichtigung eines optionalen Rabatts (`rabattProzent ?? 0m`).
   Formel: `einzelpreis * anzahl * (1m - (rabatt / 100m))`.
   Gibt `0m` zurück, wenn `anzahl <= 0` oder `einzelpreis < 0m`.
3. **TODO 3:** `FormatName(string? vorname, string? nachname, string standardName)`:
   Kombiniert Vorname und Nachname getrennt durch Leerzeichen. Falls beide `null`, leer oder nur Whitespace sind, wird `standardName` zurückgegeben.
4. **TODO 4:** `ParseAppPort(string? portInput, int defaultPort)`:
   Parst einen String in einen Integer-Port (gültig von 1 bis 65535). Bei ungültigem String, `null` oder Port außerhalb des Bereichs wird `defaultPort` geliefert.
""",
        "aufgabe": """using System;

// 🎯 C# 01: Syntax, Datentypen, Top-Level Statements & Nullables
// =============================================================

public static class Aufgabe
{
    // 🎯 TEILZIEL 1 (TODO 1): Server-Info String formatieren
    // Format: "{name} (Port {port}) - {ramGb:F1} GB RAM [{PROD/DEV}]"
    // Beispiel: ErstelleServerInfo("AppHost", 8080, 16.0, true) -> "AppHost (Port 8080) - 16.0 GB RAM [PROD]"
    // Beispiel: ErstelleServerInfo("TestBox", 5000, 4.25, false) -> "TestBox (Port 5000) - 4.3 GB RAM [DEV]"
    public static string ErstelleServerInfo(string name, int port, double ramGb, bool isProduction)
    {
        // TODO: Verwende String-Interpolation ($"...") und formatiere ramGb mit :F1
        return "";
    }

    // 🎯 TEILZIEL 2 (TODO 2): Gesamtpreis mit optionalem Rabatt berechnen
    // Falls rabattProzent null ist, wird 0% Rabatt angenommen (Null-Coalescing ?? nutzen).
    // Formel: einzelpreis * anzahl * (1m - (rabatt / 100m))
    // Falls anzahl <= 0 oder einzelpreis < 0m ist, soll 0m zurückgegeben werden.
    public static decimal BerechneGesamtpreis(decimal einzelpreis, int anzahl, decimal? rabattProzent)
    {
        // TODO: Berechne den Rabatt und den Gesamtpreis mit decimal
        return 0m;
    }

    // 🎯 TEILZIEL 3 (TODO 3): Namen sicher formatieren (Null-Safety)
    // Setze vorname und nachname zusammen: "{vorname} {nachname}".Trim()
    // Falls das Ergebnis leer ist oder beide Parameter null/whitespace sind, gib standardName zurück.
    public static string FormatName(string? vorname, string? nachname, string standardName)
    {
        // TODO: Behandle null-Werte und liefere den formatierten Namen oder standardName
        return "";
    }

    // 🎯 TEILZIEL 4 (TODO 4): Port-String sicher in Integer parsen
    // Versuche portInput mit int.TryParse zu parsen.
    // Ein Port ist gültig, wenn er zwischen 1 und 65535 (inklusive) liegt.
    // Bei ungültigem String, null oder außerhalb des Bereichs: gib defaultPort zurück.
    public static int ParseAppPort(string? portInput, int defaultPort)
    {
        // TODO: Parse und validiere den Port
        return 0;
    }
}

// Demo-Ausführung via Top-Level Statements:
Console.WriteLine(Aufgabe.ErstelleServerInfo("K8s-Node-01", 6443, 32.0, true));
Console.WriteLine($"Preis: {Aufgabe.BerechneGesamtpreis(29.90m, 3, 10m):F2} €");
Console.WriteLine($"User: {Aufgabe.FormatName("Ada", "Lovelace", "Gast")}");
Console.WriteLine($"Port: {Aufgabe.ParseAppPort("8080", 80)}");
""",
        "test": """using System;
using Xunit;

public class TestAufgabe
{
    // TEST: ErstelleServerInfo Produktion
    [Fact]
    public void Test_ErstelleServerInfo_Produktion()
    {
        string result = Aufgabe.ErstelleServerInfo("ProductionGateway", 443, 64.0, true);
        Assert.Equal("ProductionGateway (Port 443) - 64.0 GB RAM [PROD]", result);
    }

    // TEST: ErstelleServerInfo Development
    [Fact]
    public void Test_ErstelleServerInfo_Development()
    {
        string result = Aufgabe.ErstelleServerInfo("DevBox", 3000, 8.56, false);
        Assert.Equal("DevBox (Port 3000) - 8.6 GB RAM [DEV]", result);
    }

    // TEST: BerechneGesamtpreis ohne Rabatt
    [Fact]
    public void Test_BerechneGesamtpreis_OhneRabatt()
    {
        decimal result = Aufgabe.BerechneGesamtpreis(50m, 2, null);
        Assert.Equal(100m, result);
    }

    // TEST: BerechneGesamtpreis mit Rabatt
    [Fact]
    public void Test_BerechneGesamtpreis_MitRabatt()
    {
        decimal result = Aufgabe.BerechneGesamtpreis(100m, 2, 20m);
        Assert.Equal(160m, result);
    }

    // TEST: BerechneGesamtpreis ungueltige Werte
    [Fact]
    public void Test_BerechneGesamtpreis_UngueltigeWerte()
    {
        Assert.Equal(0m, Aufgabe.BerechneGesamtpreis(-10m, 5, 10m));
        Assert.Equal(0m, Aufgabe.BerechneGesamtpreis(50m, 0, null));
        Assert.Equal(0m, Aufgabe.BerechneGesamtpreis(50m, -2, 10m));
    }

    // TEST: FormatName mit Vor- und Nachname
    [Fact]
    public void Test_FormatName_Gueltig()
    {
        Assert.Equal("Alan Turing", Aufgabe.FormatName("Alan", "Turing", "Unbekannt"));
        Assert.Equal("Linus", Aufgabe.FormatName("Linus", null, "Unbekannt"));
        Assert.Equal("Torvalds", Aufgabe.FormatName(null, "Torvalds", "Unbekannt"));
    }

    // TEST: FormatName Fallback
    [Fact]
    public void Test_FormatName_Fallback()
    {
        Assert.Equal("Gast-User", Aufgabe.FormatName(null, null, "Gast-User"));
        Assert.Equal("Gast-User", Aufgabe.FormatName("", "   ", "Gast-User"));
    }

    // TEST: ParseAppPort gueltig
    [Fact]
    public void Test_ParseAppPort_Gueltig()
    {
        Assert.Equal(8080, Aufgabe.ParseAppPort("8080", 80));
        Assert.Equal(443, Aufgabe.ParseAppPort("443", 80));
        Assert.Equal(1, Aufgabe.ParseAppPort("1", 80));
        Assert.Equal(65535, Aufgabe.ParseAppPort("65535", 80));
    }

    // TEST: ParseAppPort ungueltig
    [Fact]
    public void Test_ParseAppPort_UngueltigFallback()
    {
        Assert.Equal(80, Aufgabe.ParseAppPort(null, 80));
        Assert.Equal(80, Aufgabe.ParseAppPort("invalid", 80));
        Assert.Equal(80, Aufgabe.ParseAppPort("0", 80));
        Assert.Equal(80, Aufgabe.ParseAppPort("70000", 80));
        Assert.Equal(80, Aufgabe.ParseAppPort("-5", 80));
    }
}
""",
        "muster": """using System;

public static class Aufgabe
{
    public static string ErstelleServerInfo(string name, int port, double ramGb, bool isProduction)
    {
        string env = isProduction ? "PROD" : "DEV";
        return $"{name} (Port {port}) - {ramGb:F1} GB RAM [{env}]";
    }

    public static decimal BerechneGesamtpreis(decimal einzelpreis, int anzahl, decimal? rabattProzent)
    {
        if (einzelpreis < 0m || anzahl <= 0)
        {
            return 0m;
        }

        decimal rabatt = rabattProzent ?? 0m;
        decimal brutto = einzelpreis * anzahl;
        return brutto * (1m - (rabatt / 100m));
    }

    public static string FormatName(string? vorname, string? nachname, string standardName)
    {
        string v = vorname?.Trim() ?? "";
        string n = nachname?.Trim() ?? "";

        string kombiniert = $"{v} {n}".Trim();
        return string.IsNullOrWhiteSpace(kombiniert) ? standardName : kombiniert;
    }

    public static int ParseAppPort(string? portInput, int defaultPort)
    {
        if (int.TryParse(portInput, out int port) && port >= 1 && port <= 65535)
        {
            return port;
        }
        return defaultPort;
    }
}
""",
        "html_content": """        <!-- 1. THEORIE: TOP LEVEL & VARIABLEN -->
        <section class="card">
          <h2>💡 1. Top-Level Statements &amp; Modernes C# 12</h2>
          <p>In modernem C# entfällt das starre <code>class Program { static void Main() }</code> Gerüst. Deine Datei beginnt direkt mit ausführbarem Code:</p>
          
          <pre><code>// Modernes Top-Level Statement in C#:
string appName = "Enterprise Cloud Service";
int workerThreads = 16;
var isHealthy = true; // Typ automatisch 'bool' dank 'var'

Console.WriteLine($"Status von {appName}: Aktiv ({workerThreads} Threads, Healthy: {isHealthy})");</code></pre>

          <div class="box box-analogie">
            <div class="box-title">🏢 Analogie: Wertetypen (Stack) vs. Referenztypen (Heap)</div>
            <p><strong>Wertetypen (Value Types)</strong> wie <code>int</code>, <code>double</code>, <code>decimal</code> sind wie handschriftliche Notizzettel in deiner Hosentasche (Stack) – extrem schnell und direkt im Zugriff. <strong>Referenztypen (Reference Types)</strong> wie <code>string</code> oder <code>class</code> sind wie Schließfächer im Banktresor (Heap): Die Variable hält nur den Schlüssel (die Speicheradresse / Referenz) zum eigentlichen Objekt.</p>
          </div>
        </section>

        <!-- 2. THEORIE: NULLABLE REFERENCE TYPES -->
        <section class="card">
          <h2>🛡️ 2. Nullable Reference Types &amp; Null-Safety</h2>
          <p>C# verhindert den berüchtigten <em>Billion Dollar Mistake</em> durch strikte Null-Prüfungen zur Compile-Zeit:</p>

          <div style="overflow-x: auto;">
            <table style="width: 100%; border-collapse: collapse; font-size: 0.9rem; margin-bottom: 16px;">
              <thead>
                <tr style="border-bottom: 2px solid var(--border-color); background: var(--bg-subtle);">
                  <th style="padding: 8px 12px;">C# Syntax</th>
                  <th style="padding: 8px 12px;">Bedeutung</th>
                  <th style="padding: 8px 12px;">Beispiel</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom: 1px solid var(--border-color);">
                  <td style="padding: 8px 12px;"><code>string</code></td>
                  <td style="padding: 8px 12px;">Non-Nullable (Darf niemals <code>null</code> sein)</td>
                  <td style="padding: 8px 12px;"><code>string title = "C# Mastery";</code></td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-color);">
                  <td style="padding: 8px 12px;"><code>string?</code></td>
                  <td style="padding: 8px 12px;">Nullable (Kann Text oder <code>null</code> enthalten)</td>
                  <td style="padding: 8px 12px;"><code>string? nickname = null;</code></td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-color);">
                  <td style="padding: 8px 12px;"><code>??</code> (Coalescing)</td>
                  <td style="padding: 8px 12px;">Fallback-Wert falls links <code>null</code> ist</td>
                  <td style="padding: 8px 12px;"><code>string user = nickname ?? "Gast";</code></td>
                </tr>
                <tr>
                  <td style="padding: 8px 12px;"><code>?.</code> (Conditional)</td>
                  <td style="padding: 8px 12px;">Sicherer Zugriff nur wenn nicht <code>null</code></td>
                  <td style="padding: 8px 12px;"><code>int? len = nickname?.Length;</code></td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- 3. THEORIE: STRING INTERPOLATION & DECIMAL -->
        <section class="card">
          <h2>💰 3. String-Interpolation &amp; <code>decimal</code> für Finanzen</h2>
          <p>Für Finanz- und Währungsberechnungen in Enterprise-Anwendungen nutzt C# den präzisen 128-Bit Datentyp <code>decimal</code> (Suffix <code>m</code>):</p>
          <pre><code>decimal einzelpreis = 19.99m;
int anzahl = 5;
decimal? rabatt = 15m; // 15% Rabatt

decimal faktor = 1m - ((rabatt ?? 0m) / 100m);
decimal endpreis = einzelpreis * anzahl * faktor;

// Formatierung mit :F2 (zwei Dezimalstellen)
Console.WriteLine($"Endbetrag: {endpreis:F2} €");</code></pre>
        </section>

        <!-- 4. AUFGABEN CHECKLISTE -->
        <section class="card">
          <h2>🎯 Aufgaben &amp; Checkliste in <code>Aufgabe.cs</code></h2>
          <div class="task-item">
            <input type="checkbox" class="task-checkbox" id="t1">
            <label class="task-label" for="t1"><strong>TODO 1:</strong> <code>ErstelleServerInfo</code>: Liefere formatierten String <code>"{name} (Port {port}) - {ramGb:F1} GB RAM [{PROD/DEV}]"</code>.</label>
          </div>
          <div class="task-item">
            <input type="checkbox" class="task-checkbox" id="t2">
            <label class="task-label" for="t2"><strong>TODO 2:</strong> <code>BerechneGesamtpreis</code>: Berechne Gesamtpreis mit <code>decimal</code> und Null-Coalescing <code>rabattProzent ?? 0m</code>.</label>
          </div>
          <div class="task-item">
            <input type="checkbox" class="task-checkbox" id="t3">
            <label class="task-label" for="t3"><strong>TODO 3:</strong> <code>FormatName</code>: Kombiniere Vor- und Nachname mit Null-Safety oder liefere <code>standardName</code>.</label>
          </div>
          <div class="task-item">
            <input type="checkbox" class="task-checkbox" id="t4">
            <label class="task-label" for="t4"><strong>TODO 4:</strong> <code>ParseAppPort</code>: Parse mit <code>int.TryParse</code> und validiere Portbereich <code>1..65535</code>.</label>
          </div>

          <div class="box box-tipp" style="margin-top: 20px;">
            <div class="box-title">💡 .NET Pro-Tipp: String.IsNullOrWhiteSpace()</div>
            <p>Nutze die Methode <code>string.IsNullOrWhiteSpace(str)</code>, um gleichzeitig auf <code>null</code>, leere Strings <code>""</code> und reine Leerzeichen <code>"   "</code> zu prüfen!</p>
          </div>

          <div style="margin-top: 25px; display: flex; gap: 12px; flex-wrap: wrap;">
            <a href="../../../workspace.html?course=csharp&track=track_1_csharp_basics&chapter=01_syntax_datentypen_und_top_level_statements" class="btn" style="background: #7c3aed; color: #fff; font-weight: 700;">💻 In Web-IDE öffnen &rarr;</a>
            <a href="../02_kontrollfluss_und_pattern_matching/index.html" class="btn btn-secondary">Weiter zu C# 02 &rarr;</a>
          </div>
        </section>"""
    }
]

print("Module data defined.")
