# Modul 13: SRV-Service Records für Active Directory & SIP (RFC 2782)

## 📌 Didaktische Einführung & Relevanz für IT-Systemintegration
Ein Standard A-Record löst einen Hostnamen in eine IP-Adresse auf. Doch welcher Dienst (HTTP, LDAP, Kerberos, SIP) läuft auf welchem Port? Ohne SRV-Records mussten Client-Anwendungen Ports hardcoden oder manuell konfiguriert werden.

**RFC 2782 definiert den SRV-Record (Service Record)**. Er verbindet:
1. **Dienst & Protokoll** (`_service._proto.name`)
2. **Priorität (Priority)**: Niedrigere Zahl = bevorzugt (wie bei MX).
3. **Gewichtung (Weight)**: Lastverteilung unter Servern mit gleicher Priorität.
4. **Port**: TCP- oder UDP-Portnummer (z. B. 389 für LDAP, 88 für Kerberos, 5060 für SIP).
5. **Ziel-Host (Target)**: Der vollqualifizierte Hostname (FQDN) des Zielservers.

In **Microsoft Active Directory** ist DNS mit SRV-Records das absolute Herzstück: Ein Windows-Client findet seinen zuständigen Domain Controller über `_ldap._tcp.dc._msdcs.domaene.local`!

---

## ⚙️ RFC 2782 Syntax im BIND Zonenformat

```text
; _service._proto.name.  TTL   Class SRV Priority Weight Port Target.
_ldap._tcp.corp.local.   86400 IN    SRV 0        100    389  dc01.corp.local.
_ldap._tcp.corp.local.   86400 IN    SRV 10       50     389  dc02.corp.local.
_sip._udp.firma.de.      3600  IN    SRV 10       60     5060 pbx01.firma.de.
_sip._udp.firma.de.      3600  IN    SRV 10       40     5060 pbx02.firma.de.
```

### Die Felder im Detail:
1. **Name**: Muss mit einem Unterstrich `_` für Service und Protokoll beginnen (`_ldap._tcp.domain.tld.`).
2. **Priority (0-65535)**: Der Client kontaktiert zuerst den Zielserver mit der niedrigsten Prioritätsnummer.
3. **Weight (0-65535)**: Wenn zwei Server dieselbe Priorität haben (z. B. 10), bestimmt das Verhältnis ihrer Gewichte (z. B. 60 und 40) die Wahrscheinlichkeit der Auswahl (60% zu 40%). Wenn Gewicht 0 ist, wird der Server minimal gewichtet.
4. **Port (1-65535)**: Der Zielport des Dienstes.
5. **Target**: Der FQDN des Servers mit Schlusspunkt `.`. **Ein CNAME als Ziel ist laut RFC 2782 strikt verboten!**

---

## 🎯 Deine Aufgaben im Modul 13:

1. **`format_srv_record`**:
   Erzeugt einen RFC 2782 BIND SRV-Record:
   `format_srv_record "_ldap" "_tcp" "corp.de" 0 100 389 "dc1.corp.de" 86400`
   -> `_ldap._tcp.corp.de. 86400 IN SRV 0 100 389 dc1.corp.de.`

2. **`parse_srv_record`**:
   Nimmt eine SRV-Zeile entgegen und extrahiert Service, Proto, Priority, Weight, Port und Target im Key-Value-Format:
   `SERVICE=_ldap PROTO=_tcp PRIO=0 WEIGHT=100 PORT=389 TARGET=dc1.corp.de.`

3. **`generate_ad_srv_records`**:
   Erzeugt die essenziellen Microsoft Active Directory Discovery Records für einen DC (`_ldap._tcp` Port 389, `_kerberos._tcp` Port 88, `_gc._tcp` Port 3268 für Global Catalog).

4. **`select_srv_target_by_prio`**:
   Nimmt eine Liste von SRV-Records entgegen und ermittelt den primären Ziel-Host mit der niedrigsten Prioritätszahl.
