# DNS 05: A- & AAAA-Records (IPv4 & IPv6 Dual-Stack)

Willkommen zu **Modul 05** des Kurses **DNS-Records, Domain Name System & E-Mail-Sicherheit**!

In diesem Modul lernst du die elementaren Vorwärts-Resource-Records des Internets kennen: **A-Records für IPv4** und **AAAA-Records für IPv6**. Du erfährst, wie moderne Dual-Stack-Architekturen aufgebaut werden, wie Round-Robin DNS funktioniert und führst ein automatisches Dual-Stack-Audit durch.

---

## 💡 1. Das Wichtigste in Kürze

### A-Record (IPv4 Address)
- Weist einem Namen eine 32-Bit IPv4-Adresse zu (z.B. `192.0.2.1`).
- Syntax: `www   3600  IN  A   192.0.2.1`

### AAAA-Record (IPv6 Address)
- Weist einem Namen eine 128-Bit IPv6-Adresse zu (z.B. `2001:db8::1`).
- Heißt „Quad-A“, weil 128 Bit genau 4-mal so lang sind wie 32 Bit.
- Syntax: `www   3600  IN  AAAA  2001:db8::1`

### Round-Robin DNS
Wenn du mehrere Server für Lastverteilung besitzt, erstellst du mehrere A-Records unter demselben Namen:
```dns
web   300   IN  A   192.0.2.10
web   300   IN  A   192.0.2.11
web   300   IN  A   192.0.2.12
```
Der Nameserver liefert bei jeder Anfrage die Liste in rotierter Reihenfolge zurück.

---

## 🎯 Deine Aufgaben in `aufgabe.sh`

1. **TODO 1 (`format_a_record`):** Validiere eine IPv4-Adresse und formatiere den BIND A-Record.
2. **TODO 2 (`format_aaaa_record`):** Validiere eine IPv6-Adresse und formatiere den BIND AAAA-Record.
3. **TODO 3 (`generate_round_robin_pool`):** Erzeuge mehrere A-Records für denselben Hostnamen.
4. **TODO 4 (`audit_dual_stack`):** Prüfe eine Zonendatei darauf, ob alle IPv4-Hosts auch einen AAAA-Record besitzen.

---

## 🧪 Tests ausführen

Führe im Terminal folgenden Befehl aus:
```bash
bash test_aufgabe.sh
```
