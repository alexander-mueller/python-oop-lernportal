# DNS 12: DMARC Policy & Phishing-Abwehr

Willkommen zum Kurs **DNS-Records, Domain Name System & E-Mail-Sicherheit** im IT-Praxisportal!

## 💡 Das Wichtigste in Kürze
- **Ziel:** Die Krone der Mail-Sicherheit: DMARC Policy (_dmarc.domain.de), SPF/DKIM Alignment und RUA/RUF Reporting.
- **Wichtigstes Tool:** `checkdmarc`

## 🎯 Deine Aufgaben (Checkliste)
1. **Teilziel 1:** DMARC TXT-Record unter _dmarc.domain.de anlegen
2. **Teilziel 2:** Policy-Stufen (p=none -> p=quarantine -> p=reject) staffeln
3. **Teilziel 3:** Aggregierte Report-Adresse (rua=mailto:dmarc@domain.de) einrichten
4. **Teilziel 4:** Strenges vs. relatives Alignment (aspf/adkim) festlegen

## 🧪 Tests ausführen
```bash
bash test_aufgabe.sh
```
