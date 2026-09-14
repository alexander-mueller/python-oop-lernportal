#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IHK Prüfungsfragen-Generator für Fachinformatiker Systemintegration (AP1 & AP2).
Generiert 165 authentische, strukturierte Prüfungsfragen nach den offiziellen
IHK/AkA/ZPA-Operatoren (Nennen, Erläutern, Berechnen, Begründen, Skizzieren).
"""

import json
from pathlib import Path

questions = []

def add_q(qid, exam, lf, topic, scenario, qtext, points, sol, qtype='text', options=None):
    questions.append({
        'id': qid,
        'exam': exam,           # 'AP1', 'AP2_T1', 'AP2_T2', 'WiSo'
        'lernfeld': lf,
        'topic': topic,
        'scenario': scenario,
        'question': qtext,
        'points': points,
        'solution': sol,
        'type': qtype,
        'options': options or []
    })

# ==============================================================================
# BEREICH 1: AP1 (Lernfelder 1 bis 8) - Einrichten eines IT-gestützten Arbeitsplatzes
# ==============================================================================

# --- LF 1: Unternehmen & Organisation ---
add_q('ap1_lf1_001', 'AP1', 'LF 1', 'Rechtsformen Einzelunternehmen vs GmbH',
      'Der IT-Dienstleister Max Weber überlegt, sein Einzelunternehmen in eine GmbH umzuwandeln.',
      'Vergleichen Sie das Einzelunternehmen und die Gesellschaft mit beschränkter Haftung (GmbH) hinsichtlich Haftung der Inhaber und Mindestkapital.',
      6,
      'Einzelunternehmen: Inhaber haftet unbeschränkt persönlich mit dem gesamten Privat- und Geschäftsvermögen; kein Mindestkapital vorgeschrieben. (3 Pkt.)\n'
      'GmbH: Haftung ist auf das Gesellschaftsvermögen beschränkt; Mindeststammkapital beträgt 25.000 EUR (mind. 12.500 EUR bei Gründung einzuzahlen). (3 Pkt.)')

add_q('ap1_lf1_002', 'AP1', 'LF 1', 'Projektmanagement Wasserfall vs Agil (Scrum)',
      'In der IT-Abteilung soll ein neues Ticketsystem eingeführt werden. Diskutiert wird das Vorgehen nach dem klassischen Wasserfallmodell versus Scrum.',
      'Nennen Sie zwei wesentliche Unterschiede zwischen dem sequentiellen Phasenmodell (Wasserfall) und dem agilen Vorgehen nach Scrum und begründen Sie, wann Scrum zu bevorzugen ist.',
      8,
      'Unterschiede:\n'
      '1. Planung & Flexibilität: Wasserfall plant den gesamten Projektumfang im Voraus starr; Scrum arbeitet in kurzen iterativen Sprints (1-4 Wochen) und erlaubt flexible Anforderungsanpassungen. (3 Pkt.)\n'
      '2. Lieferergebnisse: Wasserfall liefert das fertige Endprodukt erst am Projektende; Scrum liefert nach jedem Sprint ein potenziell auslieferbares Produktinkrement (Shippable Increment). (3 Pkt.)\n'
      'Begründung: Scrum ist zu bevorzugen, wenn Anforderungen zu Projektbeginn unvollständig oder dynamisch sind und schnelles Feedback der Anwender nötig ist. (2 Pkt.)')

add_q('ap1_lf1_003', 'AP1', 'LF 1', 'Scrum Rollen und Artefakte',
      'Ein Softwareentwicklungsteam arbeitet nach dem Scrum-Framework.',
      'Nennen Sie die drei Kernrollen in Scrum und beschreiben Sie die Aufgaben des Scrum Masters.',
      6,
      'Drei Rollen: Product Owner, Scrum Master, Developers / Entwicklerteam. (3 Pkt.)\n'
      'Aufgaben des Scrum Masters: Dient als Servant Leader und Coach, sorgt für die Einhaltung der Scrum-Regeln, beseitigt Hindernisse (Impediments) und schützt das Team vor externen Störungen. (3 Pkt.)')

add_q('ap1_lf1_004', 'AP1', 'LF 1', 'Vertragsarten Dienstvertrag vs Werkvertrag',
      'Ein externes Beratungsunternehmen wird für die Installation eines Netzwerks und die Schulung der Mitarbeiter beauftragt.',
      'Unterscheiden Sie Dienstvertrag (§ 611 BGB) und Werkvertrag (§ 631 BGB) hinsichtlich der geschuldeten Leistung und Gewährleistungsansprüche und ordnen Sie die beiden Tätigkeiten zu.',
      8,
      'Dienstvertrag (§ 611 BGB): Geschuldet wird lediglich das bloße Tätigwerden/Bemühen, kein konkreter Erfolg; keine Mängelgewährleistung. Beispiel: Mitarbeiterschulung. (4 Pkt.)\n'
      'Werkvertrag (§ 631 BGB): Geschuldet wird ein konkreter, fehlerfreier Erfolg (das Werk); der Auftragnehmer haftet für Mängel (Nacherfüllung, Minderung, Rücktritt). Beispiel: Installation und betriebsbereite Übergabe des Netzwerks. (4 Pkt.)')

add_q('ap1_lf1_005', 'AP1', 'LF 1', 'Organisationsformen Matrixorganisation',
      'Ein Systemhaus mit 120 Mitarbeitern führt eine Matrixorganisation ein.',
      'Erläutern Sie das Funktionsprinzip einer Matrixorganisation und nennen Sie einen wesentlichen Vorteil sowie einen typischen Nachteil.',
      6,
      'Funktionsprinzip: Mehrdimensionale Organisationsstruktur, bei der Mitarbeiter gleichzeitig einer funktionalen Fachabteilung (z. B. Netzwerktechnik) und einer Projektleitung disziplinarisch bzw. fachlich unterstellt sind (Mehrliniensystem). (2 Pkt.)\n'
      'Vorteil: Hohe Flexibilität, optimale Auslastung von Spezialisten, abteilungsübergreifender Wissenstransfer. (2 Pkt.)\n'
      'Nachteil: Hohes Konfliktpotenzial durch Kompetenzstreitigkeiten zwischen Fach- und Projektleitern, Doppelunterstellung kann Mitarbeiter überlasten. (2 Pkt.)')

add_q('ap1_lf1_006', 'AP1', 'LF 1', 'Magisches Dreieck des Projektmanagements',
      'In einem IT-Migrationsprojekt fordert der Kunde kurzfristig zusätzliche Funktionalitäten ohne Erhöhung des Budgets.',
      'Beschreiben Sie die drei Eckpunkte des Magischen Dreiecks und erläutern Sie die Auswirkungen dieser Kundenforderung auf das Projekt.',
      6,
      'Eckpunkte: Zeit (Termine/Dauer), Kosten (Budget/Ressourcen), Qualität/Umfang (Scope/Leistung). (3 Pkt.)\n'
      'Auswirkung: Wenn der Umfang erweitert wird, aber Kosten/Budget gleich bleiben, gerät das Dreieck aus dem Gleichgewicht: Die Fertigstellungszeit muss verlängert werden, oder die Qualität des Produkts sinkt durch Zeitdruck und reduzierte Tests. (3 Pkt.)')

add_q('ap1_lf1_007', 'AP1', 'LF 1', 'Stakeholder-Analyse',
      'Vor dem Rollout einer neuen ERP-Software wird eine Stakeholder-Analyse durchgeführt.',
      'Definieren Sie den Begriff Stakeholder und nennen Sie vier typische Stakeholder eines solchen Projekts.',
      6,
      'Definition: Alle Personen, Gruppen oder Organisationen, die ein berechtigtes Interesse am Projekt haben oder durch dessen Verlauf/Ergebnis direkt oder indirekt beeinflusst werden. (2 Pkt.)\n'
      'Vier Stakeholder: 1. Endanwender/Mitarbeiter, 2. Projektleitung/Management, 3. Betriebsrat, 4. Software-Lieferant/Dienstleister. (Je 1 Pkt. = 4 Pkt.)')

add_q('ap1_lf1_008', 'AP1', 'LF 1', 'Gantt-Diagramm und Kritischer Pfad',
      'Im Rahmen der Netzwerkmigration wird der Terminplan mittels Netzplantechnik optimiert.',
      'Definieren Sie den Begriff Kritischer Pfad und erklären Sie, warum Vorgänge auf diesem Pfad besondere Aufmerksamkeit erfordern.',
      6,
      'Definition: Die längste Kette zeitlich voneinander abhängiger Vorgänge vom Projektstart bis zum Projektende, bei denen der Gesamtpuffer (GP) und freie Puffer (FP) jeweils null Tage betragen. (3 Pkt.)\n'
      'Bedeutung: Jede Verzögerung bei einem Vorgang auf dem kritischen Pfad führt unmittelbar zu einer Verzögerung des gesamten Projektendtermins. (3 Pkt.)')

# --- LF 2: Arbeitsplätze ausstatten (Hardware, USV, Ergonomie, TCO) ---
add_q('ap1_lf2_001', 'AP1', 'LF 2', 'USV-Klassen nach EN 62040-3',
      'Die Geschäftsleitung der Meier Logistik AG rüstet ihren Serverraum mit einer unterbrechungsfreien Stromversorgung aus.',
      'Nennen Sie die drei USV-Klassen nach EN 62040-3 und erläutern Sie, warum für unternehmenskritische Server ausschließlich eine VFI-USV (Online-Doppelwandler) eingesetzt werden sollte.',
      8,
      '1. VFD (Offline/Voltage and Frequency Dependent): Umschaltzeit 4-10 ms, schützt nur vor Stromausfall. (2 Pkt.)\n'
      '2. VI (Line-Interactive/Voltage Independent): Umschaltzeit 2-4 ms, Spannungsstabilisierung via AVR. (2 Pkt.)\n'
      '3. VFI (Online/Voltage and Frequency Independent): Keine Umschaltzeit (0 ms), permanente Doppelwandlung AC->DC->AC, filtert alle Netzstörungen, Oberschwingungen und Frequenzschwankungen heraus. (4 Pkt.)')

add_q('ap1_lf2_002', 'AP1', 'LF 2', 'USV-Dimensionierung Berechnung',
      'Zwei Virtualisierungshosts mit je 550 Watt Leistungsaufnahme und ein SAN-Storage mit 300 Watt sollen bei einem Stromausfall für mindestens 20 Minuten weiterbetrieben werden können. Der Wirkungsgrad der USV liegt bei 85 %.',
      'Berechnen Sie die mindestens bereitzustellende Energie der USV-Akkus in Wattstunden (Wh). Geben Sie Formel und Rechenweg an.',
      6,
      'Gesamtlast: P_ges = (2 * 550 W) + 300 W = 1400 Watt. (2 Pkt.)\n'
      'Leistungsbedarf inkl. Wirkungsgrad: P_aufwand = 1400 W / 0,85 = 1647,06 Watt. (2 Pkt.)\n'
      'Energie für 20 Minuten (20/60 h = 1/3 h): E = 1647,06 W * (1/3) h = 549,02 Wh. (Mindestens 550 Wh). (2 Pkt.)',
      qtype='calc')

add_q('ap1_lf2_003', 'AP1', 'LF 2', 'Schnittstellen Thunderbolt 4 vs USB4',
      'Für die Grafikabteilung werden Notebooks beschafft, die über ein einziges Kabel an eine Dockingstation zwei 4K-Displays mit 60 Hz ansteuern, das Notebook mit 85 Watt laden und 10-Gbit-Ethernet bereitstellen sollen.',
      'Nennen Sie die erforderliche Schnittstelle am Notebook und erläutern Sie zwei relevante Leistungsmerkmale (Power Delivery & DisplayPort Alt Mode).',
      6,
      'Schnittstelle: Thunderbolt 4 oder USB4 (mindestens 40 Gbit/s Bandbreite). (2 Pkt.)\n'
      'Power Delivery (USB-PD): Unterstützt bidirektionale Ladeleistungen bis 100W bzw. 240W über dasselbe Kabel. (2 Pkt.)\n'
      'DisplayPort Alt Mode: Ermöglicht die native Übertragung von DisplayPort-Audiodateien und Videosignalen über die physischen Leitungen. (2 Pkt.)')

add_q('ap1_lf2_004', 'AP1', 'LF 2', 'RAM & ECC-Funktionsweise',
      'Ein Kunde fragt, warum in Servern spezieller ECC-Arbeitsspeicher (Error-Correcting Code) verbaut wird, während in Desktop-PCs Non-ECC RAM zum Einsatz kommt.',
      'Erläutern Sie die Funktionsweise von ECC-Speicher und begründen Sie die Notwendigkeit im Serverbetrieb.',
      6,
      'Funktionsweise: ECC-RAM nutzt zusätzliche Prüfbits (z. B. 72 Bit Datenbreite statt 64 Bit für 8 Paritätsbits), um 1-Bit-Speicherfehler (Single Bit Flips) mittels Hamming-Code automatisch zur Laufzeit im laufenden Betrieb zu korrigieren und 2-Bit-Fehler zu erkennen. (4 Pkt.)\n'
      'Notwendigkeit: Verhindert Serverabstürze (Blue Screens / Kernel Panics) und schleichende Datenkorruption in Datenbanken bei 24/7-Dauerbetrieb. (2 Pkt.)')

add_q('ap1_lf2_005', 'AP1', 'LF 2', 'DGUV Ergonomie am Bildschirmarbeitsplatz',
      'Im Rahmen einer Gefährdungsbeurteilung nach der Arbeitsstättenverordnung (ArbStättV / DGUV Information 215-410) wird ein Bildschirmarbeitsplatz überprüft.',
      'Nennen Sie vier konkrete ergonomische Anforderungen an die Ausgestaltung des Bildschirmarbeitsplatzes.',
      8,
      '1. Sehabstand zum Monitor: 50 bis 70 cm (bei größeren Bildschirmen bis 80 cm). (2 Pkt.)\n'
      '2. Positionierung zum Fenster: Blickrichtung parallel zur Fensterfront zur Vermeidung von Direkt- und Reflexblendung. (2 Pkt.)\n'
      '3. Höhe der Bildschirmoberkante: Maximal auf Augenhöhe, sodass der Blick um ca. 20-35 Grad leicht nach unten geneigt ist. (2 Pkt.)\n'
      '4. Beleuchtung: Mindestens 500 Lux mittlere Beleuchtungsstärke im Arbeitsbereich. (2 Pkt.)')

add_q('ap1_lf2_006', 'AP1', 'LF 2', 'TCO CapEx vs OpEx Kostenrechnung',
      'Bei der Anschaffung einer neuen Serverinfrastruktur vergleicht die Geschäftsleitung den Kauf eigener Server (On-Premises) mit einem Cloud-Modell (IaaS).',
      'Definieren Sie die Begriffe CapEx und OpEx und ordnen Sie jeweils zwei typische Kostenpositionen zu.',
      6,
      'CapEx (Capital Expenditure): Einmalige Investitionsausgaben für langlebiges Anlagevermögen. Beispiele: Anschaffungskosten der Server-Hardware, Kauf von Switches, USV-Anlage. (3 Pkt.)\n'
      'OpEx (Operational Expenditure): Laufende Betriebsausgaben zur Aufrechterhaltung des Betriebs. Beispiele: Monatliche Cloud-Abonnements, Stromkosten im Rechenzentrum, Wartungs- und Supportverträge. (3 Pkt.)')

add_q('ap1_lf2_007', 'AP1', 'LF 2', 'Nutzwertanalyse Durchführung',
      'Ein Systemhaus bewertet drei Angebote für Notebooks anhand gewichteter Kriterien.',
      'Erläutern Sie das rechnerische Vorgehen zur Ermittlung des gewichteten Gesamtnutzens und begründen Sie, warum das Angebot mit den niedrigsten Anschaffungskosten nicht zwingend den Zuschlag erhält.',
      6,
      'Vorgehen: Für jedes Kriterium wird die vergebene Punktzahl (z. B. 1-10) mit dem Gewichtungsfaktor in Prozent multipliziert. Die Summe aller gewichteten Teilnutzwerte ergibt den Gesamtnutzwert. Das Angebot mit dem höchsten Gesamtnutzen gewinnt. (4 Pkt.)\n'
      'Begründung: Die NWA ist ein multikriterielles Verfahren, das qualitative und funktionale Merkmale (z. B. Akkulaufzeit, Displayqualität, Garantie) gleichberechtigt neben den reinen Anschaffungspreis stellt. (2 Pkt.)')

add_q('ap1_lf2_008', 'AP1', 'LF 2', 'DIN 66399 SSD-Datenlöschung',
      'Ausgemusterte Mitarbeiter-Laptops mit SSD-Speichern (Solid State Drives) sollen entsorgt werden.',
      'Beschreiben Sie zwei zulässige Verfahren zur sicheren Datenlöschung auf Solid State Drives nach DIN 66399 und erklären Sie, warum klassisches Überschreiben mit Nullen bei SSDs ungeeignet ist.',
      8,
      '1. ATA-Secure-Erase / NVMe-Sanitize-Befehl: Weist den internen Flash-Controller an, alle Speicherzellen inkl. Reservesektoren durch Spannungsimpulse zu entladen und den internen AES-Schlüssel zu löschen (Crypto Erase). (3 Pkt.)\n'
      '2. Mechanisches Schreddern: Physische Zerstörung des SSD-Datenträgers nach Sicherheitsstufe H-4 oder H-5 (Partikelgröße kleiner 30 mm² bzw. 10 mm²). (3 Pkt.)\n'
      'Warum Nullen ungeeignet sind: Durch Wear-Leveling und Reservesektoren (Over-Provisioning) adressieren normale Schreibbefehle nicht alle physischen Flash-Zellen; Daten verbleiben ungelöscht. (2 Pkt.)')

add_q('ap1_lf2_009', 'AP1', 'LF 2', 'UEFI vs BIOS & TPM 2.0',
      'Für moderne Windows-Installationen müssen alle neuen PCs bestimmte Hardwareanforderungen erfüllen.',
      'Nennen Sie drei wesentliche technische Unterschiede zwischen Legacy-BIOS und UEFI und erklären Sie die Kernfunktion des TPM 2.0 Chips.',
      8,
      'Unterschiede:\n'
      '1. Partitionstabelle: UEFI nutzt GPT (Partitionen > 2 TB, bis zu 128 Partitionen), BIOS nutzt MBR (max. 2 TB, nur 4 primäre Partitionen). (2 Pkt.)\n'
      '2. Sicherheit: UEFI unterstützt Secure Boot (Signaturprüfung des Bootloaders). (2 Pkt.)\n'
      '3. Architektur: UEFI läuft im 64-Bit-Modus mit eigener grafischer Oberfläche und Netzwerkunterstützung, BIOS im 16-Bit-Real-Mode. (2 Pkt.)\n'
      'TPM 2.0 (Trusted Platform Module): Kryptografischer Hardwarechip zur sicheren Schlüsselspeicherung (z. B. für BitLocker) und zur Integritätsmessung der Bootkette (Measured Boot). (2 Pkt.)')

add_q('ap1_lf2_010', 'AP1', 'LF 2', 'Dateisysteme Vergleich exFAT vs NTFS vs ext4',
      'Ein Techniker muss ein externes USB-Laufwerk formatieren, das Dateien über 4 GB speichern soll und an Windows-, macOS- und Linux-Rechnern ohne Zusatzsoftware les- und schreibbar sein muss.',
      'Ermitteln Sie das am besten geeignete Dateisystem und begründen Sie den Ausschluss von FAT32 und NTFS.',
      6,
      'Geeignetes Dateisystem: exFAT (Extended File Allocation Table). (2 Pkt.)\n'
      'Ausschluss FAT32: Unterstützt nur eine maximale Dateigröße von 4 GiB (2^32 - 1 Bytes) und maximale Partitionsgrößen von 2 TB bzw. 32 GB unter Windows-Formatierung. (2 Pkt.)\n'
      'Ausschluss NTFS: Wird unter macOS standardmäßig nur lesend unterstützt; Schreibzugriffe erfordern proprietäre Treiber von Drittanbietern. (2 Pkt.)')

add_q('ap1_lf2_011', 'AP1', 'LF 2', 'Netzteile Wirkungsgrad 80 PLUS',
      'Ein Servernetzteil mit 80 PLUS Platinum Zertifizierung liefert 800 Watt Ausgangsleistung an die Serverkomponenten bei einem Wirkungsgrad von 92 %.',
      'Berechnen Sie die Wirkleistung, die das Netzteil aus dem 230V-Netz aufnimmt, und die entstehende thermische Verlustleistung in Watt.',
      6,
      'Aufgenommene Leistung: P_in = P_out / Wirkungsgrad = 800 W / 0,92 = 869,57 Watt. (3 Pkt.)\n'
      'Verlustleistung (Wärmeabgabe): P_verlust = P_in - P_out = 869,57 W - 800 W = 69,57 Watt. (3 Pkt.)',
      qtype='calc')

add_q('ap1_lf2_012', 'AP1', 'LF 2', 'PUE-Wert im Rechenzentrum',
      'Ein Rechenzentrum verbraucht insgesamt 1.500.000 kWh elektrische Energie pro Jahr. Davon entfallen 1.000.000 kWh direkt auf die IT-Hardware (Server, Storage, Netzwerk).',
      'Berechnen Sie den PUE-Wert (Power Usage Effectiveness) und erläutern Sie dessen Bedeutung.',
      6,
      'Formel: PUE = Gesamte aufgenommene Energie / Energiebedarf der IT-Hardware. (2 Pkt.)\n'
      'Berechnung: PUE = 1.500.000 kWh / 1.000.000 kWh = 1,50. (2 Pkt.)\n'
      'Bedeutung: Ein Wert von 1,5 bedeutet, dass für jedes Watt IT-Leistung zusätzliche 0,5 Watt für Infrastruktur (Kühlung, USV-Verluste, Beleuchtung) benötigt werden. Idealwert ist 1,0. (2 Pkt.)',
      qtype='calc')

# --- LF 3: Netzwerke & Subnetting ---
add_q('ap1_lf3_001', 'AP1', 'LF 3', 'IPv4 Subnetting /27 Berechnung',
      'Einem Subnetz ist die IP-Adresse 172.20.14.98 mit der CIDR-Präfixlänge /27 zugewiesen.',
      'Berechnen Sie: 1. Subnetzmaske in Dezimalpunkt-Notation, 2. Netzwerkadresse, 3. Erste nutzbare Host-IP, 4. Letzte nutzbare Host-IP, 5. Broadcastadresse, 6. Anzahl nutzbarer Hostadressen.',
      12,
      '1. Subnetzmaske: 255.255.255.224 (/27 entspricht 11111111.11111111.11111111.11100000). (2 Pkt.)\n'
      '2. Schrittweite: 256 - 224 = 32. Blockgrenzen: 0, 32, 64, 96, 128... -> Netzadresse: 172.20.14.96. (2 Pkt.)\n'
      '3. Erste nutzbare Host-IP: 172.20.14.97. (2 Pkt.)\n'
      '4. Broadcastadresse: 172.20.14.127. (2 Pkt.)\n'
      '5. Letzte nutzbare Host-IP: 172.20.14.126. (2 Pkt.)\n'
      '6. Nutzbare Hostadressen: 2^5 - 2 = 32 - 2 = 30 Hosts. (2 Pkt.)',
      qtype='calc')

add_q('ap1_lf3_002', 'AP1', 'LF 3', 'VLSM Variable Length Subnet Mask',
      'Das Basisnetz 192.168.50.0/24 soll mittels VLSM für drei Abteilungen aufgeteilt werden: Vertrieb (55 Hosts), Entwicklung (28 Hosts) und Support (12 Hosts).',
      'Ermitteln Sie für alle drei Subnetze jeweils die Netzadresse und die CIDR-Präfixlänge.',
      9,
      'Vertrieb (55 Hosts + 2 = 57 Adressen -> 2^6 = 64): Netzadresse 192.168.50.0/26 (Bereich: .0 bis .63). (3 Pkt.)\n'
      'Entwicklung (28 Hosts + 2 = 30 Adressen -> 2^5 = 32): Netzadresse 192.168.50.64/27 (Bereich: .64 bis .95). (3 Pkt.)\n'
      'Support (12 Hosts + 2 = 14 Adressen -> 2^4 = 16): Netzadresse 192.168.50.96/28 (Bereich: .96 bis .111). (3 Pkt.)',
      qtype='calc')

add_q('ap1_lf3_003', 'AP1', 'LF 3', 'IPv6 Kürzungsregeln nach RFC 5952',
      'Ein Client hat die IPv6-Adresse 2001:0db8:0000:0042:0000:0000:0000:0001/64 konfiguriert.',
      'Kürzen Sie die Adresse nach den offiziellen RFC-5952-Regeln und erläutern Sie die Bedeutung der Link-Local-Adresse (fe80::/10).',
      6,
      'Gekürzte Adresse: 2001:db8:0:42::1/64 (Führende Nullen pro Block weglassen; die längste zusammenhängende Folge von Null-Blöcken einmalig durch :: ersetzen). (3 Pkt.)\n'
      'Link-Local (fe80::/10): Automatisch generierte, nicht im Internet geroutete Adresse zur lokalen Kommunikation im selben Subnetz (z. B. für Neighbor Discovery Protocol NDP, DHCPv6 und Router Solicitations). (3 Pkt.)')

add_q('ap1_lf3_004', 'AP1', 'LF 3', 'DHCP DORA-Prozess',
      'Ein neuer Arbeitsplatz-PC wird mit dem Unternehmensnetzwerk per Patchkabel verbunden.',
      'Beschreiben Sie die vier Phasen des DHCP-Lease-Prozesses (DORA) und geben Sie jeweils an, ob die Nachricht als Broadcast oder Unicast gesendet wird.',
      8,
      '1. DHCPDISCOVER (Broadcast): Client sucht im lokalen Netz nach verfügbaren DHCP-Servern. (2 Pkt.)\n'
      '2. DHCPOFFER (Unicast oder Broadcast): DHCP-Server bieten dem Client eine freie IP-Adresse samt Parametern an. (2 Pkt.)\n'
      '3. DHCPREQUEST (Broadcast): Client wählt ein Angebot aus und fordert die Bindung an (Broadcast informiert auch andere Server). (2 Pkt.)\n'
      '4. DHCPACK (Unicast oder Broadcast): Server bestätigt die Vergabe und überträgt Lease-Dauer, Subnetzmaske, Gateway und DNS. (2 Pkt.)')

add_q('ap1_lf3_005', 'AP1', 'LF 3', 'DNS Resource Records',
      'Ein Administrator verwaltet die Forward- und Reverse-Lookup-Zonen im internen DNS-Server.',
      'Erklären Sie die jeweilige Funktion der folgenden vier DNS-Resource-Records: A, AAAA, CNAME und PTR.',
      8,
      '1. A-Record: Löst einen vollqualifizierten Domänennamen (FQDN) in eine IPv4-Adresse auf. (2 Pkt.)\n'
      '2. AAAA-Record: Löst einen FQDN in eine 128-Bit IPv6-Adresse auf. (2 Pkt.)\n'
      '3. CNAME-Record (Canonical Name): Dient als Alias/Verweis auf einen anderen bestehenden A- oder AAAA-Record. (2 Pkt.)\n'
      '4. PTR-Record (Pointer): Ermöglicht das Reverse-DNS-Lookup (Auflösung einer IP-Adresse in den FQDN). (2 Pkt.)')

add_q('ap1_lf3_006', 'AP1', 'LF 3', 'OSI-Referenzmodell Zuordnung',
      'Netzwerkgeräte und Protokolle werden im 7-Schichten-Modell nach ISO/IEC 7498-1 eingeordnet.',
      'Ordnen Sie die folgenden vier Begriffe der jeweils korrekten Schicht (1 bis 7) mit deutschem und englischem Namen zu: Switch, Router, TCP, HTTP.',
      8,
      '1. Switch: Schicht 2 (Sicherungsschicht / Data Link Layer - Weiterleitung anhand von MAC-Adressen). (2 Pkt.)\n'
      '2. Router: Schicht 3 (Vermittlungsschicht / Network Layer - Weiterleitung anhand logischer IP-Adressen). (2 Pkt.)\n'
      '3. TCP: Schicht 4 (Transportschicht / Transport Layer - End-to-End-Verbindung und Segmentierung). (2 Pkt.)\n'
      '4. HTTP: Schicht 7 (Anwendungsschicht / Application Layer - Protokoll für Webdienste). (2 Pkt.)')

add_q('ap1_lf3_007', 'AP1', 'LF 3', 'Kupferverkabelung Cat 6a vs Cat 7',
      'Bei einer Neuausstattung eines Bürogebäudes wird über Cat 6a versus Cat 7 diskutiert.',
      'Nennen Sie Übertragungsfrequenz und max. Datenrate von Cat 6a und erläutern Sie die Bezeichnung S/FTP.',
      6,
      'Cat 6a: Grenzfrequenz 500 MHz, Datenrate bis zu 10 Gbit/s (10GBASE-T) über die maximale Kanallänge von 100 Metern. (2 Pkt.)\n'
      'S/FTP: Shielded with Foiled Twisted Pair -> S = Gesamtabschirmung des Kabels durch ein Kupfergeflecht (Braid Screen); FTP = Jedes einzelne der vier Adernpaare ist zusätzlich mit einer Aluminium-Abschirmfolie umwickelt. (4 Pkt.)')

add_q('ap1_lf3_008', 'AP1', 'LF 3', 'LWL Fasertypen Singlemode vs Multimode',
      'Zwei Firmengebäude im Abstand von 950 Metern sollen über ein Glasfaserkabel miteinander verbunden werden.',
      'Vergleichen Sie Singlemode- (OS2) und Multimode-Glasfasern (OM4) bezüglich Kerndurchmesser, Lichtquelle und Reichweite und begründen Sie Ihre Wahl für das Projekt.',
      8,
      'Singlemode (OS2): Kerndurchmesser ca. 9 µm, Lichtquelle Laser, Reichweite bis über 40 km, keine Modendispersion. (3 Pkt.)\n'
      'Multimode (OM4): Kerndurchmesser 50 µm, Lichtquelle VCSEL/LED, Reichweite typisch max. 400-550 Meter bei 10 Gbit/s. (3 Pkt.)\n'
      'Entscheidung: Für 950 m muss zwingend Singlemode-Glasfaser (OS2) gewählt werden, da Multimode bei 10 Gbit/s die geforderte Distanz überschreitet. (2 Pkt.)')

add_q('ap1_lf3_009', 'AP1', 'LF 3', 'Switch MAC-Address Table & Flooding',
      'Ein Switch empfängt einen Frame auf Port 3 mit einer Ziel-MAC-Adresse, die nicht in seiner internen SAT-Tabelle (Source Address Table / CAM-Table) verzeichnet ist.',
      'Beschreiben Sie die Reaktion des Switches auf diesen Frame (Unicast Flooding) und erklären Sie, wie der Switch seine MAC-Adresstabelle füllt.',
      6,
      'Reaktion (Unknown Unicast Flooding): Der Switch leitet den Frame an alle aktiven Ports desselben VLANs weiter, mit Ausnahme des Eingangsports 3. (3 Pkt.)\n'
      'Lernen (MAC Learning): Der Switch liest bei jedem eingehenden Frame die Quell-MAC-Adresse (Source MAC) aus dem Ethernet-Header und speichert die Zuordnung Port <-> MAC zusammen mit einem Aging-Timer in seiner CAM-Tabelle. (3 Pkt.)')

add_q('ap1_lf3_010', 'AP1', 'LF 3', 'WLAN Wi-Fi 6 (802.11ax) Technologien',
      'Ein Unternehmen stattet Besprechungsräume mit Wi-Fi 6 Access Points aus.',
      'Nennen und erläutern Sie zwei Schlüsseltechnologien von Wi-Fi 6 (OFDMA und MU-MIMO), die für hohe Clientdichten sorgen.',
      6,
      'OFDMA (Orthogonal Frequency Division Multiple Access): Teilt einen Funkkanal in viele kleine Unterträger (Resource Units) auf, sodass der AP gleichzeitig mit mehreren Clients Datenpakete in einem einzigen Übertragungszyklus austauschen kann (geringe Latenz). (3 Pkt.)\n'
      'MU-MIMO (Multi-User MIMO): Ermöglicht gleichzeitiges Senden und Empfangen über mehrere räumliche Streams (Spatial Streams) an mehrere Endgeräte zeitgleich in Up- und Downlink. (3 Pkt.)')

add_q('ap1_lf3_011', 'AP1', 'LF 3', 'Kollisionsdomäne vs Broadcastdomäne',
      'In einer Netzwerktopologie befinden sich Hubs, Switche und Router.',
      'Definieren Sie die Begriffe Kollisionsdomäne und Broadcastdomäne und geben Sie an, wie viele dieser Domänen ein 24-Port-Layer-2-Switch standardmäßig besitzt.',
      6,
      'Kollisionsdomäne: Netzwerkbereich, in dem Datenpakete kollidieren können, wenn zwei Stationen gleichzeitig senden (CSMA/CD). (2 Pkt.)\n'
      'Broadcastdomäne: Netzwerkbereich, in dem ein gesendeter Broadcast-Frame (Ziel: FF:FF:FF:FF:FF:FF) alle angeschlossenen Knoten erreicht. (2 Pkt.)\n'
      '24-Port-Switch: Besitzt 24 separate Kollisionsdomänen (1 pro Vollduplex-Port) und genau 1 gemeinsame Broadcastdomäne (sofern keine VLANs eingerichtet sind). (2 Pkt.)')

add_q('ap1_lf3_012', 'AP1', 'LF 3', 'CSMA/CD vs CSMA/CA',
      'Vergleichen Sie das Medienzugriffsverfahren im klassischen kabelgebundenen Halbduplex-Ethernet mit dem im WLAN.',
      'Erläutern Sie den Unterschied zwischen Collision Detection (CD) und Collision Avoidance (CA).',
      6,
      'CSMA/CD (Ethernet): Stationen senden und hören gleichzeitig die Leitung ab. Erkennt eine Station eine Kollision (Spannungsanstieg), sendet sie ein JAM-Signal, bricht ab und wartet eine zufällige Backoff-Zeit. (3 Pkt.)\n'
      'CSMA/CA (WLAN): Da Funkgeräte beim Senden ihr eigenes Empfangssignal überlagern, können Kollisionen nicht zuverlässig erkannt werden. Stattdessen wird der Kanal abgehört (Carrier Sense) und vor dem Senden eine zufällige Wartezeit (Contention Window) eingelegt, ggf. ergänzt durch RTS/CTS-Handshakes. (3 Pkt.)')

add_q('ap1_lf3_013', 'AP1', 'LF 3', 'Netzwerk-Übertragungszeit Berechnung',
      'Ein Backup-Image von 450 GiB soll über eine 1-Gbit/s-Ethernet-Leitung auf ein NAS übertragen werden. Der Protokoll-Overhead (TCP/IP/Ethernet) beträgt 8 % und die durchschnittliche Netto-Leitungsauslastung liegt bei 85 %.',
      'Berechnen Sie die Übertragungsdauer in Stunden und Minuten. (1 GiB = 1024^3 Byte; 1 Gbit/s = 10^9 Bit/s).',
      8,
      'Dateigröße in Bit: 450 * 1024 * 1024 * 1024 * 8 Bit = 3.865.470.566.400 Bit. (2 Pkt.)\n'
      'Nutzdatenrate der Leitung: 1.000.000.000 Bit/s * 0,85 * (1 - 0,08) = 782.000.000 Bit/s = 782 Mbit/s. (2 Pkt.)\n'
      'Dauer in Sekunden: 3.865.470.566.400 / 782.000.000 s = 4943,05 Sekunden. (2 Pkt.)\n'
      'Umrechnung: 4943,05 / 3600 = 1,373 h -> 1 Stunde und 22 Minuten (82 Minuten). (2 Pkt.)',
      qtype='calc')

add_q('ap1_lf3_014', 'AP1', 'LF 3', 'PoE Power over Ethernet Standards',
      'Für neue IP-Telefone und Überwachungskameras wird PoE nach IEEE 802.3at (PoE+) auf den Access-Switches benötigt.',
      'Nennen Sie die maximale Leistungsabgabe pro Port nach IEEE 802.3af (PoE) und IEEE 802.3at (PoE+) und erklären Sie den Unterschied zwischen Endspan und Midspan.',
      6,
      'PoE (802.3af): Max. 15,4 Watt am Switch-Port (min. 12,95 W am Endgerät). (2 Pkt.)\n'
      'PoE+ (802.3at): Max. 30,0 Watt am Switch-Port (min. 25,5 W am Endgerät). (2 Pkt.)\n'
      'Endspan: Die Stromversorgung erfolgt direkt über den Ethernet-Switch selbst. (1 Pkt.)\n'
      'Midspan: Ein separater PoE-Injektor oder Patchpanel wird zwischen Non-PoE-Switch und Endgerät geschaltet. (1 Pkt.)')

add_q('ap1_lf3_015', 'AP1', 'LF 3', 'ARP-Protokoll & ARP-Cache',
      'Host A (192.168.1.10) möchte ein TCP-Paket an Host B (192.168.1.50) im selben Subnetz senden.',
      'Beschreiben Sie, wie Host A mithilfe des Address Resolution Protocols (ARP) die Ziel-Hardwareadresse ermittelt und was geschieht, wenn der Eintrag im Cache veraltet.',
      6,
      '1. ARP-Request: Host A prüft seinen ARP-Cache. Ist kein Eintrag vorhanden, sendet er einen ARP-Request als Ethernet-Broadcast (FF:FF:FF:FF:FF:FF) mit dem Inhalt: \"Wer hat 192.168.1.50? Bitte antworte an 192.168.1.10!\". (2 Pkt.)\n'
      '2. ARP-Reply: Host B erkennt seine IP und antwortet per Unicast direkt an die MAC von Host A mit seiner MAC-Adresse. (2 Pkt.)\n'
      '3. Cache & Aging: Host A trägt die MAC in seinen ARP-Cache ein. Nach Ablauf des Aging-Timers (typisch 5-20 Min.) wird der Eintrag gelöscht und muss bei erneutem Bedarf neu angefragt werden. (2 Pkt.)')

# --- LF 4: Schutzbedarfsanalyse, Cyber-Sicherheit & DSGVO ---
add_q('ap1_lf4_001', 'AP1', 'LF 4', 'CIA-Triade Grundwerte der Informationssicherheit',
      'Ein IT-Sicherheitskonzept nach BSI IT-Grundschutz basiert auf den drei klassischen Sicherheitszielen.',
      'Definieren Sie die Schutzziele Vertraulichkeit, Integrität und Verfügbarkeit und nennen Sie zu jedem Ziel eine konkrete technische oder organisatorische Maßnahme.',
      9,
      '1. Vertraulichkeit (Confidentiality): Informationen sind nur autorisierten Personen zugänglich und vor unbefugtem Zugriff geschützt. Maßnahme: Festplattenverschlüsselung (BitLocker), TLS-Transportverschlüsselung, Rollen- und Rechtekonzept. (3 Pkt.)\n'
      '2. Integrität (Integrity): Daten sind vor unbefugter oder unbeabsichtigter Veränderung/Manipulation geschützt und korrekt. Maßnahme: Kryptografische Hashwerte (SHA-256), digitale Signaturen, Schreibschutz. (3 Pkt.)\n'
      '3. Verfügbarkeit (Availability): Autorisierte Benutzer können jederzeit im vereinbarten Zeitrahmen auf Systeme und Daten zugreifen. Maßnahme: Redundante Netzteile, USV, RAID-Systeme, Backup-Konzepte. (3 Pkt.)')

add_q('ap1_lf4_002', 'AP1', 'LF 4', 'Backup-Methoden Vergleich',
      'In einem Unternehmen fallen täglich 60 GB veränderte Daten an. Für das Backup-Konzept werden die Verfahren Vollsicherung, differenzielle und inkrementelle Sicherung abgewogen.',
      'Vergleichen Sie differenzielle und inkrementelle Backups hinsichtlich Speichervolumen und Aufwand/Schritte bei einer vollständigen Systemwiederherstellung.',
      8,
      'Differenzielle Sicherung: Sichert alle Daten, die sich seit der LETZTEN VOLLSICHERUNG geändert haben. Speicherbedarf wächst täglich bis zur nächsten Vollsicherung. Wiederherstellung: Sehr schnell, es werden nur 2 Sicherungssätze benötigt (letzte Vollsicherung + gewünschter differenzieller Stand). (4 Pkt.)\n'
      'Inkrementelle Sicherung: Sichert nur die Daten, die sich seit der UNMITTELBAR VORANGEGANGENEN (Voll- oder Inkrementellen) Sicherung geändert haben. Geringster Speicherbedarf. Wiederherstellung: Aufwändig und zeitintensiv, da die Vollsicherung sowie ausnahmslos ALLE darauffolgenden inkrementellen Stände lückenlos in Reihe eingespielt werden müssen. (4 Pkt.)')

add_q('ap1_lf4_003', 'AP1', 'LF 4', '3-2-1-Backup-Regel und Air-Gap',
      'Die Geschäftsleitung fordert die konsequente Umsetzung der 3-2-1-Backup-Strategie zum Schutz vor Ransomware-Angriffen.',
      'Erläutern Sie die drei Vorgaben der 3-2-1-Regel und beschreiben Sie das Konzept eines Air-Gaps.',
      8,
      '3: Es müssen mindestens 3 Datenkopien existieren (1 Produktivdaten + 2 Backups). (2 Pkt.)\n'
      '2: Die Sicherungen müssen auf mindestens 2 unterschiedlichen Medientechnologien gespeichert werden (z. B. lokales Festplatten-NAS und LTO-Magnetband). (2 Pkt.)\n'
      '1: Mindestens 1 Sicherungskopie muss an einem separaten, externen Standort (Offsite / Cloud / Brandschutzabschnitt) aufbewahrt werden. (2 Pkt.)\n'
      'Air-Gap: Eine physische oder logische vollständige Trennung des Backup-Mediums vom Produktivnetzwerk (z. B. entnommene LTO-Tape-Kassetten oder Offline-Storage), sodass Schadsoftware über das Netzwerk keinen Schreib- oder Löschzugriff auf das Backup erlangen kann. (2 Pkt.)')

add_q('ap1_lf4_004', 'AP1', 'LF 4', 'SLA-Kennzahlen RTO und RPO',
      'Im Katastrophenfall-Plan (Disaster Recovery Plan) einer Bank sind vereinbart: RTO = 2 Stunden und RPO = 15 Minuten.',
      'Definieren Sie RTO (Recovery Time Objective) und RPO (Recovery Point Objective) und interpretieren Sie die beiden Kennzahlen anhand des Szenarios.',
      6,
      'RTO (Recovery Time Objective): Die maximal tolerierbare Zeitdauer vom Auftreten des Ausfalls bis zur vollständigen Wiederherstellung der Betriebsbereitschaft. Im Szenario: Nach spätestens 2 Stunden muss das System wieder produktiv laufen. (3 Pkt.)\n'
      'RPO (Recovery Point Objective): Der maximal tolerierbare Zeitraum, für den Daten im Katastrophenfall verloren gehen dürfen (gemessen zurück vom Ausfallzeitpunkt). Im Szenario: Es dürfen maximal Transaktionsdaten der letzten 15 Minuten verloren gehen (erfordert z. B. synchrone Replikation). (3 Pkt.)')

add_q('ap1_lf4_005', 'AP1', 'LF 4', 'DSGVO Art. 32 Technisch-organisatorische Maßnahmen (TOMs)',
      'Ein Rechenzentrum verarbeitet personenbezogene Kundendaten und muss nach Art. 32 DSGVO angemessene technische und organisatorische Maßnahmen nachweisen.',
      'Nennen Sie sechs der acht klassischen Kontrollbereiche (TOMs) und geben Sie jeweils ein konkretes Praxisbeispiel an.',
      6,
      '1. Zutrittskontrolle: Schutz vor unbefugtem räumlichen Betreten (z. B. Chipkarten-Leser, Biometrie, Alarmanlage). (1 Pkt.)\n'
      '2. Zugangskontrolle: Schutz vor unbefugter Systemnutzung (z. B. sichere Passwörter, 2FA, Kontosperrung). (1 Pkt.)\n'
      '3. Zugriffskontrolle: Schutz vor unbefugtem Lesen/Ändern von Daten (z. B. Rollen- und Rechtekonzept nach Least Privilege). (1 Pkt.)\n'
      '4. Weitergabekontrolle: Schutz bei Übertragung und Transport (z. B. VPN, TLS-Verschlüsselung, Transportprotokolle). (1 Pkt.)\n'
      '5. Eingabekontrolle: Nachvollziehbarkeit, wer wann welche Daten geändert hat (z. B. manipulationssicheres Logging/Audit-Trail). (1 Pkt.)\n'
      '6. Verfügbarkeitskontrolle: Schutz vor Zerstörung und Verlust (z. B. USV, RAID, Brandschutz, tägliches Backup). (1 Pkt.)')

add_q('ap1_lf4_006', 'AP1', 'LF 4', 'DSGVO Betroffenenrechte',
      'Ein ehemaliger Kunde verlangt die vollständige Löschung seiner gespeicherten Daten.',
      'Nennen Sie den maßgeblichen Artikel der DSGVO (Recht auf Löschen / Recht auf Vergessenwerden) und beschreiben Sie zwei gesetzliche Gründe, die einer sofortigen Löschung entgegenstehen.',
      6,
      'Recht auf Löschung: Art. 17 DSGVO. (2 Pkt.)\n'
      'Ausnahmen/Aufbewahrungspflichten:\n'
      '1. Handels- und steuerrechtliche Aufbewahrungsfristen nach § 257 HGB und § 147 AO (Rechnungen und Buchungsbelege müssen 10 Jahre archiviert werden). (2 Pkt.)\n'
      '2. Geltendmachung, Ausübung oder Verteidigung von Rechtsansprüchen im Rahmen gesetzlicher Verjährungsfristen (z. B. § 195 BGB). (2 Pkt.)')

add_q('ap1_lf4_007', 'AP1', 'LF 4', 'BSI IT-Grundschutz Vorgehensweise',
      'Ein IT-Sicherheitsbeauftragter erstellt ein Sicherheitskonzept nach BSI-Standard 200-2.',
      'Bringen Sie die folgenden Schritte in die korrekte chronologische Reihenfolge und erläutern Sie die Schutzbedarfsfeststellung: Strukturanalyse, Schutzbedarfsfeststellung, Modellierung, IT-Grundschutz-Check, Risikoanalyse.',
      8,
      'Reihenfolge:\n'
      '1. Strukturanalyse (Erfassung aller IT-Systeme, Netze, Räume, Anwendungen und Daten). (1 Pkt.)\n'
      '2. Schutzbedarfsfeststellung. (1 Pkt.)\n'
      '3. Modellierung (Zuordnung der Bausteine des IT-Grundschutz-Kompendiums). (1 Pkt.)\n'
      '4. IT-Grundschutz-Check (Soll-Ist-Vergleich der Basisanforderungen). (1 Pkt.)\n'
      '5. Risikoanalyse (für Bereiche mit hohem Schutzbedarf oder nicht abgedeckten Gefährdungen). (1 Pkt.)\n'
      'Schutzbedarfsfeststellung: Ermittelt für jede Anwendung und jedes System die Schadensauswirkungen bei Verlust von Vertraulichkeit, Integrität und Verfügbarkeit in den Kategorien \"Normal\", \"Hoch\" oder \"Sehr hoch\" unter Anwendung des Maximumprinzips. (3 Pkt.)')

add_q('ap1_lf4_008', 'AP1', 'LF 4', 'Zwei-Faktor-Authentifizierung (2FA / MFA)',
      'Zur Absicherung von VPN-Zugängen wird eine Zwei-Faktor-Authentifizierung (2FA) vorgeschrieben.',
      'Nennen Sie die drei klassischen Authentifizierungsfaktoren mit jeweils einem Beispiel und erläutern Sie das Funktionsprinzip von TOTP (Time-based One-Time Password).',
      8,
      'Drei Faktoren:\n'
      '1. Wissen (etwas, das man weiß): z. B. Passwort, PIN. (2 Pkt.)\n'
      '2. Besitz (etwas, das man hat): z. B. Smartphone, Hardware-Token (YubiKey), Smartcard. (2 Pkt.)\n'
      '3. Inhärenz / Sein (etwas, das man ist): z. B. Fingerabdruck, Gesichtsscan, Iris. (2 Pkt.)\n'
      'TOTP-Prinzip: Server und Client-App teilen ein geheimes Shared Secret. Aus diesem Secret und dem aktuellen Unix-Zeitstempel (in 30-Sekunden-Schritten) berechnet ein kryptografischer HMAC-Algorithmus (HMAC-SHA1) einen 6-stelligen Code, der nur für dieses 30s-Zeitfenster gültig ist. (2 Pkt.)')

add_q('ap1_lf4_009', 'AP1', 'LF 4', 'Ransomware Incident Response Maßnahmen',
      'Ein Mitarbeiter bemerkt am Montagmorgen, dass auf seinem PC Dateien die Endung \".locked\" erhalten haben und eine Textdatei mit einer Lösegeldforderung auf dem Desktop liegt.',
      'Nennen Sie vier Sofortmaßnahmen, die der IT-Support unverzüglich ergreifen muss, und begründen Sie, warum der Rechner nicht einfach ausgeschaltet werden darf.',
      8,
      'Vier Sofortmaßnahmen:\n'
      '1. Netzwerkverbindung sofort physisch trennen (LAN-Kabel ziehen, WLAN deaktivieren), um Lateral Movement im Firmennetz zu stoppen. (2 Pkt.)\n'
      '2. Incident-Response-Team und IT-Sicherheitsbeauftragten alarmieren. (1 Pkt.)\n'
      '3. Firewall-Logs und Netflow-Daten auf externe C2-Server-Kommunikation prüfen und betroffene Segmente isolieren. (1 Pkt.)\n'
      '4. Meldepflichten nach Art. 33 DSGVO (72h-Meldung an die Datenschutzaufsichtsbehörde) prüfen. (1 Pkt.)\n'
      'Warum nicht hart ausschalten: Durch hartes Ausschalten (Stecker ziehen) gehen flüchtige Speicherinhalte im RAM verloren (z. B. unverschlüsselte Keys, C2-Verbindungen, Injektionspfade), die für die digitale Forensik und Speicheranalyse essenziell sind (Einfrieren/Ruhezustand bevorzugen). (3 Pkt.)')

add_q('ap1_lf4_010', 'AP1', 'LF 4', 'Phishing & Social Engineering Abwehrmaßnahmen',
      'Ein Mitarbeiter erhält eine scheinbar von der Geschäftsleitung stammende E-Mail mit der dringenden Aufforderung, eine Überweisung über 45.000 EUR auf ein ausländisches Konto freizugeben (CEO-Fraud).',
      'Definieren Sie Social Engineering und nennen Sie drei organisatorische Maßnahmen, um Angriffe dieser Art wirksam zu verhindern.',
      6,
      'Definition: Zwischenmenschliche Beeinflussung und Manipulation von Mitarbeitern unter Ausnutzung von Hilfsbereitschaft, Respekt vor Autorität oder Zeitdruck, um vertrauliche Informationen zu erlangen oder Handlungen auszulösen. (3 Pkt.)\n'
      'Maßnahmen:\n'
      '1. Vier-Augen-Prinzip bei Zahlungsfreigaben ab bestimmten Betragsgrenzen. (1 Pkt.)\n'
      '2. Regelmäßige Security-Awareness-Schulungen und simulierte Phishing-Kampagnen. (1 Pkt.)\n'
      '3. Verpflichtender Callback-Kanal (Rückversicherung über ein separates Kommunikationsmedium, z. B. Telefonat mit bekannter Festnetznummer). (1 Pkt.)')

add_q('ap1_lf4_011', 'AP1', 'LF 4', 'Passwortrichtlinien nach BSI',
      'Die bestehende Passwortrichtlinie verlangt ein monatliches Ändern von 8-stelligen Passwörtern.',
      'Erläutern Sie, warum moderne BSI-Empfehlungen das erzwungene regelmäßige Wechseln ablehnen und welche zwei Kriterien stattdessen für ein sicheres Passwort ausschlaggebend sind.',
      6,
      'Kritik am Wechselzwang: Erzwungene periodische Wechsel führen nachweislich dazu, dass Benutzer vorhersehbare Muster wählen (z. B. Sommer2024! -> Herbst2024!) oder Passwörter auf Post-its notieren, anstatt echte Entropie zu nutzen. (2 Pkt.)\n'
      'Moderne Kriterien:\n'
      '1. Passwortlänge: Mindestens 10 bis 12 Zeichen bei komplexen Passwörtern, bzw. Passphrasen mit 20+ Zeichen aus mehreren Wörtern. (2 Pkt.)\n'
      '2. Keine Nutzung bekannter Wörterbuchwörter oder persönlicher Daten; Passwort nur wechseln, wenn ein konkreter Verdacht auf Kompromittierung besteht. (2 Pkt.)')

add_q('ap1_lf4_012', 'AP1', 'LF 4', 'Symmetrische vs Asymmetrische Verschlüsselung',
      'Zur Absicherung vertraulicher Datenübertragungen werden kryptografische Algorithmen eingesetzt.',
      'Vergleichen Sie symmetrische und asymmetrische Verschlüsselungsverfahren hinsichtlich Schlüsselverwaltung, Rechenaufwand und typischer Einsatzszenarien und nennen Sie jeweils ein bekanntes Algorithmenbeispiel.',
      8,
      'Symmetrische Verschlüsselung: Verwendet denselben gemeinsamen geheimen Schlüssel (Shared Secret) zum Ver- und Entschlüsseln. Sehr schnell und recheneffizient. Problem: Sicherer Schlüsselaustausch. Beispiel: AES (Advanced Encryption Standard). (4 Pkt.)\n'
      'Asymmetrische Verschlüsselung: Verwendet ein mathematisches Schlüsselpaar aus öffentlichem Schlüssel (Public Key) und privatem Schlüssel (Private Key). Rechenintensiv und langsamer. Ideal für Schlüsselaustausch und Signaturen. Beispiel: RSA, ECC (Elliptic Curve Cryptography). (4 Pkt.)')

add_q('ap1_lf4_013', 'AP1', 'LF 4', 'Hybride Verschlüsselung TLS',
      'Der Zugriff auf die Intranet-Webseite des Unternehmens wird per HTTPS (TLS 1.3) abgesichert.',
      'Erläutern Sie das Verfahren der hybriden Verschlüsselung und begründen Sie, warum weder rein symmetrische noch rein asymmetrische Verschlüsselung allein verwendet wird.',
      6,
      'Verfahren: Der Verbindungsaufbau (Handshake) erfolgt asymmetrisch (z. B. via Diffie-Hellman-Schlüsselaustausch / ECDHE und RSA/ECC-Zertifikat), um die Identität des Servers zu prüfen und einen temporären symmetrischen Sitzungsschlüssel (Session Key) auszuhandeln. Die eigentlichen Nutzdaten werden anschließend hochperformant symmetrisch (z. B. AES-256-GCM) verschlüsselt. (4 Pkt.)\n'
      'Begründung: Kombiniert die Sicherheit des asymmetrischen Schlüsselaustauschs ohne vorheriges Geheimnis mit der enormen Rechengeschwindigkeit symmetrischer Chiffren für Massendaten. (2 Pkt.)')

add_q('ap1_lf4_014', 'AP1', 'LF 4', 'Digitale Signatur und Hashfunktionen',
      'Ein Softwareentwickler signiert ein Update-Paket digital, bevor es an Kunden ausgeliefert wird.',
      'Beschreiben Sie Schritt für Schritt, wie die digitale Signatur beim Ersteller erzeugt und beim Kunden auf Echtheit und Unverfälschtheit geprüft wird.',
      8,
      'Erzeugung beim Ersteller:\n'
      '1. Über die Update-Datei wird ein kryptografischer Hashwert (z. B. SHA-256) gebildet. (2 Pkt.)\n'
      '2. Dieser Hashwert wird mit dem privaten Schlüssel (Private Key) des Erstellers asymmetrisch verschlüsselt -> Das Ergebnis ist die digitale Signatur. (2 Pkt.)\n'
      'Prüfung beim Kunden:\n'
      '3. Der Kunde entschlüsselt die Signatur mit dem öffentlichen Schlüssel (Public Key) des Erstellers und erhält den Original-Hash. (2 Pkt.)\n'
      '4. Der Kunde berechnet unabhängig den Hashwert über die heruntergeladene Datei. Stimmen beide Hashwerte exakt überein, ist die Software integer (unverändert) und authentisch (vom echten Ersteller). (2 Pkt.)')

# --- LF 5: Software zur Datenverwaltung anpassen (Trace-Tabellen, UML, Pseudocode) ---
add_q('ap1_lf5_001', 'AP1', 'LF 5', 'UML-Aktivitätsdiagramm & Pseudocode Schleifenlogik',
      'Für einen automatisierten Backup-Prozess soll die Kontrolllogik modelliert werden: Es wird geprüft, ob ausreichend Speicherplatz frei ist. Wenn ja, werden Dateien kopiert und eine Erfolgsmeldung gesendet. Wenn nein, wird ein Fehler protokolliert und der Vorgang abgebrochen.',
      'Vergleichen Sie die Modellierung von Kontrollstrukturen im UML-Aktivitätsdiagramm (Entscheidungsknoten / Raute, Guards) mit strukturiertem Pseudocode (WENN-DANN-SONST) und erläutern Sie die Funktion von Fork- und Join-Knoten (Synchronisationsbalken) bei parallelen Abläufen.',
      6,
      'Entscheidungsknoten & Guards: Im UML-Aktivitätsdiagramm stellt eine Raute eine Verzweigung dar; die ausgehenden Kanten tragen Bedingungen in eckigen Klammern [Guards], von denen exakt eine wahr sein muss (äquivalent zu WENN-DANN-SONST im Pseudocode). (3 Pkt.)\n'
      'Fork- und Join-Knoten: Ein Fork-Knoten (dicker Balken) teilt einen eingehenden Kontrollfluss in mehrere nebenläufig/parallel ausgeführte Pfade auf. Ein Join-Knoten synchronisiert diese parallelen Pfade wieder und lässt den Kontrollfluss erst weiterlaufen, wenn ALLE eingehenden Aktionen abgeschlossen sind. (3 Pkt.)')

add_q('ap1_lf5_002', 'AP1', 'LF 5', 'Trace-Tabelle Quersumme Algorithmus',
      'Gegeben ist folgender Pseudocode zur Berechnung der Quersumme einer Zahl:\n'
      'GANZZAHL zahl = 384\nGANZZAHL quersumme = 0\n'
      'SOLANGE zahl > 0 WIEDERHOLE:\n'
      '    quersumme = quersumme + (zahl MOD 10)\n'
      '    zahl = zahl DIV 10\n'
      'ENDE_SOLANGE',
      'Erstellen Sie eine vollständige Trace-Tabelle für alle Schleifendurchläufe mit den Spalten: Durchlauf, zahl, (zahl MOD 10), quersumme, (zahl DIV 10) und Bedingung (zahl > 0).',
      10,
      'Initial: zahl=384, quersumme=0\n'
      'Durchlauf 1: zahl=384 -> 384>0 (wahr) -> MOD 10 = 4 -> quersumme = 0 + 4 = 4 -> zahl = 384 DIV 10 = 38. (3 Pkt.)\n'
      'Durchlauf 2: zahl=38 -> 38>0 (wahr) -> MOD 10 = 8 -> quersumme = 4 + 8 = 12 -> zahl = 38 DIV 10 = 3. (3 Pkt.)\n'
      'Durchlauf 3: zahl=3 -> 3>0 (wahr) -> MOD 10 = 3 -> quersumme = 12 + 3 = 15 -> zahl = 3 DIV 10 = 0. (3 Pkt.)\n'
      'Ende: zahl=0 -> 0>0 (falsch) -> Schleifenabbruch. Endergebnis quersumme = 15. (1 Pkt.)',
      qtype='calc')

add_q('ap1_lf5_003', 'AP1', 'LF 5', 'Trace-Tabelle Lineare Suche',
      'Gegeben ist das Array werte = [14, 27, 42, 55, 68] und gesucht = 42.\n'
      'GANZZAHL pos = -1\n'
      'FÜR i VON 0 BIS 4 SCHRITT 1:\n'
      '    WENN werte[i] == gesucht DANN\n'
      '        pos = i\n'
      '        VERLASSE_SCHLEIFE\n'
      '    ENDE_WENN\n'
      'ENDE_FÜR',
      'Führen Sie die Trace-Tabelle bis zum Schleifenabbruch und geben Sie den Endwert von pos und die Anzahl der Vergleiche an.',
      8,
      'Schritt i=0: werte[0]=14 == 42 ist FALSCH (1. Vergleich). (2 Pkt.)\n'
      'Schritt i=1: werte[1]=27 == 42 ist FALSCH (2. Vergleich). (2 Pkt.)\n'
      'Schritt i=2: werte[2]=42 == 42 ist WAHR (3. Vergleich). pos wird auf 2 gesetzt. Schleife wird abgebrochen. (3 Pkt.)\n'
      'Endwert pos: 2; Gesamtanzahl Vergleiche: 3. (1 Pkt.)',
      qtype='calc')

add_q('ap1_lf5_004', 'AP1', 'LF 5', 'UML-Klassendiagramm Sichtbarkeiten und Syntax',
      'Für eine IT-Asset-Management-Software soll die Klasse \"Server\" modelliert werden. Attribute: hostname (String, öffentlich), ipAdresse (String, privat), id (Integer, geschützt). Methoden: booten() (kein Rückgabewert, öffentlich), ping(ip: String) (Rückgabewert boolean, öffentlich).',
      'Stellen Sie die Klasse als UML-Klassendiagramm nach DIN/OMG-Standard dar und beachten Sie die korrekten Sichtbarkeitssymbole.',
      8,
      'Dreigeteilter Kasten:\n'
      'Oberes Feld (Klassenname): Server (2 Pkt.)\n'
      'Mittleres Feld (Attribute mit Sichtbarkeiten):\n'
      '+ hostname : String\n'
      '- ipAdresse : String\n'
      '# id : Integer (3 Pkt.)\n'
      'Unteres Feld (Methoden):\n'
      '+ booten() : void\n'
      '+ ping(ip : String) : Boolean (3 Pkt.)')

add_q('ap1_lf5_005', 'AP1', 'LF 5', 'UML Assoziation Aggregation vs Komposition',
      'In einem Objektmodell stehen die Klassen \"Firma\", \"Abteilung\" und \"Mitarbeiter\" in Beziehung zueinander.',
      'Unterscheiden Sie Aggregation und Komposition anhand von grafischer Darstellung und Lebensdauer-Abhängigkeit und ordnen Sie die Beziehungen der Klassen begründet zu.',
      8,
      'Komposition (ausgefüllte Raute): Strikte existenzielle Abhängigkeit (Teil-Ganzes-Beziehung). Das Teil kann ohne das Ganze nicht existieren. Beispiel: Firma <*-- Abteilung (Wird die Firma aufgelöst, hören ihre Abteilungen auf zu existieren). (4 Pkt.)\n'
      'Aggregation (leere Raute): Lose Beziehung. Die Teile können auch unabhängig vom übergeordneten Ganzen fortbestehen. Beispiel: Abteilung o-- Mitarbeiter (Wird eine Abteilung aufgelöst, bleibt der Mitarbeiter weiterhin als Person/Arbeitnehmer bestehen). (4 Pkt.)')

add_q('ap1_lf5_006', 'AP1', 'LF 5', 'UML Sequenzdiagramm Lebenslinie und Nachrichten',
      'Ein Authentifizierungsprozess zwischen Client, Webserver und Datenbank soll visualisiert werden.',
      'Erläutern Sie die Elemente eines UML-Sequenzdiagramms (Lebenslinie, Aktivierungsbalken, synchrone Nachricht, asynchrone Nachricht, Antwortnachricht).',
      8,
      'Lebenslinie (Lifeline): Vertikale gestrichelte Linie, die das Vorhandensein eines Objekts über die Zeit darstellt. (2 Pkt.)\n'
      'Aktivierungsbalken (Execution Occurrence): Schmaler vertikaler Kasten auf der Lebenslinie, der anzeigt, dass das Objekt gerade aktiv eine Operation ausführt. (2 Pkt.)\n'
      'Synchrone Nachricht: Durchgezogene Linie mit ausgefüllter Pfeilspitze; der Aufrufer wartet blockierend auf die Antwort. (2 Pkt.)\n'
      'Antwortnachricht (Reply Message): Gestrichelte Linie mit offener Pfeilspitze zur Rückgabe des Ergebnisses. (2 Pkt.)')

add_q('ap1_lf5_007', 'AP1', 'LF 5', 'Datenbank Normalisierung 1NF bis 3NF',
      'Gegeben ist eine unnormalisierte Tabelle: bestellungen(bestell_nr, datum, kunden_name, kunden_ort, artikel_liste, artikel_preise).',
      'Definieren Sie die 1., 2. und 3. Normalform und überführen Sie das Schema schrittweise in die 3. Normalform.',
      12,
      '1. Normalform (1NF): Alle Attribute sind atomar (jede Zelle enthält nur einen elementaren Wert; keine Wiederholgruppen). Tabelle aufteilen in Bestelldaten und einzelne Bestellpositionen (artikel_liste/preise auflösen). (4 Pkt.)\n'
      '2. Normalform (2NF): Das Schema ist in 1NF und jedes Nichtschlüssel-Attribut ist vom gesamten Primärschlüssel voll funktional abhängig (keine Abhängigkeit von Teilen eines zusammengesetzten Schlüssels). Trennung von Bestellpositionen und Artikelstammdaten. (4 Pkt.)\n'
      '3. Normalform (3NF): Das Schema ist in 2NF und es existieren keine transitiven Abhängigkeiten zwischen Nichtschlüssel-Attributen (Nichtschlüssel bestimmen keine anderen Nichtschlüssel). Auslagerung von Ort über die PLZ (kunden_name -> kunden_plz -> kunden_ort auflösen). (4 Pkt.)')

add_q('ap1_lf5_008', 'AP1', 'LF 5', 'ER-Modellierung Kardinalitäten',
      'Modellieren Sie die Beziehung zwischen \"Projekt\" und \"Mitarbeiter\": Ein Projekt kann von mehreren Mitarbeitern bearbeitet werden; ein Mitarbeiter kann in mehreren Projekten mitarbeiten. Zu jeder Mitarbeit wird die Anzahl der investierten Arbeitsstunden erfasst.',
      'Geben Sie den Beziehungstyp (Kardinalität) an und erklären Sie, wie diese Beziehung in einem relationalen Datenbankschema aufgelöst wird.',
      8,
      'Kardinalität: n:m-Beziehung (Many-to-Many). (2 Pkt.)\n'
      'Auflösung im relationalen Schema: Eine n:m-Beziehung kann nicht direkt über Fremdschlüssel in den beiden Haupttabellen abgebildet werden. Es wird eine Zwischentabelle / Verknüpfungstabelle (z. B. projekt_mitarbeiter) benötigt. (3 Pkt.)\n'
      'Struktur der Zwischentabelle: Enthält als Fremdschlüssel projekt_id und mitarbeiter_id (bilden gemeinsam den zusammengesetzten Primärschlüssel) sowie das Beziehungsattribut arbeitsstunden. (3 Pkt.)')

add_q('ap1_lf5_009', 'AP1', 'LF 5', 'ER-Modellierung Chen vs Krähenfuß-Notation',
      'Zur Dokumentation eines Kundensystems werden Entity-Relationship-Modelle (ERM) eingesetzt.',
      'Vergleichen Sie die Chen-Notation mit der Krähenfuß-Notation (Martin-Notation) hinsichtlich der Darstellung von Entitäten, Attributen und Kardinalitäten (1:1, 1:n, n:m).',
      8,
      'Entitäten: Bei Chen als Rechteck dargestellt; bei Krähenfuß ebenfalls als Rechteck/Tabelle mit getrenntem Kopf für den Entitätsnamen. (2 Pkt.)\n'
      'Attribute: Bei Chen als Ellipsen, die mit der Entität verbunden sind (Primärschlüssel unterstrichen); bei Krähenfuß direkt als Zeilen innerhalb des Entitätsrechtecks aufgelistet (PK/FK gekennzeichnet). (3 Pkt.)\n'
      'Kardinalitäten: Bei Chen über Rauten als Beziehungselemente mit Beschriftung 1, n, m an den Kanten; bei Krähenfuß direkt an den Linienenden über Symbole (Strich = genau eins, Kreis = optional/null, Dreizack/Krähenfuß = viele). (3 Pkt.)')

add_q('ap1_lf5_010', 'AP1', 'LF 5', 'Relationales Datenmodell & Referenzielle Integrität',
      'In einer relationalen Datenbank werden Kundendaten und deren Bestellungen verwaltet.',
      'Definieren Sie die Begriffe Primärschlüssel, Fremdschlüssel und Referenzielle Integrität und erklären Sie, welche Gefahr droht, wenn die referenzielle Integrität verletzt wird.',
      8,
      'Primärschlüssel (Primary Key): Ein Attribut oder eine minimale Attributkombination, die jeden Datensatz einer Tabelle eindeutig und unveränderlich identifiziert (Darf weder Duplikate noch NULL enthalten). (2 Pkt.)\n'
      'Fremdschlüssel (Foreign Key): Ein Attribut in einer Relation, das auf den Primärschlüssel einer anderen (oder derselben) Relation verweist und logische Beziehungen herstellt. (2 Pkt.)\n'
      'Referenzielle Integrität: Die Integritätsbedingung besagt, dass jeder Fremdschlüsselwert entweder NULL sein muss oder tatsächlich als gültiger Primärschlüsselwert in der referenzierten Elterntabelle existieren muss. (2 Pkt.)\n'
      'Gefahr bei Verletzung: Entstehung von \"verwaisten Datensätzen\" (Orphan Records), z. B. Bestellungen ohne zugehörigen Kunden, was zu inkonsistenten Datenbeständen und Abstürzen in Auswertungen führt. (2 Pkt.)')

add_q('ap1_lf5_011', 'AP1', 'LF 5', 'Trace-Tabelle Array-Filterung und Schwellenwert',
      'Gegeben ist ein Array messwerte = [18, 24, 12, 31, 20] und folgender Pseudocode:\n'
      'GANZZAHL anzahl = 0\n'
      'FÜR i VON 0 BIS 4 SCHRITT 1:\n'
      '    WENN messwerte[i] >= 20 DANN\n'
      '        anzahl = anzahl + 1\n'
      '    ENDE_WENN\n'
      'ENDE_FÜR',
      'Führen Sie eine vollständige Trace-Tabelle mit den Spalten: i, messwerte[i], Bedingung (>= 20), anzahl für alle 5 Schleifendurchläufe und geben Sie den Endwert von anzahl an.',
      8,
      'Initial: anzahl = 0\n'
      'Schritt 1: i=0 -> messwerte[0]=18 -> 18>=20 (falsch) -> anzahl bleibt 0. (1,5 Pkt.)\n'
      'Schritt 2: i=1 -> messwerte[1]=24 -> 24>=20 (wahr) -> anzahl = 0 + 1 = 1. (1,5 Pkt.)\n'
      'Schritt 3: i=2 -> messwerte[2]=12 -> 12>=20 (falsch) -> anzahl bleibt 1. (1,5 Pkt.)\n'
      'Schritt 4: i=3 -> messwerte[3]=31 -> 31>=20 (wahr) -> anzahl = 1 + 1 = 2. (1,5 Pkt.)\n'
      'Schritt 5: i=4 -> messwerte[4]=20 -> 20>=20 (wahr) -> anzahl = 2 + 1 = 3. (1,5 Pkt.)\n'
      'Ende: Schleife beendet, Endwert anzahl = 3. (0,5 Pkt.)',
      qtype='calc')

add_q('ap1_lf5_012', 'AP1', 'LF 5', 'Transaktionskonzept & ACID-Eigenschaften',
      'Bei der Erfassung eines Kundenauftrags müssen Kundendaten, Bestellkopf und fünf Bestellpositionen zeitgleich in der Datenbank gespeichert werden.',
      'Nennen und erläutern Sie die vier ACID-Eigenschaften und beschreiben Sie, warum ein automatisches Rollback erforderlich ist, wenn das Speichern der vierten Bestellposition fehlschlägt.',
      8,
      'Atomarität (Atomicity): Alles-oder-Nichts-Prinzip. Eine Transaktion wird entweder vollständig oder gar nicht in der Datenbank festgeschrieben. (2 Pkt.)\n'
      'Konsistenz (Consistency): Vor Beginn und nach Abschluss einer Transaktion befindet sich die Datenbank in einem konsistenten, widerspruchsfreien Zustand. (2 Pkt.)\n'
      'Isolation: Parallele Transaktionen dürfen sich nicht gegenseitig beeinflussen, als liefen sie isoliert nacheinander ab. (1 Pkt.)\n'
      'Dauerhaftigkeit (Durability): Nach erfolgreichem Transaktionsabschluss (Commit) sind die Daten dauerhaft und vor Systemabstürzen geschützt gespeichert. (1 Pkt.)\n'
      'Bedarf für Rollback: Schlägt die vierte Position fehl, verhindert das Rollback eine unvollständige Bestellung (Kopf ohne alle Positionen), indem alle bereits geschriebenen Teilschritte rückgängig gemacht werden. (2 Pkt.)')

# --- LF 6: Cyber-Physische Systeme & IoT ---
add_q('ap1_lf6_001', 'AP1', 'LF 6', 'Sensoren und Aktoren im CPS',
      'In einem intelligenten Serverraum überwachen Sensoren die Umgebungstemperatur und steuern bei Bedarf automatisch Lüftungsklappen.',
      'Definieren Sie die Begriffe Sensor und Aktor in einem Cyber-Physischen System (CPS) und nennen Sie je zwei typische Komponenten in einem Rechenzentrum.',
      6,
      'Sensor: Technisches Bauteil, das physikalische oder chemische Größen (z. B. Temperatur, Helligkeit, Druck) erfasst und in elektrische bzw. digitale Signale umwandelt. Beispiele: Temperaturfühler (PT100/NTC), Rauchmelder, Feuchtigkeitssensor. (3 Pkt.)\n'
      'Aktor (Aktorik): Bauteil, das elektrische Steuerbefehle in mechanische Bewegung, Schaltvorgänge oder andere physikalische Wirkungen umsetzt. Beispiele: Stellmotor für Lüftungsklappen, Relais zum Einschalten von Kühlaggregaten, Magnet-Türschloss. (3 Pkt.)')

add_q('ap1_lf6_002', 'AP1', 'LF 6', 'MQTT-Protokoll Publish-Subscribe',
      'Zur Übertragung von Messwerten hunderter IoT-Sensoren an einen Server wird MQTT anstelle von HTTP REST gewählt.',
      'Beschreiben Sie die Funktionsweise des Publish-Subscribe-Musters bei MQTT unter Nennung der Rollen Broker, Publisher und Subscriber und erläutern Sie einen Vorteil gegenüber HTTP.',
      8,
      'Funktionsweise: Publisher (z. B. ein Temperatursensor) sendet Nachrichten zu einem bestimmten Thema (Topic, z. B. \"serverraum/rack1/temp\") an den zentralen Vermittler (MQTT-Broker). Subscriber (z. B. ein Dashboard oder Alarmdienst) abonnieren dieses Topic beim Broker. Der Broker leitet jede neue Nachricht automatisch an alle aktiven Abonnenten weiter. (5 Pkt.)\n'
      'Vorteil gegenüber HTTP: Extrem geringer Protokoll-Overhead (Header ab 2 Byte), Push-Prinzip statt ständigem Polling, ideal für bandbreitenarme Verbindungen und stromsparende Mikrocontroller. (3 Pkt.)')

add_q('ap1_lf6_003', 'AP1', 'LF 6', 'MQTT Quality of Service (QoS Level)',
      'In einem IoT-Überwachungssystem müssen verschiedene Meldungen übertragen werden: Regelmäßige Temperaturwerte alle 5 Sekunden und kritische Rauchmelder-Alarme.',
      'Erläutern Sie die drei MQTT QoS-Stufen (QoS 0, QoS 1, QoS 2) und ordnen Sie die beiden Meldungstypen begründet zu.',
      8,
      'QoS 0 (At most once): Nachricht wird maximal einmal ohne Empfangsbestätigung versendet (\"Fire and forget\"). Verlust möglich. (2 Pkt.)\n'
      'QoS 1 (At least once): Nachricht wird garantiert mindestens einmal zugestellt (Bestätigung via PUBACK), Duplikate sind möglich. (2 Pkt.)\n'
      'QoS 2 (Exactly once): Nachricht wird garantiert genau einmal ohne Duplikate über einen 4-Wege-Handshake zugestellt. Höchster Overhead. (2 Pkt.)\n'
      'Zuordnung: Regelmäßige Temperaturwerte -> QoS 0 (einzelner Verlust unkritisch); Rauchmelder-Alarm -> QoS 1 oder 2 (darf keinesfalls verloren gehen). (2 Pkt.)')

add_q('ap1_lf6_004', 'AP1', 'LF 6', 'Analog-Digital-Wandlung & Abtasttheorem',
      'Ein analoger Drucksensor liefert eine Spannung zwischen 0 und 10 Volt. Ein Mikrocontroller liest das Signal mit einem 10-Bit-A/D-Wandler ein.',
      'Berechnen Sie die kleinste auflösbare Spannungsstufe (Auflösung) des Wandlers und formulieren Sie das Nyquist-Shannon-Abtasttheorem für periodische Signale.',
      6,
      '10-Bit Auflösung: 2^10 = 1024 diskrete Stufen. (2 Pkt.)\n'
      'Spannungsschritt: 10 V / 1024 = 0,009765 V = ca. 9,77 mV. (2 Pkt.)\n'
      'Nyquist-Shannon-Abtasttheorem: Um ein bandbegrenztes analoges Signal ohne Informationsverlust (Aliasing) digital rekonstruieren zu können, muss die Abtastfrequenz (Sampling Rate) mehr als doppelt so hoch sein wie die höchste im Signal vorkommende Grenzfrequenz (f_abtast > 2 * f_max). (2 Pkt.)',
      qtype='calc')

# --- LF 7: Cyber-Physische Systeme instand halten ---
add_q('ap1_lf7_001', 'AP1', 'LF 7', 'ESD-Schutzmaßnahmen DIN EN 61340-5-1',
      'Vor dem Austausch eines Mainboards und RAM-Moduls in einem Server müssen Maßnahmen gegen elektrostatische Entladung (ESD) getroffen werden.',
      'Erklären Sie, wie ESD-Schäden an Halbleiterkomponenten entstehen und nennen Sie vier konkrete Schutzmaßnahmen an einem EPA-Arbeitsplatz (Electrostatic Protected Area).',
      8,
      'Entstehung: Durch Reibungselektrizität (Triboelektrischer Effekt) laden sich Personen oder Werkzeuge auf mehrere tausend Volt auf. Bei Annäherung an mikroelektronische Bauteile entlädt sich die Spannung schlagartig über kleinste Leiterbahnen und Gate-Oxide, was zu thermischer Zerstörung oder latenten Vorschäden führt. (3 Pkt.)\n'
      'Vier Schutzmaßnahmen:\n'
      '1. Antistatisches Erdungsarmband mit Sicherheitswiderstand (1 MOhm). (1 Pkt.)\n'
      '2. Leitfähige, geerdete ESD-Tischmatte und ableitfähiger Bodenbelag. (1 Pkt.)\n'
      '3. Verwendung von ESD-sicherem Werkzeug (leitfähige Griffe). (1 Pkt.)\n'
      '4. Transport von Komponenten ausschließlich in antistatischen Abschirmbeuteln (Shielding Bags). (1 Pkt.)')

add_q('ap1_lf7_002', 'AP1', 'LF 7', 'Fehlereingrenzung Top-Down vs Bottom-Up',
      'Ein Client-PC kann nach einem Umbau keine Webseiten mehr aufrufen.',
      'Vergleichen Sie die Fehlersuchstrategien Top-Down und Bottom-Up anhand des OSI-Referenzmodells und nennen Sie je einen Prüfschritt.',
      6,
      'Bottom-Up-Strategie: Fehlersuche beginnt auf Schicht 1 (Physical) und arbeitet sich nach oben vor. Prüfschritt: Link-LED an Netzwerkkarte und Switch prüfen, Patchkabel austauschen. Gut bei Neuinstallationen. (3 Pkt.)\n'
      'Top-Down-Strategie: Fehlersuche beginnt auf Schicht 7 (Application) und arbeitet sich nach unten vor. Prüfschritt: DNS-Auflösung und Browserkonfiguration (Proxy) testen. Gut, wenn der Fehler auf eine bestimmte Anwendung beschränkt scheint. (3 Pkt.)')

add_q('ap1_lf7_003', 'AP1', 'LF 7', 'S.M.A.R.T. Parameter von Festplatten',
      'Ein Server-Monitoring meldet eine Warnung für eine Enterprise-SATA-Festplatte.',
      'Erläutern Sie den Zweck von S.M.A.R.T. und nennen Sie zwei kritische Attribute, die auf einen unmittelbar bevorstehenden Hardwaredefekt hinweisen.',
      6,
      'Zweck: Self-Monitoring, Analysis and Reporting Technology überwacht interne mechanische und elektronische Betriebsparameter von HDDs/SSDs, um Ausfälle frühzeitig vorherzusagen. (2 Pkt.)\n'
      'Zwei kritische Attribute:\n'
      '1. Reallocated Sectors Count (Anzahl defekter Sektoren, die auf Reservebereiche umgemappt wurden). (2 Pkt.)\n'
      '2. Current Pending Sector Count (Anzahl instabiler Sektoren, die auf eine Neuzuweisung warten). (2 Pkt.)')

# --- LF 8: Datenflüsse optimieren & Schnittstellen anpassen ---
add_q('ap1_lf8_001', 'AP1', 'LF 8', 'REST-API und HTTP-Methoden',
      'Ein Ticketsystem stellt eine RESTful-API für Drittanwendungen bereit.',
      'Ordnen Sie die vier grundlegenden CRUD-Operationen (Create, Read, Update, Delete) den entsprechenden HTTP-Verben zu und erklären Sie, was Idempotenz bedeutet.',
      8,
      'CRUD Zuordnung:\n'
      'Create -> POST (oder PUT bei bekannter URI). (1 Pkt.)\n'
      'Read -> GET. (1 Pkt.)\n'
      'Update -> PUT (vollständiges Ersetzen) oder PATCH (partielles Ändern). (2 Pkt.)\n'
      'Delete -> DELETE. (1 Pkt.)\n'
      'Idempotenz: Eine Eigenschaft von HTTP-Methoden, bei der mehrfache identische Anfragen denselben Serverzustand zur Folge haben wie eine einzelne Anfrage. GET, PUT und DELETE sind idempotent; POST ist nicht idempotent (mehrfache Ausführung erzeugt mehrfache Ressourcen). (3 Pkt.)')

add_q('ap1_lf8_002', 'AP1', 'LF 8', 'HTTP-Statuscodes Zuordnung',
      'Bei der Entwicklung einer Schnittstelle treten verschiedene Fehlerfälle auf.',
      'Nennen Sie die Bedeutungen und typischen Anwendungsfälle der folgenden vier HTTP-Statuscodes: 200, 201, 401, 404 und 500.',
      10,
      '1. 200 OK: Anfrage erfolgreich ausgeführt und Nutzdaten geliefert. (2 Pkt.)\n'
      '2. 201 Created: Neue Ressource wurde erfolgreich angelegt (z. B. nach POST). (2 Pkt.)\n'
      '3. 401 Unauthorized: Zugriff verweigert, Authentifizierung fehlt oder ist ungültig. (2 Pkt.)\n'
      '4. 404 Not Found: Die angeforderte URI existiert auf dem Server nicht. (2 Pkt.)\n'
      '5. 500 Internal Server Error: Unerwarteter Serverfehler bei der Verarbeitung. (2 Pkt.)')

add_q('ap1_lf8_003', 'AP1', 'LF 8', 'Datenformate JSON vs XML',
      'Eine Schnittstelle soll Datenstrukturen austauschen.',
      'Vergleichen Sie JSON und XML hinsichtlich Syntax-Overhead, Lesbarkeit, Datentypen-Unterstützung und Schema-Validierung.',
      8,
      'Syntax-Overhead & Payload: JSON hat durch schlichte Key-Value-Klammerung { } deutlich weniger Overhead als XML mit seinen redundanten schließenden Tags <tag></tag>. (2 Pkt.)\n'
      'Datentypen: JSON unterstützt native Typen (String, Number, Boolean, Array, Null, Object). XML interpretiert alle Werte primär als Text. (2 Pkt.)\n'
      'Schema-Validierung: XML besitzt ausgereifte, standardisierte Validierungsmechanismen über XSD (XML Schema Definition) und DTD; bei JSON ist JSON Schema zwar verfügbar, aber historisch weniger formalisiert. (2 Pkt.)\n'
      'Parsing-Performance: JSON lässt sich nativ in Webtechnologien und modernen Programmiersprachen signifikant schneller und speicherschonender parsen. (2 Pkt.)')

add_q('ap1_lf8_004', 'AP1', 'LF 8', 'API-Authentifizierung JWT Bearer Token',
      'Der Zugriff auf eine REST-API wird über JSON Web Tokens (JWT) abgesichert.',
      'Beschreiben Sie den dreiteiligen Aufbau eines JWT (Header, Payload, Signature) und erläutern Sie, wie der Server die Integrität prüft, ohne das Token in einer Datenbank nachzuschlagen (Stateless).',
      8,
      'Dreiteiliger Aufbau (durch Punkte getrennt, Base64Url-codiert):\n'
      '1. Header: Enthält den Token-Typ (JWT) und den verwendeten Hashing-Algorithmus (z. B. HS256 oder RS256). (2 Pkt.)\n'
      '2. Payload (Claims): Enthält die Nutzdaten (z. B. user_id, rollen, ablaufdatum exp). (2 Pkt.)\n'
      '3. Signature: Wird erzeugt, indem der codierte Header und Payload mit einem geheimen Serverschlüssel gehasht/signiert werden. (2 Pkt.)\n'
      'Stateless-Prüfung: Der Server benötigt keine Session-Datenbank. Er berechnet aus empfangenem Header und Payload mit seinem geheimen Schlüssel die Signatur neu. Stimmt sie mit der im Token mitgelieferten Signatur überein und ist exp nicht abgelaufen, ist das Token garantiert echt und unverfälscht. (2 Pkt.)')


# --- AP1 NEU (ZPA 2. Auflage): BPMN 2.0, EPK, KI-Support, Belege, Netzplantechnik & IEC-Präfixe ---

add_q('ap1_bpmn_001', 'AP1', 'LF 1', 'BPMN 2.0 Gateways (Exklusiv XOR, Parallel AND, Inklusiv OR)',
      'In einem IT-Service-Helpdesk wird die Bearbeitung eingehender Störungsmeldungen als BPMN 2.0 Geschäftsprozess modelliert.',
      'Erläutern Sie die Funktionsweise und grafischen Symbole der drei BPMN-Gateways: Exklusives Gateway (XOR), Paralleles Gateway (AND) und Inklusives Gateway (OR) beim Verzweigen (Diverging) und Zusammenführen (Converging).',
      8,
      'Exklusives Gateway (XOR, Raute mit X oder leer): Genau ein einziger ausgehender Pfad wird gewählt, dessen Bedingung zutrifft. Beim Zusammenführen wartet es nicht, sondern leitet jedes eintreffende Token sofort weiter. (3 Pkt.)\n'
      'Paralleles Gateway (AND, Raute mit Pluszeichen +): Alle ausgehenden Pfade werden gleichzeitig/nebenläufig aktiviert (Fork). Beim Zusammenführen (Join) wartet das Gateway, bis auf ALLEN eingehenden Pfaden ein Token eingetroffen ist, bevor der Prozess fortgesetzt wird. (3 Pkt.)\n'
      'Inklusives Gateway (OR, Raute mit Kreis O): Ein oder mehrere Pfade werden gewählt, deren Bedingungen wahr sind. Beim Zusammenführen synchronisiert es alle tatsächlich aktiven eingehenden Pfade. (2 Pkt.)')

add_q('ap1_bpmn_002', 'AP1', 'LF 1', 'BPMN 2.0 Pools, Lanes und Flussregeln',
      'Zur Abbildung eines Bestell- und Freigabeprozesses für Neugeräte zwischen Kunde, IT-Einkauf und Buchhaltung wird ein BPMN-Diagramm erstellt.',
      'Unterscheiden Sie Pools und Swimlanes (Bahnen) und erläutern Sie die Regeln bezüglich Sequenzfluss (Sequence Flow) und Nachrichtenfluss (Message Flow).',
      6,
      'Pool: Repräsentiert eine eigenständige Organisationseinheit, ein externes Unternehmen oder einen eigenständigen Teilnehmer/Prozess (Black Box oder White Box). (2 Pkt.)\n'
      'Lane: Unterteilt einen Pool in interne Rollen, Abteilungen oder Systeme (z. B. IT-Einkauf, Buchhaltung). (1 Pkt.)\n'
      'Flussregeln: Ein Sequenzfluss (durchgezogener Pfeil) verbindet Aktivitäten innerhalb DENSELBEN Pools und darf niemals Pool-Grenzen überschreiten. Ein Nachrichtenfluss (gestrichelte Linie mit offenem Pfeil und Kreis am Start) stellt die asynchrone Kommunikation ZWISCHEN zwei unterschiedlichen Pools dar. (3 Pkt.)')

add_q('ap1_epk_001', 'AP1', 'LF 1', 'Ereignisgesteuerte Prozesskette (EPK) Modellierungsregeln',
      'Ein Onboarding-Prozess für neue Mitarbeiter wird als Ereignisgesteuerte Prozesskette (EPK) dokumentiert.',
      'Nennen Sie die drei Grundelemente einer EPK mit ihren geometrischen Symbolen und erläutern Sie zwei fundamentale Syntaxregeln für die Verknüpfung von Ereignissen und Funktionen.',
      8,
      'Grundelemente:\n'
      '1. Ereignis: Sechseck (Hexagon). Beschreibt einen eingetretenen Zustand (Auslöser/Ergebnis, z. B. \"Mitarbeitervertrag unterzeichnet\"). (2 Pkt.)\n'
      '2. Funktion: Rechteck mit abgerundeten Ecken. Beschreibt eine auszuführende Transformation/Aktivität im Infinitiv (z. B. \"Benutzerkonto im AD anlegen\"). (2 Pkt.)\n'
      '3. Logischer Konnektor: Kreis mit Symbol (UND, ODER, XOR) zur Verzweigung/Zusammenführung. (1 Pkt.)\n'
      'Zwei Syntaxregeln:\n'
      '- Alternierungsregel: Ereignisse und Funktionen müssen sich im Ablauf immer strikt abwechseln (niemals Ereignis direkt auf Ereignis oder Funktion direkt auf Funktion ohne Konnektor). (1,5 Pkt.)\n'
      '- Konnektorenregel: Ein Ereignis hat keine Entscheidungskraft; nach einem einzelnen Ereignis darf daher niemals ein ODER- oder XOR-Konnektor verzweigen (nur UND ist nach Einzelereignis zulässig). (1,5 Pkt.)')

add_q('ap1_ki_001', 'AP1', 'LF 1', 'Künstliche Intelligenz im First-Level-Support & Tickettriage',
      'Ein IT-Service-Desk plant den Einsatz eines KI-Systems (Large Language Model / NLP) zur automatisierten Entgegennahme und Priorisierung von Störungstickets.',
      'Nennen Sie drei konkrete Aufgaben, die das KI-System im First-Level-Support übernehmen kann, und erläutern Sie eine zentrale Herausforderung (Risiko) beim automatisierten Ticket-Dispatching.',
      6,
      'Drei Aufgaben:\n'
      '1. Automatische Klassifizierung & Triage: Analysieren des Freitextes und Zuweisen der richtigen Fehlerkategorie und Priorität (Prio 1-4). (1,5 Pkt.)\n'
      '2. Lösungsvorschläge & Self-Service: Automatischer Abgleich mit der Knowledge Base (FAQ) und Bereitstellung von Standard-Lösungsschritten für den Anwender (z. B. Kennwort-Reset). (1,5 Pkt.)\n'
      '3. Routing & Zuweisung: Gezielte Weiterleitung an das zuständige Fach-Supportteam (Second Level). (1 Pkt.)\n'
      'Herausforderung / Risiko: Fehlklassifikation (False Positives / Negatives) bei Sarkasmus, unpräziser Sprache oder kombinierten Problemen; ein kritischer Netzwerkausfall könnte fälschlich als Prio 4 eingestuft werden und SLA-Fristen verletzen. (2 Pkt.)')

add_q('ap1_ki_002', 'AP1', 'LF 4', 'KI-Software am Arbeitsplatz & Datenschutz (DSGVO)',
      'Mitarbeiter möchten öffentlich zugängliche Cloud-KI-Dienste (z. B. ChatGPT) zur Analyse von Server-Logdateien und Programmcode am Arbeitsplatz einsetzen.',
      'Erläutern Sie zwei datenschutzrechtliche Risiken nach DSGVO und formulieren Sie zwei verbindliche Unternehmensrichtlinien für den zulässigen KI-Einsatz.',
      6,
      'Zwei Risiken:\n'
      '1. Unzulässige Drittlandübermittlung & Auftragsverarbeitung: Logdateien enthalten oft personenbezogene Daten (IP-Adressen, Benutzernamen). Werden diese ohne Auftragsverarbeitungsvertrag (AVV nach Art. 28 DSGVO) an US-Cloudanbieter übertragen, liegt ein schwerer Datenschutzverstoß vor. (2 Pkt.)\n'
      '2. Verlust von Geschäftsgeheimnissen: Öffentliche KIs können eingegebene Prompts und vertraulichen Source Code zum Weitertrainieren zukünftiger Modelle verwenden. (1 Pkt.)\n'
      'Zwei Richtlinien:\n'
      '1. Striktes Verbot der Eingabe personenbezogener Daten (PII), Passwörter, API-Keys oder interner Geschäftsgeheimnisse in nicht freigegebene öffentliche KIs (Anonymisierungspflicht). (1,5 Pkt.)\n'
      '2. Vier-Augen-Prinzip & menschliche Letztverantwortung: Von KI generierter Quellcode oder Skripte müssen vor Produktivbetrieb immer zwingend durch IT-Fachpersonal auf Sicherheit und Korrektheit geprüft werden (kein unbesehenes Copy-Paste). (1,5 Pkt.)')

add_q('ap1_praefix_001', 'AP1', 'LF 2', 'Binärpräfixe (IEC) vs. Dezimalpräfixe (SI) bei Speichermedien',
      'Ein Festplattenhersteller deklariert eine NVMe-SSD mit einer Speicherkapazität von exakt 4 TB (Terabyte). Das Betriebssystem zeigt nach der Formatierung jedoch eine Kapazität in GiB (Gibibyte) bzw. TiB (Tebibyte) an.',
      'Berechnen Sie die Kapazität der Festplatte in Byte auf Basis der Herstellerangabe (SI-Präfix), rechnen Sie diese exakt in GiB und TiB (IEC-Präfixe) um und ermitteln Sie die prozentuale scheinbare Differenz.',
      8,
      '1. Herstellerangabe in Byte (Dezimal / SI, Basis 10):\n'
      '   4 TB = 4 * 10^12 Byte = 4.000.000.000.000 Byte. (2 Pkt.)\n'
      '2. Umrechnung in GiB und TiB (Binär / IEC, Basis 2):\n'
      '   1 GiB = 1.024^3 Byte = 1.073.741.824 Byte.\n'
      '   Kapazität in GiB = 4.000.000.000.000 / 1.073.741.824 ≈ 3.725,29 GiB. (2 Pkt.)\n'
      '   1 TiB = 1.024^4 Byte = 1.099.511.627.776 Byte.\n'
      '   Kapazität in TiB = 4.000.000.000.000 / 1.099.511.627.776 ≈ 3,638 TiB. (2 Pkt.)\n'
      '3. Prozentuale scheinbare Differenz:\n'
      '   (4,000 - 3,638) / 4,000 = 0,362 / 4,000 = 9,05 % (bzw. bezogen auf 4 TiB fehlen ca. 9,1 %). (2 Pkt.)',
      qtype='calc')

add_q('ap1_praefix_002', 'AP1', 'LF 3', 'Datenübertragungsrate (Mbit/s) vs. Dateigröße (GiB)',
      'Über eine Glasfaser-Internetanbindung mit einer nutzbaren Download-Bandbreite von 250 Mbit/s soll ein virtuelles Festplatten-Image mit einer Dateigröße von 45 GiB heruntergeladen werden. Durch TCP/IP- und Protokoll-Header entsteht ein Overhead von 8 %.',
      'Berechnen Sie die reine Übertragungszeit in Minuten und Sekunden.',
      8,
      '1. Umrechnung Dateigröße von GiB in Byte und Bit:\n'
      '   45 GiB = 45 * 1.024^3 Byte = 45 * 1.073.741.824 Byte = 48.318.382.080 Byte. (2 Pkt.)\n'
      '   In Bit: 48.318.382.080 * 8 = 386.547.056.640 Bit. (1 Pkt.)\n'
      '2. Berücksichtigung des Protokoll-Overheads (8 %):\n'
      '   Gesamte zu übertragende Bitmenge = 386.547.056.640 * 1,08 = 417.470.821.171 Bit. (2 Pkt.)\n'
      '3. Übertragungsrate in Bit/s (SI-Präfix bei Netzwerk!):\n'
      '   250 Mbit/s = 250 * 10^6 Bit/s = 250.000.000 Bit/s. (1 Pkt.)\n'
      '4. Download-Dauer:\n'
      '   Zeit = 417.470.821.171 / 250.000.000 ≈ 1.669,88 Sekunden. (1 Pkt.)\n'
      '   In Minuten: 1.669,88 / 60 ≈ 27 Minuten und 50 Sekunden (bzw. 27,83 Min.). (1 Pkt.)',
      qtype='calc')

add_q('ap1_beleg_001', 'AP1', 'LF 1', 'Kaufmännische Rechnung PrintTop GmbH (Rabatt, Skonto, MwSt.)',
      'Die Meier IT-Solutions bestellt bei der PrintTop GmbH 10 Netzwerkdrucker zu einem Listenpreis von je 650,00 EUR netto. Die PrintTop GmbH gewährt 8 % Mengenrabatt. Bei Zahlung innerhalb von 14 Tagen werden 2 % Skonto eingeräumt. Die Frachtkosten betragen pauschal 70,00 EUR netto. Es gilt der reguläre Mehrwertsteuersatz von 19 %.',
      'Erstellen Sie das vollständige kaufmännische Prüfungsschema nach ZPA-Belegstandard und berechnen Sie: 1. Gesamter Listenpreis, 2. Rabattbetrag, 3. Bareinkaufspreis vor Fracht, 4. Netto-Rechnungsbetrag, 5. Skontobetrag, 6. Überweisungsbetrag bei fristgerechter Zahlung.',
      10,
      '1. Listenpreis gesamt (netto): 10 * 650,00 EUR = 6.500,00 EUR. (1 Pkt.)\n'
      '2. - 8 % Liefererrabatt: 6.500,00 * 0,08 = 520,00 EUR. (1,5 Pkt.)\n'
      '3. = Zieleinkaufspreis: 6.500,00 - 520,00 = 5.980,00 EUR. (1,5 Pkt.)\n'
      '4. + Frachtkosten (netto): 5.980,00 + 70,00 = 6.050,00 EUR (Rechnungsbetrag Netto). (1,5 Pkt.)\n'
      '5. + 19 % Umsatzsteuer: 6.050,00 * 0,19 = 1.149,50 EUR -> Rechnungsbetrag Brutto: 7.199,50 EUR. (1,5 Pkt.)\n'
      '6. - 2 % Skonto (auf skontofähigen Betrag 5.980 EUR Warenwert bzw. Bruttowarenwert 7.116,20 EUR):\n'
      '   Skonto auf Bruttorechnung (7.199,50 EUR * 0,02) = 143,99 EUR (oder warenwertbezogen 119,60 EUR netto = 142,32 EUR brutto). (1,5 Pkt.)\n'
      '7. Überweisungsbetrag (Zahlbetrag): 7.199,50 EUR - 143,99 EUR = 7.055,51 EUR. (1,5 Pkt.)',
      qtype='calc')

add_q('ap1_beleg_002', 'AP1', 'LF 1', 'Lieferungsverzug und Verzugszinsen nach BGB (§ 288 BGB)',
      'Die Systemhaus Nord GmbH hat eine fällige Rechnung eines gewerblichen Kunden (B2B) über 12.000,00 EUR brutto. Das Zahlungsziel war der 15. März. Nach Eintritt des Verzugs zahlt der Kunde die Gesamtsumme erst nach 45 Tagen Verzug. Der Basiszinssatz der Deutschen Bundesbank beträgt zum Stichtag 3,62 %.',
      'Erläutern Sie die gesetzlichen Voraussetzungen für den Verzugseintritt bei Entgeltforderungen im B2B-Bereich (§ 286 BGB), berechnen Sie den gesetzlichen Verzugszinssatz nach § 288 Abs. 2 BGB und ermitteln Sie die geschuldeten Verzugszinsen sowie die gesetzliche Verzugspauschale (§ 288 Abs. 5 BGB).',
      8,
      '1. Verzugseintritt im B2B-Geschäft (§ 286 Abs. 3 BGB): Gerät spätestens 30 Tage nach Fälligkeit und Zugang einer Rechnung automatisch in Verzug, ohne dass es einer gesonderten Mahnung bedarf. (2 Pkt.)\n'
      '2. Gesetzlicher Verzugszinssatz (§ 288 Abs. 2 BGB für Rechtsgeschäfte ohne Verbraucherbeteiligung):\n'
      '   Basiszinssatz + 9 Prozentpunkte = 3,62 % + 9,00 % = 12,62 % p. a. (2 Pkt.)\n'
      '3. Berechnung der Verzugszinsen für 45 Tage (kaufmännische Zinsformel Z = (K * p * t) / (100 * 360)):\n'
      '   Zinsen = (12.000 EUR * 12,62 * 45) / 36.000 = 6.814.800 / 36.000 = 189,30 EUR. (2 Pkt.)\n'
      '4. Gesetzliche Mahn- und Verzugspauschale nach § 288 Abs. 5 BGB: Gesetzlicher Anspruch auf eine Pauschale von 40,00 EUR bei B2B-Zahlungsverzug. (2 Pkt.)',
      qtype='calc')

add_q('ap1_netzplan_001', 'AP1', 'LF 1', 'Netzplantechnik Vorwärts- und Rückwärtsrechnung',
      'Gegeben ist ein Projektausschnitt mit folgenden Vorgängen (Dauer D in Tagen):\n'
      '- Vorgang A: Server beschaffen (D=4, kein Vorgänger)\n'
      '- Vorgang B: Betriebssystem installieren (D=3, Vorgänger A)\n'
      '- Vorgang C: Verkabelung prüfen (D=2, kein Vorgänger)\n'
      '- Vorgang D: Datenbank einrichten (D=5, Vorgänger B und C)\n'
      'Projektstart ist an Tag 0.',
      'Berechnen Sie für alle Vorgänge (A, B, C, D) den Frühesten Anfangszeitpunkt (FAZ), den Frühesten Endzeitpunkt (FEZ), den Spätesten Anfangszeitpunkt (SAZ) und den Spätesten Endzeitpunkt (SEZ) und geben Sie die minimale Projektdauer an.',
      10,
      'Vorwärtsrechnung (FAZ + Dauer = FEZ):\n'
      '- A: FAZ = 0, FEZ = 0 + 4 = 4. (1,5 Pkt.)\n'
      '- B: Vorgänger A -> FAZ = 4, FEZ = 4 + 3 = 7. (1,5 Pkt.)\n'
      '- C: Kein Vorgänger -> FAZ = 0, FEZ = 0 + 2 = 2. (1,5 Pkt.)\n'
      '- D: Vorgänger B (FEZ 7) und C (FEZ 2) -> FAZ = MAX(7, 2) = 7, FEZ = 7 + 5 = 12. (1,5 Pkt.)\n'
      'Projektdauer: 12 Tage. (1 Pkt.)\n'
      'Rückwärtsrechnung (SEZ - Dauer = SAZ):\n'
      '- D: SEZ = 12, SAZ = 12 - 5 = 7. (1 Pkt.)\n'
      '- B: Nachfolger D -> SEZ = 7, SAZ = 7 - 3 = 4. (1 Pkt.)\n'
      '- C: Nachfolger D -> SEZ = 7, SAZ = 7 - 2 = 5. (1 Pkt.)\n'
      '- A: Nachfolger B -> SEZ = 4, SAZ = 4 - 4 = 0. (1 Pkt.)',
      qtype='calc')

add_q('ap1_netzplan_002', 'AP1', 'LF 1', 'Kritischer Pfad und Pufferzeiten (GP vs. FP)',
      'Bezugnehmend auf den Netzplan aus Vorgang A, B, C und D mit Projektdauer 12 Tage.',
      'Definieren Sie Gesamtpuffer (GP) und freien Puffer (FP) mit ihren mathematischen Formeln, berechnen Sie GP und FP für Vorgang C und identifizieren Sie den kritischen Pfad des Projekts.',
      8,
      'Definitionen & Formeln:\n'
      '- Gesamtpuffer (GP = SAZ - FAZ bzw. SEZ - FEZ): Die Zeitspanne, um die ein Vorgang maximal verschoben werden darf, ohne den gesamten Projektendtermin zu gefährden. (2 Pkt.)\n'
      '- Freier Puffer (FP = FAZ_Nachfolger - FEZ_aktuell): Die Zeitspanne, um die ein Vorgang maximal verschoben werden darf, ohne den frühesten Anfangszeitpunkt des direkten Nachfolgers zu beeinflussen. (2 Pkt.)\n'
      'Berechnung für Vorgang C (FAZ=0, FEZ=2, SAZ=5, SEZ=7, Nachfolger D mit FAZ=7):\n'
      '- GP(C) = 5 - 0 = 5 Tage (oder 7 - 2 = 5 Tage). (1,5 Pkt.)\n'
      '- FP(C) = FAZ(D) - FEZ(C) = 7 - 2 = 5 Tage. (1,5 Pkt.)\n'
      'Kritischer Pfad: Die Kette von Vorgängen, bei denen der Gesamtpuffer 0 beträgt: Start -> A (GP=0) -> B (GP=0) -> D (GP=0) -> Ende (Dauer 12 Tage). (1 Pkt.)',
      qtype='calc')


# ==============================================================================
# BEREICH 2: AP2 FISI TEIL 1 (Lernfelder 9 & 11) - Planen & Umsetzen von IT-Systemen
# ==============================================================================

# --- LF 9: Netzwerke & Dienste bereitstellen (VLAN, Routing, Redundanz, Firewall) ---
add_q('ap2_lf9_001', 'AP2_T1', 'LF 9', 'IEEE 802.1Q Frame-Tagging',
      'In einem Firmennetzwerk werden VLANs über Trunk-Verbindungen zwischen Switchen übertragen.',
      'Beschreiben Sie den Aufbau des 4-Byte 802.1Q-VLAN-Tags (TPID, TCI, VID) und unterscheiden Sie Access- und Trunk-Ports.',
      8,
      'Aufbau des 802.1Q-Tags (wird hinter Source-MAC eingefügt):\n'
      '1. TPID (Tag Protocol Identifier): 2 Byte mit dem festen Hex-Wert 0x8100 zur Identifikation des VLAN-Frames. (2 Pkt.)\n'
      '2. TCI (Tag Control Information): 2 Byte bestehend aus PCP (3 Bit Priorität / CoS), DEI (1 Bit Drop Eligible) und VID (VLAN Identifier, 12 Bit für 4096 VLANs 0-4095). (2 Pkt.)\n'
      'Access-Port: Gehört genau einem untagged VLAN an. Endgeräte empfangen Standard-Ethernet-Frames ohne Tag. (2 Pkt.)\n'
      'Trunk-Port (Tagged): Leitet Datenpakete mehrerer VLANs gleichzeitig weiter; jeder Frame erhält das 802.1Q-Tag (ausgenommen das native VLAN). (2 Pkt.)')

add_q('ap2_lf9_002', 'AP2_T1', 'LF 9', 'Inter-VLAN Routing Router-on-a-Stick',
      'Zwei Abteilungen befinden sich in VLAN 10 (192.168.10.0/24) und VLAN 20 (192.168.20.0/24). Ein physischer Router ist über eine einzelne Gigabit-Leitung an den Core-Switch angebunden.',
      'Erläutern Sie das Verfahren \"Router-on-a-Stick\" und geben Sie die wesentlichen Konfigurationsschritte auf dem Router (Subinterfaces, dot1Q) an.',
      8,
      'Verfahren: Der Router wickelt das Routing zwischen mehreren VLANs über eine einzige physische Schnittstelle ab, indem diese als Trunk betrieben wird. (2 Pkt.)\n'
      'Konfigurationsschritte:\n'
      '1. Physisches Interface aktivieren (no shutdown), keine IP zuweisen. (2 Pkt.)\n'
      '2. Logische Subinterfaces anlegen (z. B. interface GigabitEthernet0/0.10 und .20). (2 Pkt.)\n'
      '3. Dem Subinterface das entsprechende VLAN zuweisen (encapsulation dot1Q 10 bzw. 20) und die jeweilige Gateway-IP-Adresse konfigurieren. (2 Pkt.)')

add_q('ap2_lf9_003', 'AP2_T1', 'LF 9', 'Layer-3-Switch SVI Konfiguration',
      'Zur Entlastung des Routers soll das Routing zwischen zehn VLANs direkt auf einem Layer-3-Core-Switch durchgeführt werden.',
      'Erklären Sie den Unterschied zwischen einem Layer-2- und einem Layer-3-Switch und beschreiben Sie die Funktion eines Switched Virtual Interface (SVI).',
      6,
      'Unterschied: Ein Layer-2-Switch leitet Daten nur innerhalb desselben Broadcast-/VLAN-Segments anhand von MAC-Adressen weiter (Hardware-ASIC). Ein Layer-3-Switch verfügt zusätzlich über Routing-Funktionalität (IP-Routing) auf Hardware-Ebene (ASIC wire-speed routing) und kann ohne externen Router zwischen VLANs routen. (3 Pkt.)\n'
      'SVI (Switched Virtual Interface): Eine logische Layer-3-Schnittstelle auf dem Switch (z. B. interface Vlan10), der eine IP-Adresse zugewiesen wird. Sie fungiert als Default Gateway für alle Hosts in diesem VLAN. (3 Pkt.)')

add_q('ap2_lf9_004', 'AP2_T1', 'LF 9', 'Spanning Tree Protocol RSTP 802.1w',
      'Drei Switche sind im Dreieck redundant miteinander verkabelt.',
      'Welche drei gravierenden Netzwerkprobleme treten ohne Spanning Tree auf und wie verhindert Rapid STP (802.1w) Schleifen im Netzwerk?',
      8,
      'Probleme ohne STP:\n'
      '1. Broadcast Storms: Broadcast-Frames zirkulieren endlos und bringen die Bandbreite zum Einsturz. (1 Pkt.)\n'
      '2. MAC Table Flapping: Die Switch-Tabellen werden kontinuierlich überschrieben, da derselbe Frame über wechselnde Ports eintrifft. (1 Pkt.)\n'
      '3. Multiple Frame Transmission: Endgeräte erhalten dieselben Pakete mehrfach. (1 Pkt.)\n'
      'RSTP-Funktionsweise: Wählt die Root Bridge mit der niedrigsten Bridge-ID (Priorität + MAC). Alle Switche berechnen den kürzesten Pfad zur Root Bridge. Redundante Ports werden in den Zustand \"Discarding\" (Alternate/Backup Port) versetzt. Bei einem Linkausfall konvergiert RSTP aktiv über Handshake in wenigen hundert Millisekunden. (5 Pkt.)')

add_q('ap2_lf9_005', 'AP2_T1', 'LF 9', 'Link Aggregation LACP 802.3ad',
      'Zwei Switche werden über vier parallele 1-Gbit/s-Kupferkabel miteinander verbunden.',
      'Erläutern Sie die Vorteile von Link Aggregation (LAG / LACP) gegenüber Einzelverbindungen mit Spanning Tree und beschreiben Sie, wie die Lastverteilung erfolgt.',
      8,
      'Vorteile:\n'
      '1. Bandbreitenbündelung: Alle 4 Links werden gleichzeitig aktiv genutzt (kumulierte Bandbreite 4 Gbit/s), während STP sonst 3 Ports blockieren würde. (3 Pkt.)\n'
      '2. Unterbrechungsfreie Redundanz: Fällt ein Kabel aus, läuft der Datenverkehr nahtlos über die verbleibenden 3 Leitungen weiter. (2 Pkt.)\n'
      'Lastverteilung: Erfolgt über Hash-Algorithmen (z. B. Quell-/Ziel-IP, Quell-/Ziel-MAC oder TCP-Ports). Alle Pakete eines einzelnen TCP-Streams laufen über denselben physischen Port, um Paket-Out-of-Order-Probleme zu verhindern (keine 4 Gbit/s für einen Einzel-Download). (3 Pkt.)')

add_q('ap2_lf9_006', 'AP2_T1', 'LF 9', 'OSPF Link-State Routing & Kostenberechnung',
      'In einem Unternehmensnetzwerk mit mehreren Standorten wird OSPF (Open Shortest Path First) als dynamisches Routing-Protokoll eingesetzt.',
      'Erklären Sie das Link-State-Konzept von OSPF und berechnen Sie die OSPF-Metrik für eine 100-Mbit/s- und eine 10-Gbit/s-Leitung bei einer Referenzbandbreite von 100 Gbit/s (100.000 Mbit/s).',
      8,
      'Link-State-Konzept: Jeder Router baut eine vollständige Topologiekarte des gesamten Netzwerks auf (Link-State Database / LSDB) über Link-State Advertisements (LSAs) und berechnet mit dem Dijkstra-Algorithmus (SPF) den kürzesten Pfad. (4 Pkt.)\n'
      'Metrik-Formel: Cost = Referenzbandbreite / Interfacebandbreite.\n'
      '100 Mbit/s Leitung: Cost = 100.000 Mbit/s / 100 Mbit/s = 1000. (2 Pkt.)\n'
      '10 Gbit/s Leitung (10.000 Mbit/s): Cost = 100.000 Mbit/s / 10.000 Mbit/s = 10. (2 Pkt.)',
      qtype='calc')

add_q('ap2_lf9_007', 'AP2_T1', 'LF 9', 'BGP Autonomous Systems & Peering',
      'Ein Unternehmen bindet sein Rechenzentrum über zwei verschiedene Internet-Service-Provider (Multihoming) an.',
      'Definieren Sie den Begriff Autonomes System (AS) und erklären Sie den Unterschied zwischen eBGP und iBGP.',
      6,
      'Autonomes System (AS): Eine Sammlung von IP-Netzen unter gemeinsamer administrativer Kontrolle und einheitlicher Routing-Policy, das eine weltweit eindeutige ASN (Autonomous System Number) besitzt. (2 Pkt.)\n'
      'eBGP (External BGP): Routing-Protokoll zum Austausch von Routing-Informationen ZWISCHEN zwei unterschiedlichen Autonomen Systemen (z. B. Kunde <-> Provider). (2 Pkt.)\n'
      'iBGP (Internal BGP): Austausch von extern gelernten BGP-Routen INNERHALB desselben Autonomen Systems zwischen den Border-Routern. (2 Pkt.)')

add_q('ap2_lf9_008', 'AP2_T1', 'LF 9', 'NAT vs PAT (NAPT) Funktionsweise',
      'Ein Firmennetzwerk mit 250 Clients nutzt private IPv4-Adressen (10.0.0.0/24) und besitzt eine einzige offizielle, öffentliche IPv4-Adresse am Router.',
      'Erklären Sie den Unterschied zwischen statischem 1:1-NAT und PAT (Port Address Translation / NAT-Overload) und beschreiben Sie die Rolle der Translation-Table.',
      8,
      'Statisches NAT (1:1): Mappt eine private IP dauerhaft und exklusiv auf eine öffentliche IP. Für 250 Hosts wären 250 öffentliche IP-Adressen nötig. (2 Pkt.)\n'
      'PAT (Port and Address Translation / NAPT): Mappt hunderte interne private IP-Adressen auf eine einzige öffentliche IP-Adresse, indem der Router jedem internen Datenstrom einen eindeutigen Quell-Port (Source Port) zuweist. (3 Pkt.)\n'
      'Translation Table: Der Router führt eine Übersetzungstabelle (Private IP + Private Port <-> Public IP + Übersetzter Port). Eintreffende Antwortpakete aus dem Internet werden anhand der Ziel-Portnummer identifiziert und wieder an den ursprünglichen internen Client zurückgeroutet. (3 Pkt.)')

add_q('ap2_lf9_009', 'AP2_T1', 'LF 9', 'Site-to-Site VPN IPsec IKEv2 Phasen',
      'Zwei Unternehmensstandorte sollen dauerhaft über ein IPsec-Site-to-Site-VPN verschlüsselt miteinander verbunden werden.',
      'Beschreiben Sie die zwei Phasen des IKEv2-Handshakes (Internet Key Exchange) und unterscheiden Sie die Protokolle AH und ESP.',
      8,
      'Phase 1 (IKE_SA_INIT): Aushandeln der Sicherheitsvereinbarungen (Kryptoverfahren, DH-Gruppe) und Erstellen des sicheren, verschlüsselten Tunnels für den weiteren Schlüsselaustausch. (2 Pkt.)\n'
      'Phase 2 (IKE_AUTH / Child SA): Authentifizierung der Tunnelendpunkte (via Pre-Shared Key oder X.509-Zertifikaten) und Aufbau der eigentlichen IPsec-Sicherheitsassoziationen (SAs) für die Nutzdaten. (2 Pkt.)\n'
      'AH (Authentication Header): Bietet nur Integrität und Absenderauthentizität, verschlüsselt die Daten NICHT (daher in der Praxis kaum genutzt). (2 Pkt.)\n'
      'ESP (Encapsulating Security Payload): Bietet Vertraulichkeit (Verschlüsselung mit AES), Integrität und Authentizität. (2 Pkt.)')

add_q('ap2_lf9_010', 'AP2_T1', 'LF 9', 'Stateful Packet Inspection vs Next-Gen Firewall (NGFW)',
      'Im Unternehmen soll eine alte Paketfilter-Firewall durch eine Next-Generation-Firewall (NGFW) ersetzt werden.',
      'Vergleichen Sie Stateful Inspection mit Deep Packet Inspection (DPI) einer NGFW und nennen Sie zwei moderne NGFW-Features.',
      8,
      'Stateful Packet Inspection (SPI): Überwacht den Verbindungszustand von TCP/UDP-Sitzungen (SYN, ACK, FIN) und Header-Informationen auf Layer 3 und 4 (IPs, Ports). Erkennt keine Anwendungsbedrohungen im Payload. (3 Pkt.)\n'
      'Deep Packet Inspection (DPI): Untersucht die tatsächlichen Anwendungsnutzdaten auf Layer 7 (Payload), unabhängig vom verwendeten Port (erkennt z. B. BitTorrent über Port 80/443). (3 Pkt.)\n'
      'Zwei NGFW-Features: 1. Intrusion Prevention System (IPS / Signaturerkennung); 2. SSL/TLS-Inspection (Aufbrechen und Scannen verschlüsselter Datenströme). (2 Pkt.)')

add_q('ap2_net_001', 'AP2_T1', 'LF 9', 'Normierte Netzwerkplan-Symbole nach VRT Network Equipment',
      'In einem IHK-Prüfungsszenario soll ein Unternehmensnetzwerk nach dem offiziellen VRT-Symbolstandard der ZPA Nord-West dokumentiert werden.',
      'Erläutern Sie die visuellen Unterscheidungsmerkmale und Funktionen der genormten VRT-Symbole für: 1. Layer-2-Switch, 2. Layer-3-Switch, 3. Router mit NAT/PAT, 4. Firewall (Stateful Inspection / NGFW) und 5. Access Point.',
      8,
      '1. Layer-2-Switch: Flacher Quader mit 4 gegensätzlichen Pfeilen auf der Oberseite (horizontale Vermittlung auf Layer 2 / MAC). (1,5 Pkt.)\n'
      '2. Layer-3-Switch: Quader mit kreuzförmigen Pfeilen nach innen und außen (kombiniert L2-Switching mit hardwarebasiertem L3-Routing). (1,5 Pkt.)\n'
      '3. Router: Zylinder (Trommel) mit vier Pfeilen (zwei hinein, zwei heraus) bzw. mit NAT/PAT-Kennzeichnung; verbindet autonome IP-Netze auf Layer 3. (1,5 Pkt.)\n'
      '4. Firewall: Quader mit Ziegelsteinmauer-Muster; trennt Sicherheitszonen (LAN, DMZ, WAN) und filtert Pakete zustandsbasiert oder auf Applikationsebene. (2 Pkt.)\n'
      '5. Access Point: Kleines Gehäuse mit Antennensymbolen / Funkwellen; bridged Funkzellen (IEEE 802.11) ins kabelgebundene Ethernet (802.3). (1,5 Pkt.)')

add_q('ap2_net_002', 'AP2_T1', 'LF 9', 'Redundante Netzwerkinfrastruktur mit VRRP & LACP',
      'Für eine hochverfügbare Rechenzentrumsanbindung werden zwei Layer-3-Switches als redundantes Standard-Gateway für Clients eingerichtet. Gleichzeitig werden Server über mehrere Netzwerkkarten redundant angebunden.',
      'Erklären Sie das Zusammenspiel von Virtual Router Redundancy Protocol (VRRP) für die Gateway-Redundanz und Link Aggregation Control Protocol (LACP nach 802.3ad) für die Serveranbindung.',
      8,
      'VRRP Funktionsweise: Beide L3-Switches teilen sich eine gemeinsame virtuelle IP-Adresse (VIP) und virtuelle MAC-Adresse. Ein Switch ist Master und beantwortet ARP-Requests für die VIP. Fällt der Master aus, übernimmt der Backup-Switch innerhalb von Sekundenbruchteilen die VIP nahtlos (Keepalive-Multicasts bleiben aus), ohne dass Clients umkonfiguriert werden müssen. (4 Pkt.)\n'
      'LACP (802.3ad): Bündelt mehrere physische Netzwerkkabel zu einem einzigen logischen Link (Trunk / NIC-Teaming). Erhöht die aggregierte Bandbreite und bietet automatische Link-Redundanz (fällt ein Kabel aus, läuft der Traffic unterbrechungsfrei über die verbleibenden Ports weiter). (4 Pkt.)')


# --- LF 11: Speicher- und Hochverfügbarkeitssysteme implementieren ---
add_q('ap2_lf11_001', 'AP2_T1', 'LF 11', 'RAID 5 vs RAID 6 Nutzkapazität und URE',
      'Ein Storage-Server wird mit 8 Enterprise-Festplatten zu je 10 TB Bruttokapazität bestückt.',
      'Berechnen Sie die nutzbare Speicherkapazität für RAID 5 und RAID 6 und begründen Sie die Empfehlung von RAID 6 bei großen Festplatten anhand des URE-Risikos (Unrecoverable Read Error).',
      10,
      'RAID 5 Nutzkapazität: (N - 1) * Kapazität = (8 - 1) * 10 TB = 70 TB (1 Paritätsplatte). (2 Pkt.)\n'
      'RAID 6 Nutzkapazität: (N - 2) * Kapazität = (8 - 2) * 10 TB = 60 TB (2 Paritätsplatten). (2 Pkt.)\n'
      'URE-Risiko: Enterprise-SATA-Platten weisen eine URE-Fehlerrate von ca. 1 Bit pro 10^14 bis 10^15 gelesenen Bits auf. Beim tagelangen Rebuild eines RAID 5 nach Plattenausfall müssen zig Terabyte Daten lückenlos fehlerfrei gelesen werden. Tritt dabei ein einzelner Lesefehler auf, bricht der Rebuild ab -> Totalverlust des gesamten Arrays. RAID 6 toleriert durch zweifache Parität den gleichzeitigen Ausfall von zwei Platten und übersteht Lesefehler beim Rebuild unbeschadet. (6 Pkt.)',
      qtype='calc')

add_q('ap2_lf11_002', 'AP2_T1', 'LF 11', 'RAID 10 Aufbau und Fehlertoleranz',
      'Ein Datenbankadministrator benötigt maximale I/O-Performance und hohe Ausfallsicherheit und wählt ein RAID 10 aus 8 Festplatten zu je 4 TB.',
      'Beschreiben Sie den Aufbau eines RAID 10 (Stripe of Mirrors) und berechnen Sie die Nutzkapazität sowie die maximale und minimale Anzahl an Festplattenausfällen, die das Array überlebt.',
      8,
      'Aufbau: Kombination aus RAID 1 (Spiegelung) und RAID 0 (Striping). Zunächst werden jeweils 2 Festplatten zu einem RAID-1-Spiegelpaar zusammengefasst (4 Paare). Über diese 4 Spiegelpaare wird anschließend ein RAID 0 gestriped. (3 Pkt.)\n'
      'Nutzbare Kapazität: (N / 2) * Kapazität = (8 / 2) * 4 TB = 16 TB. (2 Pkt.)\n'
      'Fehlertoleranz:\n'
      'Minimaler Ausfall: 2 Platten (wenn zufällig beide Platten DENSELBEN RAID-1-Spiegelpaars ausfallen -> Datenverlust). (1,5 Pkt.)\n'
      'Maximaler Ausfall: Bis zu 4 Platten (sofern aus jedem der vier Spiegelpaare genau eine Platte ausfällt). (1,5 Pkt.)',
      qtype='calc')

add_q('ap2_lf11_003', 'AP2_T1', 'LF 11', 'Speicherarchitekturen DAS vs NAS vs SAN',
      'Für die Unternehmens-IT werden verschiedene Storage-Lösungen verglichen.',
      'Vergleichen Sie DAS, NAS und SAN bezüglich Zugriffsebene (Block vs File), Übertragungsmedien/Protokolle und typischem Einsatzzweck.',
      9,
      'DAS (Direct Attached Storage): Direkt am Server angeschlossener lokaler Speicher (SATA/SAS/NVMe). Block-Level-Zugriff. Nicht teilbar, nur für Einzelserver. (3 Pkt.)\n'
      'NAS (Network Attached Storage): Eigenständiges Dateisystem im Standard-LAN. File-Level-Zugriff (Datei-Ebene) über SMB/CIFS oder NFS. Ideal für zentrale Dateiablagen und Fileserver. (3 Pkt.)\n'
      'SAN (Storage Area Network): Dediziertes Hochgeschwindigkeits-Speichernetzwerk. Block-Level-Zugriff (RAW-LUNs erscheinen dem Host wie lokale Datenträger). Übertragung via Fibre Channel (FC) oder iSCSI. Ideal für Virtualisierungs-Cluster und Datenbanken. (3 Pkt.)')

add_q('ap2_lf11_004', 'AP2_T1', 'LF 11', 'SAN Protokolle Fibre Channel vs iSCSI',
      'Zur Anbindung eines VMware-vSphere-Clusters steht die Wahl zwischen Fibre Channel (FC) und iSCSI an.',
      'Vergleichen Sie FC und iSCSI hinsichtlich Hardware-Komponenten, Übertragungsmedium, MTU/Jumbo Frames und Kosten.',
      8,
      'Fibre Channel (FC): Benötigt dedizierte FC-Host-Bus-Adapter (HBAs), optische Transceiver und spezialisierte Fibre-Channel-Switche. Verlustfreies Protokoll mit extrem geringen Latenzen und festem Framing; sehr hohe Anschaffungskosten. (4 Pkt.)\n'
      'iSCSI: Kapselt SCSI-Befehle in Standard-TCP/IP-Pakete über normales Ethernet (10/25 GbE). Kostengünstiger, da Standard-Netzwerkkomponenten genutzt werden können. Erfordert zur Minimierung des Overheads zwingend Jumbo Frames (MTU 9000) und dedizierte/isolierte VLANs. (4 Pkt.)')

add_q('ap2_lf11_005', 'AP2_T1', 'LF 11', 'High-Availability Cluster Active-Passive vs Active-Active',
      'Ein Web- und Datenbanksystem soll hochverfügbar ausgelegt werden.',
      'Unterscheiden Sie ein Active/Passive-Cluster von einem Active/Active-Cluster und erklären Sie das Phänomen des Split-Brain-Syndroms.',
      8,
      'Active/Passive (Failover): Node 1 bedient alle Anfragen aktiv. Node 2 befindet sich im Standby und übernimmt die Dienste erst, wenn Node 1 ausfällt. Keine Lastverteilung, aber einfaches Datenmodell. (2 Pkt.)\n'
      'Active/Active (Load Balancing): Beide Nodes verarbeiten gleichzeitig produktive Anfragen parallel und synchronisieren Daten laufend. Optimale Ressourcenauslastung, erfordert komplexe Cluster-Dateisysteme / verteilte Locks. (2 Pkt.)\n'
      'Split-Brain-Syndrom: Wenn das interne Kommunikationsnetzwerk (Heartbeat-Netzwerk) zwischen den Clusterknoten abreißt, können die Knoten einander nicht mehr sehen. Jeder Knoten nimmt fälschlicherweise an, der andere sei tot, und übernimmt alle Ressourcen exklusiv. Beide schreiben gleichzeitig auf denselben Shared Storage -> Datenkorruption und Datenverlust. (4 Pkt.)')

add_q('ap2_lf11_006', 'AP2_T1', 'LF 11', 'Quorum und Fencing (STONITH)',
      'Um Split-Brain in einem 2-Node-Cluster sicher zu verhindern, wird ein Quorum-Mechanismus und STONITH eingerichtet.',
      'Erläutern Sie die Funktionsweise von Quorum (Mehrheitsentscheid) und beschreiben Sie das Prinzip von STONITH (Shoot The Other Node In The Head).',
      6,
      'Quorum: Regel, wonach ein Cluster-Teilbereich nur dann Entscheidungen treffen und Dienste weiterführen darf, wenn er über mehr als 50 % aller Cluster-Stimmen verfügt (z. B. 3 Knoten oder 2 Knoten + Witness/Quorum-Server). Bei Netztrennung verliert der isolierte Knoten das Quorum und schaltet sich passiv. (3 Pkt.)\n'
      'STONITH: Fencing-Methode. Ein gesunder Knoten schaltet einen nicht mehr reagierenden oder unklaren Knoten über eine IPMI/iLO-Schnittstelle oder eine schaltbare Steckdosenleiste (PDU) hardwareseitig hart ab (Strom aus), um unkontrollierte Schreibzugriffe auf den Shared Storage sicher auszuschließen. (3 Pkt.)')


# ==============================================================================
# BEREICH 3: AP2 FISI TEIL 2 (Lernfelder 10 & 12) - Betreiben von IT-Systemen
# ==============================================================================

# --- LF 10: Serverdienste & Automation ---
add_q('ap2_lf10_001', 'AP2_T2', 'LF 10', 'Active Directory FSMO-Rollen',
      'In einer Microsoft Active Directory Domain Services (AD DS) Gesamtstruktur existieren fünf FSMO-Rollen (Flexible Single Master Operations).',
      'Nennen Sie die fünf FSMO-Rollen, unterscheiden Sie zwischen gesamtstrukturweiten und domänenweiten Rollen und erläutern Sie die Aufgaben des PDC-Emulators.',
      10,
      'Gesamtstrukturweite Rollen (Forest-wide, genau 1-mal pro Forest):\n'
      '1. Schemamaster: Zuständig für Änderungen am AD-Datenbankschema. (1,5 Pkt.)\n'
      '2. Domänennamen-Master: Verwaltet das Hinzufügen und Entfernen von Domänen. (1,5 Pkt.)\n'
      'Domänenweite Rollen (Domain-wide, 1-mal pro Domäne):\n'
      '3. RID-Master: Vergibt RID-Pools an Domain Controller zur Erzeugung eindeutiger SIDs. (1,5 Pkt.)\n'
      '4. Infrastrukturmaster: Aktualisiert standortübergreifende Objektverweise (Phantom-Objekte). (1,5 Pkt.)\n'
      '5. PDC-Emulator: Haupt-Zeitquelle (NTP-Zeitserver) der Domäne, sofortige Synchronisation von Kennwortänderungen, Verwaltung von Kontosperrungen und Abwärtskompatibilität zu NT4. (4 Pkt.)')

add_q('ap2_lf10_002', 'AP2_T2', 'LF 10', 'Group Policy Objects (GPO) Vererbung LSDOU',
      'In einer Active-Directory-Umgebung werden Gruppenrichtlinien (GPOs) angewendet.',
      'Erläutern Sie die Auswertungsreihenfolge von Richtlinien nach der LSDOU-Regel und beschreiben Sie die Auswirkung der Einstellungen \"Vererbung deaktivieren\" (Block Inheritance) und \"Erzwungen\" (Enforced).',
      8,
      'LSDOU-Reihenfolge:\n'
      '1. Local (Lokal auf dem Clientcomputer)\n'
      '2. Site (Active Directory Standort)\n'
      '3. Domain (Domänenebene)\n'
      '4. OU (Organisationseinheit, von oberer OU zur untergeordneten OU).\n'
      'Die zuletzt ausgewertete Richtlinie überschreibt bei Konflikten vorherige Einstellungen (OU gewinnt gegen Domäne). (4 Pkt.)\n'
      'Vererbung deaktivieren: Verhindert, dass übergeordnete Richtlinien an untergeordnete OUs vererbt werden. (2 Pkt.)\n'
      'Erzwungen (Enforced): Setzt eine Richtlinie ausnahmslos durch; überstimmt Vererbungsblockaden untergeordneter OUs und kann nicht überschrieben werden. (2 Pkt.)')

add_q('ap2_lf10_003', 'AP2_T2', 'LF 10', 'Kerberos-Authentifizierung 3-Wege-Handshake',
      'Active Directory verwendet standardmäßig das Kerberos-Protokoll zur sicheren Benutzerauthentifizierung.',
      'Beschreiben Sie die drei Schritte des Kerberos-Prozesses unter Nennung der Rollen KDC, AS, TGS, TGT und Service-Ticket.',
      8,
      '1. Authentication Service (AS-Exchange): Client sendet Anmeldeanforderung an den Authentication Server des KDC. Der AS prüft die Anmeldedaten und antwortet mit einem TGT (Ticket Granting Ticket), das mit dem geheimen Schlüssel des KDC verschlüsselt ist. (3 Pkt.)\n'
      '2. Ticket Granting Service (TGS-Exchange): Möchte der Client auf eine Ressource zugreifen, sendet er das TGT an den Ticket Granting Server. Dieser validiert das TGT und stellt ein Service-Ticket für den gewünschten Zielserver aus. (3 Pkt.)\n'
      '3. Client-to-Server-Exchange: Der Client übergibt das Service-Ticket an den Zielserver. Der Server entschlüsselt das Ticket mit seinem eigenen Computerkonto-Schlüssel und gewährt den Zugriff ohne Passwortübertragung im Netz. (2 Pkt.)')

add_q('ap2_lf10_004', 'AP2_T2', 'LF 10', 'Public Key Infrastructure (PKI) X.509',
      'Ein Unternehmen baut eine zweistufige Public-Key-Infrastruktur (PKI) mit Offline-Root-CA und Online-Sub-CA auf.',
      'Begründen Sie, warum die Root-CA offline betrieben wird, und erklären Sie den Unterschied zwischen einer Sperrliste (CRL) und OCSP.',
      8,
      'Offline Root-CA: Die Stammzertifizierungsstelle ist die Vertrauensbasis der gesamten Organisation. Wird ihr privater Schlüssel kompromittiert, ist die gesamte PKI wertlos. Sie wird offline gehalten (abgeschaltet, im Tresor), um sie vor Netzwerkangriffen zu schützen, und signiert nur die Zertifikate der untergeordneten ausstellenden CAs (Sub-CAs). (4 Pkt.)\n'
      'CRL (Certificate Revocation List): Eine signierte Datei, die periodisch von der CA veröffentlicht wird und alle widerrufenen Zertifikate auflistet. Nachteil: Kann sehr groß werden und ist bis zum nächsten Update zeitlich verzögert. (2 Pkt.)\n'
      'OCSP (Online Certificate Status Protocol): Ermöglicht eine Echtzeit-Statusabfrage für ein einzelnes konkretes Zertifikat beim OCSP-Responder; extrem bandbreitenschonend und aktuell. (2 Pkt.)')

add_q('ap2_lf10_005', 'AP2_T2', 'LF 10', 'E-Mail-Sicherheit SPF, DKIM und DMARC',
      'Zur Verhinderung von Spam, Spoofing und Phishing im Namen der eigenen Firmendomäne werden DNS-Einträge konfiguriert.',
      'Erläutern Sie die Aufgaben und Funktionsweisen von SPF, DKIM und DMARC.',
      9,
      'SPF (Sender Policy Framework): Ein DNS-TXT-Record, in dem der Domäneninhaber festlegt, welche IP-Adressen und Mailserver berechtigt sind, E-Mails im Namen dieser Domäne zu versenden. Der empfangende Mailserver gleicht die Quell-IP des Absenders damit ab. (3 Pkt.)\n'
      'DKIM (DomainKeys Identified Mail): Der ausgehende Mailserver signiert Teile des E-Mail-Headers und den Body kryptografisch mit einem privaten Schlüssel. Der Empfänger prüft die Signatur mit dem im DNS publizierten öffentlichen Schlüssel auf Unverfälschtheit. (3 Pkt.)\n'
      'DMARC (Domain-based Message Authentication): Richtlinie im DNS, die festlegt, wie der empfangende Mailserver verfahren soll, wenn SPF oder DKIM fehlschlagen (z. B. none, quarantine, reject), und fordert aggregierte XML-Sicherheitsberichte an den Domäneninhaber an. (3 Pkt.)')

add_q('ap2_lf10_006', 'AP2_T2', 'LF 10', 'Infrastruktur-Automatisierung mit Ansible',
      'Zur Konfiguration von 80 Linux-Servern wird ein Infrastructure-as-Code-Werkzeug eingeführt.',
      'Erklären Sie die Begriffe Agentless und Idempotenz im Kontext von Ansible und beschreiben Sie den Aufbau eines Playbooks.',
      8,
      'Agentless: Auf den Zielsystemen muss kein spezieller Hintergrunddienst (Agent) installiert werden; Ansible steuert die Server direkt über Standardprotokolle wie SSH (Linux) oder WinRM (Windows) an und benötigt lediglich Python auf den Zielhosts. (3 Pkt.)\n'
      'Idempotenz: Ein Playbook kann beliebig oft ausgeführt werden und führt immer zum identischen Soll-Zustand. Befindet sich ein Server bereits im gewünschten Zustand (z. B. Paket ist bereits installiert), führt Ansible keine Änderungen aus (\"ok\" statt \"changed\"). (3 Pkt.)\n'
      'Aufbau eines Playbooks: In YAML-Syntax verfasste Datei, die Plays enthält. Jedes Play definiert Ziel-Hosts, Variablen und eine geordnete Liste von Tasks, die vorgefertigte Module (z. B. apt, copy, systemd) aufrufen. (2 Pkt.)')

# --- LF 10: Enterprise SQL & Relationales Datenbankmanagement (ZPA 2. Auflage) ---

add_q('ap2_sql_001', 'AP2_T2', 'LF 10', 'SQL DDL CREATE TABLE mit Constraints',
      'Für eine Ticket-Verwaltung soll die Tabelle \"ticket\" per SQL angelegt werden: id (Ganzzahl, Primärschlüssel mit Autoinkrement), titel (Text, max. 100 Zeichen, Pflichtfeld), status (Text, Standardwert \"OFFEN\"), prioritaet (Ganzzahl, Werte nur von 1 bis 5 erlaubt), ersteller_id (Ganzzahl, Fremdschlüssel auf benutzer.id mit Kaskadierung beim Löschen).',
      'Schreiben Sie das syntaktisch korrekte SQL-Statement nach ANSI/ISO-Standard.',
      10,
      'CREATE TABLE ticket (\n'
      '    id INTEGER PRIMARY KEY AUTO_INCREMENT,\n'
      '    titel VARCHAR(100) NOT NULL,\n'
      '    status VARCHAR(20) DEFAULT \'OFFEN\',\n'
      '    prioritaet INT CHECK (prioritaet BETWEEN 1 AND 5),\n'
      '    ersteller_id INT,\n'
      '    FOREIGN KEY (ersteller_id) REFERENCES benutzer(id) ON DELETE CASCADE\n'
      '); (10 Pkt. - Abzug bei fehlendem NOT NULL, CHECK, DEFAULT oder FOREIGN KEY)')

add_q('ap2_sql_002', 'AP2_T2', 'LF 10', 'SQL DML Aggregation und GROUP BY mit HAVING',
      'Gegeben sind die Tabellen kunden (id, name, stadt) und bestellungen (id, kunde_id, betrag, datum).',
      'Formulieren Sie eine SQL-Abfrage, die den Kundennamen und die Gesamtsumme aller Bestellungen für jeden Kunden ausgibt, dessen Gesamtbestellwert 10.000 EUR überschreitet. Das Ergebnis soll absteigend nach der Summe sortiert sein.',
      10,
      'SELECT k.name, SUM(b.betrag) AS gesamtumsatz\n'
      'FROM kunden k\n'
      'INNER JOIN bestellungen b ON k.id = b.kunde_id\n'
      'GROUP BY k.id, k.name\n'
      'HAVING SUM(b.betrag) > 10000\n'
      'ORDER BY gesamtumsatz DESC; (10 Pkt. - Abzug bei WHERE statt HAVING für Aggregatfunktion oder fehlendem GROUP BY)')

add_q('ap2_sql_003', 'AP2_T2', 'LF 10', 'SQL JOIN-Typen INNER vs LEFT vs FULL',
      'In einer Datenbank existieren mitarbeiter (id, name, abt_id) und abteilungen (id, bezeichnung). Einige Mitarbeiter haben keine Abteilung, und einige Abteilungen haben keine Mitarbeiter.',
      'Erläutern Sie den Unterschied im Abfrageergebnis zwischen INNER JOIN und LEFT OUTER JOIN bezüglich der Ergebniszeilen.',
      6,
      'INNER JOIN: Liefert ausschließlich Zeilen zurück, bei denen in beiden Tabellen ein übereinstimmender Wert vorliegt (Schnittmenge). Mitarbeiter ohne Abteilung und Abteilungen ohne Mitarbeiter werden vollständig verworfen. (3 Pkt.)\n'
      'LEFT OUTER JOIN (mitarbeiter LEFT JOIN abteilungen): Liefert ALLE Datensätze der linken Tabelle (mitarbeiter), selbst wenn keine Übereinstimmung in abteilungen vorliegt. Die fehlenden Abteilungsspalten werden mit NULL aufgefüllt. (3 Pkt.)')

add_q('ap2_sql_004', 'AP2_T2', 'LF 10', 'SQL Transaktionen ACID-Eigenschaften',
      'Bei einer Banküberweisung von 500 EUR von Konto A auf Konto B wird ein Transaktionsblock ausgeführt.',
      'Nennen und erläutern Sie die vier ACID-Eigenschaften und beschreiben Sie, was passiert, wenn nach dem Abbuchen von Konto A das Datenbanksystem abstürzt.',
      8,
      'Atomarität (Atomicity): Alles-oder-Nichts-Prinzip. Eine Transaktion wird entweder ganz oder gar nicht ausgeführt. (2 Pkt.)\n'
      'Konsistenz (Consistency): Nach Abschluss der Transaktion befindet sich die Datenbank in einem gültigen, integren Zustand. (2 Pkt.)\n'
      'Isolation: Gleichzeitige Transaktionen beeinflussen sich nicht gegenseitig. (1 Pkt.)\n'
      'Dauerhaftigkeit (Durability): Erfolgreich mit COMMIT bestätigte Änderungen bleiben dauerhaft im Speicher erhalten. (1 Pkt.)\n'
      'Absturzfolge: Da die Buchung nicht durch COMMIT bestätigt wurde, greift beim Neustart ein automatisches Rollback (Undo-Logging). Die Abbuchung auf Konto A wird rückgängig gemacht. (2 Pkt.)')

add_q('ap2_sql_005', 'AP2_T2', 'LF 10', 'SQL Subqueries mit IN und EXISTS',
      'Gegeben sind die Tabellen kunden (id, name, land) und bestellungen (id, kunde_id, summe).',
      'Formulieren Sie zwei SQL-Abfragen, die alle Kundennamen ausgeben, die mindestens eine Bestellung getätigt haben: Einmal unter Verwendung einer Subquery mit IN und einmal mit EXISTS.',
      8,
      'Variante 1 (IN):\n'
      'SELECT name FROM kunden WHERE id IN (SELECT kunde_id FROM bestellungen); (4 Pkt.)\n'
      'Variante 2 (EXISTS / Korrelierte Unterabfrage):\n'
      'SELECT k.name FROM kunden k WHERE EXISTS (SELECT 1 FROM bestellungen b WHERE b.kunde_id = k.id); (4 Pkt.)')

add_q('ap2_sql_006', 'AP2_T2', 'LF 10', 'SQL Window Functions ROW_NUMBER & RANK',
      'In einer Vertriebsdatenbank sollen die Top-3-Umsätze jedes Verkäufers ermittelt werden.',
      'Erläutern Sie die Funktionsweise von SQL Window Functions gegenüber GROUP BY und erklären Sie die Syntax von ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...).',
      8,
      'Unterschied zu GROUP BY: GROUP BY fasst Zeilen zusammen und reduziert die Ergebnismenge auf eine einzige Zeile pro Gruppe. Eine Window Function führt Berechnungen über eine definierte Zeilenmenge (das Fenster / Window) durch, behält jedoch die individuelle Identität jeder einzelnen Zeile bei. (4 Pkt.)\n'
      'Syntax-Erklärung:\n'
      '- ROW_NUMBER(): Vergibt eine fortlaufende Zeilennummer (1, 2, 3...).\n'
      '- PARTITION BY spalte: Teilt den Datensatz in logische Untergruppen (z. B. pro Verkäufer).\n'
      '- ORDER BY spalte DESC: Bestimmt die Sortierreihenfolge innerhalb jeder Partition (z. B. höchster Umsatz zuerst). (4 Pkt.)')

add_q('ap2_sql_007', 'AP2_T2', 'LF 10', 'SQL Datums- und Zeitfunktionen (DATEDIFF & DATEADD)',
      'In einem Support-System (Tabelle tickets mit id, erstelldatum, schliessdatum) soll die Bearbeitungsdauer analysiert werden.',
      'Formulieren Sie eine SQL-Abfrage nach ZPA-Standard, die für alle im laufenden Jahr geschlossenen Tickets die Ticket-ID und die Bearbeitungsdauer in Tagen berechnet (unter Verwendung von DATEDIFF) und nur Tickets anzeigt, deren Bearbeitung länger als 14 Tage gedauert hat.',
      8,
      'SELECT id, DATEDIFF(day, erstelldatum, schliessdatum) AS bearbeitungsdauer_tage\n'
      'FROM tickets\n'
      'WHERE schliessdatum IS NOT NULL\n'
      '  AND DATEDIFF(day, erstelldatum, schliessdatum) > 14\n'
      'ORDER BY bearbeitungsdauer_tage DESC; (8 Pkt. - Volle Punktzahl auch bei SQL-Dialekt-Varianten wie DATEDIFF(schliessdatum, erstelldatum) oder DATE_PART)')

add_q('ap2_sql_008', 'AP2_T2', 'LF 10', 'Statistische SQL-Funktionen (STDDEV, VARIANCE, CORR)',
      'Im Rahmen einer Performance-Analyse von Server-Antwortzeiten (Tabelle server_metrics mit server_id, response_time_ms, cpu_load) werden statistische Kennzahlen benötigt.',
      'Erläutern Sie die Aufgaben und mathematische Bedeutung der SQL-Aggregatfunktionen STDDEV(), VARIANCE() und CORR() und beschreiben Sie einen Anwendungsfall zur Erkennung von Lastanomalien.',
      6,
      'VARIANCE(): Berechnet die statistische Varianz (mittlere quadratische Abweichung vom Mittelwert) der Messwerte. (2 Pkt.)\n'
      'STDDEV(): Berechnet die Standardabweichung (Quadratwurzel der Varianz) als Maß für die Streuung um den Mittelwert. Anwendungsfall: Überschreitet eine Antwortzeit den Bereich Mittelwert + 3*STDDEV (3-Sigma-Regel), liegt eine signifikante Performance-Anomalie vor. (2 Pkt.)\n'
      'CORR(spalte1, spalte2): Berechnet den Pearson-Korrelationskoeffizienten (-1 bis +1) zwischen zwei Variablen, um festzustellen, ob hohe Antwortzeiten direkt linear mit hoher CPU-Last korrelieren. (2 Pkt.)')


# --- LF 12: Virtualisierung, Cloud & Monitoring ---
add_q('ap2_lf12_001', 'AP2_T2', 'LF 12', 'Hypervisor-Architekturen Typ 1 vs Typ 2',
      'Für ein IT-Konsolidierungsprojekt werden Virtualisierungslösungen evaluiert.',
      'Vergleichen Sie Typ-1-Hypervisoren (Bare-Metal) und Typ-2-Hypervisoren (Hosted) hinsichtlich Architektur, Performance und Einsatzbereich und nennen Sie jeweils zwei Produktbeispiele.',
      8,
      'Typ-1-Hypervisor (Bare-Metal): Wird direkt auf der physischen Server-Hardware ohne zwischengeschaltetes Wirtsbetriebssystem installiert. Bietet höchste I/O-Performance, minimale Latenzen und geringen Ressourcen-Overhead. Einsatz im professionellen Rechenzentrum/Enterprise-Bereich. Beispiele: VMware ESXi, Proxmox VE, Microsoft Hyper-V Server. (4 Pkt.)\n'
      'Typ-2-Hypervisor (Hosted): Läuft als normale Anwendungssoftware auf einem bestehenden Wirts-Betriebssystem (Windows, macOS, Linux). Deutlich höherer Overhead durch doppelte Treiber- und Kernel-Schichten. Einsatz auf Entwickler-Workstations und Testumgebungen. Beispiele: Oracle VirtualBox, VMware Workstation. (4 Pkt.)')

add_q('ap2_lf12_002', 'AP2_T2', 'LF 12', 'Docker-Container vs Virtuelle Maschinen',
      'Ein Entwicklerteam möchte monolithische Anwendungen in containerbasierte Microservices zerlegen.',
      'Vergleichen Sie Container und virtuelle Maschinen hinsichtlich Kernel-Architektur, Startzeiten, Speicherplatzbedarf und Isolation.',
      8,
      'Architektur & Kernel: Virtuelle Maschinen bringen ein eigenes vollständiges Gast-Betriebssystem samt eigenem Kernel mit. Docker-Container teilen sich den Kernel des Host-Betriebssystems und werden über Linux-Kernel-Features (Namespaces für Trennung von Prozessen/Netzwerk und cgroups für Ressourcenbegrenzung) isoliert. (3 Pkt.)\n'
      'Startzeit: VM benötigt 30 bis 60 Sekunden (kompletter OS-Bootvorgang); Container startet in wenigen Millisekunden (reiner Prozessstart). (2 Pkt.)\n'
      'Speicherbedarf: VM benötigt mehrere Gigabyte Festplattenspeicher; Container-Images sind oft nur wenige Megabyte groß. (1,5 Pkt.)\n'
      'Isolation: VMs bieten stärkere Hardware-Isolation über Hypervisor-Sicherheitsgrenzen; Container teilen sich denselben Kernel (bei Kernel-Exploits höheres Ausbruchsrisiko). (1,5 Pkt.)')

add_q('ap2_lf12_003', 'AP2_T2', 'LF 12', 'Cloud Service Modelle IaaS vs PaaS vs SaaS',
      'Die Unternehmensführung plant die Migration von Diensten in die Cloud.',
      'Definieren Sie die Cloud-Servicemodelle IaaS, PaaS und SaaS nach NIST und erklären Sie das Shared Responsibility Model (Gemeinsame Verantwortlichkeit).',
      9,
      'IaaS (Infrastructure as a Service): Der Provider stellt virtualisierte Hardware (VMs, Speicher, Netzwerk) bereit. Der Kunde ist verantwortlich für Betriebssystem, Patches, Middleware, Runtimes und Anwendungen. (2 Pkt.)\n'
      'PaaS (Platform as a Service): Der Provider verwaltet Hardware, Betriebssystem und Laufzeitumgebung (z. B. Python, Node.js, SQL-Engine). Der Kunde kümmert sich nur noch um seinen Anwendungscode und die Daten. (2 Pkt.)\n'
      'SaaS (Software as a Service): Der Provider betreibt die vollständige schlüsselfertige Software samt Infrastruktur. Der Kunde nutzt die Anwendung nur über Webbrowser/API (z. B. Microsoft 365). (2 Pkt.)\n'
      'Shared Responsibility Model: Definiert die genaue Grenze der Sicherheitsverantwortung: Der Cloud-Anbieter haftet für die Sicherheit DER Cloud (physische RZs, Hypervisor, Basisinfrastruktur), der Kunde ist verantwortlich für die Sicherheit IN der Cloud (Identitäten, Zugriffskontrollen, Datenverschlüsselung, Patching ab OS-Ebene bei IaaS). (3 Pkt.)')

add_q('ap2_lf12_004', 'AP2_T2', 'LF 12', 'SNMPv2c vs SNMPv3 Netzwerk-Monitoring',
      'Zur Überwachung von 50 Core-Switchen wird ein Zabbix-Monitoring-Server eingerichtet.',
      'Begründen Sie, warum SNMPv2c in modernen Netzen als Sicherheitsrisiko gilt, und erläutern Sie die drei Sicherheitsstufen von SNMPv3 (noAuthNoPriv, authNoPriv, authPriv).',
      8,
      'Sicherheitsrisiko SNMPv2c: Die Authentifizierung erfolgt ausschließlich über einen unverschlüsselten Klartext-String (Community String, z. B. \"public\"). Jeder Netzwerksniffer kann Passwörter und Konfigurationen mitlesen oder manipulieren. (3 Pkt.)\n'
      'SNMPv3 Sicherheitsstufen:\n'
      '1. noAuthNoPriv: Keine Authentifizierung, keine Verschlüsselung (nur User-ID). (1 Pkt.)\n'
      '2. authNoPriv: Authentifizierung über kryptografische Hashverfahren (HMAC-MD5/SHA), aber unverschlüsselte Nutzdatenübertragung. (2 Pkt.)\n'
      '3. authPriv: Höchste Sicherheitsstufe: Hash-basierte Authentifizierung UND symmetrische Verschlüsselung der gesamten Nutzdaten via AES/DES. (2 Pkt.)')

add_q('ap2_lf12_005', 'AP2_T2', 'LF 12', 'Hochverfügbarkeits-Berechnung Verfügbarkeit in Prozent',
      'In einem SLA garantiert ein IT-Dienstleister für einen Cloud-Dienst eine Verfügbarkeit von 99,9 % (\"Drei Neunen\") bezogen auf ein Jahr (365 Tage à 24 Stunden).',
      'Berechnen Sie die maximal zulässige Ausfallzeit in Stunden und Minuten pro Jahr.',
      6,
      'Gesamtdauer eines Jahres in Stunden: 365 Tage * 24 h = 8760 Stunden. (2 Pkt.)\n'
      'Maximal zulässige Nichtverfügbarkeit in Prozent: 100 % - 99,9 % = 0,1 % = 0,001. (2 Pkt.)\n'
      'Ausfallzeit in Stunden: 8760 h * 0,001 = 8,76 Stunden.\n'
      'Umrechnung der Nachkommastelle: 0,76 * 60 Minuten = 45,6 Minuten -> 8 Stunden und 45 Minuten (bzw. 46 Min.). (2 Pkt.)',
      qtype='calc')

add_q('ap2_lf12_006', 'AP2_T2', 'LF 12', 'Kubernetes Architektur Pods und Cluster',
      'Ein Unternehmen betreibt Microservices in einem Kubernetes-Cluster.',
      'Erläutern Sie die Aufgaben der Control Plane Komponenten (kube-apiserver, etcd, kube-scheduler) und definieren Sie das Konzept eines Pods.',
      8,
      'Control Plane Komponenten:\n'
      '1. kube-apiserver: Zentrale REST-Schnittstelle des Clusters, über die alle internen und externen Steuerungsbefehle laufen. (2 Pkt.)\n'
      '2. etcd: Konsistenter, hochverfügbarer Key-Value-Speicher für alle Zustands- und Konfigurationsdaten des Clusters. (2 Pkt.)\n'
      '3. kube-scheduler: Weist neu erstellten Pods anhand von Ressourcenanforderungen und Richtlinien passende Worker-Nodes zu. (2 Pkt.)\n'
      'Pod: Die kleinste bereitstellbare Ausführungseinheit in Kubernetes. Ein Pod kapselt einen oder mehrere eng verknüpfte Container, die sich gemeinsamen Speicher (Volumes), Netzwerk-IP und Port-Adressraum teilen. (2 Pkt.)')


# ==============================================================================
# BEREICH 4: WiSo - Wirtschafts- und Sozialkunde
# ==============================================================================

add_q('wiso_001', 'WiSo', 'WiSo', 'Gesetzliche Kündigungsfristen nach BGB § 622',
      'Ein Fachinformatiker ist seit 12 Jahren ununterbrochen in einem mittelständischen IT-Systemhaus beschäftigt. Am 18. Mai erhält er eine ordentliche, betriebsbedingte Kündigung des Arbeitgebers.',
      'Ermitteln Sie unter Angabe der gesetzlichen Bestimmungen des § 622 BGB die Kündigungsfrist und das exakte Beendigungsdatum des Arbeitsverhältnisses.',
      8,
      'Gesetzliche Frist nach § 622 Abs. 2 Nr. 4 BGB: Bei einer Betriebszugehörigkeit von 10 Jahren beträgt die Frist 4 Monate zum Ende eines Kalendermonats. (4 Pkt.)\n'
      'Fristberechnung: Die 4-Monats-Frist beginnt nach Zugang im Mai zu laufen (Juni, Juli, August, September). Beendigungstermin ist der 30. September. (4 Pkt.)',
      qtype='calc')

add_q('wiso_002', 'WiSo', 'WiSo', 'Kündigungsschutzgesetz KSchG Klagefrist',
      'Ein Arbeitnehmer erhält eine verhaltensbedingte Kündigung, die er für sachlich unbegründet und rechtswidrig hält.',
      'Nennen Sie die Frist zur Erhebung einer Kündigungsschutzklage beim Arbeitsgericht nach § 4 KSchG und beschreiben Sie, was geschieht, wenn diese Frist versäumt wird.',
      6,
      'Klagefrist: Die Klage muss innerhalb von drei Wochen nach schriftlichem Zugang der Kündigung beim Arbeitsgericht erhoben werden. (3 Pkt.)\n'
      'Rechtsfolge bei Versäumnis: Nach § 7 KSchG gilt die Kündigung als von Anfang an rechtswirksam (Fiktionswirkung); das Arbeitsverhältnis endet unwiderruflich zum Kündigungstermin. (3 Pkt.)')

add_q('wiso_003', 'WiSo', 'WiSo', 'BBiG Rechte und Pflichten von Auszubildenden',
      'Ein Auszubildender im 2. Ausbildungsjahr weigert sich, täglich 2 Stunden lang private Botengänge für den Geschäftsführer zu erledigen.',
      'Prüfen Sie die Rechtmäßigkeit dieser Anweisung nach dem Berufsbildungsgesetz (BBiG) und nennen Sie zwei wesentliche Pflichten des Ausbildenden sowie zwei Pflichten des Auszubildenden.',
      8,
      'Rechtmäßigkeit: Die Anweisung ist rechtswidrig nach § 14 Abs. 3 BBiG (Auszubildenden dürfen nur Aufgaben übertragen werden, die dem Ausbildungszweck dienen und ihren körperlichen Kräften angemessen sind). (2 Pkt.)\n'
      'Zwei Pflichten des Ausbildenden: 1. Ausbildungspflicht (Vermittlung der Ausbildungsinhalte); 2. Kostenlose Bereitstellung der Ausbildungsmittel; 3. Freistellung für Berufsschule und Prüfungen. (2 Pkt.)\n'
      'Zwei Pflichten des Auszubildenden: 1. Lernpflicht (Bemühen um Ausbildungserfolg); 2. Sorgfaltspflicht und Führen des Ausbildungsnachweises; 3. Schweigepflicht über Betriebsgeheimnisse. (2 Pkt.)')

add_q('wiso_004', 'WiSo', 'WiSo', 'BetrVG Mitbestimmung bei technischen Einrichtungen',
      'Die Geschäftsleitung führt ohne Einbindung des Betriebsrats eine Software ein, die Tastenanschläge und Login-Zeiten der Mitarbeiter minutengenau protokolliert.',
      'Beurteilen Sie die Rechtslage nach § 87 Abs. 1 Nr. 6 BetrVG und erklären Sie, welche Schritte der Betriebsrat einleiten kann.',
      8,
      'Rechtslage: Der Betriebsrat hat nach § 87 Abs. 1 Nr. 6 BetrVG ein zwingendes, erzwingbares Mitbestimmungsrecht bei der Einführung und Anwendung von technischen Einrichtungen, die dazu bestimmt oder geeignet sind, das Verhalten oder die Leistung der Arbeitnehmer zu überwachen. Ohne vorherige Zustimmung oder Betriebsvereinbarung ist die Einführung unzulässig. (4 Pkt.)\n'
      'Schritte des Betriebsrats: 1. Aufforderung an die Geschäftsleitung zur sofortigen Stilllegung/Abschaltung der Überwachung; 2. Beantragung einer einstweiligen Verfügung beim Arbeitsgericht; 3. Bei Nichteinigung Anrufung der Einigungsstelle (§ 76 BetrVG), deren Spruch die Einigung verbindlich ersetzt. (4 Pkt.)')

add_q('wiso_005', 'WiSo', 'WiSo', 'Tarifvertragsarten Manteltarif vs Entgelttarif',
      'Gewerkschaften und Arbeitgeberverbände handeln Tarifverträge aus.',
      'Unterscheiden Sie den Manteltarifvertrag (bzw. Rahmentarifvertrag) vom Entgelttarifvertrag (Vergütungstarifvertrag) hinsichtlich Inhalten und typischer Laufzeit.',
      6,
      'Manteltarifvertrag: Regelt allgemeine Arbeitsbedingungen wie Arbeitszeit, Urlaubsdauer, Kündigungsfristen, Mehrarbeitszuschläge und Schutzbestimmungen. Typische Laufzeit: Mehrere Jahre (meist 3 bis 5 Jahre). (3 Pkt.)\n'
      'Entgelttarifvertrag: Regelt die konkrete Höhe der monatlichen Vergütung, Löhne, Gehälter und Ausbildungsvergütungen eingeteilt in Tarifgruppen. Typische Laufzeit: Kurzfristig (meist 12 bis 24 Monate). (3 Pkt.)')

add_q('wiso_006', 'WiSo', 'WiSo', 'Die 5 Säulen der gesetzlichen Sozialversicherung',
      'Vom Bruttogehalt eines Arbeitnehmers werden Beiträge zur gesetzlichen Sozialversicherung abgeführt.',
      'Nennen Sie die fünf Säulen der gesetzlichen Sozialversicherung und geben Sie an, welcher Zweig im Gegensatz zu den anderen zu 100 % allein vom Arbeitgeber finanziert wird.',
      10,
      '1. Krankenversicherung (GKV) - paritätisch getragen. (2 Pkt.)\n'
      '2. Pflegeversicherung (GPV) - paritätisch getragen (+ Kinderlosenzuschlag für AN). (2 Pkt.)\n'
      '3. Rentenversicherung (GRV) - paritätisch getragen. (2 Pkt.)\n'
      '4. Arbeitslosenversicherung (ALV) - paritätisch getragen. (2 Pkt.)\n'
      '5. Unfallversicherung (Gesetzliche Unfallversicherung / Berufsgenossenschaft): Wird zu 100 % allein vom Arbeitgeber getragen! (2 Pkt.)')

add_q('wiso_007', 'WiSo', 'WiSo', 'Gehaltsabrechnung Brutto zu Netto',
      'Ein IT-Mitarbeiter (Steuerklasse 1, keine Kinder) erhält ein monatliches Bruttogehalt von 4.000 EUR.',
      'Erläutern Sie die Abzugsposten vom Brutto- zum Nettogehalt und unterscheiden Sie Steuern von Sozialversicherungsbeiträgen.',
      6,
      'Abzugsposten:\n'
      '1. Steuern: Lohnsteuer (an das Finanzamt), Solidaritätszuschlag (sofern Freigrenze überschritten), ggf. Kirchensteuer. (3 Pkt.)\n'
      '2. Gesetzliche Sozialabgaben (ca. 20-21 % AN-Anteil): Kranken-, Pflege-, Renten- und Arbeitslosenversicherung (an die zuständige Krankenkasse als Einzugsstelle). (3 Pkt.)')

add_q('wiso_008', 'WiSo', 'WiSo', 'Unternehmensformen GmbH vs Aktiengesellschaft (AG)',
      'Für die Expansion eines Cloud-Startups wird die Wahl zwischen einer GmbH und einer AG abgewogen.',
      'Vergleichen Sie GmbH und AG bezüglich Mindestkapital, Organe und Haftung.',
      8,
      'GmbH (Gesellschaft mit beschränkter Haftung):\n'
      '- Mindeststammkapital: 25.000 EUR. (1 Pkt.)\n'
      '- Organe: Geschäftsführer (Leitung) und Gesellschafterversammlung (Beschlussfassung). (2 Pkt.)\n'
      '- Haftung: Beschränkt auf das Gesellschaftsvermögen der GmbH. (1 Pkt.)\n'
      'AG (Aktiengesellschaft):\n'
      '- Mindestgrundkapital: 50.000 EUR. (1 Pkt.)\n'
      '- Organe: Vorstand (Leitung), Aufsichtsrat (Kontrolle), Hauptversammlung der Aktionäre (Beschlussfassung). (2 Pkt.)\n'
      '- Haftung: Beschränkt auf das Gesellschaftsvermögen der AG (Aktionär haftet nur mit dem Aktienwert). (1 Pkt.)')

add_q('wiso_009', 'WiSo', 'WiSo', 'Handelsregister Abteilung A vs Abteilung B',
      'Kaufleute und Gesellschaften werden im Handelsregister eingetragen.',
      'Unterscheiden Sie Abteilung A (HRA) und Abteilung B (HRB) bezüglich der eingetragenen Rechtsformen und erläutern Sie den Unterschied zwischen deklaratorischer und konstitutiver Wirkung.',
      8,
      'Abteilung A (HRA): Verzeichnet Einzelkaufleute (e.K.) und Personengesellschaften (OHG, KG). (2 Pkt.)\n'
      'Abteilung B (HRB): Verzeichnet Kapitalgesellschaften (GmbH, AG, KGaA). (2 Pkt.)\n'
      'Deklaratorische Wirkung: Rechtswirkung ist bereits vor der Eintragung eingetreten; die Eintragung stellt den bestehenden Rechtszustand lediglich öffentlich klar (z. B. Erteilung einer Prokura). (2 Pkt.)\n'
      'Konstitutive Wirkung: Die Rechtswirkung entsteht erst mit und durch die Eintragung im Handelsregister (rechtsbegründend, z. B. Entstehung einer GmbH als juristische Person). (2 Pkt.)')

add_q('wiso_010', 'WiSo', 'WiSo', 'Kaufvertragsstörungen Sachmangel und Nacherfüllung',
      'Ein Unternehmen bestellt 10 neue Laptops. Bei Lieferung stellt sich heraus, dass 3 Displays tiefe Kratzer aufweisen.',
      'Nennen Sie die vorrangigen Rechte des Käufers bei Vorliegen eines Sachmangels (§ 437, § 439 BGB) und beschreiben Sie, unter welchen Bedingungen die nachrangigen Rechte (Rücktritt, Minderung) greifen.',
      8,
      'Vorrangiges Recht (Nacherfüllung nach § 439 BGB): Der Käufer kann nach seiner Wahl die Beseitigung des Mangels (Nachbesserung / Reparatur) oder die Lieferung einer mangelfreien Sache (Nachlieferung / Ersatz) verlangen. Dem Verkäufer muss dazu eine angemessene Frist eingeräumt werden. (4 Pkt.)\n'
      'Nachrangige Rechte: Schlägt die Nacherfüllung fehl (nach dem 2. erfolglosen Nachbesserungsversuch) oder verweigert der Verkäufer diese endgültig, kann der Käufer vom Kaufvertrag zurücktreten (Rückabwicklung Zug um Zug), den Kaufpreis mindern und ggf. Schadensersatz verlangen. (4 Pkt.)')

add_q('wiso_011', 'WiSo', 'WiSo', 'Marktformen Polypol, Oligopol und Monopol',
      'Auf Märkten treffen Angebot und Nachfrage bei unterschiedlichen Marktstrukturen aufeinander.',
      'Definieren Sie die Marktformen Monopol, Oligopol und Polypol aus Sicht der Anbieter und nennen Sie jeweils ein konkretes Marktbeispiel.',
      6,
      'Monopol (Angebotsmonopol): Genau ein Anbieter steht vielen Nachfragern gegenüber. Hohe Preissetzungsmacht. Beispiel: Deutsche Bahn im Schienenfernverkehr (historisch) oder staatliches Lotteriemonopol. (2 Pkt.)\n'
      'Oligopol (Angebotsoligopol): Wenige Anbieter stehen vielen Nachfragern gegenüber. Gefahr von Preisabsprachen oder Preiskämpfen. Beispiel: Deutscher Mobilfunknetz-Markt (Telekom, Vodafone, Telefónica, 1&1) oder Mineralölkonzerne. (2 Pkt.)\n'
      'Polypol: Sehr viele Anbieter stehen sehr vielen Nachfragern gegenüber. Vollständige Konkurrenz, Preisbildung über den Gleichgewichtspreis. Beispiel: Gebrauchtwagenmarkt, Wohnungsmarkt, Gastronomie. (2 Pkt.)')

add_q('wiso_012', 'WiSo', 'WiSo', 'Konjunkturphasen Zyklus',
      'Die volkswirtschaftliche Entwicklung verläuft in zyklischen Schwankungen.',
      'Nennen Sie die vier klassischen Phasen des Konjunkturzyklus in richtiger Reihenfolge und beschreiben Sie zwei typische volkswirtschaftliche Merkmale der Hochkonjunktur (Boom).',
      6,
      'Vier Phasen:\n'
      '1. Aufschwung (Expansion)\n'
      '2. Hochkonjunktur (Boom)\n'
      '3. Abschwung (Rezession)\n'
      '4. Tiefstand (Depression). (3 Pkt.)\n'
      'Zwei Merkmale des Booms: 1. Nahezu Vollbeschäftigung / akuter Fachkräftemangel; 2. Volle Kapazitätsauslastung der Unternehmen bei steigenden Zinsen, Löhnen und Inflationsraten. (3 Pkt.)')

add_q('wiso_013', 'WiSo', 'WiSo', 'Geldpolitik der EZB Leitzins und Inflation',
      'Zur Bekämpfung einer anhaltend hohen Inflationsrate beschließt der Rat der Europäischen Zentralbank (EZB) eine Erhöhung der Leitzinsen.',
      'Erläutern Sie den Wirkungsmechanismus einer Leitzinserhöhung auf die Kreditvergabe von Geschäftsbanken, die Investitionsbereitschaft und die Preisentwicklung.',
      6,
      'Wirkungsmechanismus:\n'
      '1. Refinanzierungskosten steigen: Geschäftsbanken müssen für EZB-Zentralbankgeld höhere Zinsen zahlen und geben diese in Form höherer Kreditzinsen an Unternehmen und Verbraucher weiter. (2 Pkt.)\n'
      '2. Dämpfung der Nachfrage: Teurere Kredite führen dazu, dass Unternehmen Investitionen verschieben und private Haushalte weniger konsumieren, während Sparen attraktiver wird. (2 Pkt.)\n'
      '3. Inflationsrückgang: Die gesunkene Gesamtnachfrage reduziert den Druck auf die Güterpreise, sodass sich der Preisanstieg verlangsamt (Rückkehr zum 2%-Inflationsziel). (2 Pkt.)')

add_q('wiso_014', 'WiSo', 'WiSo', 'Kaufmännisches Mahnverfahren Zahlungsverzug',
      'Ein Kunde zahlt eine fällige Rechnung über 3.500 EUR trotz Fälligkeitsdatum nicht.',
      'Erklären Sie, wann ein Schuldner nach § 286 BGB auch ohne gesonderte Mahnung automatisch in Verzug gerät, und beschreiben Sie den Ablauf des gerichtlichen Mahnverfahrens.',
      8,
      'Automatischer Verzug nach § 286 BGB:\n'
      '1. Wenn für die Leistung eine Zeit nach dem Kalender bestimmt ist (z. B. \"zahlbar bis zum 15.10.\"). (2 Pkt.)\n'
      '2. Spätestens 30 Tage nach Fälligkeit und Zugang einer Rechnung (bei Verbrauchern nur mit entsprechendem Hinweis auf der Rechnung). (2 Pkt.)\n'
      'Gerichtliches Mahnverfahren:\n'
      '1. Gläubiger beantragt Mahnbescheid beim zentralen Mahngericht (keine materielle Rechtsprüfung). (1,5 Pkt.)\n'
      '2. Das Gericht stellt den Mahnbescheid zu; der Schuldner hat 2 Wochen Widerspruchsfrist. (1 Pkt.)\n'
      '3. Erfolgt kein Widerspruch, beantragt der Gläubiger den Vollstreckungsbescheid (vollstreckbarer Titel für Gerichtsvollzieher). (1,5 Pkt.)')

add_q('wiso_015', 'WiSo', 'WiSo', 'Mutterschutz und Elternzeit',
      'Eine Mitarbeiterin teilt ihrer Abteilungsleitung mit, dass sie schwanger ist.',
      'Nennen Sie die gesetzlichen Mutterschutzfristen vor und nach der Entbindung nach dem Mutterschutzgesetz (MuSchG) und erklären Sie die Kündigungsschutzregelung während Schwangerschaft und Elternzeit.',
      6,
      'Mutterschutzfristen: 6 Wochen vor der Entbindung (Schwangere darf auf eigenen Wunsch arbeiten) und 8 Wochen nach der Entbindung (absolutes Beschäftigungsverbot; 12 Wochen bei Früh- oder Mehrlingsgeburten). (3 Pkt.)\n'
      'Kündigungsschutz: Während der gesamten Schwangerschaft bis 4 Monate nach der Entbindung sowie während der Elternzeit besteht nach § 17 MuSchG bzw. § 18 BEEG ein striktes Kündigungsverbot. Kündigungen sind ausnahmslos unzulässig (Ausnahmen bedürfen der vorherigen behördlichen Genehmigung). (3 Pkt.)')

add_q('wiso_016', 'WiSo', 'WiSo', 'Jugendarbeitsschutzgesetz (JArbSchG)',
      'Ein 17-jähriger Auszubildender soll an einem Samstag 9 Stunden lang Überstunden in der Serverwartung leisten.',
      'Prüfen Sie die Zulässigkeit dieser Maßnahme anhand von Arbeitszeit und Samstagsruhe nach dem JArbSchG.',
      6,
      'Tägliche Höchstarbeitszeit (§ 8 JArbSchG): Jugendliche dürfen maximal 8 Stunden täglich und 40 Stunden wöchentlich beschäftigt werden (eine 9-Stunden-Schicht ist unzulässig). (3 Pkt.)\n'
      'Samstagsruhe (§ 16 JArbSchG): An Samstagen dürfen Jugendliche grundsätzlich nicht beschäftigt werden. Zulässige Ausnahmen (z. B. Krankenhäuser, Gastronomie) treffen auf reguläre IT-Bürotätigkeiten nicht zu. Die Anweisung ist somit doppelt rechtswidrig. (3 Pkt.)')

# --- ZUSÄTZLICHE AUFGABEN ZUR VOLLSTÄNDIGEN ABDECKUNG (150-FRAGEN-POOL) ---

# AP1 LF 1
add_q('ap1_lf1_009', 'AP1', 'LF 1', 'Make-or-Buy Entscheidung',
      'Ein Unternehmen überlegt, einen Helpdesk intern mit eigenen Mitarbeitern zu betreiben (Fixkosten 60.000 EUR/Jahr, variable Kosten 5 EUR pro Ticket) oder an einen externen Dienstleister zu vergeben (25 EUR pro Ticket ohne Fixkosten).',
      'Berechnen Sie die kritische Ticketmenge (Break-Even-Point), ab der der Eigenbetrieb wirtschaftlicher ist, und nennen Sie zwei qualitative Entscheidungskriterien.',
      8,
      'Break-Even-Berechnung: K_eigen = K_fremd -> 60.000 + 5 * x = 25 * x -> 60.000 = 20 * x -> x = 3.000 Tickets pro Jahr. Ab dem 3.001. Ticket ist der Eigenbetrieb kostengünstiger. (4 Pkt.)\n'
      'Qualitative Kriterien: 1. Know-how-Aufbau und Datensicherheit im eigenen Haus; 2. Qualitätskontrolle und Reaktionszeit; 3. Abhängigkeit vom externen Dienstleister (Vendor Lock-in). (4 Pkt.)',
      qtype='calc')

add_q('ap1_lf1_010', 'AP1', 'LF 1', 'Qualitätsmanagement PDCA-Zyklus (ISO 9001)',
      'Zur kontinuierlichen Verbesserung von IT-Dienstleistungen wird der PDCA-Zyklus (Deming-Kreis) nach DIN EN ISO 9001 angewendet.',
      'Benennen und erläutern Sie die vier Phasen des PDCA-Zyklus anhand eines Incident-Management-Prozesses.',
      8,
      '1. Plan (Planen): Analyse der aktuellen Störungsbeseitigung, Definition von Zielen und Festlegen von Maßnahmen (z. B. Einführung von Standardarbeitsanweisungen SOPs). (2 Pkt.)\n'
      '2. Do (Umsetzen): Durchführung und Schulung der Maßnahmen im Helpdesk auf operativer Ebene. (2 Pkt.)\n'
      '3. Check (Überprüfen): Messung der Kennzahlen (z. B. First-Time-Fix-Rate, durchschnittliche Ticket-Lösungszeit) und Soll-Ist-Vergleich. (2 Pkt.)\n'
      '4. Act (Handeln / Anpassen): Bei Zielabweichungen Korrekturmaßnahmen einleiten, erfolgreiche Prozesse als neuen Standard im Unternehmen verankern. (2 Pkt.)')

# AP1 LF 2
add_q('ap1_lf2_013', 'AP1', 'LF 2', 'Green IT & Umweltzeichen Blauer Engel',
      'Für eine öffentliche Ausschreibung von 200 Büro-PCs fordert der Auftraggeber die Zertifizierung nach dem Umweltzeichen \"Blauer Engel\" (DE-UZ 78).',
      'Nennen Sie vier ökologische und ressourcenschonende Anforderungen, die Geräte für dieses Umweltzeichen erfüllen müssen.',
      8,
      '1. Hohe Energieeffizienz des Netzteils und geringer Stromverbrauch im Standby-/Ruhezustand. (2 Pkt.)\n'
      '2. Reparierbarkeit und Upgradefähigkeit (Verwendung von Standardkomponenten, zerstörungsfreie Demontierbarkeit mit Standardwerkzeug). (2 Pkt.)\n'
      '3. Vermeidung gefährlicher Stoffe (z. B. Verzicht auf halogenierte Flammschutzmittel in Gehäusen und Leiterplatten). (2 Pkt.)\n'
      '4. Verfügbarkeit von Ersatzteilen und Software-Updates für mindestens 5 Jahre nach Produktionseinstellung. (2 Pkt.)')

add_q('ap1_lf2_014', 'AP1', 'LF 2', 'Display-Technologien IPS vs OLED vs VA',
      'Für die Beschaffung von 50 Arbeitsplatzmonitoren werden Panels verglichen.',
      'Vergleichen Sie IPS- und OLED-Panels bezüglich Blickwinkelstabilität, Kontrast/Schwarzwert, Energieverbrauch bei hellen Inhalten und Reaktionszeit.',
      8,
      'Blickwinkelstabilität: Beide sehr gut; IPS behält Farben bis fast 178 Grad naturgetreu bei, OLED hat nahezu keinen Blickwinkelverlust. (2 Pkt.)\n'
      'Kontrast/Schwarzwert: OLED bietet echtes Schwarz und unendlichen Kontrast, da selbstleuchtende Pixel komplett abgeschaltet werden; IPS benötigt Hintergrundbeleuchtung (Backlight), Schwarz wirkt leicht gräulich. (2 Pkt.)\n'
      'Energieverbrauch: IPS verbraucht konstant Strom unabhängig vom Bildschirminhalt; OLED verbraucht bei großflächig weißen Dokumenten (Office/Word) signifikant mehr Strom als IPS. (2 Pkt.)\n'
      'Burn-In-Risiko: IPS hat kein Burn-In; bei OLED besteht bei statischen Office-Elementen (Taskleiste, Fensterrahmen) im Dauerbetrieb ein Restrisiko für Pixeldegradation. (2 Pkt.)')

add_q('ap1_lf2_015', 'AP1', 'LF 2', 'Bildschirmbrille Kostenübernahme',
      'Ein Mitarbeiter klagt nach Umstellung auf Bildschirmarbeit über Kopfschmerzen und brennende Augen. Ein Augenarzt verordnet eine spezielle Bildschirmarbeitsplatzbrille.',
      'Beurteilen Sie anhand von § 6 ArbStättV und DGUV Information 250-008, unter welchen Voraussetzungen der Arbeitgeber die Kosten für die Brille übernehmen muss.',
      6,
      '1. Pflicht zur arbeitsmedizinischen Vorsorge: Der Arbeitgeber muss Mitarbeitern an Bildschirmarbeitsplätzen eine regelmäßige Augenuntersuchung ermöglichen. (2 Pkt.)\n'
      '2. Medizinische Notwendigkeit: Ergibt die Untersuchung, dass normale Sehhilfen (z. B. Alltagsbrillen, Gleitsichtbrillen) für die spezielle Arbeitsdistanz (50-70 cm) nicht ausreichen, muss der Arbeitgeber eine Bildschirmarbeitsplatzbrille bereitstellen. (2 Pkt.)\n'
      '3. Kostenübernahme: Der Arbeitgeber trägt die Kosten im angemessenen, für den Arbeitszweck notwendigen Rahmen voll (§ 6 Abs. 2 ArbStättV). (2 Pkt.)')

# AP1 LF 3
add_q('ap1_lf3_016', 'AP1', 'LF 3', 'IPv6 SLAAC vs DHCPv6',
      'In einem neu eingerichteten IPv6-Netzwerk sollen Clients ihre IP-Adressen automatisch beziehen.',
      'Vergleichen Sie SLAAC (Stateless Address Autoconfiguration) und Stateful DHCPv6 bezüglich Adressvergabe, Router Advertisements und zentraler Protokollierung.',
      8,
      'SLAAC: Client empfängt vom Router per ICMPv6 Router Advertisement (RA) das 64-Bit-Netzwerkpräfix. Den 64-Bit-Interface Identifier generiert der Client selbst (entweder via EUI-64 aus der MAC-Adresse oder zufällig via Privacy Extensions RFC 4941). Keine zentrale Adressdatenbank. (4 Pkt.)\n'
      'Stateful DHCPv6: Funktioniert wie traditionelles DHCP: Ein DHCPv6-Server verwaltet einen definierten Adresspool, vergibt spezifische Adressen an Clients und protokolliert diese in einer Lease-Datenbank (zentrale Kontrolle und Auditierbarkeit). (4 Pkt.)')

add_q('ap1_lf3_017', 'AP1', 'LF 3', 'MTU, MSS und Path MTU Discovery',
      'Nach der Einrichtung eines VPN-Tunnels können Clients zwar kleine Webseiten öffnen, der Download großer Dateien bricht jedoch mit Timeouts ab.',
      'Erklären Sie den Zusammenhang zwischen Ethernet-MTU (Maximum Transmission Unit), TCP-MSS (Maximum Segment Size), VPN-Overhead und Path MTU Discovery (PMTUD).',
      8,
      'Standard-MTU: Im Ethernet beträgt die MTU maximal 1500 Byte (inkl. 20 Byte IP-Header + 20 Byte TCP-Header -> MSS = 1460 Byte). (2 Pkt.)\n'
      'VPN-Overhead: Ein VPN-Tunnel (z. B. IPsec/ESP) fügt zusätzliche Header und Padding hinzu (ca. 40-70 Byte). Ein 1500-Byte-Paket überschreitet nun die physische Leitungs-MTU. (2 Pkt.)\n'
      'PMTUD & DF-Bit: Pakete mit gesetztem \"Don\'t Fragment\"-Bit (DF) werden vom Router verworfen, wenn sie größer als die MTU des Zwischenlinks sind. Der Router sendet ein ICMP-Paket \"Fragmentation Needed\" zurück. (2 Pkt.)\n'
      'Lösung (Black Hole Vermeidung): Werden ICMP-Nachrichten durch Firewalls blockiert, scheitert PMTUD. Abhilfe: TCP MSS Clamping auf der Firewall (MSS künstlich auf z. B. 1360 Byte reduzieren). (2 Pkt.)')

add_q('ap1_lf3_018', 'AP1', 'LF 3', 'WLAN WPA3-Sicherheit & SAE Handshake',
      'Die WLAN-Infrastruktur soll von WPA2-Personal (PSK) auf WPA3-Personal migriert werden.',
      'Erläutern Sie, warum WPA2 für Offline-Wörterbuchangriffe anfällig ist und wie der SAE-Handshake (Simultaneous Authentication of Equals / Dragonfly) in WPA3 diesen Angriff unmöglich macht.',
      8,
      'Schwachstelle WPA2: Beim klassischen 4-Wege-Handshake kann ein Angreifer die Handshake-Frames mitschneiden (Sniffing) und anschließend offline auf Hochleistungs-GPUs Milliarden Passwörter gegen den Hash testen (Dictionary Attack), ohne weitere Verbindung zum AP. (4 Pkt.)\n'
      'WPA3 / SAE-Verfahren: Verwendet den Dragonfly-Schlüsselaustausch (Diffie-Hellman-Variante auf elliptischen Kurven). Das Passwort wird direkt in die Kurvenberechnung einbezogen. Ein Angreifer kann bei jedem Fehlversuch nur genau ein einziges Passwort online verifizieren; Offline-Wörterbuchangriffe auf mitgeschnittene Pakete sind mathematisch unmöglich (Forward Secrecy). (4 Pkt.)')

add_q('ap1_lf3_019', 'AP1', 'LF 3', 'DNSSEC Funktionsweise',
      'Zur Abwehr von DNS-Spoofing und Cache Poisoning wird DNSSEC auf den Nameservern implementiert.',
      'Erläutern Sie, wie DNSSEC die Authentizität und Integrität von DNS-Antworten sicherstellt und welche Aufgaben die Records RRSIG und DNSKEY haben.',
      8,
      'Funktionsweise: DNSSEC nutzt asymmetrische Kryptografie zur hierarchischen digitalen Signatur von DNS-Zonendaten. Clients können über eine lückenlose Vertrauenskette (Chain of Trust) von der DNS-Root-Zone (. ) über die TLD (z. B. .de) bis zur Domäne prüfen, ob die Antwort unverfälscht vom autoritativen Server stammt. (4 Pkt.)\n'
      'DNSKEY: Enthält den öffentlichen Schlüssel der Zone zur Verifikation von Signaturen. (2 Pkt.)\n'
      'RRSIG (Resource Record Signature): Enthält die kryptografische Signatur über ein konkretes Resource Record Set (RRSet, z. B. A- oder MX-Records). (2 Pkt.)')

# AP1 LF 4
add_q('ap1_lf4_015', 'AP1', 'LF 4', 'DSGVO Art. 9 Besondere Kategorien von Daten',
      'Ein Softwarehaus entwickelt eine Mitarbeiter-App, in der auch Arbeitsunfähigkeitsbescheinigungen (Krankmeldungen) und Religionszugehörigkeiten (für Kirchensteuer) gespeichert werden.',
      'Definieren Sie \"besondere Kategorien personenbezogener Daten\" nach Art. 9 DSGVO und nennen Sie drei erhöhte Schutzanforderungen, die bei deren Verarbeitung zu beachten sind.',
      8,
      'Definition (Art. 9 Abs. 1 DSGVO): Hochsensible Daten, aus denen rassische und ethnische Herkunft, politische Meinungen, religiöse oder weltanschauliche Überzeugungen, Gewerkschaftszugehörigkeit, genetische Daten, biometrische Daten zur Identifizierung oder Gesundheitsdaten und Daten zum Sexualleben hervorgehen. Verarbeitung ist grundsätzlich untersagt, außer es greift ein Ausnahmetatbestand (z. B. Art. 9 Abs. 2 b für Arbeitsrecht). (4 Pkt.)\n'
      'Drei Schutzanforderungen:\n'
      '1. Zwingende Durchführung einer Datenschutz-Folgenabschätzung (DSFA nach Art. 35 DSGVO). (1,5 Pkt.)\n'
      '2. Strikte Verschlüsselung at-rest (Datenbank) und in-transit (TLS 1.3). (1,5 Pkt.)\n'
      '3. Extrem restriktives Berechtigungs- und Rollenkonzept mit detaillierter Protokollierung aller Lese- und Schreibzugriffe. (1 Pkt.)')

add_q('ap1_lf4_016', 'AP1', 'LF 4', 'Firewall DMZ-Konzepte',
      'Ein Webshop und ein Mailserver sollen so betrieben werden, dass Kunden aus dem Internet Zugriff haben, ohne dass das interne Firmennetzwerk gefährdet wird.',
      'Beschreiben Sie das Konzept einer Demilitarisierten Zone (DMZ) und vergleichen Sie eine Single-Firewall-DMZ mit einer mehrstufigen Dual-Firewall-DMZ (Screened Subnet).',
      8,
      'DMZ-Konzept: Ein separates, isoliertes Netzwerksegment zwischen dem unsicheren Internet und dem schützenswerten internen LAN. Öffentliche Server (Web, Mail, Proxy) stehen in der DMZ. Einbruch in die DMZ gewährt keinen direkten Zugriff auf das LAN. (4 Pkt.)\n'
      'Single-Firewall (Three-Homed): Eine Firewall mit 3 Interfaces (Internet, DMZ, LAN). Kostengünstig, aber Single Point of Failure (Wird die Firewall kompromittiert, ist das gesamte LAN offen). (2 Pkt.)\n'
      'Dual-Firewall (Screened Subnet): Eine äußere und eine innere Firewall unterschiedlicher Hersteller (Heterogenität). Selbst bei Ausnutzung einer Zero-Day-Lücke in der äußeren Firewall blockiert die innere Firewall den Zugriff ins LAN. (2 Pkt.)')

add_q('ap1_lf4_017', 'AP1', 'LF 4', 'Zero-Trust-Sicherheitsarchitektur',
      'Ein Unternehmen ersetzt sein traditionelles Perimeter-Sicherheitsmodell (\"Burg-und-Graben\") durch eine Zero-Trust-Architektur (NIST SP 800-207).',
      'Erläutern Sie den Leitsatz \"Never trust, always verify\" und nennen Sie drei zentrale Säulen von Zero Trust.',
      6,
      'Leitsatz: Es gibt kein inhärent sicheres Netzwerk mehr; weder externe Zugriffe noch interne Netzwerkpakete aus dem LAN dürfen a priori als vertrauenswürdig eingestuft werden. Jede einzelne Anfrage muss authentifiziert, autorisiert und verschlüsselt werden. (3 Pkt.)\n'
      'Drei Säulen: 1. Identitätsbasierte Zugriffskontrolle (starke MFA, Kontextprüfung wie Standort/Gerätestatus); 2. Mikrosegmentierung (Netze in kleinste Einheiten zerlegen); 3. Prinzip der minimalen Rechtevergabe (Least Privilege & Just-in-Time Access). (3 Pkt.)')

# AP1 LF 5
add_q('ap1_lf5_013', 'AP1', 'LF 5', 'Python Exception Handling & Custom Errors',
      'In einem Python-Skript soll eine Division durchgeführt und Benutzereingaben validiert werden.',
      'Erklären Sie die Funktionsweise von try, except, else und finally in Python und schreiben Sie einen Code-Ausschnitt, der eine Division durch Null sauber abfängt.',
      8,
      'Erklärung:\n'
      '- try: Enthält den fehleranfälligen Codeblock. (1 Pkt.)\n'
      '- except: Fängt spezifische Ausnahmen ab und behandelt sie (z. B. ZeroDivisionError). (1 Pkt.)\n'
      '- else: Wird nur ausgeführt, wenn im try-Block KEIN Fehler aufgetreten ist. (1 Pkt.)\n'
      '- finally: Wird immer ausgeführt, egal ob ein Fehler auftrat oder nicht (z. B. zum Schließen von Dateien/Sockets). (1 Pkt.)\n'
      'Code:\n'
      'try:\n'
      '    ergebnis = a / b\n'
      'except ZeroDivisionError:\n'
      '    print(\"Fehler: Division durch 0 nicht erlaubt!\")\n'
      'else:\n'
      '    print(\"Ergebnis:\", ergebnis)\n'
      'finally:\n'
      '    print(\"Berechnung abgeschlossen.\") (4 Pkt.)')

add_q('ap1_lf5_014', 'AP1', 'LF 5', 'Transformation ERM in Relationales Schema (1:n und n:m)',
      'Ein ER-Modell enthält die Entitäten \"Abteilung\" und \"Mitarbeiter\" (1:n) sowie \"Mitarbeiter\" und \"Projekt\" (n:m).',
      'Beschreiben Sie die formalen Regeln zur Überführung einer 1:n-Beziehung und einer n:m-Beziehung in ein relationales Tabellenschema (Primär-/Fremdschlüssel-Platzierung).',
      8,
      'Überführung 1:n (1 Abteilung hat n Mitarbeiter):\n'
      'Der Primärschlüssel der 1-Seite (abteilung_id) wird als Fremdschlüssel (FK) in die Relation der n-Seite (Mitarbeiter) aufgenommen. Eine eigene Zwischentabelle ist nicht erforderlich. (4 Pkt.)\n'
      'Überführung n:m (Mitarbeiter arbeitet in n Projekten):\n'
      'Es wird zwingend eine eigenständige Verknüpfungstabelle (z. B. mitarbeiter_projekt) angelegt. Diese enthält die Primärschlüssel beider beteiligter Tabellen (mitarbeiter_id und projekt_id) als Fremdschlüssel. Beide Fremdschlüssel bilden gemeinsam den zusammengesetzten Primärschlüssel der Zwischentabelle. (4 Pkt.)')

add_q('ap1_lf5_015', 'AP1', 'LF 5', 'Datenvalidierung & Konsistenzprüfung im Erfassungsdialog',
      'In einer Eingabemaske für Kundenstammdaten sollen fehlerhafte Eingaben frühzeitig abgefangen werden.',
      'Nennen und erläutern Sie vier Methoden der serverseitigen bzw. anwendungsseitigen Datenvalidierung (z. B. Typ-, Wertebereichs-, Plausibilitäts- und Pflichtfeldprüfung) anhand konkreter Beispiele.',
      8,
      '1. Pflichtfeldprüfung (Nullwertprüfung): Stellt sicher, dass zwingend notwendige Daten (z. B. Nachname, E-Mail) nicht leer übermittelt werden. (2 Pkt.)\n'
      '2. Datentypprüfung: Überprüft, ob der eingegebene Wert dem erwarteten Datentyp entspricht (z. B. Geburtstag als valides Datum YYYY-MM-DD, Kundennummer als Ganzzahl). (2 Pkt.)\n'
      '3. Wertebereichsprüfung (Range Check): Kontrolliert, ob ein numerischer Wert innerhalb zulässiger Grenzwerte liegt (z. B. Alter zwischen 18 und 120 Jahren). (2 Pkt.)\n'
      '4. Format- und Plausibilitätsprüfung: Prüfung auf bestimmte Muster mittels Regex (z. B. gültige E-Mail-Syntax @..., deutsche Postleitzahl genau 5 Ziffern) oder semantische Zusammenhänge (z. B. Vertragsende darf nicht vor Vertragsbeginn liegen). (2 Pkt.)')


# AP1 LF 6 & 7
add_q('ap1_lf6_005', 'AP1', 'LF 6', 'Feldbussysteme Modbus RTU vs Modbus TCP',
      'In einer Gebäudeleittechnik werden Energiezähler und Klimageräte über Modbus an eine Steuerung angebunden.',
      'Vergleichen Sie Modbus RTU und Modbus TCP bezüglich Übertragungsmedium, Adressierung und Fehlererkennung.',
      8,
      'Modbus RTU: Physische Zweidrahtleitung RS-485 (differenzielle Spannung). Master-Slave-Prinzip mit Slave-IDs (1 bis 247). Fehlererkennung erfolgt über eine 16-Bit-CRC-Prüfsumme (Cyclic Redundancy Check) am Frame-Ende. (4 Pkt.)\n'
      'Modbus TCP: Basiert auf Standard-Ethernet und TCP/IP (Standard-Port 502). Adressierung erfolgt über reguläre IP-Adressen und Portnummern. Die Fehlererkennung und Flusskontrolle wird vollständig von den darunterliegenden TCP- und Ethernet-Prüfsummen übernommen (kein CRC im Modbus-Header nötig). (4 Pkt.)')

add_q('ap1_lf6_006', 'AP1', 'LF 6', 'Edge Computing vs Cloud Computing',
      'In einer Industrie-4.0-Fertigung erfassen Sensoren 10.000 Messwerte pro Sekunde an einer CNC-Fräse.',
      'Begründen Sie, warum die Auswertung zur Erkennung von Werkzeugbruch über ein Edge-Device direkt an der Maschine und nicht in einer Cloud-Plattform stattfinden muss.',
      6,
      '1. Latenzzeit (Echtzeitfähigkeit): Ein Werkzeugbruch erfordert eine Notabschaltung innerhalb von Millisekunden. Der Roundtrip in eine Cloud über das Internet hat Latenzen von 20-100 ms und ist für Maschinenschutz zu langsam. (2 Pkt.)\n'
      '2. Bandbreitenbedarf: 10.000 Messwerte pro Sekunde würden kontinuierlich Gigabytes an Daten über den Internetanschluss pumpen und unnötige Kosten/Leitungsüberlastung erzeugen. (2 Pkt.)\n'
      '3. Ausfallsicherheit: Die Maschine muss auch bei einem Ausfall der Internetverbindung autark und sicher weiterlaufen. (2 Pkt.)')

add_q('ap1_lf7_004', 'AP1', 'LF 7', 'Digitalmultimeter Messungen & Sicherheit',
      'Ein Techniker überprüft ein Servernetzteil und misst Spannungen an einem Kaltgerätestecker und auf dem Mainboard.',
      'Nennen Sie den Unterschied zwischen einer Spannungs-, Strom- und Durchgangsmessung hinsichtlich der Schaltung des Multimeters (Reihe vs Parallel) und erklären Sie die Messkategorien CAT II vs CAT III.',
      8,
      'Schaltung des Messgeräts:\n'
      '- Spannungsmessung (Volt): Messgerät wird PARALLEL zur Spannungsquelle / zum Verbraucher geschaltet (sehr hoher Innenwiderstand). (2 Pkt.)\n'
      '- Strommessung (Ampere): Der Stromkreis muss aufgetrennt werden; das Multimeter wird IN REIHE geschaltet (sehr niedriger Innenwiderstand). (2 Pkt.)\n'
      '- Durchgangsmessung: Ausschließlich an spannungsfreien Bauteilen! Gerät legt kleine Prüfspannung an und misst Widerstand (Piepton bei < ca. 30 Ohm). (2 Pkt.)\n'
      'CAT-Einstufung (Überspannungskategorien): CAT II gilt für Geräte an normalen Haushaltssteckdosen; CAT III gilt für Installationen in der Gebäudeinfrastruktur (Unterverteiler, Verteilerkästen, USV-Festeinspeisung) mit höheren transienten Überspannungsrisiken. (2 Pkt.)')

add_q('ap1_lf7_005', 'AP1', 'LF 7', 'Oszilloskop Tastkopf-Teilung 10:1',
      'Zur Fehlersuche an einem Datenbus wird ein digitales Speicheroszilloskop mit einem Tastkopf angeschlossen.',
      'Erläutern Sie, warum für Hochfrequenzsignale ein 10:1-Tastkopf einem 1:1-Tastkopf vorzuziehen ist (Kapazitive Last, Signalverfälschung).',
      6,
      'Erklärung: Ein 1:1-Tastkopf besitzt eine relativ hohe Eingangskapazität (ca. 40-100 pF) und geringeren Eingangswiderstand (1 MOhm). Bei schnellen Signalflanken und hohen Frequenzen wirkt diese Kapazität als Tiefpassfilter, belastet die Schaltung und verschleift steile Rechtecksignale. (3 Pkt.)\n'
      '10:1-Tastkopf: Schaltet einen 9-MOhm-Widerstand in Reihe zum 1-MOhm-Eingang des Oszilloskops. Das Signal wird um den Faktor 10 gedämpft, wodurch sich die Eingangskapazität drastisch verringert (auf ca. 10-15 pF) und der Gesamtwiderstand auf 10 MOhm steigt -> Keine Signalverfälschung der Busleitung. (3 Pkt.)')

# AP1 LF 8
add_q('ap1_lf8_005', 'AP1', 'LF 8', 'Webhooks vs Polling Architektur',
      'Ein Ticketsystem soll ein Überwachungs-Dashboard in Echtzeit benachrichtigen, sobald ein Ticket den Status \"KRITISCH\" erhält.',
      'Vergleichen Sie Webhooks und Polling hinsichtlich Netzwerklast, Latenz und Serverressourcen.',
      6,
      'Polling (Pull-Prinzip): Der Client sendet in festen Intervallen (z. B. alle 10 Sekunden) kontinuierlich HTTP-GET-Anfragen an den Server. Erzeugt enorme Netzwerklast und Serverabfragen, selbst wenn sich stundenlang nichts ändert (leere Antworten); Latenz entspricht dem Polling-Intervall. (3 Pkt.)\n'
      'Webhook (Push-Prinzip): Der Client registriert eine Empfänger-URL beim Server. Sobald das definierte Ereignis eintritt, sendet der Server sofort eine HTTP-POST-Anfrage mit dem JSON-Payload an die URL. Minimale Netzwerklast (Traffic nur bei echten Events) und sofortige Benachrichtigung ohne Latenz. (3 Pkt.)')

# AP2 LF 9 & 11 (Teil 1)
add_q('ap2_lf9_011', 'AP2_T1', 'LF 9', 'BGP Path Attributes (AS-Path & Local Preference)',
      'Ein Internet-Knotenpunkt leitet IP-Präfixe über BGP weiter.',
      'Erläutern Sie die Funktionsweise des BGP-Attributs AS-Path zur Loop-Prävention und beschreiben Sie, wie Local Preference zur Beeinflussung des ausgehenden Datenverkehrs genutzt wird.',
      8,
      'AS-Path Loop Prevention: Jeder BGP-Router hängt beim Weiterleiten einer Route seine eigene Autonomous System Number (ASN) an die AS-Path-Liste an. Empfängt ein Router ein Routing-Update, das seine eigene ASN bereits im AS-Path enthält, verwirft er die Route sofort, um Routing-Schleifen im Internet sicher zu verhindern. (4 Pkt.)\n'
      'Local Preference: Ein lokales Attribut (nur innerhalb des eigenen AS gültig). Der Pfad mit dem HÖCHSTEN Local-Preference-Wert wird bevorzugt gewählt. Administratoren können so steuern, über welchen von mehreren Uplink-Providern der gesamte ausgehende Datenverkehr das eigene Netz verlassen soll. (4 Pkt.)')

add_q('ap2_lf9_012', 'AP2_T1', 'LF 9', 'Quality of Service QoS DiffServ und DSCP',
      'Über eine WAN-Verbindung werden gleichzeitig IP-Telefonie (VoIP-Sprachdaten) und große Dateidownloads übertragen. Die Sprachqualität leidet unter Aussetzern (Jitter).',
      'Erläutern Sie, wie Quality of Service (QoS) nach dem Differentiated Services Modell (DiffServ) mittels DSCP-Werten im IP-Header (z. B. Expedited Forwarding EF vs Best Effort) das Problem löst.',
      8,
      'DiffServ-Funktionsweise: Im IPv4-Header (TOS-Byte) bzw. IPv6-Header (Traffic Class) werden 6 Bit als Differentiated Services Code Point (DSCP) verwendet, um Datenpakete in Prioritätsklassen einzuteilen. Switche und Router werten diesen Wert aus und reihen Pakete in getrennte Ausgangswarteschlangen (Queues) ein. (4 Pkt.)\n'
      'Klassen-Zuordnung:\n'
      '- VoIP: Erhält den DSCP-Wert EF (Expedited Forwarding / DSCP 46) mit Prioritätswarteschlange (Priority Queuing), sodass Sprachpakete immer vor allen anderen Daten ohne Wartezeit weitergeleitet werden (minimiert Latenz und Jitter). (2 Pkt.)\n'
      '- Dateidownloads: Werden als Best Effort (DSCP 0) oder Assured Forwarding (AF) klassifiziert und bei Leitungsengpässen gedrosselt. (2 Pkt.)')

add_q('ap2_lf9_013', 'AP2_T1', 'LF 9', 'IPsec NAT-Traversal (NAT-T)',
      'Ein Mitarbeiter verbindet sich aus einem Hotel-WLAN (hinter einem PAT-Router) per IPsec-VPN mit der Firmenzentrale.',
      'Erklären Sie, warum Standard-IPsec mit ESP an PAT-Routern scheitert und wie NAT-Traversal (NAT-T auf UDP Port 4500) das Problem löst.',
      6,
      'Problem: ESP (IP-Protokoll 50) besitzt keine TCP/UDP-Portnummern. Ein handelsüblicher PAT-Router kann eingehende Antwortpakete daher keinem internen Client zuordnen. Zudem bricht jede Modifikation des IP-Headers durch NAT die kryptografische Integritätsprüfung (AH scheitert immer). (3 Pkt.)\n'
      'Lösung NAT-T (RFC 3948): Erkennt beim IKE-Handshake ein NAT-Gateway. Das gesamte ESP-Paket wird in ein reguläres UDP-Paket auf Port 4500 gekapselt (UDP Encapsulation). Der PAT-Router kann nun den UDP-Port manipulieren und übersetzen, während die internen ESP-Verschlüsselungsdaten unberührt bleiben. (3 Pkt.)')

add_q('ap2_lf9_014', 'AP2_T1', 'LF 9', 'VPN-Protokolle WireGuard vs OpenVPN',
      'Für mobile Arbeitsplätze wird ein modernes VPN ausgewählt.',
      'Vergleichen Sie WireGuard und OpenVPN bezüglich Architektur (Kernel- vs User-Space), Code-Komplexität, Krypto-Agilität und Roaming-Fähigkeit.',
      8,
      'Architektur & Performance: WireGuard läuft direkt im Linux-Kernel-Space; OpenVPN läuft im User-Space und muss jedes Paket über TUN/TAP-Treiber kopieren (höherer Kontextwechsel und CPU-Overhead). WireGuard erzielt deutlich höheren Durchsatz. (2 Pkt.)\n'
      'Codebasis: WireGuard hat ca. 4.000 Zeilen Code (einfach auditierbar, minimale Angriffsfläche); OpenVPN hat über 100.000 Zeilen Code. (2 Pkt.)\n'
      'Kryptografie: WireGuard verzichtet bewusst auf Krypto-Agilität und nutzt ein festes, modernes Krypto-Set (ChaCha20, Poly1305, Curve25519); OpenVPN unterstützt OpenSSL mit variablen Chiffren. (2 Pkt.)\n'
      'Roaming: WireGuard bindet Sitzungen an kryptografische Schlüssel und öffentliche Endpunkte; wechselt ein Laptop von WLAN zu LTE, bleibt der Tunnel ohne Neu-Handshake sofort aktiv. (2 Pkt.)')

add_q('ap2_lf11_007', 'AP2_T1', 'LF 11', 'ZFS Dateisystem Copy-on-Write & Prüfsummen',
      'Ein Enterprise-Speicherserver wird unter TrueNAS mit dem Dateisystem ZFS aufgesetzt.',
      'Erläutern Sie die Funktionsweise von Copy-on-Write (CoW) in ZFS und beschreiben Sie, wie ZFS \"Silent Data Corruption\" (Bit-Rot) mithilfe von Prüfsummen und Scrubbing erkennt und repariert.',
      8,
      'Copy-on-Write (CoW): ZFS überschreibt geänderte Datenblöcke niemals an derselben Stelle. Stattdessen werden veränderte Daten in neue, freie Blöcke geschrieben. Erst nach erfolgreichem Schreiben wird der Metadatenzeiger im Merkle-Tree atomar auf den neuen Block umgebogen. Verhindert Dateisystem-Inkonsistenzen bei Stromausfall komplett (kein fsck nötig). (4 Pkt.)\n'
      'Bit-Rot Schutz: ZFS speichert für jeden Datenblock eine kryptografische 256-Bit-Prüfsumme in dessen übergeordnetem Metadaten-Zeiger. Bei jedem Lesevorgang wird die Prüfsumme neu berechnet. Stimmt sie nicht überein, liest ZFS automatisch die korrekten Daten aus der RAID-Z-Parität oder dem Spiegel und repariert den defekten Block auf der Festplatte (Self-Healing). Ein regelmäßiger \"Scrub\" prüft alle Daten im Hintergrund präventiv. (4 Pkt.)')

add_q('ap2_lf11_008', 'AP2_T1', 'LF 11', 'LTO-Bandtechnologie und WORM-Speicher',
      'Zur Erfüllung gesetzlicher Revisionsanforderungen (GoBD) müssen Buchhaltungsunterlagen unveränderbar auf LTO-Tape archiviert werden.',
      'Definieren Sie das WORM-Prinzip (Write Once, Read Many) und nennen Sie zwei technische Vorteile von Magnetbändern gegenüber Festplatten zur Langzeitarchivierung.',
      6,
      'WORM-Prinzip: Daten können genau einmal auf das Bandlaufwerk geschrieben werden; jegliches nachträgliches Überschreiben, Verändern oder Löschen der Daten auf dem Band ist hardware- oder firmwareseitig dauerhaft gesperrt. (2 Pkt.)\n'
      'Zwei Vorteile von LTO-Tapes:\n'
      '1. Haltbarkeit und Zuverlässigkeit: Lagerfähigkeit von bis zu 30 Jahren unter Standardbedingungen ohne Stromzufuhr. (2 Pkt.)\n'
      '2. Perfekter Air-Gap und Kosteneffizienz: Kassetten können aus der Library entnommen und im Safe gelagert werden (100% Ransomware-Schutz) bei unschlagbar geringen Terabyte-Preisen für kalte Daten. (2 Pkt.)')

add_q('ap2_lf11_009', 'AP2_T1', 'LF 11', 'Synchrone vs Asynchrone Storage-Replikation',
      'Zwei Brandabschnitte eines Rechenzentrums im Abstand von 15 Kilometern sollen gespiegelt werden.',
      'Vergleichen Sie synchrone und asynchrone Speicherreplikation hinsichtlich Bestätigung an das Betriebssystem, Latenzabhängigkeit und RPO.',
      8,
      'Synchrone Replikation: Ein Schreibbefehl wird der Anwendung erst dann als erfolgreich quittiert (Write Acknowledged), wenn die Daten sowohl auf dem lokalen als auch auf dem entfernten Storage-System fehlerfrei im Cache/Platte geschrieben wurden. RPO = 0 (garantiert kein Datenverlust). Erfordert extrem geringe Roundtrip-Latenzen (< 5 ms) und teure Dark-Fiber-LWL-Verbindungen; begrenzte Distanz (typisch max. 20-40 km). (4 Pkt.)\n'
      'Asynchrone Replikation: Der Schreibbefehl wird der Anwendung sofort nach dem Schreiben auf das lokale System quittiert. Die Übertragung an den Remotestandort erfolgt zeitverzögert im Hintergrund. Keine Latenzbeeinträchtigung der Anwendung, unbegrenzte Distanzen möglich. RPO > 0 (Daten der letzten Minuten oder Sekunden können bei Totalausfall verloren gehen). (4 Pkt.)')

# AP2 LF 10 & 12 (Teil 2)
add_q('ap2_lf10_007', 'AP2_T2', 'LF 10', 'DHCP Snooping und Dynamic ARP Inspection (DAI)',
      'Zur Härtung der Switch-Ports gegen Man-in-the-Middle-Angriffe werden Sicherheitsfeatures aktiviert.',
      'Beschreiben Sie die Funktionsweise von DHCP Snooping (Trusted vs Untrusted Ports) und erklären Sie, wie Dynamic ARP Inspection (DAI) basierend auf der Snooping-Binding-Database Angriffe abwehrt.',
      8,
      'DHCP Snooping: Teilt Switchports in vertrauenswürdig (Trusted) und unvertrauenswürdig (Untrusted) ein. Ports zu DHCP-Servern werden als Trusted konfiguriert; Ports zu Clients als Untrusted. Sendet ein Client auf einem Untrusted Port DHCP-Server-Antworten (DHCPOFFER/ACK, Rogue DHCP), blockiert der Switch den Port sofort. Der Switch protokolliert zugewiesene IPs, MACs und Ports in der DHCP Snooping Binding Database. (4 Pkt.)\n'
      'Dynamic ARP Inspection (DAI): Verhindert ARP-Spoofing/Poisoning. Der Switch fängt jeden ARP-Reply auf Untrusted Ports ab und vergleicht, ob die Zuordnung von IP- und Quell-MAC-Adresse mit der DHCP Snooping Binding Database übereinstimmt. Weicht die MAC ab (gefälschter ARP-Frame), wird das Paket gedroppt und der Angreifer isoliert. (4 Pkt.)')

add_q('ap2_lf10_008', 'AP2_T2', 'LF 10', 'Linux Systemd Service Unit Konfiguration',
      'Ein Python-Daemon für ein Monitoring-Tool soll unter Linux automatisch beim Booten gestartet und bei Absturz neu gestartet werden.',
      'Beschreiben Sie die drei Hauptabschnitte einer Systemd-Service-Unit ([Unit], [Service], [Install]) und nennen Sie die Direktiven für Ausführungsbefehl, automatischen Neustart und Start-Ziel.',
      8,
      'Abschnitte & Direktiven:\n'
      '1. [Unit]: Metadaten und Abhängigkeiten. Direktive: Description=Mein Monitoring Dienst; After=network.target (Startet erst, wenn Netzwerk bereit ist). (2 Pkt.)\n'
      '2. [Service]: Ausführungskonfiguration. Direktiven: ExecStart=/usr/bin/python3 /opt/monitor/app.py (Startbefehl); Restart=always (Automatischer Neustart bei Crash); RestartSec=5s; User=monitoruser. (4 Pkt.)\n'
      '3. [Install]: Aktivierungsziel für systemctl enable. Direktive: WantedBy=multi-user.target (Dienst startet im regulären Mehrbenutzer-Modus). (2 Pkt.)')

add_q('ap2_lf12_007', 'AP2_T2', 'LF 12', 'Infrastructure as Code (IaC) Terraform vs Skripte',
      'Eine Cloud-Infrastruktur soll reproduzierbar und versionsverwaltet über Terraform bereitgestellt werden.',
      'Unterscheiden Sie den deklarativen Ansatz von Terraform vom imperativen Ansatz von Shell-Skripten und erläutern Sie die Funktion der Terraform State-Datei (terraform.tfstate).',
      8,
      'Deklarativ (Terraform): Der Administrator beschreibt im Code nur den gewünschten SOLL-Zustand (\"Ich möchte 3 VMs und 1 Load Balancer\"). Die Engine ermittelt selbstständig die notwendigen Schritte zur Erreichung des Zustands. (2 Pkt.)\n'
      'Imperativ (Bash/PowerShell-Skripte): Der Administrator muss jeden einzelnen Befehlsschritt (WIE) sequentiell programmieren und Fehlerzustände manuell abfangen. (2 Pkt.)\n'
      'State-Datei (terraform.tfstate): Speichert das genaue Abbild der aktuell tatsächlich in der Cloud existierenden Ressourcen und deren Metadaten (IDs, Attribute). Terraform vergleicht bei Ausführung (terraform plan) den Soll-Code mit der State-Datei und der Realität, um minimale, gezielte Deltas zu berechnen. (4 Pkt.)')

add_q('ap2_lf12_008', 'AP2_T2', 'LF 12', 'Prometheus & Grafana Monitoring-Architektur',
      'In einer Kubernetes-Umgebung wird ein Prometheus-Server zur Metrikerfassung aufgebaut.',
      'Erklären Sie das Pull-Prinzip von Prometheus gegenüber dem Push-Prinzip, erläutern Sie die Aufgabe von Exportern (z. B. Node Exporter) und definieren Sie die Metriktypen Counter und Gauge.',
      8,
      'Pull-Prinzip: Prometheus fragt Ziele (Targets) periodisch selbstständig über HTTP (/metrics-Endpunkt) ab (\"Scraping\"). Der Server hat die Kontrolle über Abfrageintervall und Systemlast. Beim Push-Prinzip senden Clients unkoordiniert Daten an den Server. (3 Pkt.)\n'
      'Exporter: Kleine Agenten/Dienste, die spezifische System- oder Anwendungsdaten (z. B. CPU-Last, RAM, Disk-I/O beim Node Exporter) auslesen und in das Prometheus-Textformat konvertieren. (2 Pkt.)\n'
      'Metriktypen:\n'
      '- Counter: Monoton ansteigender Zähler, der nur erhöht oder bei Systemneustart auf 0 zurückgesetzt wird (z. B. Anzahl empfangener HTTP-Requests, gesendete Bytes). (1,5 Pkt.)\n'
      '- Gauge: Ein Wert, der beliebig steigen oder fallen kann (z. B. aktuelle CPU-Auslastung in Prozent, freier Speicherplatz, Temperatur). (1,5 Pkt.)')

# WiSo Ergänzungen
add_q('wiso_017', 'WiSo', 'WiSo', 'Befristete Arbeitsverträge nach TzBfG',
      'Ein Arbeitgeber möchte einen Softwareentwickler befristet einstellen.',
      'Unterscheiden Sie die kalendermäßige Befristung ohne Sachgrund (§ 14 Abs. 2 TzBfG) von einer Befristung mit sachlichem Grund (§ 14 Abs. 1 TzBfG) hinsichtlich maximaler Dauer und Verlängerungsmöglichkeiten.',
      6,
      'Befristung ohne Sachgrund: Maximal für 2 Jahre zulässig. Innerhalb dieses 2-Jahres-Zeitraums darf der Vertrag maximal 3-mal verlängert werden. Unzulässig, wenn mit demselben Arbeitgeber zuvor bereits ein Arbeitsverhältnis bestand (Vorbeschäftigungsverbot). (3 Pkt.)\n'
      'Befristung mit Sachgrund: Zeitlich und in der Anzahl der Verlängerungen prinzipiell unbegrenzt, solange ein rechtlich anerkannter Sachgrund vorliegt (z. B. Vertretung wegen Elternzeit/Krankheit, vorübergehender betrieblicher Mehrbedarf an Arbeitsleistung/Projekt, Eigenart der Arbeitsleistung). (3 Pkt.)')

add_q('wiso_018', 'WiSo', 'WiSo', 'Entgeltfortzahlung im Krankheitsfall (EntgFG)',
      'Ein Mitarbeiter erkrankt arbeitsunfähig infolge einer Grippe.',
      'Erläutern Sie die gesetzlichen Regelungen zur Entgeltfortzahlung nach dem Entgeltfortzahlungsgesetz (EntgFG) und erklären Sie, welche Leistung der Mitarbeiter nach Ablauf der Fortzahlung von wem erhält.',
      6,
      'Entgeltfortzahlung durch den Arbeitgeber: Der Arbeitgeber zahlt das volle reguläre Gehalt (100 %) für die Dauer von bis zu 6 Wochen (42 Kalendertage) bei unverschuldeter Arbeitsunfähigkeit fort. Voraussetzung: Das Arbeitsverhältnis besteht seit mindestens 4 Wochen ununterbrochen. (3 Pkt.)\n'
      'Anschlussleistung nach 6 Wochen: Ab der 7. Woche zahlt die gesetzliche Krankenkasse Krankengeld (70 % des Bruttoentgelts, maximal 90 % des Nettoentgelts) für dieselbe Krankheit für bis zu 78 Wochen innerhalb von 3 Jahren. (3 Pkt.)')

add_q('wiso_019', 'WiSo', 'WiSo', 'Prokura vs Handlungsvollmacht nach HGB',
      'Der Geschäftsführer eines IT-Systemhauses möchte zwei leitende Mitarbeiter bevollmächtigen.',
      'Vergleichen Sie die Prokura (§§ 48-53 HGB) und die Handlungsvollmacht (§ 54 HGB) bezüglich Erteilung, Umfang der Vertretungsmacht, Handelsregistereintragung und Zeichnungszusatz.',
      8,
      'Erteilung: Prokura kann nur durch den Inhaber/Geschäftsführer ausdrücklich und persönlich erteilt werden; Handlungsvollmacht kann formlos auch durch Prokuristen erteilt werden. (2 Pkt.)\n'
      'Umfang: Prokura ermächtigt zu ALLEN Arten von gerichtlichen und außergerichtlichen Geschäften und Rechtshandlungen, die der Betrieb IRGENDEINES Handelsgewerbes mit sich bringt (Ausnahme: Grundstücke verkaufen/belasten bedarf gesonderter Befugnis). Handlungsvollmacht ermächtigt nur zu Geschäften, die der Betrieb DIESES KONKRETEN Handelsgewerbes gewöhnlich mit sich bringt. (3 Pkt.)\n'
      'Handelsregister: Prokura MUSS zwingend ins Handelsregister eingetragen werden (deklaratorisch); Handlungsvollmacht wird NICHT eingetragen. (1,5 Pkt.)\n'
      'Zeichnung: Prokurist zeichnet mit \"per procura\" / \"ppa. Vorname Nachname\"; Handlungsbevollmächtigter zeichnet mit \"in Vollmacht\" / \"i.V.\" oder \"in Auftrag\" / \"i.A.\". (1,5 Pkt.)')


# ==============================================================================
# FACHINFORMATIKER ANWENDUNGSENTWICKLUNG (FIAE) - AP2 FACHQUALIFIKATIONEN
# ==============================================================================
add_q('fiae_arch_001', 'AP2_T1', 'LF 9 AE', 'Clean Architecture & Schichtenmodell',
      'Für ein E-Commerce-Portal soll eine wartbare und zukunftssichere Softwarearchitektur konzipiert werden.',
      'Erläutern Sie das Prinzip der Schichtenarchitektur (Drei-Schichten-Architektur: Präsentation, Geschäftslogik, Datenzugriff). Erklären Sie die Dependency Inversion Rule (Abhängigkeitsregel) in der Clean Architecture und warum Domänenlogik unabhängig von Datenbanken und Frameworks sein muss.',
      8,
      'Drei-Schichten-Architektur:\n'
      '1. Präsentationsschicht (Presentation Layer / UI): Verantwortlich für Interaktion mit Benutzer/Client (Views, REST-Controller). Nimmt Eingaben entgegen und stellt Ergebnisse dar. (2 Pkt.)\n'
      '2. Geschäftslogikschicht (Business Logic / Domain Layer): Beinhaltet Kernregeln, Berechnungen und Validierungen des Unternehmens. Unabhängig von UI und DB. (2 Pkt.)\n'
      '3. Datenzugriffsschicht (Data Access / Persistence Layer): Verwaltet Datenbankabfragen, ORM, Dateizugriffe und externe APIs. (2 Pkt.)\n\n'
      'Clean Architecture & Dependency Inversion:\n'
      'Die Abhängigkeitsregel besagt, dass Quellcode-Abhängigkeiten immer nur nach innen auf die Domänenlogik zeigen dürfen. Äußere Schichten (DB, Web-Framework, UI) hängen von inneren Schichten (Entities, Use Cases) ab, niemals umgekehrt. Dies geschieht über Interfaces: Die Geschäftslogik definiert Schnittstellen (z. B. IUserRepository), die die äußere Datenschicht implementiert. Vorteil: Datenbanken, UI oder externe APIs können ohne Änderung der Geschäftsregeln ausgetauscht oder getestet werden. (2 Pkt.)')

add_q('fiae_arch_002', 'AP2_T1', 'LF 9 AE', 'Design Patterns Strategy vs Factory Method',
      'In einem Warenwirtschaftssystem sollen unterschiedliche Rabattberechnungen und Versandarten dynamisch zur Laufzeit angewendet werden.',
      'Beschreiben Sie das GoF-Entwurfsmuster "Strategy (Strategie)" anhand von Context, Strategy-Interface und Concrete Strategies. Grenzen Sie es kurz vom Factory Method Pattern ab.',
      8,
      'Strategy Pattern (Verhaltensmuster):\n'
      '- Zweck: Definiert eine Familie von Algorithmen, kapselt jeden einzelnen und macht sie zur Laufzeit austauschbar. (2 Pkt.)\n'
      '- Komponenten:\n'
      '  1. Strategy (Interface): Definiert die gemeinsame Methodensignatur für alle Algorithmen (z. B. calculateDiscount(Order order): double). (2 Pkt.)\n'
      '  2. Concrete Strategies: Konkrete Implementierungen des Algorithmus (z. B. VipCustomerDiscount, SeasonalDiscount, NoDiscount). (2 Pkt.)\n'
      '  3. Context (Kontext): Hält eine Referenz auf ein Strategy-Objekt und delegiert die Ausführung an dieses (z. B. OrderProcessor.setDiscountStrategy(...)). (1 Pkt.)\n'
      '- Abgrenzung zum Factory Method Pattern: Strategy ist ein Verhaltensmuster zur dynamischen Verhaltensänderung bestehender Objekte; Factory Method ist ein Erzeugungsmuster zur instanziierungsunabhängigen Erzeugung von Objekten über abgeleitete Klassen. (1 Pkt.)')

add_q('fiae_arch_003', 'AP2_T1', 'LF 9 AE', 'Design Patterns Observer & Singleton',
      'In einer Messaging-Applikation sollen mehrere Benutzeroberflächen-Komponenten sofort informiert werden, sobald eine neue Chatnachricht eintrifft.',
      'Erläutern Sie das Entwurfsmuster Observer (Beobachter) mit den Rollen Subject (Publisher) und Observer (Subscriber). Erklären Sie zudem das Singleton-Muster und warum es in modernen Softwaresystemen oft als Anti-Pattern angesehen wird.',
      8,
      'Observer Pattern (Publisher/Subscriber):\n'
      '- Subject (Publisher): Verwaltet eine Liste von Abonnenten (Observer). Bietet Methoden zum Anmelden (attach/subscribe), Abmelden (detach/unsubscribe) und Benachrichtigen (notifyObservers()). Bei Zustandsänderung durchläuft notifyObservers() die Liste und ruft update() auf. (3 Pkt.)\n'
      '- Observer (Subscriber): Definiert eine gemeinsame update()-Methode, die vom Subject aufgerufen wird, um über Änderungen informiert zu werden. Lose Kopplung zwischen Sender und Empfängern. (2 Pkt.)\n\n'
      'Singleton Pattern:\n'
      '- Zweck: Stellt sicher, dass von einer Klasse exakt eine einzige Instanz existiert, und bietet einen globalen Zugriffspunkt (privater Konstruktor, statische Instanzvariable, statische getInstance()-Methode). (1,5 Pkt.)\n'
      '- Kritik / Anti-Pattern: Erzeugt enge globale Kopplung, erschwert Unit-Testing und Mocking massiv, verstößt gegen das Single Responsibility Principle und kann in Multi-Threaded-Umgebungen Race Conditions verursachen. Moderner Ersatz: Dependency Injection. (1,5 Pkt.)')

add_q('fiae_algo_001', 'AP2_T2', 'LF 10 AE', 'Algorithmen-Komplexität O-Notation',
      'Für eine stark wachsende Plattform müssen Algorithmen auf ihre Skalierbarkeit und Laufzeitkomplexität hin analysiert werden.',
      'Erklären Sie die Landau-Symbole (O-Notation) zur Abschätzung der Zeitkomplexität. Ordnen Sie folgende Komplexitätsklassen von der effizientesten zur ineffizientesten Laufzeit: O(n log n), O(1), O(n²), O(log n), O(n). Nennen Sie je ein typisches Code- oder Algorithmenbeispiel für O(1), O(log n) und O(n).',
      8,
      'Bedeutung der O-Notation:\n'
      'Beschreibt das asymptotische Wachstumsverhalten des Ressourcenbedarfs (Laufzeit/Speicher) eines Algorithmus in Abhängigkeit von der Eingabegröße n im Worst-Case-Szenario. Konstante Faktoren werden vernachlässigt. (2 Pkt.)\n\n'
      'Reihenfolge nach Effizienz (von schnell/effizient zu langsam/ineffizient):\n'
      '1. O(1) [konstant] < 2. O(log n) [logarithmisch] < 3. O(n) [linear] < 4. O(n log n) [linear-logarithmisch] < 5. O(n²) [quadratisch]. (3 Pkt.)\n\n'
      'Beispiele:\n'
      '- O(1): Direkter Array-Zugriff per Index (z. B. array[5]) oder Abfrage per Schlüssel in einer Hash-Map. (1 Pkt.)\n'
      '- O(log n): Binäre Suche in einem sortierten Array (Halbierungsprinzip). (1 Pkt.)\n'
      '- O(n): Lineare Suche in einer unsortierten Liste oder eine einfache for-Schleife über n Elemente. (1 Pkt.)')

add_q('fiae_algo_002', 'AP2_T2', 'LF 10 AE', 'Sortieralgorithmen Quicksort vs Mergesort',
      'Ein Datenstrom von Millionen Datensätzen soll effizient sortiert werden.',
      'Vergleichen Sie Quicksort und Mergesort nach dem Divide-and-Conquer-Prinzip hinsichtlich Best-Case-, Average-Case- und Worst-Case-Laufzeit, Speicherplatzkomplexität und Stabilität.',
      8,
      'Gemeinsamkeit: Beide nutzen Divide-and-Conquer (Teile-und-Herrsche). (1 Pkt.)\n\n'
      'Quicksort:\n'
      '- Laufzeit: Best-Case O(n log n), Average-Case O(n log n), Worst-Case O(n²) (wenn Pivot-Element extrem ungünstig gewählt, z. B. bereits sortierte Liste). (2 Pkt.)\n'
      '- Speicherkomplexität: O(log n) durch Rekursions-Stack (In-Place-Verfahren, benötigt kein Zusatzarray). (1,5 Pkt.)\n'
      '- Stabilität: In der Regel instabil (gleiche Elemente können ihre relative Reihenfolge ändern). (0,5 Pkt.)\n\n'
      'Mergesort:\n'
      '- Laufzeit: Garantiert O(n log n) in Best-, Average- und Worst-Case! (2 Pkt.)\n'
      '- Speicherkomplexität: O(n), da Hilfsarrays beim Verschmelzen (Merge) benötigt werden. (0,5 Pkt.)\n'
      '- Stabilität: Stabil (relative Reihenfolge gleicher Elemente bleibt erhalten). (0,5 Pkt.)')

add_q('fiae_oop_001', 'AP2_T2', 'LF 10 AE', 'SOLID-Prinzipien der OOP',
      'Ein Software-Projekt leidet unter Spaghetti-Code und mangelnder Erweiterbarkeit.',
      'Benennen und erläutern Sie die 5 SOLID-Prinzipien der objektorientierten Programmierung. Gehen Sie vertieft auf das Single Responsibility Principle (SRP) und das Dependency Inversion Principle (DIP) ein.',
      8,
      'Die 5 SOLID-Prinzipien:\n'
      '1. S - Single Responsibility Principle (SRP): Eine Klasse sollte genau eine einzige Verantwortung (einen einzigen Grund zur Änderung) haben. Beispiel: Eine Klasse User sollte Daten halten, aber nicht selbst E-Mails versenden oder sich in der Datenbank speichern. (2 Pkt.)\n'
      '2. O - Open/Closed Principle (OCP): Software-Einheiten sollten offen für Erweiterung, aber geschlossen für Modifikation sein (z. B. durch Vererbung und Interfaces statt if/else-Ketten). (1,5 Pkt.)\n'
      '3. L - Liskov Substitution Principle (LSP): Subklassen müssen anstelle ihrer Basisklassen eingesetzt werden können, ohne dass das Programm fehlerhaft reagiert. (1,5 Pkt.)\n'
      '4. I - Interface Segregation Principle (ISP): Viele spezialisierte, schlanke Interfaces sind besser als ein riesiges Allzweck-Interface (keine erzwungene Implementierung ungenutzter Methoden). (1,5 Pkt.)\n'
      '5. D - Dependency Inversion Principle (DIP): High-Level-Module dürfen nicht von Low-Level-Modulen abhängen; beide müssen von Abstraktionen (Interfaces) abhängen. Abstraktionen dürfen nicht von Details abhängen. (1,5 Pkt.)')

add_q('fiae_api_001', 'AP2_T2', 'LF 11 AE', 'RESTful API Design & HTTP-Statuscodes',
      'Für eine Smartphone-App wird ein Backend mit REST-Schnittstellen entworfen.',
      'Definieren Sie die 4 zentralen HTTP-Verben (GET, POST, PUT, DELETE) und deren Idempotenz. Nennen und erläutern Sie je zwei typische HTTP-Statuscodes der Kategorien 2xx, 4xx und 5xx.',
      8,
      'HTTP-Verben & Idempotenz (Mehrfache Ausführung führt zum selben Serverzustand):\n'
      '- GET: Ruft Ressourcen ab. Sicher & Idempotent. (1 Pkt.)\n'
      '- POST: Erzeugt eine neue Ressource unter einer Collection. Nicht idempotent (mehrfache Aufrufe erzeugen mehrere Datensätze). (1 Pkt.)\n'
      '- PUT: Ersetzt eine bestehende Ressource vollständig. Idempotent. (1 Pkt.)\n'
      '- DELETE: Löscht eine Ressource. Idempotent. (1 Pkt.)\n\n'
      'HTTP-Statuscodes:\n'
      '- 2xx (Erfolg): 200 OK (Standard-Erfolg), 201 Created (Ressource neu angelegt), 204 No Content (Erfolg ohne Rückgabedaten). (1,5 Pkt.)\n'
      '- 4xx (Client-Fehler): 400 Bad Request (Fehlerhafte Syntax/Validierung), 401 Unauthorized (Nicht authentifiziert), 403 Forbidden (Rechte fehlen), 404 Not Found (Ressource existiert nicht). (1,5 Pkt.)\n'
      '- 5xx (Server-Fehler): 500 Internal Server Error (Unbehandelter Serverfehler), 502 Bad Gateway, 503 Service Unavailable (Überlastung/Wartung). (1 Pkt.)')

add_q('fiae_test_001', 'AP2_T2', 'LF 12 AE', 'Test-Driven Development TDD & Testpyramide',
      'In einem agilen Scrum-Team soll die Softwarequalität durch automatisierte Tests gesichert werden.',
      'Beschreiben Sie den TDD-Zyklus (Red-Green-Refactor). Erläutern Sie die Testpyramide (Unit-Tests, Integrationstests, End-to-End-Tests) und warum Unit-Tests das Fundament bilden.',
      8,
      'TDD-Zyklus (Red-Green-Refactor):\n'
      '1. Red: Einen neuen automatisierten Unit-Test für ein Feature schreiben, bevor Produktionscode existiert. Der Test muss zwingend fehlschlagen (rot). (1,5 Pkt.)\n'
      '2. Green: Minimalen Produktionscode schreiben, der gerade ausreicht, um den Test erfolgreich zu bestehen (grün). (1,5 Pkt.)\n'
      '3. Refactor: Den Code bereinigen (Duplikate entfernen, Lesbarkeit verbessern, Patterns anwenden), während sichergestellt wird, dass alle Tests weiterhin grün bleiben. (1,5 Pkt.)\n\n'
      'Testpyramide:\n'
      '- Basis: Unit-Tests (Komponententests). Testen einzelne Klassen/Methoden isoliert mit Mocks. Schnellste Ausführung (ms), geringste Kosten, höchste Testabdeckung (ca. 70-80 %). (2 Pkt.)\n'
      '- Mitte: Integrationstests. Testen das Zusammenspiel mehrerer Module (z. B. Service mit DB oder API). Längere Laufzeit, mittlere Anzahl. (1 Pkt.)\n'
      '- Spitze: End-to-End (E2E) / UI-Tests. Testen das Gesamtsystem aus Nutzersicht über Browser/Client. Langsam, fehleranfällig (brittle), teuer im Unterhalt, geringste Anzahl. (0,5 Pkt.)')

# ==============================================================================
# FACHINFORMATIKER DATEN- UND PROZESSANALYSE (FIDP) - AP2 FACHQUALIFIKATIONEN
# ==============================================================================
add_q('fidp_proc_001', 'AP2_T1', 'LF 9 DP', 'Prozessanalyse Durchlauf- und Liegezeiten',
      'In einem Logistikunternehmen soll die Auftragsabwicklung von Bestelleingang bis Warenausgang analysiert und optimiert werden.',
      'Definieren Sie Durchlaufzeit, Bearbeitungszeit, Liegezeit und Rüstzeit. Erläutern Sie die Prozess-Zykluseffizienz (Process Cycle Efficiency PCE) und wie Flaschenhälse (Bottlenecks) identifiziert werden.',
      8,
      'Zeitdefinitionen im Prozess:\n'
      '- Durchlaufzeit (DLZ): Die gesamte Zeitspanne vom Start des Prozesses (Bestelleingang) bis zur Fertigstellung (Auslieferung). (2 Pkt.)\n'
      '- Bearbeitungszeit: Die Zeit, in der tatsächlich wertschöpfend am Auftrag gearbeitet wird. (1,5 Pkt.)\n'
      '- Liegezeit / Wartezeit: Unproduktive Zeit, in der ein Auftrag auf Bearbeitung, Transport oder Freigabe wartet (macht oft 80-95 % der DLZ aus!). (1,5 Pkt.)\n'
      '- Rüstzeit: Zeit zur Vorbereitung von Maschinen/Systemen auf den nächsten Auftrag. (1 Pkt.)\n\n'
      'Prozess-Zykluseffizienz (PCE):\n'
      'PCE = (Wertschöpfende Bearbeitungszeit / Gesamte Durchlaufzeit) * 100 %. Zeigt den Grad der Prozessverschwendung. (1 Pkt.)\n'
      'Flaschenhals-Identifikation (Bottleneck): Der Prozessschritt mit der geringsten Kapazität bzw. der längsten Bearbeitungszeit je Einheit, vor dem sich Auftragsstaus bilden. Bestimmt den maximalen Durchsatz des Gesamtsystems. (1 Pkt.)')

add_q('fidp_data_001', 'AP2_T1', 'LF 9 DP', 'Datenqualität nach ISO 8000',
      'Für eine KI-gestützte Kundenanalyse sollen CRM-, ERP- und Webshop-Daten zusammengeführt werden.',
      'Nennen und erläutern Sie 4 wesentliche Dimensionen der Datenqualität nach ISO 8000 / DAMA DMBOK. Beschreiben Sie typische Methoden des Data Cleaning (Datenbereinigung).',
      8,
      'Dimensionen der Datenqualität:\n'
      '1. Vollständigkeit (Completeness): Alle benötigten Datenfelder und Datensätze sind vorhanden (keine unbegründeten NULL-Werte). (1,5 Pkt.)\n'
      '2. Korrektheit / Genauigkeit (Accuracy): Die Daten spiegeln die reale Welt fehlerfrei wider (z. B. korrekte Schreibweise von Namen und Adressen). (1,5 Pkt.)\n'
      '3. Konsistenz (Consistency): Keine widersprüchlichen Daten in verschiedenen Systemen oder Tabellen (z. B. identische Postleitzahl und Ort). (1,5 Pkt.)\n'
      '4. Aktualität (Timeliness): Die Daten repräsentieren den aktuellen Zustand und sind für den Verwendungszweck zeitnah verfügbar. (1,5 Pkt.)\n\n'
      'Methoden des Data Cleaning:\n'
      '- Deduplizierung: Erkennung und Zusammenführung doppelter Datensätze (Fuzzy Matching). (1 Pkt.)\n'
      '- Standardisierung / Normalisierung: Vereinheitlichung von Formaten (z. B. Telefonnummern im E.164-Format, Datumsformate nach ISO 8601). (1 Pkt.)')

add_q('fidp_etl_001', 'AP2_T1', 'LF 10 DP', 'ETL vs ELT Datenpipelines & CDC',
      'Ein Unternehmen baut eine moderne Analytics-Plattform mit Cloud Data Warehouse auf.',
      'Vergleichen Sie das klassische ETL-Verfahren (Extract, Transform, Load) mit dem modernen ELT-Verfahren (Extract, Load, Transform). Erläutern Sie Change Data Capture (CDC) zur inkrementellen Datenübernahme.',
      8,
      'Vergleich ETL vs. ELT:\n'
      '- ETL (Extract, Transform, Load): Daten werden aus Quellsystemen extrahiert, auf einem separaten Transformations-Server bereinigt/aggregiert und erst danach in das Ziel-Data-Warehouse geladen. Vorteil: Nur bereinigte Daten erreichen das DWH, Schutz sensibler Daten vor Laden. Nachteil: Eigener ETL-Server als Flaschenhals. (3 Pkt.)\n'
      '- ELT (Extract, Load, Transform): Rohdaten werden direkt aus den Quellen in das Zielsystem (z. B. Cloud DWH wie Snowflake, BigQuery oder Data Lake) geladen; die Transformation erfolgt dort mit der massiv parallelen Rechenleistung des DWHs. Vorteil: Extrem skalierbar, Rohdaten bleiben für spätere neue Analysen erhalten. (3 Pkt.)\n\n'
      'Change Data Capture (CDC):\n'
      'Verfahren zur Identifikation und Weiterleitung ausschließlich geänderter Daten (Inserts, Updates, Deletes) aus Quell-Datenbanken (z. B. über das Datenbank-Transaktionslog). Verhindert ressourcenfressende tägliche Vollexporte. (2 Pkt.)')

add_q('fidp_dwh_001', 'AP2_T1', 'LF 10 DP', 'Data Warehouse Star-Schema vs Snowflake-Schema',
      'Für das Management-Reporting einer Handelskette wird ein multidimensionales Datenmodell entworfen.',
      'Erklären Sie den Aufbau eines Star-Schemas (Faktentabelle und Dimensionstabellen). Grenzen Sie das Star-Schema vom Snowflake-Schema hinsichtlich Normalisierung und Abfrageperformance ab.',
      8,
      'Aufbau des Star-Schemas:\n'
      '- Faktentabelle: Zentrales Element. Enthält numerische, aggregierbare Messgrößen (Fakten, z. B. Umsatz, Menge, Rabatt) sowie Fremdschlüssel zu allen angebundenen Dimensionen. (2,5 Pkt.)\n'
      '- Dimensionstabellen: Umgeben die Faktentabelle wie Zacken eines Sterns. Enthalten beschreibende Attribute zur Filterung und Gruppierung (z. B. Zeit, Kunde, Filiale, Produkt). Sind im Star-Schema bewusst DENORMALISIERT. (2,5 Pkt.)\n\n'
      'Abgrenzung zum Snowflake-Schema:\n'
      '- Snowflake-Schema: Die Dimensionstabellen werden bis zur 3. Normalform normalisiert (z. B. Produkt -> Produktkategorie -> Hauptgruppe). Vorteil: Geringere Redundanz, Vermeidung von Update-Anomalien. (1,5 Pkt.)\n'
      '- Abfrageperformance: Star-Schema ist bei OLAP-Abfragen deutlich schneller, da weniger relationale JOINs für Berichte nötig sind. In modernen Data Warehouses wird das Star-Schema bevorzugt. (1,5 Pkt.)')

add_q('fidp_stat_001', 'AP2_T2', 'LF 11 DP', 'Statistische Kennzahlen & Hypothesentests',
      'In einer A/B-Testing-Studie soll geprüft werden, ob ein neues Checkout-Design die Conversion Rate signifikant erhöht.',
      'Unterscheiden Sie Mittelwert, Median und Modus. Erläutern Sie Standardabweichung und Varianz. Was bedeuten Nullhypothese (H0), Alternativhypothese (H1) und der p-Wert bei einem Signifikanzniveau von alpha = 0,05?',
      8,
      'Lage- und Streumaße:\n'
      '- Mittelwert: Arithmetischer Durchschnitt. Anfällig für extreme Ausreißer. (1 Pkt.)\n'
      '- Median: Der Wert, der die sortierte Datenreihe genau in zwei Hälften teilt (50 %-Quantil). Robust gegen Ausreißer. (1 Pkt.)\n'
      '- Modus: Der am häufigsten vorkommende Wert in einer Datenmenge. (1 Pkt.)\n'
      '- Varianz: Mittlere quadrierte Abweichung aller Messwerte vom arithmetischen Mittelwert. Standardabweichung ist die Quadratwurzel der Varianz (selbe Einheit wie Ausgangsdaten). (2 Pkt.)\n\n'
      'Hypothesentest:\n'
      '- Nullhypothese (H0): Annahme, dass KEIN Unterschied oder Effekt zwischen Variante A und B existiert. (1 Pkt.)\n'
      '- Alternativhypothese (H1): Die Forschungshypothese, dass ein signifikanter Unterschied besteht. (1 Pkt.)\n'
      '- p-Wert und Signifikanz: Wahrscheinlichkeit, die beobachteten Daten zu erhalten, wenn H0 wahr wäre. Ist p < 0,05, wird H0 verworfen: Das Ergebnis ist statistisch signifikant. (1 Pkt.)')

add_q('fidp_ml_001', 'AP2_T2', 'LF 12 DP', 'Machine Learning Evaluation Confusion Matrix',
      'Ein Machine-Learning-Modell soll betrügerische Kreditkartentransaktionen (Fraud) automatisiert klassifizieren.',
      'Erläutern Sie die 4 Felder einer Confusion Matrix (TP, FP, TN, FN). Definieren Sie die Kennzahlen Precision (Genauigkeit), Recall (Trefferquote/Sensitivität) und F1-Score. Warum ist die reine Accuracy (Genauigkeit) bei unausgeglichenen Datensätzen irreführend?',
      8,
      'Confusion Matrix (Wahrheitsmatrix):\n'
      '- True Positive (TP): Betrug korrekt als Betrug erkannt. (1 Pkt.)\n'
      '- False Positive (FP): Legitime Buchung fälschlicherweise als Betrug markiert (Fehlalarm, Typ-I-Fehler). (1 Pkt.)\n'
      '- True Negative (TN): Legitime Buchung korrekt als legitim eingestuft. (1 Pkt.)\n'
      '- False Negative (FN): Betrug fälschlicherweise übersehen und als legitim deklariert (Typ-II-Fehler, hohes Schadensrisiko!). (1 Pkt.)\n\n'
      'Metriken:\n'
      '- Precision = TP / (TP + FP): Wie viele der als Betrug deklarierten Fälle waren wirklich Betrug? (1 Pkt.)\n'
      '- Recall = TP / (TP + FN): Wie viel Prozent aller tatsächlichen Betrugsfälle hat das Modell aufgespürt? (1 Pkt.)\n'
      '- F1-Score = 2 * (Precision * Recall) / (Precision + Recall): Harmonisches Mittel aus Precision und Recall. (1 Pkt.)\n\n'
      'Accuracy-Problem bei Unbalanced Data: Bei 99,9 % regulären Buchungen erreicht ein primitives Modell, das einfach immer "Legitim" rät, 99,9 % Accuracy, erkennt aber NULL Betrugsfälle! Daher ist Accuracy unbrauchbar. (1 Pkt.)')

# ==============================================================================
# FACHINFORMATIKER DIGITALE VERNETZUNG (FIDV) - AP2 FACHQUALIFIKATIONEN
# ==============================================================================
add_q('fidv_cps_001', 'AP2_T1', 'LF 9 DV', 'Cyber-physische Systeme & RAMI 4.0',
      'In einer Smart Factory werden Fertigungsanlagen mit dem Cloud-Leitsystem vernetzt.',
      'Definieren Sie ein Cyber-physisches System (CPS) und dessen Komponenten. Erläutern Sie das Referenzarchitekturmodell Industrie 4.0 (RAMI 4.0) mit seinen 3 Dimensionen (Schichten, Lebenszyklus/Wertstrom, Hierarchieebenen).',
      8,
      'Cyber-physisches System (CPS):\n'
      'Verbindung von mechanischen und elektronischen Komponenten (Hardware, Sensoren, Aktoren) mit softwarebasierten Steuerungen und Kommunikationsnetzen (Internet/Ethernet). CPS erfassen physikalische Daten, werten sie autonom aus und steuern physische Prozesse über Aktoren in Echtzeit. (3 Pkt.)\n\n'
      'RAMI 4.0 (Dreidimensionales Modell):\n'
      '1. Achse: Schichten (Layers / 6 Ebenen): Asset, Integration, Communication, Information, Functional, Business. Beschreibt IT- und Geschäftsaspekte. (2 Pkt.)\n'
      '2. Achse: Lebenszyklus & Wertstrom (Life Cycle & Value Stream nach IEC 62890): Entwicklung (Typ) bis Produktion/Nutzung (Instanz). (1,5 Pkt.)\n'
      '3. Achse: Hierarchieebenen (nach IEC 62264): Vom Produkt (Product), über Feldgerät (Field Device), Steuerung (Control Device), Station, Arbeitsplatz (Work Center), Unternehmen (Enterprise) bis zur vernetzten Welt (Connected World). (1,5 Pkt.)')

add_q('fidv_bus_001', 'AP2_T1', 'LF 10 DV', 'Industrielle Feldbusse Profinet vs Modbus TCP',
      'Eine Industrieanlage soll mit Steuerungen (SPS) und Antrieben vernetzt werden.',
      'Vergleichen Sie Modbus TCP und Profinet hinsichtlich OSI-Schicht, Echtzeitfähigkeit (Jitter, Latenz) und Einsatzgebieten. Erklären Sie die 3 Conformance Classes (CC-A, CC-B, CC-C) bzw. RT und IRT von Profinet.',
      8,
      'Modbus TCP vs. Profinet:\n'
      '- Modbus TCP: Einfaches Master-Slave / Client-Server Protokoll auf OSI-Schicht 7 über Standard-TCP/IP (Port 502). Nicht echtzeitfähig, da TCP-Handshakes und Retransmissions unvorhersehbare Latenzen erzeugen. Sehr weit verbreitet für einfache Sensorabfragen. (2 Pkt.)\n'
      '- Profinet: Industrial Ethernet Standard (IEC 61158). Bietet deterministische Echtzeitkommunikation durch Umgehung des TCP/IP-Stacks bei Prozessdaten. (2 Pkt.)\n\n'
      'Profinet Echtzeitklassen:\n'
      '- Profinet Standard (TCP/IP): Für Konfiguration und Diagnose (Zykluszeit > 100 ms). (1 Pkt.)\n'
      '- Profinet RT (Real-Time): Prozessdaten umgehen TCP/IP und laufen direkt auf Layer 2 mit VLAN-Priorisierung (Zykluszeit 1-10 ms, softwarebasiert). (1,5 Pkt.)\n'
      '- Profinet IRT (Isochronous Real-Time): Taktsynchron mit Hardware-Unterstützung (spezielle ASIC-Switches). Zeitschlitzverfahren (TDMA) garantiert Latenzen < 1 ms und Jitter < 1 µs für hochpräzise Motion-Control-Antriebe. (1,5 Pkt.)')

add_q('fidv_iot_001', 'AP2_T1', 'LF 10 DV', 'OPC UA Informationsmodell vs MQTT',
      'Maschinendaten einer heterogenen Produktionslinie sollen sowohl an das interne SCADA-System als auch an ein Cloud-Analytics-System übertragen werden.',
      'Vergleichen Sie OPC UA (Open Platform Communications Unified Architecture) mit dem MQTT-Protokoll bezüglich Kommunikationsmuster (Client/Server vs. Publish/Subscribe), Datenmodellierung, Overhead und typischem Einsatzzweck.',
      8,
      'Vergleich OPC UA vs. MQTT:\n'
      '- Kommunikationsmuster:\n'
      '  • OPC UA: Primär Client/Server (Punkt-zu-Punkt Anfrage/Antwort), optional auch Pub/Sub. Bietet Methodenaufrufe (RPC) und Quittierungen. (1,5 Pkt.)\n'
      '  • MQTT: Reines Publish/Subscribe über einen zentralen Message Broker. Entkoppelt Sender und Empfänger zeitlich und räumlich. (1,5 Pkt.)\n'
      '- Datenmodellierung & Semantik:\n'
      '  • OPC UA: Extrem mächtiges, objektorientiertes Informationsmodell (Nodes, References, Datentypen, Einheiten). Die Maschine beschreibt sich selbst semantisch! (2 Pkt.)\n'
      '  • MQTT: Vollkommen payload-agnostisch (reiner Byte-Stream im Body, z. B. JSON). Keine standardisierte Semantik. (1 Pkt.)\n'
      '- Overhead & Einsatzzweck:\n'
      '  • OPC UA: Höherer Protokoll-Overhead, ideal für M2M-Kommunikation und vertikale Integration von der Maschine ins MES/ERP. (1 Pkt.)\n'
      '  • MQTT: Extrem schlanker Header (ab 2 Byte), ideal für bandbreitenarme Funknetze (LoRaWAN, Mobilfunk) und Massen-Telemetriedaten in die Cloud. (1 Pkt.)')

add_q('fidv_sec_001', 'AP2_T2', 'LF 11 DV', 'Industrial Security nach IEC 62443',
      'Das Automatisierungsnetzwerk einer Fabrik soll gegen Cyber-Angriffe und Sabotage gehärtet werden.',
      'Erläutern Sie das Zonen- und Conduit-Modell nach der Normenreihe IEC 62443. Was ist ein Conduit (Verbindungskanal)? Welche Sicherheitsanforderungen gelten an den Schnittstellen zwischen IT- und OT-Netzen?',
      8,
      'Zonen- und Conduit-Modell (IEC 62443):\n'
      '- Zonen (Zones): Gruppierung logischer oder physischer Assets mit denselben Sicherheitsanforderungen (Security Level SL 1 bis 4). Alle Systeme innerhalb einer Zone vertrauen einander weitgehend. (3 Pkt.)\n'
      '- Conduits (Verbindungskanäle): Kommunikationspfade zwischen unterschiedlichen Zonen. Ein Conduit bündelt alle Verbindungen und MUSS durch Sicherheitsmaßnahmen (z. B. Industrial Firewall, VPN, IDS) überwacht und reglementiert werden. Unkontrollierte Querkommunikation zwischen Zonen ist verboten. (3 Pkt.)\n\n'
      'IT/OT-Schnittstellen:\n'
      '- Strikt getrennte Demilitarisierte Zone (Industrial DMZ / IDMZ) nach dem Purdue-Modell (Level 3.5).\n'
      '- Kein direkter Datenverkehr zwischen Office-IT (Level 4/5) und Fertigungs-OT (Level 0-3). Kommunikation darf nur über Proxies, Bastion Hosts oder Jump-Server in der IDMZ erfolgen. (2 Pkt.)')

add_q('fidv_net_001', 'AP2_T2', 'LF 12 DV', 'Redundanzprotokolle PRP und HSR in der OT',
      'In einem Energie-Umspannwerk darf bei einem Netzwerkausfall keine einzige Millisekunde Datenübertragung verloren gehen.',
      'Erläutern Sie die industriellen Redundanzprotokolle Parallel Redundancy Protocol (PRP) und High-availability Seamless Redundancy (HSR) nach IEC 62439-3. Warum reicht das klassische Spanning Tree Protocol (RSTP) in diesen Anwendungen nicht aus?',
      8,
      'Kritik an Spanning Tree (RSTP):\n'
      'RSTP benötigt nach einem Linkausfall mehrere hundert Millisekunden bis Sekunden zur Rekonvergenz. Für zeitkritische Schutzabschaltungen in Industrie und Energie (Schaltzeit < 4 ms) bedeutet dies einen unzulässigen Stillstand. (2 Pkt.)\n\n'
      'PRP (Parallel Redundancy Protocol):\n'
      '- Ein Endgerät (DANP - Dual Attached Node with PRP) ist gleichzeitig an ZWEI komplett voneinander getrennte Netzwerke (LAN A und LAN B) angeschlossen.\n'
      '- Datenframes werden dupliziert und zeitgleich über beide Netze versendet. Der Empfänger verarbeitet das zuerst eintreffende Paket und verwirft das Duplikat nahtlos (Umschaltzeit: EXAKT 0 ms!). Fällt ein Netz komplett aus, läuft der Betrieb ohne Unterbrechung weiter. (3 Pkt.)\n\n'
      'HSR (High-availability Seamless Redundancy):\n'
      '- Ring-Topologie ohne zentrale Switche. Jedes Gerät sendet das Paket zeitgleich in beide Ringrichtungen (im und gegen den Uhrzeigersinn). Der Empfänger entnimmt das erste Paket und verwirft das zweite (Umschaltzeit 0 ms). (3 Pkt.)')

# ==============================================================================
# SPEICHERN DER FRAGENDATENBANK ALS JSON & JS (ZERO-CORS)
# ==============================================================================
out_path = Path('/root/uebungen_python/assets/ihk_tools/ihk_question_bank.json')
out_js_path = Path('/root/uebungen_python/assets/ihk_tools/ihk_question_bank.js')
out_path.parent.mkdir(parents=True, exist_ok=True)

with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

with open(out_js_path, 'w', encoding='utf-8') as f:
    f.write('// Automatisch generierte IHK-Fragendatenbank\n')
    f.write('window.IHK_QUESTION_BANK = ')
    json.dump(questions, f, ensure_ascii=False, indent=2)
    f.write(';\n')

print(f'ERFOLG: {len(questions)} hochkarätige IHK-Prüfungsfragen generiert in {out_path} und {out_js_path}!')

