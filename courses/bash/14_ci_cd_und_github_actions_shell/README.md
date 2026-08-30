# Bash 14: CI/CD Workflows & GitHub Actions Shell Scripting 🛠️

Willkommen zu **Modul 14**! In modernen Software-Unternehmen laufen hunderte Shell-Skripte in CI/CD-Pipelines (GitHub Actions, GitLab CI, Jenkins, Azure DevOps).

In diesem Modul lernst du die Besonderheiten und Best Practices für Shell-Code in Runner-Umgebungen kennen: Workflow-Commands, Maskierung von Passwörtern, Step-Outputs und plattformübergreifendes Multi-OS Scripting.

---

## 💡 1. Das Wichtigste in Kürze

### 1.1 Step Outputs & Environment Files
In GitHub Actions kommunizieren Pipeline-Schritte über spezielle Dateipfade:
```bash
# 🎯 Einfacher Step Output:
echo "version=1.0.0" >> "$GITHUB_OUTPUT"

# 🎯 Mehrzeiliger Output (z.B. Release Notes / Git Log):
cat <<_EOF_ >> "$GITHUB_OUTPUT"
release_notes<<EOF
- Feature A implementiert
- Bugfix im Login-Modul
EOF
_EOF_

# 🎯 Globale Umgebungsvariable für nachfolgende Steps setzen:
echo "NODE_ENV=production" >> "$GITHUB_ENV"
```

### 1.2 Secret Masking (Zero-Leakage Policy)
Verhindert, dass API-Tokens oder Passwörter in den öffentlichen Pipeline-Logs lesbar sind:
```bash
# Sobald dieser Befehl läuft, maskiert der Runner jedes Auftreten des Werts mit ***
echo "::add-mask::$TEMP_SECRET_TOKEN"
```

### 1.3 Rich Step Summaries ($GITHUB_STEP_SUMMARY)
Erzeugt übersichtliche Markdown-Reports direkt auf der Job-Zusammenfassungsseite:
```bash
cat <<EOF >> "$GITHUB_STEP_SUMMARY"
### 🚀 Deployment Report
| Service | Status | Version |
|---|---|---|
| Auth-API | ✅ OK | v2.1.0 |
| Payment  | ✅ OK | v1.8.4 |
EOF
```

### 1.4 Multi-OS & Matrix Builds
Skripte müssen sich dynamisch an Ubuntu, Alpine Linux, macOS oder RHEL anpassen:
```bash
case "$(uname -s)" in
    Darwin) brew install jq ;;
    Linux)
        if [ -f /etc/alpine-release ]; then
            apk add --no-cache jq
        else
            apt-get update -y && apt-get install -y jq
        fi
        ;;
esac
```

---

## 🎯 Aufgaben in `aufgabe.sh`

1. **`write_github_output(name, value, output_file)`**:
   Schreibt Schlüssel-Wert-Paare (inkl. sicherer Multiline-Syntax) in `$GITHUB_OUTPUT`.
2. **`mask_github_secret(secret)`**:
   Gibt den offiziellen Workflow-Befehl `::add-mask::<secret>` aus.
3. **`generate_step_summary_table(title, pairs_str, summary_file)`**:
   Schreibt eine formatierte Markdown-Tabelle in `$GITHUB_STEP_SUMMARY`.
4. **`detect_os_and_package_install_cmd(pkg, os_type)`**:
   Ermittelt das Ziel-Betriebssystem und liefert den passenden Paketinstallationsbefehl (apt, apk, dnf, brew).

---

## 🧪 Tests ausführen

```bash
# Eigene Lösung testen:
bash test_aufgabe.sh

# Musterlösung testen:
bash test_aufgabe.sh musterloesung.sh
```
