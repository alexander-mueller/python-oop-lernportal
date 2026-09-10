#!/usr/bin/env python3
"""
Java Modules Generator for Courses: Lehrpfad 1 & 2 (Module 01 bis 08)
Erstellt alle 8 Module mit:
- index.html
- README.md
- Aufgabe.java
- TestAufgabe.java
- Musterloesung.java
"""

import os
from pathlib import Path

BASE_DIR = Path("/root/uebungen_python/courses/java")

# ==============================================================================
# MODUL 01: Java Syntax & Primitive Datentypen
# ==============================================================================
MOD_01_INDEX = """<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Java 01: Java Syntax &amp; Primitive Datentypen</title>
  <link rel="stylesheet" href="../../../assets/style.css">
</head>
<body>
  <div class="app-layout">
    <div class="app-main">
      <header>
        <div class="header-container">
          <div class="header-badge">☕ Java 21+ Enterprise &amp; IHK/Uni Standard</div>
          <h1>Java 01: Syntax, Primitive Datentypen &amp; Type Casting</h1>
          <p>Tauche ein in das strenge, statische Typensystem von Java: Lerne die 8 primitiven Datentypen, den JVM Entry-Point <code>public static void main</code> und sicheres Type Casting.</p>
        </div>
      </header>

      <main class="container">
        <!-- 1. THEORIE: STRUKTUR & MAIN -->
        <section class="card">
          <h2>🏛️ 1. Grundstruktur eines Java-Programms</h2>
          <p>In Java ist alles in <strong>Klassen</strong> organisiert. Der Dateiname muss exakt dem Namen der <code>public class</code> entsprechen (inklusive Groß-/Kleinschreibung):</p>
          
          <pre><code>public class Aufgabe {
    // Der Einstiegspunkt für die Java Virtual Machine (JVM)
    public static void main(String[] args) {
        System.out.println("Willkommen in Java 21 Enterprise!");
    }
}</code></pre>

          <div class="box box-analogie">
            <div class="box-title">🏢 Didaktische Analogie: Der Schlüssel zum Haupttor</div>
            <p>Die <code>main</code>-Methode ist der Generalschlüssel der JVM: <code>public</code> (jeder darf rein), <code>static</code> (das Gebäude muss nicht erst instanziiert werden), <code>void</code> (keine Rückgabe an das Betriebssystem nötig) und <code>String[] args</code> (die Übergabeparameter beim Starten).</p>
          </div>
        </section>

        <!-- 2. THEORIE: PRIMITIVE DATENTYPEN -->
        <section class="card">
          <h2>🔢 2. Die 8 primitiven Datentypen</h2>
          <p>Java unterscheidet strikt zwischen <strong>primitiven Typen</strong> (direkt auf dem Stack gespeichert) und <strong>Referenztypen</strong> (Objekte auf dem Heap):</p>

          <div style="overflow-x: auto;">
            <table style="width: 100%; border-collapse: collapse; font-size: 0.9rem; margin-bottom: 16px;">
              <thead>
                <tr style="border-bottom: 2px solid var(--border-color); background: var(--bg-subtle);">
                  <th style="padding: 8px 12px;">Typ</th>
                  <th style="padding: 8px 12px;">Größe</th>
                  <th style="padding: 8px 12px;">Wertebereich</th>
                  <th style="padding: 8px 12px;">Standardwert</th>
                  <th style="padding: 8px 12px;">Beispiel</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom: 1px solid var(--border-color);">
                  <td style="padding: 8px 12px;"><code>byte</code></td>
                  <td style="padding: 8px 12px;">8 Bit (1 Byte)</td>
                  <td style="padding: 8px 12px;">-128 bis 127</td>
                  <td style="padding: 8px 12px;"><code>0</code></td>
                  <td style="padding: 8px 12px;"><code>byte b = 42;</code></td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-color);">
                  <td style="padding: 8px 12px;"><code>short</code></td>
                  <td style="padding: 8px 12px;">16 Bit (2 Byte)</td>
                  <td style="padding: 8px 12px;">-32.768 bis 32.767</td>
                  <td style="padding: 8px 12px;"><code>0</code></td>
                  <td style="padding: 8px 12px;"><code>short s = 1024;</code></td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-color);">
                  <td style="padding: 8px 12px;"><code>int</code></td>
                  <td style="padding: 8px 12px;">32 Bit (4 Byte)</td>
                  <td style="padding: 8px 12px;">-2.147.483.648 bis 2.147.483.647</td>
                  <td style="padding: 8px 12px;"><code>0</code></td>
                  <td style="padding: 8px 12px;"><code>int port = 8080;</code></td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-color);">
                  <td style="padding: 8px 12px;"><code>long</code></td>
                  <td style="padding: 8px 12px;">64 Bit (8 Byte)</td>
                  <td style="padding: 8px 12px;">-9 Trillionen bis +9 Trillionen</td>
                  <td style="padding: 8px 12px;"><code>0L</code></td>
                  <td style="padding: 8px 12px;"><code>long timestamp = 1700000000000L;</code></td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-color);">
                  <td style="padding: 8px 12px;"><code>float</code></td>
                  <td style="padding: 8px 12px;">32 Bit (4 Byte)</td>
                  <td style="padding: 8px 12px;">~6-7 Dezimalstellen</td>
                  <td style="padding: 8px 12px;"><code>0.0f</code></td>
                  <td style="padding: 8px 12px;"><code>float pi = 3.14159f;</code></td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-color);">
                  <td style="padding: 8px 12px;"><code>double</code></td>
                  <td style="padding: 8px 12px;">64 Bit (8 Byte)</td>
                  <td style="padding: 8px 12px;">~15-16 Dezimalstellen (Standard)</td>
                  <td style="padding: 8px 12px;"><code>0.0d</code></td>
                  <td style="padding: 8px 12px;"><code>double saldo = 1250.75;</code></td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-color);">
                  <td style="padding: 8px 12px;"><code>boolean</code></td>
                  <td style="padding: 8px 12px;">1 Bit / JVM</td>
                  <td style="padding: 8px 12px;"><code>true</code> oder <code>false</code></td>
                  <td style="padding: 8px 12px;"><code>false</code></td>
                  <td style="padding: 8px 12px;"><code>boolean isProd = true;</code></td>
                </tr>
                <tr>
                  <td style="padding: 8px 12px;"><code>char</code></td>
                  <td style="padding: 8px 12px;">16 Bit (2 Byte)</td>
                  <td style="padding: 8px 12px;">Unicode (0 bis 65.535)</td>
                  <td style="padding: 8px 12px;"><code>'\\u0000'</code></td>
                  <td style="padding: 8px 12px;"><code>char grade = 'A';</code></td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- 3. THEORIE: TYPE CASTING -->
        <section class="card">
          <h2>🔄 3. Type Casting: Widening vs. Narrowing</h2>
          <p>Wenn Werte zwischen Datentypen übergeben werden, unterscheidet Java zwei Fälle:</p>

          <pre><code>// 1. Widening Casting (Automatisch/Implizit - kein Datenverlust):
// byte -> short -> char -> int -> long -> float -> double
int kleineZahl = 100;
double kommazahl = kleineZahl; // 100.0 (Automatisch erweitert)

// 2. Narrowing Casting (Manuell/Explizit - möglicher Datenverlust/Überlauf):
// double -> float -> long -> int -> char -> short -> byte
double preis = 99.99;
int gerundet = (int) preis;   // 99 (Nachkommastellen werden abgeschnitten!)

// ⚠️ Vorsicht bei Ganzzahl-Division:
int summe = 10;
int anzahl = 4;
double falsch = summe / anzahl;          // Ergibt 2.0 (Ganzzahldivision 10/4 = 2!)
double richtig = (double) summe / anzahl; // Ergibt 2.5 (10.0 / 4 = 2.5)</code></pre>
        </section>

        <!-- 4. AUFGABEN CHECKLISTE -->
        <section class="card">
          <h2>🎯 Aufgaben &amp; Checkliste in <code>Aufgabe.java</code></h2>
          <div class="task-item">
            <input type="checkbox" class="task-checkbox" id="t1">
            <label class="task-label" for="t1"><strong>TODO 1:</strong> <code>getServerInfo(serverName, port, cpuUsage, isProduction, status)</code> formatieren.</label>
          </div>
          <div class="task-item">
            <input type="checkbox" class="task-checkbox" id="t2">
            <label class="task-label" for="t2"><strong>TODO 2:</strong> <code>berechneNotendurchschnitt(summePunkte, anzahlPruefungen)</code> mit explizitem Cast zu <code>double</code> fehlerfrei berechnen.</label>
          </div>
          <div class="task-item">
            <input type="checkbox" class="task-checkbox" id="t3">
            <label class="task-label" for="t3"><strong>TODO 3:</strong> <code>verschiebeZeichen(c, offset)</code> und <code>istGrossbuchstabe(c)</code> mit Unicode/char-Arithmetik umsetzen.</label>
          </div>
          <div class="task-item">
            <input type="checkbox" class="task-checkbox" id="t4">
            <label class="task-label" for="t4"><strong>TODO 4:</strong> <code>konvertiereZuByte(wert)</code> mit Bereichsprüfung (-128 bis 127) und Narrowing Cast programmieren.</label>
          </div>

          <div class="box box-tipp" style="margin-top: 20px;">
            <div class="box-title">💡 Java Pro-Tipp: String.format &amp; Locale</div>
            <p>Nutze <code>String.format(java.util.Locale.US, "%.1f%%", cpuUsage * 100)</code> für international standardisierte Punktdarstellung bei Fließkommazahlen.</p>
          </div>

          <div style="margin-top: 25px; display: flex; gap: 12px; flex-wrap: wrap;">
            <a href="../../../workspace.html?course=java&track=track_1_java_basics&chapter=01_java_syntax_und_primitive_typen" class="btn" style="background: #e11d48; color: #fff; font-weight: 700;">💻 In Web-IDE öffnen &rarr;</a>
            <a href="../02_kontrollfluss_und_verzweigungen/index.html" class="btn btn-secondary">Weiter zu Java 02 &rarr;</a>
          </div>
        </section>
      </main>
    </div>
  </div>
</body>
</html>
"""

