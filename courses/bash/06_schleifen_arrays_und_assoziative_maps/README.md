# Bash 06: Schleifen, Arrays & Assoziative Maps 🔄

Willkommen zu **Modul 06** des Linux Bash & DevOps Lehrpfads!

In diesem Modul meisterst du `for`- und `while`-Schleifen, sicheres zeilenweises Einlesen von Streams (`while IFS= read -r`), indizierte Arrays, **assoziative Arrays (`declare -A`)** als Hashmaps sowie professionelles CLI-Parameter-Parsing mit `getopts`.

---

## 💡 1. Das Wichtigste in Kürze

### Schleifenkonstrukte
- **`for item in "${arr[@]}"`**: Iteriert über Elemente eines Arrays.
- **`while IFS= read -r line; do ... done`**: Sicheres zeilenweises Einlesen ohne Whitespace-Trimming.

### Indizierte Arrays
```bash
SERVERS=("web01" "web02" "db01")
SERVERS+=("cache01")          # Element anhängen
echo ${SERVERS[0]}            # web01
echo ${#SERVERS[@]}           # 4 (Länge des Arrays)
echo "${SERVERS[@]}"          # Alle Elemente
```

### Assoziative Arrays (Hashmaps / Dictionaries)
Mit `declare -A` erstellst du Key-Value-Speicher in Bash:
```bash
declare -A HOST_IPS=(
  ["web"]="192.168.1.10"
  ["db"]="192.168.1.20"
)

HOST_IPS["redis"]="192.168.1.30"
echo "Web-IP: ${HOST_IPS["web"]}"
echo "Alle Keys: ${!HOST_IPS[@]}"
echo "Alle Values: ${HOST_IPS[@]}"
```

### CLI-Optionen mit `getopts`
Sauberes Verarbeiten von Flags wie `-e prod -p 8080 -v`:
```bash
while getopts "e:p:v" opt; do
  case "$opt" in
    e) ENV="$OPTARG" ;;
    p) PORT="$OPTARG" ;;
    v) VERBOSE=true ;;
  esac
done
```

---

## 🎯 Aufgaben in `aufgabe.sh`

1. **TODO 1 (`summiere_zahlen_array`)**: Summiere beliebig viele Zahlen mit einer `for`-Schleife.
2. **TODO 2 (`lese_csv_zeilenweise`)**: Lies CSV-Daten mit `while IFS=',' read -r` ein und gib eine gewünschte Spalte aus.
3. **TODO 3 (`verwalte_server_hashmap`)**: Verwalte ein assoziatives Array (`declare -A`) mit `get`, `set` und `keys`.
4. **TODO 4 (`zaehle_element_haeufigkeit`)**: Zähle Vorkommen von Items mit einer assoziativen Counter-Map.
5. **TODO 5 (`parse_cli_flags`)**: Parse CLI-Parameter (`-e`, `-p`, `-v`) mit `getopts`.

---

## 🧪 Tests ausführen

```bash
bash test_aufgabe.sh
```
