# Bash 07: Text-Mining mit grep, sed, awk & jq 📊

Willkommen zu **Modul 07** des Linux Bash & DevOps Lehrpfads!

In diesem Modul lernst du die vier Textverarbeitungs-Giganten der Linux-Welt beherrschen: `grep` (Muster finden), `sed` (Stream Editor & Transformation), `awk` (Spaltenanalyse & Metrik-Aggregation) und **`jq`** (High-Speed JSON-Parsing im Terminal).

---

## 💡 1. Das Wichtigste in Kürze

### `grep` (Global Regular Expression Print)
- `grep -E "pattern"`: Nutzt erweiterte reguläre Ausdrücke (Extended Regex wie `(foo|bar)`).
- `grep -i`: Ignoriert Groß-/Kleinschreibung (Case-Insensitive).
- `grep -v "debug"`: Invertiert die Suche (zeigt alle Zeilen, die **nicht** matchen).

### `sed` (Stream Editor)
- `sed -E 's/alt/neu/g'`: Ersetzt alle Vorkommen im Stream.
- `sed -E '/^#/d'`: Löscht Zeilen, die mit `#` beginnen.

### `awk` (Die Muster-Aktions-Sprache)
- `awk '{ print $1, $NF }'`: Gibt die erste und die letzte Spalte aus.
- Aggregationen mit `BEGIN`, Muster-Blöcken und `END`:
```bash
cat access.log | awk '
  NF >= 1 { sum += $NF; count++ }
  END { print "Gesamt-Bytes:", sum, "Durchschnitt:", int(sum/count) }
'
```

### `jq` (Der JSON-Prozessor im Terminal)
Unverzichtbar in modernen Cloud- und Kubernetes-Umgebungen:
```bash
# 1. Array filtern & Feld extrahieren (-r für Raw String):
echo "$JSON" | jq -r '.[] | select(.active == true) | .username'

# 2. JSON in CSV transformieren:
echo "$JSON" | jq -r '.[] | "\(.hostname),\(.ip),\(.status)"'
```

---

## 🎯 Aufgaben in `aufgabe.sh`

1. **TODO 1 (`extrahiere_fehler_logs`)**: Finde Zeilen mit ERROR/CRITICAL/FATAL und filtere DEBUG-Meldungen heraus.
2. **TODO 2 (`maskiere_passwoerter_sed`)**: Maskiere Passwörter und API-Keys per `sed -E`.
3. **TODO 3 (`berechne_weblog_traffic_awk`)**: Aggregiere Requests, Gesamt-Bytes und Durchschnitt per `awk`.
4. **TODO 4 (`filtere_aktive_benutzer_jq`)**: Extrahiere aktive Usernamen aus JSON mit `jq`.
5. **TODO 5 (`transformiere_server_json_zu_csv`)**: Wandle JSON-Serverlisten in saubere CSV-Zeilen um.

---

## 🧪 Tests ausführen

```bash
bash test_aufgabe.sh
```
