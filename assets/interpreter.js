/**
 * 🩺 PYTHON TRACEBACK & FEHLER-DOLMETSCHER 🩺
 * ============================================
 * Basiert auf der didaktischen Fehlerforschung (Brett Becker et al., SIGCSE).
 * Übersetzt kryptische Python-Fehlermeldungen in einfühlsames, klares Deutsch
 * mit konkreten Handlungsanweisungen für Schülerinnen und Schüler.
 */

(function () {
  const ERROR_RULES = [
    {
      type: "SyntaxError",
      pattern: /SyntaxError: (invalid syntax|expected ':'|was never closed|cannot assign to expression)/i,
      title: "✍️ Schreibweise- & Grammatikfehler (SyntaxError)",
      explanation: "Python versteht den Aufbau deines Codes an dieser Stelle nicht. Meist fehlt ein Satzzeichen oder eine Klammer.",
      causes: [
        "Fehlender Doppelpunkt <code>:</code> am Ende von <code>def</code>, <code>if</code>, <code>elif</code>, <code>else</code>, <code>for</code> oder <code>while</code>.",
        "Eine geöffnete Klammer <code>(</code> oder ein Anführungszeichen <code>\"</code> wurde nicht geschlossen.",
        "Verwechslung von Zuweisung <code>=</code> und Vergleich <code>==</code> in einer <code>if</code>-Bedingung."
      ],
      fix: "Prüfe die Zeile ganz genau: Steht am Zeilenende ein Doppelpunkt? Sind alle Klammern und Anführungszeichen paarweise geschlossen? Nutze <code>if a == b:</code> zum Vergleichen!"
    },
    {
      type: "IndentationError",
      pattern: /IndentationError: (expected an indented block|unindent does not match)/i,
      title: "📐 Einrückungsfehler (IndentationError)",
      explanation: "Python nutzt Einrückungen (Standard: genau 4 Leerzeichen), um zu erkennen, welcher Code zu einer Funktion, `if`-Bedingung oder Schleife gehört.",
      causes: [
        "Nach einem Doppelpunkt (<code>def ...:</code>, <code>if ...:</code>, <code>for ...:</code>) fehlt die Einrückung.",
        "Leerzeichen und Tabulatoren wurden versehentlich gemischt."
      ],
      fix: "Drücke nach dem Doppelpunkt <kbd>Enter</kbd> und rücke die Zeile mit <kbd>Tab</kbd> oder 4 Leerzeichen ein. Mit <kbd>Umschalt</kbd> + <kbd>Tab</kbd> kannst du Zeilen wieder nach links rücken."
    },
    {
      type: "TypeError String Concatenation",
      pattern: /TypeError: can only concatenate str \(not "(int|float)"\) to str/i,
      title: "🔤 Text und Zahl vermischt (TypeError)",
      explanation: "Du versuchst einen Text (<code>str</code>) und eine Zahl (<code>int/float</code>) mit <code>+</code> zusammenzufügen.",
      causes: [
        "In Python kann man Text und Zahlen nicht einfach addieren (z.B. <code>\"Alter: \" + 16</code> schlägt fehl)."
      ],
      fix: "Nutze einen modernen <strong>f-String</strong>: <code>f\"Alter: {alter}\"</code> oder wandle die Zahl mit <code>str(zahl)</code> um."
    },
    {
      type: "TypeError NoneType",
      pattern: /TypeError: 'NoneType' object is not (subscriptable|iterable|callable)/i,
      title: "🕳️ Zugriff auf 'None' (TypeError)",
      explanation: "Du versuchst auf ein Objekt zuzugreifen, das gar nicht existiert oder den Wert <code>None</code> hat.",
      causes: [
        "Eine aufgerufene Funktion hat vergessen, ihr Ergebnis mit <code>return</code> zurückzugeben.",
        "Eine Listen-Methode wie <code>liste.sort()</code> oder <code>liste.append()</code> gibt immer <code>None</code> zurück (sie verändert die Liste direkt!)."
      ],
      fix: "Prüfe in deinen Funktionen, ob am Ende ein <code>return ergebnis</code> steht. Schreibe niemals <code>x = liste.sort()</code>, sondern nur <code>liste.sort()</code>."
    },
    {
      type: "AttributeError",
      pattern: /AttributeError: '([^']+)' object has no attribute '([^']+)'/i,
      title: "🔍 Unbekanntes Attribut oder Methode (AttributeError)",
      explanation: "Python konnte an dem Objekt die gewünschte Methode oder Eigenschaft nicht finden.",
      causes: [
        "Tippfehler im Namen der Methode oder Variable (z.B. <code>anhängen</code> statt <code>append</code>).",
        "Groß- und Kleinschreibung nicht beachtet (z.B. <code>.Name</code> statt <code>.name</code>).",
        "In der Klassen-Methode wurde <code>self.</code> vergessen (z.B. <code>alter</code> statt <code>self.alter</code>)."
      ],
      fix: "Überprüfe die Schreibweise des Attributs exakt Buchstabe für Buchstabe. Nutze in Klassen immer <code>self.attributname</code>."
    },
    {
      type: "TypeError self missing",
      pattern: /TypeError: ([^\(]+)\(\) takes \d+ positional arguments? but \d+ were given/i,
      title: "🧩 Fehlendes 'self' in Methoden-Definition (TypeError)",
      explanation: "Eine Methode in einer Klasse erwartet weniger oder mehr Parameter als übergeben wurden.",
      causes: [
        "Der klassische Anfängerfehler: Du hast im Methodenkopf das <code>self</code> als ersten Parameter vergessen! (z.B. <code>def fahren():</code> statt <code>def fahren(self):</code>)."
      ],
      fix: "Schreibe in jeder Methode deiner Klasse als allerersten Parameter immer <code>self</code>: z.B. <code>def beschleunigen(self, kmh):</code>."
    },
    {
      type: "IndexError",
      pattern: /IndexError: (list index out of range|string index out of range)/i,
      title: "🎯 Index außerhalb des gültigen Bereichs (IndexError)",
      explanation: "Du greifst auf eine Position (Index) in einer Liste oder einem String zu, die gar nicht existiert.",
      causes: [
        "Off-by-One Fehler: In Python beginnt die Zählung bei <code>0</code>! Eine Liste mit 3 Elementen hat nur die Indizes <code>0, 1, 2</code> (nicht 3).",
        "Die Liste ist noch leer."
      ],
      fix: "Prüfe die Länge der Liste mit <code>len(liste)</code>. Das letzte Element erreichst du immer sicher mit <code>liste[-1]</code>."
    },
    {
      type: "KeyError",
      pattern: /KeyError: (.+)/i,
      title: "🔑 Schlüssel nicht im Dictionary gefunden (KeyError)",
      explanation: "Du hast versucht, aus einem Dictionary <code>dict[schluessel]</code> einen Eintrag abzufragen, der nicht existiert.",
      causes: [
        "Der gesuchte Key ist nicht im Dictionary vorhanden oder falsch geschrieben."
      ],
      fix: "Nutze die sichere Abfrage mit <code>dict.get(key, standardwert)</code> statt der eckigen Klammern, um Abstürze zu vermeiden!"
    },
    {
      type: "NameError",
      pattern: /NameError: name '([^']+)' is not defined/i,
      title: "❓ Name nicht definiert (NameError)",
      explanation: "Python kennt das Wort oder die Variable an dieser Stelle nicht.",
      causes: [
        "Die Variable wurde weiter unten oder in einer anderen Funktion definiert (Gültigkeitsbereich/Scope).",
        "Ein Tippfehler im Variablennamen.",
        "Ein Modul wie <code>import math</code> wurde noch nicht importiert."
      ],
      fix: "Prüfe, ob du die Variable vor ihrer Benutzung angelegt hast und ob alle benötigten Module oben mit <code>import ...</code> eingebunden sind."
    },
    {
      type: "ValueError",
      pattern: /ValueError: (invalid literal for int\(\)|math domain error)/i,
      title: "⚠️ Ungültiger Wert (ValueError)",
      explanation: "Der Datentyp war zwar richtig, aber der übergebene Wert macht für diesen Befehl keinen Sinn.",
      causes: [
        "Umwandlung von Text mit Buchstaben in eine Zahl (z.B. <code>int(\"hallo\")</code>).",
        "Mathematisch unzulässige Werte (z.B. Wurzel aus einer negativen Zahl)."
      ],
      fix: "Prüfe vorher mit <code>text.isdigit()</code>, ob der Text nur aus Ziffern besteht, oder sichere die Umwandlung mit <code>try-except ValueError:</code> ab."
    },
    {
      type: "AssertionError",
      pattern: /AssertionError: (.+)/i,
      title: "🧪 Unittest fehlgeschlagen (AssertionError)",
      explanation: "Dein Programmcode läuft zwar ohne Absturz durch, liefert aber noch nicht das von der Aufgabe erwartete Ergebnis.",
      causes: [
        "Ein Rechenfehler oder eine falsche Formel in der Funktion.",
        "Rückgabewert vergessen (<code>return</code> fehlt).",
        "Grenzfall nicht beachtet (z.B. 0 oder leere Liste)."
      ],
      fix: "Vergleiche die Rückgabe deiner Funktion mit dem in der Testmeldung geforderten Soll-Wert. Lies die Aufgabenbeschreibung noch einmal aufmerksam durch!"
    },
    {
      type: "ZeroDivisionError",
      pattern: /ZeroDivisionError: division by zero/i,
      title: "➗ Division durch Null (ZeroDivisionError)",
      explanation: "In der Mathematik und in Python ist das Teilen durch <code>0</code> nicht erlaubt.",
      causes: [
        "Der Nenner / Teiler hat den Wert <code>0</code>."
      ],
      fix: "Sichere die Division mit einer <code>if teiler != 0:</code> Bedingung oder fange sie mit <code>try-except ZeroDivisionError:</code> ab."
    }
  ];

  window.interpretiereTraceback = function (errorText) {
    if (!errorText || !errorText.trim()) {
      return {
        matched: false,
        name: "💡 Bitte füge eine Fehlermeldung ein",
        title: "💡 Bitte füge eine Fehlermeldung ein",
        explanation: "Kopiere deinen Traceback aus dem Terminal und füge ihn hier ein.",
        causes: ["Noch keine Fehlermeldung eingegeben."],
        fixes: ["Starte deinen Code oder Unittests, um eventuelle Fehler zu sehen."],
        fix: "Starte deinen Code oder Unittests, um eventuelle Fehler zu sehen."
      };
    }

    for (let rule of ERROR_RULES) {
      if (rule.pattern.test(errorText)) {
        return {
          matched: true,
          type: rule.type,
          name: rule.title,
          title: rule.title,
          explanation: rule.explanation,
          causes: rule.causes,
          fixes: [rule.fix],
          fix: rule.fix
        };
      }
    }

    return {
      matched: false,
      name: "🔍 Allgemeiner Python-Fehler",
      title: "🔍 Allgemeiner Python-Fehler",
      explanation: "Lies den Traceback immer von ganz unten nach oben: In der allerletzten Zeile nennt Python die genaue Fehlerart und Zeilennummer.",
      causes: ["Syntax- oder Logikfehler in deinem Code."],
      fixes: ["Überprüfe die in der letzten Zeile genannte Zeilennummer in deiner aufgabe.py Datei."],
      fix: "Überprüfe die in der letzten Zeile genannte Zeilennummer in deiner aufgabe.py Datei."
    };
  };

  // Exportiertes Objekt für Workspace & Widgets
  window.INTERPRETER = {
    translate: window.interpretiereTraceback
  };

  // Widget rendern, falls Container vorhanden
  document.addEventListener("DOMContentLoaded", () => {
    const interpreterEl = document.getElementById("error-interpreter-widget");
    if (!interpreterEl) return;

    const input = document.getElementById("error-input");
    const btn = document.getElementById("btn-interpret-error");
    const result = document.getElementById("error-result");

    if (btn && input && result) {
      btn.addEventListener("click", () => {
        const res = window.interpretiereTraceback(input.value);
        document.getElementById("error-name").innerText = res.title;
        document.getElementById("error-explanation").innerHTML = res.explanation;
        const fixList = document.getElementById("error-fixes");
        if (fixList) {
          fixList.innerHTML = (res.causes || []).map(c => `<li>${c}</li>`).join("") + `<li><strong>Lösung:</strong> ${res.fix}</li>`;
        }
        result.style.display = "block";
      });
    }
  });
})();
