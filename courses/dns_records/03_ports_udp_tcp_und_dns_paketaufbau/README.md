# DNS 03: UDP vs. TCP Port 53 & EDNS0

Willkommen zum Kurs **DNS-Records, Domain Name System & E-Mail-Sicherheit** im IT-Praxisportal!

## 💡 Das Wichtigste in Kürze
- **Ziel:** Transportprotokolle: Port 53 UDP für Standardabfragen (< 512 Bytes), Port 53 TCP für Zonentransfers (AXFR) & DNSSEC.
- **Wichtigstes Tool:** `dig +tcp`

## 🎯 Deine Aufgaben (Checkliste)
1. **Teilziel 1:** DNS-Anfrage über UDP Port 53 versenden
2. **Teilziel 2:** Truncation Flag (TC-Bit) und TCP-Fallback erkennen
3. **Teilziel 3:** EDNS0 (Extension Mechanisms for DNS) Puffergröße auf 4096 Byte setzen
4. **Teilziel 4:** TCP-Verbindung für Zonentransfers absichern

## 🧪 Tests ausführen
```bash
bash test_aufgabe.sh
```
