/**
 * 🌐 JS 04: ARRAYS, SETS & MAPS 🌐
 * =================================
 * Funktionale Datenstrukturen, Mengen ohne Duplikate (Set) und Schlüssel-Wert-Speicher (Map).
 */

// 🎯 TEILZIEL 1 (TODO 1): verdoppeln(zahlen)
// Erstelle ein neues Array, in dem alle Zahlen verdoppelt sind (unter Nutzung von .map()).
function verdoppeln(zahlen) {
  // TODO: Array mit .map() transformieren
  return [];
}

// 🎯 TEILZIEL 2 (TODO 2): filterGeradeZahlen(zahlen)
// Filtere nur die geraden Zahlen aus dem Array heraus (unter Nutzung von .filter()).
function filterGeradeZahlen(zahlen) {
  // TODO: Nur gerade Zahlen mit .filter() beibehalten
  return [];
}

// 🎯 TEILZIEL 3 (TODO 3): arraySumme(zahlen)
// Berechne die Gesamtsumme aller Zahlen im Array mit .reduce().
// Bei leerem Array soll 0 zurückgegeben werden.
function arraySumme(zahlen) {
  // TODO: Summe mit .reduce() aggregieren
  return 0;
}

// 🎯 TEILZIEL 4 (TODO 4): entferneDuplikate(liste)
// Entferne alle doppelten Werte aus dem Array 'liste' mithilfe einer Set-Datenstruktur (new Set()).
// Gib das Ergebnis als echtes Array zurück (z.B. mit dem Spread-Operator [...new Set(liste)]).
// Beispiel: entferneDuplikate([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]
function entferneDuplikate(liste) {
  // TODO: new Set() nutzen und als Array zurückgeben
  return [];
}

// 🎯 TEILZIEL 5 (TODO 5): erstelleWoerterbuch(paare)
// Erstelle aus einem zweidimensionalen Array von Schlüssel-Wert-Paaren eine JavaScript Map (new Map()).
// Beispiel: erstelleWoerterbuch([["de", "Hallo"], ["en", "Hello"]]) -> Map { 'de' => 'Hallo', 'en' => 'Hello' }
function erstelleWoerterbuch(paare) {
  // TODO: new Map(paare) erstellen und zurückgeben
  return null;
}

// 🎯 TEILZIEL 6 (TODO 6): zaehleHaeufigkeiten(woerter)
// Zähle, wie oft jedes Wort im übergebenen Array 'woerter' vorkommt.
// Nutze eine Map, um die Zählerstände zu verwalten (map.set(wort, (map.get(wort) || 0) + 1)).
// Gib die fertige Map zurück.
// Beispiel: zaehleHaeufigkeiten(["apfel", "banane", "apfel"]) -> Map { 'apfel' => 2, 'banane' => 1 }
function zaehleHaeufigkeiten(woerter) {
  // TODO: Map instanziieren, Wörter durchlaufen und Häufigkeit zählen
  return new Map();
}
