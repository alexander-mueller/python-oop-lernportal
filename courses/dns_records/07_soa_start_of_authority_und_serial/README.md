# DNS 07: SOA Start of Authority & Serial

Willkommen zum Kurs **DNS-Records, Domain Name System & E-Mail-Sicherheit** im IT-Praxisportal!

## 💡 Das Wichtigste in Kürze
- **Ziel:** Der wichtigste Record jeder Zone: Primary Master, Hostmaster-E-Mail, Seriennummer (YYYYMMDDNN) und Timer.
- **Wichtigstes Tool:** `named-compilezone`

## 🎯 Deine Aufgaben (Checkliste)
1. **Teilziel 1:** SOA-Record mit RFC-konformer Seriennummer (YYYYMMDDNN) anlegen
2. **Teilziel 2:** Hostmaster E-Mail mit Punkt-Notation (admin.domain.de) formatieren
3. **Teilziel 3:** Timer: Refresh, Retry, Expire und Minimum-TTL abstimmen
4. **Teilziel 4:** Zonenaktualisierung über Seriennummer-Inkrement triggern

## 🧪 Tests ausführen
```bash
bash test_aufgabe.sh
```
