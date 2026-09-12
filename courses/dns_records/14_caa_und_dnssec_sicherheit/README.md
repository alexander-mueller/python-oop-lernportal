# DNS 14: CAA Records & DNSSEC Vertrauenskette

Willkommen zum Kurs **DNS-Records, Domain Name System & E-Mail-Sicherheit** im IT-Praxisportal!

## 💡 Das Wichtigste in Kürze
- **Ziel:** CAA zur Autorisierung von Zertifizierungsstellen (Let's Encrypt) und DNSSEC Signierung (RRSIG, DNSKEY, DS).
- **Wichtigstes Tool:** `delv`

## 🎯 Deine Aufgaben (Checkliste)
1. **Teilziel 1:** CAA-Record für autorisierte CAs ('issue "letsencrypt.org"') anlegen
2. **Teilziel 2:** DNSSEC Komponenten: Key Signing Key (KSK) & Zone Signing Key (ZSK) verstehen
3. **Teilziel 3:** Delegation Signer (DS) Record für die übergeordnete TLD berechnen
4. **Teilziel 4:** DNSSEC Vertrauenskette mit delv oder dig +dnssec validieren

## 🧪 Tests ausführen
```bash
bash test_aufgabe.sh
```
