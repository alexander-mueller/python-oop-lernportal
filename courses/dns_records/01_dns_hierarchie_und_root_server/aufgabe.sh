#!/usr/bin/env bash
# ==============================================================================
# 🌐 DNS Grundlagen - DNS 01: DNS-Hierarchie & Root-Server
# ==============================================================================

# 🎯 TEILZIEL 1: FQDN in Hostname, SLD und TLD zerlegen
# 🎯 TEILZIEL 2: Root-Server-Cluster (A-M) und Anycast-Routing erklären
# 🎯 TEILZIEL 3: Unterschied autoritativer vs. rekursiver Nameserver definieren
# 🎯 TEILZIEL 4: DNS-Baumpfad für www.it-praxisportal.de konstruieren

analyze_dns_hierarchy() {
  local domain="${1:-it-praxisportal.de}"
  echo "▶ Analysiere DNS-Konfiguration für $domain..."

  # TODO: Implementiere die geforderten DNS-Prüfungen oder Record-Erstellungen
  return 1
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  analyze_dns_hierarchy "$@"
fi
