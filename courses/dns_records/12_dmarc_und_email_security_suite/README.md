# DNS 12: DMARC Policy & Phishing-Abwehr

Willkommen zu **Modul 12** des Kurses **DNS-Records, Domain Name System & E-Mail-Sicherheit**!

In diesem Modul komplettieren wir die E-Mail-Sicherheits-Trilogie: **DMARC (RFC 7489)** verbindet SPF und DKIM zu einer bindenden Durchsetzungsrichtlinie. Du lernst, wie du per `p=reject` Spoofing im Keim erstickst, aggregierte XML-Reports (`rua=`) auswertest und führst ein automatisches Gesamtaudit deiner Domain durch.

---

## 💡 1. Das Wichtigste in Kürze

### Was DMARC leistet
Ohne DMARC weiß ein empfangender Server nicht, was er tun soll, wenn SPF oder DKIM fehlschlagen. DMARC gibt dem Domain-Inhaber die Kontrolle zurück:
```dns
_dmarc.it-praxisportal.de.   3600   IN   TXT   "v=DMARC1; p=reject; rua=mailto:dmarc-reports@it-praxisportal.de; pct=100"
```

### Die drei Policies (`p=`)
1. **`p=none` (Monitoring):** Zum Start. Mails werden zugestellt, du erhältst aber tägliche Reports über unberechtigte Sender.
2. **`p=quarantine` (Spam):** Mails ohne gültigen Nachweis landen im Spam-Ordner.
3. **`p=reject` (Abweisung):** Die Königsdisziplin! Der empfangende Server bricht die Verbindung noch während des SMTP-Dialogs ab (`550 5.7.1 Unauthenticated mail rejected`).

---

## 🎯 Deine Aufgaben in `aufgabe.sh`

1. **TODO 1 (`format_dmarc_record`):** Erstelle einen standardkonformen DMARC TXT-Record unter `_dmarc.<domain>.`.
2. **TODO 2 (`evaluate_dmarc_verdict`):** Simuliere die Empfänger-Entscheidung (Pass, Deliver, Quarantine, Reject).
3. **TODO 3 (`audit_email_security_suite`):** Führe ein 100-Punkte-Audit der Kombination aus SPF, DKIM und DMARC durch.

---

## 🧪 Tests ausführen

Führe im Terminal folgenden Befehl aus:
```bash
bash test_aufgabe.sh
```
