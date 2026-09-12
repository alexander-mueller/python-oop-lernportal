# DNS 06: CNAME Alias & das Apex-Problem

Willkommen zum Kurs **DNS-Records, Domain Name System & E-Mail-Sicherheit** im IT-Praxisportal!

## 💡 Das Wichtigste in Kürze
- **Ziel:** Kanonische Namen (CNAME), Zeiger auf Hostnames, Alias-Kollisionen und das Apex-/Root-Domain-Verbot (RFC 1912).
- **Wichtigstes Tool:** `dig CNAME`

## 🎯 Deine Aufgaben (Checkliste)
1. **Teilziel 1:** CNAME-Record für Subdomain (api.domain.de -> elb.aws.com) erstellen
2. **Teilziel 2:** RFC-Kollision prüfen (CNAME darf nicht mit anderen Records koexistieren)
3. **Teilziel 3:** Apex/Root-Domain Problem (example.de vs. MX/SOA) verstehen
4. **Teilziel 4:** Moderne ALIAS / ANAME Provider-Lösungen analysieren

## 🧪 Tests ausführen
```bash
bash test_aufgabe.sh
```
