# DNS 08: NS-Delegation, Reverse DNS (PTR) & FCrDNS

Willkommen zu **Modul 08** des Kurses **DNS-Records, Domain Name System & E-Mail-Sicherheit**!

In diesem Modul lernst du die Verwaltung autoritativer **Nameserver-Delegationen (NS)** und die Funktionsweise von **Reverse DNS (PTR-Records)** kennen. Du erfährst, wie IP-Adressen für die `.in-addr.arpa`-Zone umgekehrt werden und warum **Forward-Confirmed Reverse DNS (FCrDNS)** für produktive Mail-Server zwingend erforderlich ist.

---

## 💡 1. Das Wichtigste in Kürze

### NS-Records (Delegation)
NS-Records delegieren eine Zone oder Subdomain an zuständige Server:
```dns
firma.de.   86400   IN  NS   ns1.provider.de.
firma.de.   86400   IN  NS   ns2.provider.de.
```
> [!IMPORTANT]
> **Redundanz-Anforderung:** Nach RFC 2182 müssen mindestens zwei autoritative Nameserver existieren, die sich in unterschiedlichen Subnetzen (vorzugsweise unterschiedlichen Autonomen Systemen / AS) befinden.

### Reverse DNS & PTR-Records (`in-addr.arpa`)
Normales DNS übersetzt `Name -> IP`. Reverse DNS übersetzt `IP -> Name`.
Da DNS-Bäume von links nach rechts spezifischer werden, müssen die 4 Oktette einer IPv4-Adresse für die `in-addr.arpa`-Hierarchie **umgekehrt** werden:
- IP: `198.51.100.42`
- PTR-Eintrag: `42.100.51.198.in-addr.arpa. IN PTR mail.firma.de.`

### FCrDNS (Forward-Confirmed Reverse DNS)
Damit Spammer keine gefälschten Hostnamen vortäuschen können, prüfen empfangende Mailserver das **FCrDNS-Prinzip**:
1. Empfänger schlägt die IP des sendenden Servers per Reverse-Lookup nach: `198.51.100.42` &rarr; `mail.firma.de`.
2. Empfänger schlägt nun sofort diesen Hostnamen per A-Record nach: `mail.firma.de` &rarr; `198.51.100.42`.
3. Nur wenn beide IP-Adressen exakt übereinstimmen, wird die Verbindung akzeptiert!

---

## 🎯 Deine Aufgaben in `aufgabe.sh`

1. **TODO 1 (`ipv4_to_ptr_name`):** Kehre die 4 Oktette einer IPv4-Adresse um und bilde den `in-addr.arpa.`-Namen.
2. **TODO 2 (`format_ptr_record`):** Formatiere einen vollständigen BIND9 PTR-Record.
3. **TODO 3 (`format_ns_delegation`):** Erstelle zwei redundante NS-Records für eine Zonen-Delegation.
4. **TODO 4 (`verify_fcrdns`):** Validiere das Forward-Confirmed Reverse DNS Prinzip.

---

## 🧪 Tests ausführen

Führe im Terminal folgenden Befehl aus:
```bash
bash test_aufgabe.sh
```
