#!/usr/bin/env bash
# ==============================================================================
# 🌐 DNS 03: UDP VS. TCP PORT 53, TRUNCATION & EDNS0
# ==============================================================================
#
# TRANSPORTPROTOKOLLE IM DNS:
# - Standard-Port: Port 53 (sowohl UDP als auch TCP).
#
# WANN UDP?
# - Für normale Anfragen und kurze Antworten (Standard).
# - Extrem schnell, verbindungslos, minimaler Netzwerk-Overhead.
# - Historisches Limit nach RFC 1035: Maximal 512 Bytes Nutzlast pro UDP-Paket!
#
# WANN TCP?
# 1. Zonentransfers (AXFR / IXFR):
#    Die Replikation kompletter Zonendateien von Master- auf Slave-Server erfolgt
#    stets über TCP/53 (zuverlässiger Datenstrom).
# 2. Truncation Fallback:
#    Wenn eine Antwort größer als 512 Bytes ist (ohne EDNS0), setzt der Server
#    das TC-Flag (Truncated = 1). Der Client muss die Anfrage daraufhin sofort
#    über TCP/53 wiederholen!
#
# EDNS0 (RFC 6891 - Extension Mechanisms for DNS):
# - Erweitert den UDP-Puffer auf typischerweise 1232 bis 4096 Bytes über einen
#   speziellen OPT-Pseudorecord in der Additional Section.
# - Essentiell für DNSSEC, da kryptografische Signaturen (RRSIG) oft >512B groß sind.
# ==============================================================================

# 🎯 TEILZIEL 1 (TODO 1): Transportprotokoll dynamisch auswählen
# Funktion: select_dns_transport "$packet_size" "$query_type" "$edns_supported"
# Parameter $1: Paketgröße in Bytes (Zahl, z.B. 450 oder 1200)
# Parameter $2: Query-Typ (z.B. "A", "MX", "AXFR", "TXT")
# Parameter $3: EDNS0-Unterstützung ("true" oder "false")
# Regeln:
# - Wenn query_type == "AXFR" oder "IXFR" -> Ausgabe: "TCP (Grund: Zonentransfer erfordert zwingend TCP)"
# - Wenn packet_size <= 512 -> Ausgabe: "UDP (Grund: Paket passt in Standard-512B-Puffer)"
# - Wenn packet_size > 512 UND edns_supported == "true" UND packet_size <= 4096 ->
#     Ausgabe: "UDP_EDNS0 (Grund: EDNS0 erweitert UDP-Puffer auf bis zu 4096 Bytes)"
# - Wenn packet_size > 512 UND edns_supported == "false" ->
#     Ausgabe: "TCP_TRUNCATED (Grund: TC=1 gesetzt, Fallback auf TCP erforderlich)"
select_dns_transport() {
  local size="$1"
  local qtype="$2"
  local edns="$3"
  # TODO 1: Implementiere die Protokollauswahl
  return 0
}

# 🎯 TEILZIEL 2 (TODO 2): DNS-Header Sektionszähler parsen
# Funktion: parse_section_counts "$qdcount" "$ancount" "$nscount" "$arcount"
# Parameter $1: QDCOUNT (Anzahl Fragen / Questions)
# Parameter $2: ANCOUNT (Anzahl Antworten / Answers)
# Parameter $3: NSCOUNT (Anzahl autoritativer Nameserver / Authority)
# Parameter $4: ARCOUNT (Anzahl Zusatzinformationen / Additional)
# Anforderungen:
# - Formatiere die Ausgabe als übersichtlichen Report:
#   QUESTIONS=<qdcount>
#   ANSWERS=<ancount>
#   AUTHORITY=<nscount>
#   ADDITIONAL=<arcount>
#   STATUS=<EMPTY_RESPONSE | HAS_ANSWERS | REFERRAL_ONLY>
# Status-Regeln:
# - Wenn ancount > 0 -> "HAS_ANSWERS"
# - Wenn ancount == 0 UND nscount > 0 -> "REFERRAL_ONLY"
# - Wenn ancount == 0 UND nscount == 0 -> "EMPTY_RESPONSE"
parse_section_counts() {
  local qd="$1"
  local an="$2"
  local ns="$3"
  local ar="$4"
  # TODO 2: Parse die Zähler und bestimme den Status
  return 0
}

# 🎯 TEILZIEL 3 (TODO 3): EDNS0-Prüfung aus dig-Output
# Funktion: verify_edns0_in_dig "$dig_output_file"
# Parameter $1: Pfad zu einer Textdatei mit einer `dig`-Ausgabe
# Anforderungen:
# - Suche in der Datei nach der Zeile: ";; OPT PSEUDOSECTION:"
# - Prüfe, ob "EDNS: version: 0" und "udp:" vorhanden sind.
# - Extrahiere die Puffergröße (z.B. "4096" oder "1232" hinter "udp:").
# - Ausgabe wenn vorhanden: "EDNS0_ACTIVE: Puffergröße <size> Bytes" und return 0.
# - Ausgabe wenn fehlt: "EDNS0_INACTIVE: Kein OPT Pseudo-Record gefunden (512B Limit)" und return 1.
verify_edns0_in_dig() {
  local file="$1"
  # TODO 3: Prüfe den dig-Output auf EDNS0
  return 0
}

# 🎯 TEILZIEL 4 (TODO 4): Zonentransfer-Sperre in BIND absichern
# Funktion: secure_zone_transfers "$zone_name" "$allowed_slave_ip" "$output_file"
# Parameter $1: Zonenname (z.B. "it-praxisportal.de")
# Parameter $2: Erlaubte Slave-IP (z.B. "192.168.1.55")
# Parameter $3: Zieldatei (z.B. "/etc/bind/named.conf.local")
# Hintergrund:
# Ein ungeschützter Nameserver erlaubt jedem Internetnutzer den Download der kompletten
# Zonendatei via `dig AXFR @ns1.domain.de domain.de`. Dies verrät alle internen Server!
# Anforderungen:
# - Schreibe die Zonendefinition in die Zieldatei:
# zone "<zone_name>" {
#     type master;
#     file "/var/lib/bind/db.<zone_name>";
#     allow-transfer { <allowed_slave_ip>; };
# };
secure_zone_transfers() {
  local zone="$1"
  local slave_ip="$2"
  local out_file="$3"
  # TODO 4: Erzeuge die abgesicherte BIND-Zonendeklaration
  return 0
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  echo "=== Test Teilziel 1 ==="
  select_dns_transport 700 "TXT" "false"
  echo ""
  echo "=== Test Teilziel 2 ==="
  parse_section_counts 1 2 0 1
fi
