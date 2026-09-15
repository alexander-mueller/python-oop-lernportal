# DNS 06: CNAME (Canonical Name) & das Zone-Apex Problem

Willkommen zu **Modul 06** des Kurses **DNS-Records, Domain Name System & E-Mail-Sicherheit**!

In diesem Modul meisterst du eines der anspruchsvollsten Themen der DNS-Konfiguration: **CNAME-Aliase**, die strikte **Koexistenz-Regel** nach RFC 1912/2181, das berüchtigte **Zone-Apex-Problem (`@`)** und das Auflösen von CNAME-Ketten.

---

## 💡 1. Das Wichtigste in Kürze

### Die RFC 1912 / 2181 CNAME-Regel
> **„Wenn für einen Node ein CNAME existiert, darf kein anderer Record-Typ für denselben Node existieren!“**

Das bedeutet:
- `blog IN CNAME myhost.com.` ist erlaubt.
- Wenn du aber zusätzlich `blog IN TXT "info"` oder `blog IN MX 10 mail.de.` hinzufügst, verletzt du den DNS-Standard! Resolver verwerfen entweder die zusätzlichen Records oder den CNAME komplett.

### Das Zone-Apex Problem (`@`)
Der Zone-Apex ist der Ursprung deiner Domain (z.B. `it-praxisportal.de` ohne Subdomain).
- Jede Zone MUSS am Apex zwingend **SOA** und mindestens zwei **NS-Records** besitzen.
- Wegen der CNAME-Regel darf am Zone-Apex **NIEMALS ein CNAME** angelegt werden!
- *Lösung für moderne Cloud-Infrastrukturen:* Verwende statische A/AAAA-Records oder sogenannte **ALIAS / ANAME** Pseudo-Records deines DNS-Providers (z.B. Cloudflare CNAME Flattening, AWS Route 53 Alias).

### Der Schlusspunkt bei Zielen
```dns
; KORREKT (Absoluter FQDN):
app   IN  CNAME   lb-123.amazonaws.com.

; FALSCH (Relativer Hostname):
app   IN  CNAME   lb-123.amazonaws.com
; BIND ergänzt $ORIGIN: lb-123.amazonaws.com.it-praxisportal.de. (Dead Link!)
```

---

## 🎯 Deine Aufgaben in `aufgabe.sh`

1. **TODO 1 (`format_cname_record`):** Formatiere einen CNAME-Record und stelle sicher, dass das Ziel mit einem Punkt `.` endet.
2. **TODO 2 (`validate_apex_cname_rule`):** Verhindere das Erstellen von CNAME-Records auf dem Zone-Apex (`@`).
3. **TODO 3 (`detect_cname_collisions`):** Durchsuche eine Zonendatei nach illegalen Koexistenz-Konflikten.
4. **TODO 4 (`trace_cname_chain`):** Verfolge eine mehrstufige CNAME-Kette bis zum finalen Ziel und erkenne Endlosschleifen.

---

## 🧪 Tests ausführen

Führe im Terminal folgenden Befehl aus:
```bash
bash test_aufgabe.sh
```
