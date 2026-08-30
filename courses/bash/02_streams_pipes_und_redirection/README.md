# Bash 02: I/O Streams, Pipes & Redirection 🌊

Willkommen zu **Modul 02** des Linux Bash & DevOps Lehrpfads!

In Unix ist alles ein Datenstrom. In diesem Modul lernst du die drei Standard-Dateideskriptoren (`stdin`, `stdout`, `stderr`), mächtige Redirection-Operatoren (`>`, `>>`, `2>`, `&>`), Datenstrom-Verzweigung mit `tee` und strukturierte Textgenerierung mit Here-Documents (`<<EOF`).

---

## 💡 1. Das Wichtigste in Kürze

### Die drei Standard-Streams (File Descriptors)
- **`0` (`stdin`)**: Standard-Eingabe (Tastatur oder Pipe)
- **`1` (`stdout`)**: Standard-Ausgabe (normale Befehlsausgaben)
- **`2` (`stderr`)**: Standard-Fehlerkanal (Fehlermeldungen und Warnungen)

### Redirection-Operatoren
```bash
# 1. Überschreiben vs. Anhängen
echo "Init" > log.txt        # Überschreibt die Datei komplett
echo "Update" >> log.txt     # Hängt eine neue Zeile hinten an

# 2. Fehlerkanal umleiten
command 2> error.log         # Leitet nur Fehlermeldungen in error.log
command 2> /dev/null         # Unterdrückt alle Fehlermeldungen (Bit-Bucket)
command > all.log 2>&1       # Leitet stdout UND stderr zusammen in all.log
command &> all.log           # Moderne Kurzform in Bash für obiges

# 3. Here-Documents (Mehrzeilige Texte schreiben)
cat <<EOF > /etc/app.conf
[server]
port = 8080
mode = production
EOF
```

### Pipes & `tee`
- Die Pipe `|` verbindet den `stdout` des linken Befehls mit dem `stdin` des rechten Befehls: `cat data.txt | grep "error" | wc -l`.
- `tee` wirkt wie ein T-Stück im Rohrleitungssystem: Es schreibt den Datenstrom in eine Datei **und** gibt ihn gleichzeitig auf `stdout` weiter (`command | tee output.log | grep ...`).

---

## 🎯 Aufgaben in `aufgabe.sh`

1. **TODO 1 (`erstelle_system_bericht`)**: Schreibe mit einem Here-Doc (`<<EOF`) und `>` einen strukturierten Header in die Zieldatei.
2. **TODO 2 (`haenge_status_an`)**: Hänge formatierte Statuszeilen mit `>>` an die Logdatei an.
3. **TODO 3 (`trenne_befehls_ausgabe`)**: Führe einen Befehl aus und trenne `stdout` (`1>`) und `stderr` (`2>`) in zwei separate Dateien.
4. **TODO 4 (`unterdruecke_fehler`)**: Führe einen Befehl aus und leite Fehlermeldungen nach `/dev/null` um.
5. **TODO 5 (`pipe_und_tee_pipeline`)**: Baue eine Daten-Pipeline mit Filterung (`grep`), Konvertierung (`tr`), Spiegelung (`tee`) und Sortierung (`sort`).

---

## 🧪 Tests ausführen

```bash
bash test_aufgabe.sh
```
