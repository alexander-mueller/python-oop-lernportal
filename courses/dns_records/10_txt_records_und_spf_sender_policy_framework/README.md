# DNS 10: SPF (Sender Policy Framework) & das 10-Lookup Limit

Willkommen zu **Modul 10** des Kurses **DNS-Records, Domain Name System & E-Mail-Sicherheit**!

In diesem Modul lernst du den ersten der drei Pfeiler moderner E-Mail-Sicherheit kennen: das **Sender Policy Framework (SPF, RFC 7208)**. Du erfährst, wie du per DNS-TXT-Record festlegst, welche Server Mails für deine Domain versenden dürfen, welche Risiken bei `+all` drohen und warum das **10-DNS-Lookup-Limit** viele Admins zur Verzweiflung bringt.

---

## 💡 1. Das Wichtigste in Kürze

### Wie SPF funktioniert
Ein Absender schickt eine Mail mit `From: chef@firma.de`. Der empfangende Server fragt den TXT-Record von `firma.de` ab und vergleicht die IP-Adresse des Verbindungsaufbaus mit den im SPF-Record erlaubten IPs und Hostnamen.

```dns
@   IN   TXT   "v=spf1 mx ip4:188.245.100.5 include:_spf.google.com -all"
```

### Die Mechanismen
- `mx`: Erlaubt alle eigenen MX-Server.
- `ip4:<ip>`: Erlaubt konkrete IPv4-Adressen oder Subnetze.
- `include:<domain>`: Übernimmt die Regeln eines Cloud-Providers (z.B. Google Workspace oder Microsoft 365).

### Die Qualifier am Ende
| Qualifier | Name | Empfänger-Aktion |
| :--- | :--- | :--- |
| **`-all`** | HardFail | **Strikte Ablehnung:** Nicht gelistete Server werden geblockt (Best Practice!). |
| **`~all`** | SoftFail | **Warnung:** Mails werden angenommen, aber als Spam verdächtigt. |
| **`?all`** | Neutral | Keine Aussage / Testmodus. |
| **`+all`** | Pass | **Sicherheitsdesaster!** Erlaubt buchstäblich jedem Rechner der Welt das Versenden in deinem Namen! |

### Das 10-Lookup Limit (RFC 7208)
Um Denial-of-Service-Angriffe auf DNS-Server zu verhindern, bricht die SPF-Prüfung sofort mit `PermError` ab, wenn zur Evaluierung **mehr als 10 DNS-Abfragen** (durch `include`, `a`, `mx`, `redirect`) nötig sind.

---

## 🎯 Deine Aufgaben in `aufgabe.sh`

1. **TODO 1 (`build_spf_record`):** Bilde einen vollständigen SPF-String aus Parametern zusammen.
2. **TODO 2 (`count_spf_lookups`):** Zähle die DNS-Lookups und schlage Alarm bei Überschreitung des 10er-Limits.
3. **TODO 3 (`audit_spf_qualifier`):** Prüfe die Sicherheitsstufe des All-Qualifiers (`-all` vs. `+all`).
4. **TODO 4 (`format_spf_txt_record`):** Erstelle den finalen BIND TXT-Record.

---

## 🧪 Tests ausführen

Führe im Terminal folgenden Befehl aus:
```bash
bash test_aufgabe.sh
```
