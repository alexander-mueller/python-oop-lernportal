# DNS 03: UDP vs. TCP Port 53, Truncation & EDNS0

Willkommen zu **Modul 03** des Kurses **DNS-Records, Domain Name System & E-Mail-Sicherheit**!

In diesem Modul erfährst du, warum DNS auf **Port 53** sowohl UDP als auch TCP nutzt, was das historische **512-Byte-UDP-Limit** bedeutet, wie das **TC-Flag (Truncated)** funktioniert und warum **EDNS0 (RFC 6891)** für modernes DNSSEC unverzichtbar ist.

---

## 💡 1. Das Wichtigste in Kürze

### Port 53: Warum zwei Protokolle?
1. **UDP/53 (User Datagram Protocol):**
   - Standard für DNS-Abfragen und normale Antworten.
   - Schnell, geringer Overhead (kein 3-Wege-Handshake wie bei TCP).
   - Historisches Limit nach RFC 1035: **Maximal 512 Bytes** Payload pro UDP-Paket.
2. **TCP/53 (Transmission Control Protocol):**
   - **Zonentransfers (AXFR / IXFR):** Die Replikation vollständiger Zonen zwischen Master- und Secondary-Nameservern erfordert TCP für garantierte Datenübertragung.
   - **Fallback bei Truncation:** Passt eine Antwort nicht in den UDP-Puffer, sendet der Server ein Paket mit gesetztem `TC=1` (Truncated) Flag. Der Client wiederholt dieselbe Abfrage unverzüglich über TCP/53.

### EDNS0: Extension Mechanisms for DNS (RFC 6891)
Um ständige TCP-Verbindungsaufbauten bei großen Antworten (z.B. DNSSEC-Signaturen mit >1000 Bytes) zu verhindern, führt EDNS0 eine Pseudo-Resource-Record (`OPT`) in der *Additional Section* ein.
Damit signalisiert der Client dem Server: *„Mein UDP-Puffer kann bis zu 4096 (oder 1232) Bytes empfangen!“*

---

## 🎯 Deine Aufgaben in `aufgabe.sh`

1. **TODO 1 (`select_dns_transport`):** Entscheide anhand von Paketgröße, Query-Typ und EDNS0-Status, ob UDP, TCP oder ein Fallback nötig ist.
2. **TODO 2 (`parse_section_counts`):** Wertet die 4 Header-Zähler aus (Questions, Answers, Authority, Additional) und ermittelt den Response-Status.
3. **TODO 3 (`verify_edns0_in_dig`):** Prüft einen `dig`-Output auf das Vorhandensein der `OPT PSEUDOSECTION` und liest die Puffergröße aus.
4. **TODO 4 (`secure_zone_transfers`):** Schützt BIND9 vor unautorisierten Zonentransfers (`allow-transfer`).

---

## 🧪 Tests ausführen

Führe im Terminal folgenden Befehl aus:
```bash
bash test_aufgabe.sh
```
