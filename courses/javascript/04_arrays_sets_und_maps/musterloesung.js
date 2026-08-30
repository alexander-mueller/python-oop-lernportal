function verdoppeln(zahlen) {
  return zahlen.map(x => x * 2);
}

function filterGeradeZahlen(zahlen) {
  return zahlen.filter(x => x % 2 === 0);
}

function arraySumme(zahlen) {
  return zahlen.reduce((acc, curr) => acc + curr, 0);
}

function entferneDuplikate(liste) {
  return [...new Set(liste)];
}

function erstelleWoerterbuch(paare) {
  return new Map(paare);
}

function zaehleHaeufigkeiten(woerter) {
  const haeufigkeit = new Map();
  for (const wort of woerter) {
    haeufigkeit.set(wort, (haeufigkeit.get(wort) || 0) + 1);
  }
  return haeufigkeit;
}
