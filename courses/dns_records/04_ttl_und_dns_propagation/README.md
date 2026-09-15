# DNS 04: TTL (Time to Live), Caching & DNS-Propagation

Willkommen zu **Modul 04** des Kurses **DNS-Records, Domain Name System & E-Mail-Sicherheit**!

In diesem Modul lernst du das Herzstück der globalen DNS-Skalierbarkeit kennen: **Caching und die Time to Live (TTL)**. Du erfährst, warum DNS-Propagation Zeit benötigt, wie Servermigrationen ohne Downtime geplant werden und was **Negative Caching** bedeutet.

---

## 💡 1. Das Wichtigste in Kürze

### Wie Caching funktioniert
- Jeder DNS-Record besitzt eine TTL in Sekunden.
- Fragt ein Resolver einen Eintrag an, speichert er ihn im lokalen RAM-Cache.
- Bei Folgeabfragen liefert der Resolver die Antwort direkt aus dem Cache und zählt die TTL sekundengenau herunter.
- Nach Ablauf der TTL (`TTL=0`) verwirft der Resolver den Eintrag und kontaktiert den autoritativen Server erneut.

### Die typische Migrations-Katastrophe
Ein Unternehmen will am Samstag um 20:00 Uhr seine Website auf eine neue Server-IP umziehen. Die aktuelle TTL des A-Records beträgt **86.400 Sekunden (24 Stunden)**.
- *Fehler:* Der Administrator ändert die IP erst am Samstag um 20:00 Uhr.
- *Die Folge:* Bis zu 24 Stunden lang leiten Caches von Telekom, Vodafone, Google und Co. Besucher auf den alten Server weiter!
- *Best Practice:*
  1. Mindestens **24 bis 48 Stunden vor dem Umzug** die TTL auf **300 Sekunden (5 Minuten)** senken.
  2. Am Samstag umziehen (die Änderung ist nun innerhalb von 5 Minuten weltweit aktiv).
  3. Nach erfolgreichem Test die TTL wieder auf 86.400s anheben.

### Negative Caching (RFC 2308)
Auch Nicht-Existenz (`NXDOMAIN`) wird gecacht! Die Gültigkeitsdauer dafür bestimmt das **5. numerische Feld im SOA-Record** (Minimum / Negative Cache TTL). Typische Werte liegen zwischen 1.800s (30 Min.) und 7.200s (2 Std.).

---

## 🎯 Deine Aufgaben in `aufgabe.sh`

1. **TODO 1 (`format_ttl_human`):** Rechne Sekundenwerte in Tage, Stunden, Minuten und Sekunden um.
2. **TODO 2 (`plan_dns_migration`):** Berechne die Vorlaufzeit für eine Servermigration basierend auf der aktuellen TTL.
3. **TODO 3 (`simulate_cache_decay`):** Berechne die verbleibende Rest-TTL im Resolver-Cache.
4. **TODO 4 (`extract_soa_negative_ttl`):** Extrahiere das Negative Caching Feld aus einem SOA-Record und prüfe die RFC-Konformität.

---

## 🧪 Tests ausführen

Führe im Terminal folgenden Befehl aus:
```bash
bash test_aufgabe.sh
```
