# DNS 08: NS Delegation & PTR Reverse DNS

Willkommen zum Kurs **DNS-Records, Domain Name System & E-Mail-Sicherheit** im IT-Praxisportal!

## 💡 Das Wichtigste in Kürze
- **Ziel:** Delegierung an Nameserver (NS) und Reverse-Lookup-Zonen (in-addr.arpa / ip6.arpa) für FCrDNS.
- **Wichtigstes Tool:** `dig -x`

## 🎯 Deine Aufgaben (Checkliste)
1. **Teilziel 1:** Mindestens zwei autoritative Nameserver (NS) delegieren
2. **Teilziel 2:** Reverse-Lookup-Zone für /24 Subnetz (1.168.192.in-addr.arpa) anlegen
3. **Teilziel 3:** PTR-Record für Mailserver zur SPAM-Vermeidung eintragen
4. **Teilziel 4:** Forward-Confirmed Reverse DNS (FCrDNS) validieren

## 🧪 Tests ausführen
```bash
bash test_aufgabe.sh
```
