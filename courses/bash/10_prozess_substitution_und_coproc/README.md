# Bash 10: Prozess-Substitution, Named Pipes & Co-Prozesse (coproc) 🔄

Willkommen zu **Modul 10**! In diesem Modul lernst du fortgeschrittene IPC-Mechanismen (Inter-Process Communication) und Stream-Manipulationen kennen, mit denen professionelle DevOps-Ingenieure Datenströme ohne langsame temporäre Festplattendateien verarbeiten.

---

## 💡 1. Das Wichtigste in Kürze

### 1.1 Process Substitution `<(...)` (Befehl als Datei lesen)
Viele Unix-Befehle (wie `diff`, `comm`, `join`) akzeptieren nur Dateipfade als Argumente, keine Pipes. Mit `<(command)` erstellt die Shell einen virtuellen Datei-Deskriptor (`/dev/fd/63`):
```bash
# Vergleicht die Ausgaben zweier Server-Konfigurationen direkt:
diff -u <(ssh srv1 "cat /etc/nginx/nginx.conf") <(ssh srv2 "cat /etc/nginx/nginx.conf")

# Variablenverlust in while-Schleifen vermeiden:
count=0
while read -r line; do
    ((count++))
done < <(find . -type f)
echo "Gefundene Dateien: $count" # Funktioniert! (Keine Subshell)
```

### 1.2 Process Substitution `>(...)` (In Befehl schreiben)
Erlaubt das Verzweigen von Streams mit `tee`:
```bash
# Schreibt Logs roh in access.log und filtert parallel 500er Fehler in errors.log:
cat stream.log | tee >(grep "500 Internal Error" > errors.log) > access.log
```

### 1.3 Named Pipes (`mkfifo`)
Eine Named Pipe ist eine Datei im Dateisystem, die als bidirektionaler Puffer zwischen zwei unabhängigen Prozessen agiert:
```bash
mkfifo /tmp/my_pipe
# Prozess A (Schreiber):
echo "Build complete" > /tmp/my_pipe &

# Prozess B (Leser):
read -r status < /tmp/my_pipe
echo "Status empfangen: $status"
rm -f /tmp/my_pipe
```

### 1.4 Bash Co-Prozesse (`coproc`)
Ein `coproc` startet ein Programm asynchron im Hintergrund und öffnet zwei Dateideskriptoren für bidirektionale Kommunikation:
```bash
coproc WORKER {
    while read -r input; do
        [ "$input" = "QUIT" ] && break
        echo "PROCESSED: $input"
    done
}

# In den Worker schreiben:
echo "payload1" >&"${WORKER[1]}"

# Antwort vom Worker lesen:
read -r response <&"${WORKER[0]}"
echo "Antwort: $response"

# Beenden:
echo "QUIT" >&"${WORKER[1]}"
```

---

## 🎯 Aufgaben in `aufgabe.sh`

1. **`compare_command_outputs(cmd1, cmd2)`**:
   Vergleicht zwei Shell-Befehle direkt mit `diff -u <(...) <(...)`. Liefert `"IDENTICAL"` bei Gleichheit.
2. **`stream_splitter_tee(input_text, raw_file, uppercase_file)`**:
   Nutzt `tee >(tr '[:lower:]' '[:upper:]' > "$upper")`, um Daten in zwei Streams aufzuspalten.
3. **`named_pipe_transfer(fifo_path, message)`**:
   Erstellt eine Named Pipe (`mkfifo`), überträgt eine Nachricht asynchron und liest sie im Hauptprozess.
4. **`coproc_calculator_interactive(expr1, expr2)`**:
   Startet einen interaktiven `coproc` Rechen-Daemon und kommuniziert über Dateideskriptoren `${CALC[0]}` und `${CALC[1]}`.

---

## 🧪 Tests ausführen

```bash
# Eigene Lösung testen:
bash test_aufgabe.sh

# Musterlösung testen:
bash test_aufgabe.sh musterloesung.sh
```
