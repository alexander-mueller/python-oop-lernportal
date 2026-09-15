#!/usr/bin/env bash
# ==============================================================================
# 🌐 DNS 10: SPF (SENDER POLICY FRAMEWORK) & DAS 10-LOOKUP LIMIT
# ==============================================================================
#
# WAS IST SPF (RFC 7208)?
# Das Sender Policy Framework verhindert E-Mail-Spoofing. Der Domaininhaber
# hinterlegt einen TXT-Record im DNS, der festlegt, welche Server und IP-Adressen
# berechtigt sind, Mails mit dieser Absenderdomäne zu verschicken.
#
# SYNTAX EINES SPF-RECORDS:
#   @   IN   TXT   "v=spf1 mx ip4:188.245.100.5 include:_spf.google.com -all"
#
# DIE BESTANDTEILE:
# 1. Versionskennung: "v=spf1" (muss exakt am Anfang stehen)
# 2. Mechanismen:
#    - "mx" : Alle im MX-Record gelisteten Server dürfen senden
#    - "ip4:<ip>/<cidr>" : Konkrete IPv4-Adressen oder Netze
#    - "ip6:<ipv6>" : IPv6-Adressen
#    - "include:<domain>" : Übernimmt die SPF-Regeln eines Dienstleisters
# 3. Der All-Qualifier (Das Urteil für alle anderen):
#    - "-all" (HardFail): Strikte Ablehnung unberechtigter Server (empfohlen!)
#    - "~all" (SoftFail): Akzeptieren, aber als Spam markieren
#    - "?all" (Neutral): Keine Aussage
#    - "+all" (Pass): EXTREM GEFÄHRLICH! Erlaubt jedem Spammer den Versand!
#
# ⚠️ DAS 10-DNS-LOOKUP-LIMIT:
# Ein SPF-Check darf maximal 10 DNS-Lookups auslösen ("include", "a", "mx", "ptr").
# Überschreitet der Record dieses Limit, bricht der Empfänger mit "PermError" ab!
# ==============================================================================

# 🎯 TEILZIEL 1 (TODO 1): Syntaktisch validen SPF-String zusammenbauen
# Funktion: build_spf_record "$mx_allowed" "$ipv4_list" "$include_list" "$qualifier"
# Parameter $1: "true" oder "false" (ob der "mx" Mechanismus enthalten sein soll)
# Parameter $2: Leerzeichen-separierte Liste von IPv4-Adressen (z.B. "192.0.2.1 198.51.100.10")
# Parameter $3: Leerzeichen-separierte Liste von Includes (z.B. "_spf.google.com")
# Parameter $4: Qualifier ("-all" oder "~all")
# Ausgabe:
#   v=spf1 [mx] [ip4:...] [include:...] <qualifier>
# Beispiel:
#   v=spf1 mx ip4:192.0.2.1 include:_spf.google.com -all
build_spf_record() {
  local use_mx="$1"
  local ips="$2"
  local incs="$3"
  local qual="${4:--all}"
  # TODO 1: Bilde den SPF-String
  return 0
}

# 🎯 TEILZIEL 2 (TODO 2): SPF DNS-Lookups zählen (RFC 7208 Limit)
# Funktion: count_spf_lookups "$spf_string"
# Parameter $1: Ein vollständiger SPF-String (z.B. "v=spf1 a mx include:a.de include:b.de -all")
# Anforderungen:
# - Zähle jedes Vorkommen von Mechanismen, die einen DNS-Lookup auslösen:
#   * "include:"
#   * "a" oder "a:"
#   * "mx" oder "mx:"
#   * "ptr"
#   * "redirect="
# - Wenn count <= 10:
#     Gib aus: "LOOKUP_COUNT=<count> | RFC7208_OK"
#     return 0
# - Wenn count > 10:
#     Gib aus: "LOOKUP_LIMIT_EXCEEDED: <count> Lookups überschreiten das 10er-Limit!"
#     return 1
count_spf_lookups() {
  local spf="$1"
  # TODO 2: Zähle die DNS-Lookups
  return 0
}

# 🎯 TEILZIEL 3 (TODO 3): All-Qualifier Sicherheit prüfen
# Funktion: audit_spf_qualifier "$spf_string"
# Parameter $1: Ein SPF-String
# Anforderungen:
# - Wenn "+all" enthalten ist:
#     Gib aus: "DANGEROUS: +all erlaubt jedem Server weltweit das Spoofing!"
#     return 1
# - Wenn "?all" enthalten ist:
#     Gib aus: "WEAK: ?all ist neutral und bietet keinen Fälschungsschutz."
#     return 1
# - Wenn "~all" enthalten ist:
#     Gib aus: "SOFTFAIL: ~all akzeptabel für Testphasen."
#     return 0
# - Wenn "-all" enthalten ist:
#     Gib aus: "SECURE: -all HardFail erzwingt strikten Schutz."
#     return 0
audit_spf_qualifier() {
  local spf="$1"
  # TODO 3: Prüfe den Qualifier
  return 0
}

# 🎯 TEILZIEL 4 (TODO 4): Vollständigen BIND TXT-Record erzeugen
# Funktion: format_spf_txt_record "$domain" "$spf_string" "$ttl"
# Parameter $1: Domäne (z.B. "@" oder "firma.de.")
# Parameter $2: Der SPF-String
# Parameter $3: TTL (Standard: 3600)
# Anforderungen:
# - Formatiere als BIND TXT Record mit Anführungszeichen:
#   <domain>    <ttl>   IN  TXT "<spf_string>"
format_spf_txt_record() {
  local domain="$1"
  local spf="$2"
  local ttl="${3:-3600}"
  # TODO 4: Formatiere den BIND TXT-Record
  return 0
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  echo "=== Test Teilziel 1 ==="
  build_spf_record "true" "192.0.2.1" "_spf.google.com" "-all"
  echo ""
  echo "=== Test Teilziel 2 ==="
  count_spf_lookups "v=spf1 mx include:_spf.google.com -all"
  echo ""
  echo "=== Test Teilziel 3 ==="
  audit_spf_qualifier "v=spf1 +all"
fi
