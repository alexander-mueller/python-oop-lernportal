# DNS 11: DKIM (DomainKeys Identified Mail) & Kryptografische Signaturen

Willkommen zu **Modul 11** des Kurses **DNS-Records, Domain Name System & E-Mail-Sicherheit**!

In diesem Modul lernst du den zweiten Pfeiler moderner Mail-Security kennen: **DKIM (RFC 6376)**. Du erfährst, wie asymmetrische Kryptografie (RSA/Ed25519) die Unveränderbarkeit von E-Mails sicherstellt, wie der **DKIM-Selector** im DNS adressiert wird und wie das **255-Zeichen-String-Limit** bei langen 2048-Bit Schlüsseln gelöst wird.

---

## 💡 1. Das Wichtigste in Kürze

### Wie DKIM funktioniert
1. Der versendende Mail-Server signiert Body und wichtige Header mit seinem privaten Schlüssel (`Private Key`).
2. Die Signatur wird als Mail-Header `DKIM-Signature:` in die E-Mail eingebettet.
3. Der empfangende Server liest den Selector `s=` aus und schlägt den öffentlichen Schlüssel im DNS nach:
   `<selector>._domainkey.<domain>.`
4. Stimmt die mathematische Signaturprüfung, ist bewiesen: **Die E-Mail wurde nach dem Absenden nicht manipuliert!**

### Der BIND 255-Byte Split
Ein 2048-Bit RSA-Schlüssel ist knapp 400 Zeichen lang. Ein einzelnes String-Literal in DNS darf maximal 255 Zeichen lang sein. BIND erlaubt die Aufteilung in zwei Strings in runden Klammern:
```dns
s2026._domainkey.firma.de.  IN  TXT  (
    "v=DKIM1; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA123..."
    "...RestDesSchluesselsHierFortgesetzt" )
```

---

## 🎯 Deine Aufgaben in `aufgabe.sh`

1. **TODO 1 (`build_dkim_fqdn`):** Erzeuge den standardkonformen DKIM-DNS-Namen (`<selector>._domainkey.<domain>.`).
2. **TODO 2 (`audit_dkim_key_security`):** Prüfe die Schlüssellänge und warne vor unsicheren 1024-Bit RSA-Keys.
3. **TODO 3 (`format_dkim_record`):** Formatiere den TXT-Record mit 255-Zeichen-Splitting für BIND.
4. **TODO 4 (`parse_dkim_record`):** Extrahiere Version, Algorithmus und Public Key aus einem DKIM-String.

---

## 🧪 Tests ausführen

Führe im Terminal folgenden Befehl aus:
```bash
bash test_aufgabe.sh
```
