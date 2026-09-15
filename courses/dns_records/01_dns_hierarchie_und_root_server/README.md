# DNS 01: DNS-Hierarchie, FQDN-Struktur & Root-Server

Willkommen zu **Modul 01** des Kurses **DNS-Records, Domain Name System & E-Mail-Sicherheit**!

In diesem Modul lernst du die fundamentale Architektur des globalen Domain Name Systems kennen: Wie der umgekehrte DNS-Baum aufgebaut ist, wie Fully Qualified Domain Names (FQDN) strukturiert sind, welche Rolle die 13 weltweiten Root-Server-Cluster spielen und wie Delegationspfade funktionieren.

---

## 💡 1. Das Wichtigste in Kürze

### Die DNS-Baumstruktur (Inverted Tree)
Das DNS ist von oben nach unten organisiert:
- **Root Zone (`.`):** Die oberste Wurzel aller Domains.
- **Top-Level Domains (TLD):** 
  - *ccTLD (Country-Code):* `.de`, `.ch`, `.at`, `.fr`, `.uk`
  - *gTLD (Generic):* `.com`, `.org`, `.net`, `.info`
  - *new gTLD:* `.cloud`, `.dev`, `.app`, `.tech`
- **Second-Level Domains (SLD):** Der registrierte Name der Organisation oder Person (z.B. `it-praxisportal` in `it-praxisportal.de`).
- **Subdomains / Third-Level Domains:** Beliebig tiefe Unterteilungen (z.B. `intern`, `api`, `staging`).
- **Hostname:** Der Name des konkreten Dienstes oder Host-Servers (`srv01`, `www`, `mail`).

```
                . (Root)
               /       \
             de.        com. (TLD)
             /            \
  it-praxisportal.de.   google.com. (SLD)
        /
     intern. (Subdomain)
      /
   srv01. (Hostname)
```

### Der Fully Qualified Domain Name (FQDN)
Ein vollständiger Domänenname enthält alle Ebenen von links nach rechts bis zum abschließenden Punkt der Root-Zone:
`srv01.intern.it-praxisportal.de.`

> [!IMPORTANT]
> **Der abschließende Punkt (`.`):** In DNS-Zonendateien (BIND) ist der Schlusspunkt entscheidend!
> - `www.example.de.` (mit Punkt) = Absoluter FQDN.
> - `www` (ohne Punkt) = Relativer Bezeichner, an den BIND automatisch den Zonennamen anhängt (`$ORIGIN`).
> Ein vergessener Schlusspunkt bei Zielen führt zu Fehlern wie `mail.example.de.example.de.`!

### Die 13 Root-Server-Cluster
Es gibt genau 13 logische IP-Adress-Cluster (A bis M, z.B. `k.root-servers.net`). 
Dank **BGP Anycast** verbergen sich hinter diesen 13 IP-Adressen mehr als 1.500 physische Serverknoten weltweit. Dadurch sind Root-Server extrem ausfallsicher gegen DDoS-Angriffe und Serverausfälle geschützt.

---

## 🎯 Deine Aufgaben in `aufgabe.sh`

1. **TODO 1 (`parse_fqdn`):** Zerlege einen übergebenen FQDN in `HOST`, `DOMAIN`, `SLD`, `TLD` und prüfe, ob der abschließende Root-Punkt gesetzt ist (`HAS_ROOT_DOT: YES/NO`).
2. **TODO 2 (`list_root_server`):** Ermittle den zuständigen Betreiber und FQDN für die Root-Cluster A bis M oder gib alle 13 Cluster aus.
3. **TODO 3 (`build_delegation_path`):** Konstruiere den schrittweisen Delegationspfad von der Root (`.`) über TLD und SLD bis zum FQDN.
4. **TODO 4 (`validate_fqdn_syntax`):** Validiere Domain-Namen nach den RFC-1035-Regeln (Längenlimits, keine unzulässigen Bindestriche).

---

## 🧪 Tests ausführen

Führe im Terminal folgenden Befehl aus:
```bash
bash test_aufgabe.sh
```