MOD_01_README = """# ☕ Java 01: Syntax, Primitive Datentypen & Type Casting

Willkommen zum ersten Modul des Java Enterprise Kurses! In dieser Einheit lernst du die fundamentale Struktur von Java-Programmen, das strenge statische Typensystem und den sicheren Umgang mit Typkonvertierungen kennen.

---

## 🎯 Lernziele

Nach Bearbeitung dieses Moduls kannst du:
1. Den Aufbau einer Java-Klasse und die Signatur der `public static void main(String[] args)` Methode fehlerfrei erklären.
2. Alle **8 primitiven Datentypen** (`byte`, `short`, `int`, `long`, `float`, `double`, `boolean`, `char`) zielgerichtet auswählen und Speichergrößen abschätzen.
3. Den Unterschied zwischen **Stack-Speicher** (primitive Typen) und **Heap-Speicher** (Objekte) verstehen.
4. **Widening** (implizit) und **Narrowing** (explizit) Type Casting anwenden und Ganzzahldivisions-Fallen vermeiden.
5. Zeichenarithmetik mit `char` und Unicode durchführen.

---

## 💡 Theoretische Grundlagen

### 1. Das statische Typensystem von Java
Java ist streng und statisch typisiert. Das bedeutet: Jede Variable besitzt bereits zur **Compile-Zeit** einen unveränderlichen Typ.

```java
int port = 8080;
// port = "achtzig"; // COMPILE-FEHLER: Incompatible types!
```

### 2. Primitive Datentypen im Überblick

| Typ | Bit-Breite | Wertebereich | Standardwert |
| :--- | :--- | :--- | :--- |
| `byte` | 8 Bit | -128 bis 127 | `0` |
| `short` | 16 Bit | -32.768 bis 32.767 | `0` |
| `int` | 32 Bit | -2.147.483.648 bis 2.147.483.647 | `0` |
| `long` | 64 Bit | -9 Trillionen bis +9 Trillionen | `0L` |
| `float` | 32 Bit | IEEE 754 Fließkomma (~7 Dezimalstellen) | `0.0f` |
| `double` | 64 Bit | IEEE 754 Fließkomma (~16 Dezimalstellen) | `0.0d` |
| `boolean` | 1 Bit / JVM | `true` oder `false` | `false` |
| `char` | 16 Bit | Unicode `\\u0000` bis `\\uffff` (0 bis 65.535) | `'\\u0000'` |

### 3. Type Casting (Typumwandlung)

```java
// Widening (Automatisch ohne Informationsverlust):
int count = 42;
double countDouble = count; // 42.0

// Narrowing (Expliziter Cast erforderlich, da Daten verloren gehen können):
double preis = 19.99;
int euro = (int) preis; // 19 (Nachkommastelle wird abgeschnitten!)

// ⚠️ Typische Falle: Ganzzahldivision
int a = 7;
int b = 2;
double res1 = a / b;          // 3.0 (weil 7/2 als int gerechnet wird!)
double res2 = (double) a / b; // 3.5 (7.0 / 2 wird als double gerechnet)
```

---

## 🎯 Aufgabenübersicht in `Aufgabe.java`

1. **TODO 1: `getServerInfo(...)`**:
   Erzeuge einen formatierten String aus Servername, Port, CPU-Last in Prozent, Produktionsstatus und Status-Zeichen.
2. **TODO 2: `berechneNotendurchschnitt(...)`**:
   Berechne den exakten Notendurchschnitt mit `(double) summe / anzahl`. Gib `0.0` zurück bei `anzahl <= 0`.
3. **TODO 3: `verschiebeZeichen(...)` & `istGrossbuchstabe(...)`**:
   Führe Unicode-Verschiebung durch und prüfe auf Großbuchstaben (`'A'` bis `'Z'`).
4. **TODO 4: `konvertiereZuByte(...)`**:
   Überprüfe, ob der Wert im Bereich `-128` bis `127` liegt. Falls nicht, wirf eine `IllegalArgumentException`. Führe ansonsten den Narrowing Cast `(byte) wert` durch.

---

## 🧪 Tests ausführen

In der Web-IDE: Klicke auf **"Code ausführen & testen"**.
Lokal mit Standard-Java:
```bash
javac Aufgabe.java TestAufgabe.java
java TestAufgabe
```
"""

