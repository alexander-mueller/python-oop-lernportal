# DNS 10: SPF Sender Policy Framework (TXT)

Willkommen zum Kurs **DNS-Records, Domain Name System & E-Mail-Sicherheit** im IT-Praxisportal!

## 💡 Das Wichtigste in Kürze
- **Ziel:** Schutz vor E-Mail-Spoofing: Autorisierte Absender-IPs im TXT-Record definieren (v=spf1 mx ip4:... -all).
- **Wichtigstes Tool:** `dig TXT`

## 🎯 Deine Aufgaben (Checkliste)
1. **Teilziel 1:** Gültigen SPF TXT-Record für die Domain erstellen
2. **Teilziel 2:** Mechanismen (ip4, a, mx, include) kombinieren
3. **Teilziel 3:** Unterschied Hardfail (-all) vs. Softfail (~all) implementieren
4. **Teilziel 4:** Das 10-DNS-Lookup-Limit des SPF-Standards (RFC 7208) einhalten

## 🧪 Tests ausführen
```bash
bash test_aufgabe.sh
```
