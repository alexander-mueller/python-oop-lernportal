# DNS 07: SOA (Start of Authority) & Serial-Management

Willkommen zu **Modul 07** des Kurses **DNS-Records, Domain Name System & E-Mail-Sicherheit**!

In diesem Modul lernst du den wichtigsten administrativen Record einer jeden Zonendatei kennen: den **SOA-Record (Start of Authority)**. Du erfährst, wie die **10-stellige Serial-Nummer** funktioniert, wie E-Mail-Adressen in DNS-Notation umgewandelt werden und welche Bedeutung die Timer **Refresh**, **Retry**, **Expire** und **Minimum TTL** haben.

---

## 💡 1. Das Wichtigste in Kürze

### Aufbau des SOA-Records
```dns
@   IN  SOA  ns1.firma.de.  hostmaster.firma.de. (
    2026091501 ; Serial: Versionsnummer YYYYMMDDNN
    7200       ; Refresh (2h): Secondary fragt alle 2 Stunden nach Updates
    3600       ; Retry (1h): Wiederholung nach 1 Stunde bei Nichterreichbarkeit
    1209600    ; Expire (2 Wochen): Secondary stoppt Antworten nach 2 Wochen ohne Master
    3600       ; Minimum TTL: Gültigkeitsdauer für negatives Caching (NXDOMAIN)
)
```

### Die E-Mail-Adresse im SOA
Weil das Zeichen `@` im DNS-Format den Zonenursprung (`$ORIGIN`) repräsentiert, wird in der Administrator-E-Mail das `@` durch einen Punkt `.` ersetzt:
- `hostmaster@firma.de` &rarr; `hostmaster.firma.de.`

### Die Serial-Nummer (`YYYYMMDDNN`)
- `YYYYMMDD`: 8-stelliges Datum (z.B. `20260915`).
- `NN`: 2-stellige Revisionszählung des Tages (z.B. `01`, `02`, `03`).
- **Secondary-Replikation:** Ein Slave-Nameserver führt nur dann einen Zonentransfer durch, wenn die Serial des Masters **größer** ist als seine eigene lokale Serial!

---

## 🎯 Deine Aufgaben in `aufgabe.sh`

1. **TODO 1 (`format_hostmaster_email`):** Konvertiere eine normale E-Mail-Adresse in DNS-kompatible SOA-Notation.
2. **TODO 2 (`generate_soa_serial`):** Generiere eine 10-stellige Serial `YYYYMMDDNN`.
3. **TODO 3 (`increment_soa_serial`):** Inkrementiere die Serial für denselben Tag oder setze sie an einem neuen Tag auf `01`.
4. **TODO 4 (`generate_complete_soa`):** Schreibe einen vollständigen BIND9-kompatiblen SOA-Header-Block.

---

## 🧪 Tests ausführen

Führe im Terminal folgenden Befehl aus:
```bash
bash test_aufgabe.sh
```
