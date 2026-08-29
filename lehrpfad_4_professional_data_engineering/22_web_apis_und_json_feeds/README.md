# Kapitel 22: Web-APIs, REST & JSON-Feeds 🌐📡

In diesem Kapitel lernst du, wie moderne Web-Anwendungen über REST-APIs kommunizieren, wie du strukturierte JSON-Feeds in Python parst, verschachtelte Daten extrahierst und Fehler robust abfängst.

---

## 🎯 Was du lernst

1. **Was ist eine REST-API?**
   - Client-Server-Architektur im Web: Der Client stellt eine Anfrage (**Request**) per HTTP GET/POST an den Endpunkt, der Server antwortet (**Response**).
2. **Die Kellner-Analogie:**
   - **Gast (Client/Python-Skript):** Möchte Daten (z.B. Wetterbericht oder Aktienkurse) haben.
   - **Kellner (API):** Nimmt die Bestellung entgegen, bringt sie in die Küche und serviert die Antwort.
   - **Küche/Koch (Server/Datenbank):** Verarbeitet die Anfrage und bereitet die Rohdaten zu.
   - **Speisekarte (API-Dokumentation):** Beschreibt, welche Endpunkte und Parameter erlaubt sind.
3. **JSON als Universalsprache des Internets:**
   - `json.loads(json_string)`: Wandelt einen empfangenen JSON-Text in ein Python-Dictionary bzw. eine Python-Liste um.
   - `json.dumps(obj, indent=2)`: Wandelt ein Python-Objekt in einen JSON-formatierten String um.
4. **HTTP Status-Codes:**
   - `200 OK`: Anfrage erfolgreich beantwortet.
   - `400 Bad Request`: Fehlerhafte Anfrage / ungültige Parameter.
   - `404 Not Found`: Endpunkt oder Ressource nicht gefunden.
   - `500 Internal Server Error`: Unerwarteter Serverfehler.
5. **Robuste Fehlerbehandlung & Defensives Parsen:**
   - `json.JSONDecodeError`: Wenn der Server HTML statt JSON sendet oder der Payload unvollständig ist.
   - `KeyError` / `IndexError`: Wenn erwartete Felder im JSON fehlen.
   - Sicheres Auslesen mit `.get()` und Standardwerten.
6. **100% Offline- & Pyodide-kompatibel:**
   - Alle Übungen und Tests nutzen realistische Mock-JSON-Strings, sodass keine Internetverbindung oder externe API-Keys benötigt werden.

---

## 📁 Die Dateien in diesem Ordner

- **`index.html`**: Die interaktive Lernseite mit Kellner-Analogie, API-Ablaufdiagramm, JSON Cheat-Sheet und Subgoals.
- **`aufgabe.py`**: Dein Arbeitsblatt mit Parser-Funktionen und der Klasse `WetterApiParser`.
- **`test_aufgabe.py`**: Automatische Unittest-Suite (`python3 test_aufgabe.py`).
- **`musterloesung.py`**: Vollständig ausprogrammierte Beispiellösung.

---

## 🚀 Schnellstart

```bash
# 1. Bearbeite aufgabe.py
# 2. Teste deine Lösung:
python3 test_aufgabe.py
```
