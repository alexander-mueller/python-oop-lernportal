# DNS 09: MX-Records & Mail-Prioritäten

Willkommen zu **Modul 09** des Kurses **DNS-Records, Domain Name System & E-Mail-Sicherheit**!

In diesem Modul lernst du, wie E-Mail-Zustellung über das Domain Name System gesteuert wird: **MX-Records (Mail Exchange)**, **Prioritäts-Routing** für Hochverfügbarkeit und Store-and-Forward sowie die strikte RFC-Regel, warum MX-Ziele niemals auf CNAME-Records verweisen dürfen.

---

## 💡 1. Das Wichtigste in Kürze

### Was ist ein MX-Record?
Ein MX-Record bestimmt den Mail-Server, der für den Empfang von E-Mails einer Domäne zuständig ist:
```dns
it-praxisportal.de.   86400   IN   MX   10   mail.it-praxisportal.de.
it-praxisportal.de.   86400   IN   MX   20   backup-mail.relay.de.
```

### Die Prioritäts-Regel
- **Niedrigere Zahl = Höhere Priorität!**
- Der sendende MTA kontaktiert zwingend zuerst Server mit Priorität `10`.
- Nur wenn dieser Server offline oder nicht erreichbar ist, weicht der Sender auf Priorität `20` aus.

### Die CNAME-Falle nach RFC 2181
> **RFC 2181 / RFC 5321:** *„The domain name in an MX record MUST NOT be an alias (CNAME).“*
Ein MX-Ziel muss immer direkt auf einen A- oder AAAA-Record verweisen. Ein CNAME führt bei vielen Mail-Gateways zu Schleifen und Zustellabbrüchen.

---

## 🎯 Deine Aufgaben in `aufgabe.sh`

1. **TODO 1 (`format_mx_record`):** Validiere die numerische Priorität und formatiere einen BIND MX-Record.
2. **TODO 2 (`sort_mx_records`):** Lies eine Liste von MX-Records ein und sortiere sie aufsteigend nach Priorität.
3. **TODO 3 (`validate_mx_target_type`):** Verhindere CNAME-Ziele nach RFC 2181.
4. **TODO 4 (`generate_redundant_mx_setup`):** Erstelle ein redundantes MX-Paar (Primary Prio 10, Backup Prio 20).

---

## 🧪 Tests ausführen

Führe im Terminal folgenden Befehl aus:
```bash
bash test_aufgabe.sh
```
