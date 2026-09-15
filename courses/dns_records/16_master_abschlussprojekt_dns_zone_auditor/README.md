# Modul 16: Master-Abschlussprojekt &ndash; Enterprise DNS Zone Auditor

## 🏆 Willkommen zum Master-Abschlussprojekt des DNS-Kurses!
Du hast die gesamte DNS-Architektur gemeistert: Von den 13 Root-Clustern über CNAME-Apex-Konflikte, SPF/DKIM/DMARC E-Mail-Sicherheit bis hin zu Active Directory SRV-Records und DNSSEC.

In diesem Abschlussprojekt entwickelst du ein **vollständiges, produktionsreifes DNS-Zone-Auditing-Werkzeug** in Bash.

---

## 🎯 Anforderungen an den DNS Zone Auditor:

Der Auditor liest eine BIND-Zonendatei oder simuliert die Überprüfung einer Live-Domain und führt 5 fundamentale Checks durch:

1. **Check 1: SOA-Record Validierung**:
   - Existiert ein SOA-Record?
   - Hat die Serial das gültige 10-stellige Datumsformat `YYYYMMDDNN`?
2. **Check 2: NS-Redundanz (RFC 2182)**:
   - Sind mindestens **2 verschiedene Nameserver (NS)** definiert?
3. **Check 3: CNAME-Apex Kollisionsprüfung (RFC 1912)**:
   - Befindet sich am Zone-Apex (`@`) versehentlich ein CNAME-Record?
4. **Check 4: E-Mail-Sicherheits-Trilogie**:
   - Existiert ein SPF TXT Record mit sicherem `-all`?
   - Existiert ein DMARC Record mit `p=quarantine` oder `p=reject`?
5. **Check 5: Gesamtbewertung & Score**:
   - Berechnet einen Gesamt-Sicherheits-Score (0 bis 100 Punkte) und gibt das Urteil `AUDIT_PASSED` (>=80) oder `AUDIT_FAILED` aus.