MOD_01_AUFGABE = """public class Aufgabe {

    // 🎯 TEILZIEL 1 (TODO 1): Server-Konfigurationsdaten als String formatieren
    // Format: "Server: [serverName] | Port: [port] | CPU: [cpuUsage in %] | Status: [status] | Prod: [isProduction]"
    // Beispiel: getServerInfo("PROD-1", 8080, 0.755, true, 'A')
    // Rückgabe: "Server: PROD-1 | Port: 8080 | CPU: 75.5% | Status: A | Prod: true"
    // Hinweis: Nutze java.util.Locale.US für Punkt-Notation bei Prozentangaben (%.1f%%).
    public static String getServerInfo(String serverName, int port, double cpuUsage, boolean isProduction, char status) {
        // TODO: Implementiere die Formatierung
        return "";
    }

    // 🎯 TEILZIEL 2 (TODO 2): Genauen Notendurchschnitt mit Typkonvertierung berechnen
    // Berechne den Durchschnitt als double.
    // Falls anzahlPruefungen <= 0 ist, gib 0.0 zurück.
    // Achte darauf, dass KEINE Ganzzahldivision stattfindet!
    public static double berechneNotendurchschnitt(int summePunkte, int anzahlPruefungen) {
        // TODO: Prüfe auf <= 0 und führe expliziten Type Cast durch
        return 0.0;
    }

    // 🎯 TEILZIEL 3 (TODO 3): Char-Transformation & Unicode-Arithmetik
    // Verschiebt das gegebene Zeichen c um 'offset' Positionen im Zeichensatz.
    // Beispiel: verschiebeZeichen('A', 3) -> 'D'
    // Beispiel: verschiebeZeichen('a', 1) -> 'b'
    public static char verschiebeZeichen(char c, int offset) {
        // TODO: Führe char-Arithmetik mit explizitem Cast (char)(...) durch
        return ' ';
    }

    // Prüft, ob das gegebene Zeichen ein lateinischer Großbuchstabe ('A' bis 'Z') ist.
    public static boolean istGrossbuchstabe(char c) {
        // TODO: Prüfe den Bereich 'A' <= c <= 'Z'
        return false;
    }

    // 🎯 TEILZIEL 4 (TODO 4): Narrowing Casting mit Wertebereichs-Prüfung
    // Konvertiert einen int-Wert sicher in einen byte (-128 bis 127).
    // Falls der Wert < -128 oder > 127 ist, soll eine IllegalArgumentException mit der Nachricht
    // "Wert außerhalb des Byte-Bereichs: " + wert geworfen werden.
    public static byte konvertiereZuByte(int wert) {
        // TODO: Validiere Wertebereich und caste zu byte
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(getServerInfo("PROD-1", 8080, 0.755, true, 'A'));
        System.out.println("Schnitt (15 Punkte / 4): " + berechneNotendurchschnitt(15, 4));
        System.out.println("Verschiebe 'A' um 3: " + verschiebeZeichen('A', 3));
        System.out.println("Ist 'G' groß? " + istGrossbuchstabe('G'));
        System.out.println("Byte-Cast (42): " + konvertiereZuByte(42));
    }
}
"""

