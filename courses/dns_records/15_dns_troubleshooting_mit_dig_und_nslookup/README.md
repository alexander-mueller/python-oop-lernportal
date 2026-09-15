# Modul 15: DNS-Troubleshooting mit dig & nslookup

## 📌 Didaktische Einführung & Relevanz für IT-Systemintegration
"It's not DNS. There's no way it's DNS. It was DNS." &ndash; Dieser alte Sysadmin-Witz spiegelt den Berufsalltag wider: Fehler in der DNS-Konfiguration führen zu nicht erreichbaren Websites, verworfenen E-Mails und scheiternden Logins.

Professionelle Fachinformatiker nutzen das Tool `dig` (Domain Information Groper), um DNS-Probleme strukturiert einzugrenzen.

---

## 🔍 Wichtige DNS-RCODEs (Response Codes)

1. **`NOERROR` (Code 0)**: Anfrage war erfolgreich. Wenn die ANSWER SECTION leer ist, existiert der Name zwar, aber nicht der angefragte Typ (NODATA).
2. **`NXDOMAIN` (Code 3 - Non-Existent Domain)**: Der abgefragte FQDN existiert nicht im Namensraum.
3. **`SERVFAIL` (Code 2 - Server Failure)**: Der Nameserver konnte die Anfrage nicht auflösen (häufig bei DNSSEC Validierungsfehlern, Netzwerk-Timeouts oder Zonenkonfigurationsfehlern).
4. **`REFUSED` (Code 5)**: Der Server lehnt die Antwort ab (z. B. keine Rekursion für externe Clients erlaubt oder Zonentransfer gesperrt).

---

## 🛠️ Wichtige dig-Befehle im Arsenal

```bash
# Kurzantwort für Skripte
dig +short www.heise.de A

# Schrittweise Verfolgung vom Root bis zum Autoritativen Server
dig +trace www.heise.de

# Gezielte Abfrage eines bestimmten DNS-Resolvers
dig @1.1.1.1 google.com MX

# Zonentransfer-Test (Sicherheitsüberprüfung)
dig @ns1.firma.de firma.de AXFR
```

---

## 🎯 Deine Aufgaben im Modul 15:

1. **`diagnose_dns_rcode`**:
   Interpretiert den RCODE aus einer dig-Antwort und gibt präzise Fehlerbeschreibungen und Sysadmin-Handlungsempfehlungen aus.

2. **`extract_dig_ips`**:
   Filtert aus einer rohen dig-Ausgabe alle gültigen IPv4-Adressen der ANSWER SECTION heraus.

3. **`detect_soa_desync`**:
   Vergleicht die SOA-Serial eines Primary Masters mit einem Secondary Slave Server. Wenn die Serial abweicht, wird `DESYNC: Slave out of date` gemeldet.

4. **`verify_axfr_blocked`**:
   Prüft, ob ein Zonentransfer (AXFR) ordnungsgemäß abgewiesen wird (`Transfer failed` oder `REFUSED`).
