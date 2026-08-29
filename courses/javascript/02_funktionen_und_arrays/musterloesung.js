function verdoppeln(zahlen) {
  return zahlen.map(x => x * 2);
}

function filterGeradeZahlen(zahlen) {
  return zahlen.filter(x => x % 2 === 0);
}

function arraySumme(zahlen) {
  return zahlen.reduce((acc, curr) => acc + curr, 0);
}
