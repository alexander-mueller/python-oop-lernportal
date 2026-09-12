# DNS 11: DKIM Kryptografische E-Mail-Signatur

Willkommen zum Kurs **DNS-Records, Domain Name System & E-Mail-Sicherheit** im IT-Praxisportal!

## 💡 Das Wichtigste in Kürze
- **Ziel:** Public Key im DNS: Selektoren (s1._domainkey.domain.de), RSA/Ed25519 Schlüssel und Header-Validierung.
- **Wichtigstes Tool:** `opendkim-testkey`

## 🎯 Deine Aufgaben (Checkliste)
1. **Teilziel 1:** DKIM-Schlüsselpaar (Private/Public RSA 2048 Bit) generieren
2. **Teilziel 2:** DNS TXT-Record unter dem Selektor s1._domainkey eintragen
3. **Teilziel 3:** Tags v=DKIM1; k=rsa; p=PublicKey im Record formatieren
4. **Teilziel 4:** DKIM-Signaturprüfung simulieren

## 🧪 Tests ausführen
```bash
bash test_aufgabe.sh
```