MOD_01_TEST = """import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import static org.junit.jupiter.api.Assertions.*;

public class TestAufgabe {

    @Test
    @DisplayName("TODO 1: getServerInfo formatiert alle primitiven Typen korrekt")
    void testGetServerInfo() {
        String info1 = Aufgabe.getServerInfo("PROD-1", 8080, 0.755, true, 'A');
        assertEquals("Server: PROD-1 | Port: 8080 | CPU: 75.5% | Status: A | Prod: true", info1);

        String info2 = Aufgabe.getServerInfo("DEV-NODE", 3000, 0.12, false, 'I');
        assertEquals("Server: DEV-NODE | Port: 3000 | CPU: 12.0% | Status: I | Prod: false", info2);
    }

    @Test
    @DisplayName("TODO 2: berechneNotendurchschnitt verhindert Ganzzahldivision & Division durch 0")
    void testBerechneNotendurchschnitt() {
        assertEquals(3.75, Aufgabe.berechneNotendurchschnitt(15, 4), 0.0001);
        assertEquals(2.3333, Aufgabe.berechneNotendurchschnitt(7, 3), 0.001);
        assertEquals(0.0, Aufgabe.berechneNotendurchschnitt(100, 0), 0.0001);
        assertEquals(0.0, Aufgabe.berechneNotendurchschnitt(50, -2), 0.0001);
    }

    @Test
    @DisplayName("TODO 3: verschiebeZeichen und istGrossbuchstabe arbeiten mit Unicode/ASCII")
    void testCharOperationen() {
        assertEquals('D', Aufgabe.verschiebeZeichen('A', 3));
        assertEquals('z', Aufgabe.verschiebeZeichen('a', 25));
        assertEquals('A', Aufgabe.verschiebeZeichen('C', -2));

        assertTrue(Aufgabe.istGrossbuchstabe('A'));
        assertTrue(Aufgabe.istGrossbuchstabe('M'));
        assertTrue(Aufgabe.istGrossbuchstabe('Z'));
        assertFalse(Aufgabe.istGrossbuchstabe('a'));
        assertFalse(Aufgabe.istGrossbuchstabe('1'));
        assertFalse(Aufgabe.istGrossbuchstabe('!'));
    }

    @Test
    @DisplayName("TODO 4: konvertiereZuByte wirft Exception bei Überlauf und castet gültige Werte")
    void testKonvertiereZuByte() {
        assertEquals((byte) 42, Aufgabe.konvertiereZuByte(42));
        assertEquals((byte) -128, Aufgabe.konvertiereZuByte(-128));
        assertEquals((byte) 127, Aufgabe.konvertiereZuByte(127));

        assertThrows(IllegalArgumentException.class, () -> Aufgabe.konvertiereZuByte(128));
        assertThrows(IllegalArgumentException.class, () -> Aufgabe.konvertiereZuByte(-129));
        assertThrows(IllegalArgumentException.class, () -> Aufgabe.konvertiereZuByte(1000));
    }

    // Standalone Runner für direkte Ausführung ohne externes Framework
    public static void main(String[] args) {
        System.out.println("🧪 Starte Tests für Java 01: Syntax & Primitive Typen...");
        TestAufgabe t = new TestAufgabe();
        int passed = 0;
        int total = 4;

        try { t.testGetServerInfo(); passed++; System.out.println("  [✔] Test 1: getServerInfo PASSED"); } catch (Throwable e) { System.out.println("  [✘] Test 1 FAILED: " + e.getMessage()); }
        try { t.testBerechneNotendurchschnitt(); passed++; System.out.println("  [✔] Test 2: berechneNotendurchschnitt PASSED"); } catch (Throwable e) { System.out.println("  [✘] Test 2 FAILED: " + e.getMessage()); }
        try { t.testCharOperationen(); passed++; System.out.println("  [✔] Test 3: Char-Operationen PASSED"); } catch (Throwable e) { System.out.println("  [✘] Test 3 FAILED: " + e.getMessage()); }
        try { t.testKonvertiereZuByte(); passed++; System.out.println("  [✔] Test 4: konvertiereZuByte PASSED"); } catch (Throwable e) { System.out.println("  [✘] Test 4 FAILED: " + e.getMessage()); }

        System.out.printf("\\nErgebnis: %d/%d Tests bestanden.\\n", passed, total);
        if (passed == total) {
            System.out.println("🎉 Alle Tests erfolgreich!");
        } else {
            System.exit(1);
        }
    }
}
"""

