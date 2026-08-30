function erstelleZaehler(startWert = 0) {
  let zaehler = startWert;
  return function() {
    zaehler++;
    return zaehler;
  };
}

function multiplizierer(faktor) {
  return (x) => x * faktor;
}

function summiereAlles(...zahlen) {
  return zahlen.reduce((sum, n) => sum + n, 0);
}

function erstellePraefixierer(praefix) {
  return (text) => `${praefix}${text}`;
}
