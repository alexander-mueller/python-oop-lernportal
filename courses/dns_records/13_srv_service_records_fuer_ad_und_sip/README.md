# DNS 13: SRV Service Records (Active Directory & SIP)

Willkommen zum Kurs **DNS-Records, Domain Name System & E-Mail-Sicherheit** im IT-Praxisportal!

## 💡 Das Wichtigste in Kürze
- **Ziel:** Dienste automatisch im Netzwerk finden: _service._proto.name TTL Class SRV Priority Weight Port Target.
- **Wichtigstes Tool:** `dig SRV`

## 🎯 Deine Aufgaben (Checkliste)
1. **Teilziel 1:** SRV-Record für Active Directory LDAP (_ldap._tcp.dc._msdcs) erstellen
2. **Teilziel 2:** SRV-Record für Kerberos Authentifizierung (_kerberos._tcp) anlegen
3. **Teilziel 3:** Priorität und Gewichtung (Weight) für Lastverteilung berechnen
4. **Teilziel 4:** Service-Discovery Abfragen mit dig SRV durchführen

## 🧪 Tests ausführen
```bash
bash test_aufgabe.sh
```
