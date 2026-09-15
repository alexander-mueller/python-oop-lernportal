# Modul 14: CAA Records & DNSSEC Sicherheit (RFC 8659, RFC 4034)

## 📌 Didaktische Einführung & Relevanz für IT-Sicherheit
Klassisches DNS besitzt **keine Authentizität und keine Integritätsprüfung**. Jeder Man-in-the-Middle kann gefälschte DNS-Antworten unterschieben (DNS Spoofing / Cache Poisoning). Zudem kann theoretisch jede öffentliche Zertifizierungsstelle (CA) SSL/TLS-Zertifikate für beliebige Domains ausstellen.

Dieses Modul schließt beide Sicherheitslücken:
1. **CAA Records (Certification Authority Authorization - RFC 8659)**:
   Legt verbindlich fest, welche CAs (z. B. Let's Encrypt oder DigiCert) überhaupt TLS-Zertifikate für die Domain ausstellen dürfen. Verhindert unautorisierte Zertifikatsausstellung!
2. **DNSSEC (DNS Security Extensions - RFC 4033-4035)**:
   Signiert DNS-Resource-Records kryptografisch mit asymmetrischen Schlüsseln.
   - **RRSIG**: Die digitale Signatur über ein Record-Set (RRset).
   - **DNSKEY**: Der öffentliche Schlüssel der Zone (ZSK: Zone Signing Key & KSK: Key Signing Key).
   - **DS (Delegation Signer)**: Der SHA-256 Hash des KSK, der in der übergeordneten Parent-Zone (z. B. `.de`) hinterlegt wird.

---

## ⚙️ CAA-Record Syntax im BIND-Format

```text
; domain.tld.  TTL   Class CAA Flags Tag   Value
firma.de.      3600  IN    CAA 0     issue "letsencrypt.org"
firma.de.      3600  IN    CAA 0     issuewild ";"
firma.de.      3600  IN    CAA 0     iodef "mailto:security@firma.de"
```

### Die CAA-Tags:
- `issue`: Erlaubt der genannten CA normale Host-Zertifikate auszustellen.
- `issuewild`: Regelt Wildcard-Zertifikate (`*.firma.de`). Der Wert `";"` verbietet Wildcards komplett!
- `iodef`: Empfängt Vorfalls-Meldungen (Incident Reporting) bei unberechtigten Ausstellungsversuchen.

---

## 🔐 DNSSEC Vertrauenskette (Chain of Trust)

```text
  [ Root-Zone . ]  --> Verankert mit Trust Anchor
         ↓ (DS Record für 'de')
  [ TLD-Zone .de ] --> DNSKEY & RRSIG
         ↓ (DS Record für 'firma.de')
  [ Eigene Zone firma.de ] --> KSK signiert ZSK, ZSK signiert A/AAAA/MX
```

---

## 🎯 Deine Aufgaben im Modul 14:

1. **`format_caa_record`**:
   Erzeugt standardkonforme BIND CAA Records mit Tag und Anführungszeichen:
   `format_caa_record "firma.de" "issue" "letsencrypt.org" 3600`
   -> `firma.de. 3600 IN CAA 0 issue "letsencrypt.org"`

2. **`format_caa_wildcard_block`**:
   Erzeugt die Richtlinie, die normale Zertifikate über Let's Encrypt erlaubt, Wildcard-Zertifikate aber strikt blockiert (`issuewild ";"`).

3. **`parse_ds_record`**:
   Zerlegt einen DNSSEC DS-Record in Key-Tag, Algorithmus, Digest-Type und Digest-Hash:
   Eingabe: `firma.de. 3600 IN DS 2371 13 2 49FD...`
   Ausgabe: `KEY_TAG=2371 ALGO=13 DIGEST_TYPE=2 HASH=49FD...`

4. **`verify_dnssec_chain_status`**:
   Prüft, ob KSK und DS übereinstimmen und liefert `DNSSEC_VALIDATED` oder `BOGUS_CHAIN_BROKEN`.