MOD_01_LOESUNG = """import java.util.Locale;

public class Musterloesung {

    // 🎯 TEILZIEL 1: Server-Konfigurationsdaten als String formatieren
    public static String getServerInfo(String serverName, int port, double cpuUsage, boolean isProduction, char status) {
        return String.format(Locale.US, "Server: %s | Port: %d | CPU: %.1f%% | Status: %c | Prod: %b",
                serverName, port, cpuUsage * 100.0, status, isProduction);
    }

    // 🎯 TEILZIEL 2: Genauen Notendurchschnitt mit Typkonvertierung berechnen
    public static double berechneNotendurchschnitt(int summePunkte, int anzahlPruefungen) {
        if (anzahlPruefungen <= 0) {
            return 0.0;
        }
        return (double) summePunkte / anzahlPruefungen;
    }

    // 🎯 TEILZIEL 3: Char-Transformation & Unicode-Arithmetik
    public static char verschiebeZeichen(char c, int offset) {
        return (char) (c + offset);
    }

    public static boolean istGrossbuchstabe(char c) {
        return c >= 'A' && c <= 'Z';
    }

    // 🎯 TEILZIEL 4: Narrowing Casting mit Wertebereichs-Prüfung
    public static byte konvertiereZuByte(int wert) {
        if (wert < -128 || wert > 127) {
            throw new IllegalArgumentException("Wert außerhalb des Byte-Bereichs: " + wert);
        }
        return (byte) wert;
    }

    public static void main(String[] args) {
        System.out.println(getServerInfo("PROD-1", 8080, 0.755, true, 'A'));
        System.out.println("Schnitt: " + berechneNotendurchschnitt(15, 4));
        System.out.println("Char: " + verschiebeZeichen('A', 3));
        System.out.println("Großbuchstabe: " + istGrossbuchstabe('X'));
        System.out.println("Byte: " + konvertiereZuByte(100));
    }
}
"""

print("Modul 01 Data ready.")
