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
        title: "💡 Bitte füge eine Fehlermeldung ein",
        explanation: "Kopiere deinen Traceback aus dem Terminal und füge ihn hier ein.",
        fix: "Starte dein Skript im Terminal mit python3 test_aufgabe.py"
      };
    }

    for (let rule of ERROR_RULES) {
      if (rule.pattern.test(errorText)) {
        return {
          matched: true,
          type: rule.type,
          title: rule.title,
          explanation: rule.explanation,
          causes: rule.causes,
          fix: rule.fix
        };
      }
    }

    return {
      matched: false,
      title: "🔍 Allgemeiner Python-Fehler",
      explanation: "Lies den Traceback immer von ganz unten nach oben: In der allerletzten Zeile nennt Python die genaue Fehlerart und Zeilennummer.",
      causes: ["Syntax- oder Logikfehler in deinem Code."],
      fix: "Überprüfe die in der letzten Zeile genannte Zeilennummer in deiner aufgabe.py Datei."
    };
  };

  // Widget rendern, falls Container vorhanden
  document.addEventListener("DOMContentLoaded", () => {
    const interpreterEl = document.getElementById("error-interpreter-widget");
    if (!interpreterEl) return;

    interpreterEl.innerHTML = `
      <div class="card" style="border-left: 5px solid var(--secondary);">
        <h2>🩺 Interaktiver Python-Fehler-Dolmetscher</h2>
        <p>Du verstehst eine Fehlermeldung aus dem Terminal nicht? Füge sie hier ein und erhalte sofort eine schülerfreundliche deutsche Erklärung mit Reparatur-Anleitung!</p>
        
        <textarea id="traceback-input" placeholder="Füge hier deinen Traceback ein (z.B. TypeError: ... oder IndexError: list index out of range)" style="width: 100%; height: 90px; padding: 12px; font-family: var(--font-mono); font-size: 0.88rem; border-radius: var(--radius-sm); border: 1px solid var(--border-color); margin-bottom: 12px;"></textarea>
        
        <button id="btn-interpret" class="btn" style="background: var(--secondary);">🔍 Fehlermeldung übersetzen</button>
        
        <div id="interpreter-result" style="margin-top: 15px; display: none;"></div>
      </div>
    `;

    const input = document.getElementById("traceback-input");
    const btn = document.getElementById("btn-interpret");
    const result = document.getElementById("interpreter-result");

    btn.addEventListener("click", () => {
      const res = window.interpretiereTraceback(input.value);
      result.innerHTML = `
        <div class="box ${res.matched ? 'box-warning' : 'box-tipp'}">
          <div class="box-title">${res.title}</div>
          <p><strong>Was bedeutet das?</strong> ${res.explanation}</p>
          ${res.causes ? `<p><strong>Mögliche Ursachen:</strong></p><ul style="margin-left: 20px;">${res.causes.map(c => `<li>${c}</li>`).join("")}</ul>` : ''}
          <div style="margin-top: 10px; padding-top: 10px; border-top: 1px solid rgba(0,0,0,0.1);">
            <strong>🔧 So behebst du den Fehler:</strong>
            <p style="margin-top: 4px;">${res.fix}</p>
          </div>
        </div>
      `;
      result.style.display = "block";
    });
  });
})();
