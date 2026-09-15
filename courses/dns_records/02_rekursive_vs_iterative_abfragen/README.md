# DNS 02: Rekursive vs. Iterative Abfragen & DNS-Flags

Willkommen zu **Modul 02** des Kurses **DNS-Records, Domain Name System & E-Mail-Sicherheit**!

In diesem Modul lernst du den Unterschied zwischen der rekursiven Anfrage eines Clients und der iterativen Recherche des Resolvers im globalen DNS-Baum kennen. Zudem analysierst du zentrale DNS-Header-Flags und schützt Nameserver vor dem gefährlichen **Open Resolver**-Zustand.

---

## 💡 1. Das Wichtigste in Kürze

### Rekursiv vs. Iterativ
- **Rekursive Abfrage (Client &rarr; Resolver):**
  - Der Client fordert: *„Finde die IP für mich heraus, ich warte auf das fertige Ergebnis!“*
  - Signalisiert durch das Flag **RD** (Recursion Desired = 1).
  - Der Server antwortet mit **RA** (Recursion Available = 1), falls er diesen Dienst anbietet.
- **Iterative Abfrage (Resolver &rarr; Nameserver-Hierarchie):**
  - Der Resolver fragt den Server: *„Kennst du die IP?“*
  - Der Nameserver antwortet: *„Nein, aber frage bitte den Server X, der ist für die Zone zuständig (Referral)!“*
  - Der Resolver hangelt sich von der Root (`.`) über die TLD (`.de`) bis zum autoritativen Server (`firma.de`).
  - Der letzte Server setzt das Flag **AA** (Authoritative Answer = 1), da er die Master-Zonendatei besitzt.

```
+-------------+                 +----------------------+
| Client (PC) | -- RD=1 Query ->| Rekursiver Resolver  |
|             | <-  IP Result --| (z.B. Router / BIND) |
+-------------+                 +----------------------+
                                   |         ^
                       1. Root (.) |         | Referral to .de
                                   v         |
                               +----------------------+
                               |   Root-Server (.)    |
                               +----------------------+
                                   |         ^
                     2. TLD (.de)  |         | Referral to firma.de
                                   v         |
                               +----------------------+
                               |  TLD-Server (.de)    |
                               +----------------------+
                                   |         ^
                 3. SLD (firma.de) |         | AA=1 (192.0.2.1)
                                   v         |
                               +----------------------+
                               | Auth NS (firma.de)   |
                               +----------------------+
```

### Die wichtigsten DNS-Flags
| Flag | Name | Bedeutung |
| :--- | :--- | :--- |
| **QR** | Query / Response | `0` = Anfrage, `1` = Antwort |
| **AA** | Authoritative Answer | `1` = Antwort stammt direkt vom Master-Nameserver der Zone |
| **TC** | Truncated | `1` = Antwort war größer als der UDP-Puffer und wurde abgeschnitten |
| **RD** | Recursion Desired | `1` = Client wünscht rekursive Auflösung |
| **RA** | Recursion Available | `1` = Server unterstützt Rekursion |

### Sicherheitsrisiko: Open Resolver
Ein Nameserver mit `RA=1`, der Anfragen aus dem gesamten Internet (`0.0.0.0/0`) beantwortet, ist ein **Open Resolver**.
Angreifer nutzen solche Server für **DNS Amplification Attacks**: Sie fälschen die Absender-IP (IP-Spoofing auf das Opfer) und senden kleine Anfragen mit riesiger Antwort (z.B. `dig ANY isc.org`), wodurch das Opfer mit Gigabit-Datenmengen überflutet wird!

---

## 🎯 Deine Aufgaben in `aufgabe.sh`

1. **TODO 1 (`parse_dns_flags`):** Zerlege einen Flag-String und ermittle den Status von `QR`, `AA`, `TC`, `RD` und `RA`.
2. **TODO 2 (`simulate_iterative_steps`):** Gib die 4 aufeinanderfolgenden Schritte der iterativen Auflösung für eine gegebene Domain aus.
3. **TODO 3 (`detect_open_resolver`):** Prüfe Nameserver-Flags und ACL-Netzwerk auf Open-Resolver-Schwachstellen.
4. **TODO 4 (`generate_forwarder_config`):** Generiere eine sichere BIND9-Konfiguration mit Upstream-Forwardern.

---

## 🧪 Tests ausführen

Führe im Terminal folgenden Befehl aus:
```bash
bash test_aufgabe.sh
```
