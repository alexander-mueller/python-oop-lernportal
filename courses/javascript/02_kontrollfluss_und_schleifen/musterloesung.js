function kategorisiereAlter(alter) {
  if (alter < 13) {
    return "Kind";
  } else if (alter <= 17) {
    return "Jugendlicher";
  } else if (alter <= 64) {
    return "Erwachsener";
  } else {
    return "Senior";
  }
}

function wochentagName(tagNummer) {
  switch (tagNummer) {
    case 1:
      return "Montag";
    case 2:
      return "Dienstag";
    case 3:
      return "Mittwoch";
    case 4:
      return "Donnerstag";
    case 5:
      return "Freitag";
    case 6:
      return "Samstag";
    case 7:
      return "Sonntag";
    default:
      return "Ungültig";
  }
}

function berechneRabattpreis(preis, istPremium, hatGutschein) {
  let rabattSatz = 0;
  if (istPremium && hatGutschein) {
    rabattSatz = 0.3;
  } else if (istPremium) {
    rabattSatz = 0.2;
  } else if (hatGutschein) {
    rabattSatz = 0.1;
  }
  return preis * (1 - rabattSatz);
}

function summeGeraderZahlen(start, ende) {
  let summe = 0;
  for (let i = start; i <= ende; i++) {
    if (i % 2 !== 0) {
      continue;
    }
    summe += i;
  }
  return summe;
}

function findeErstesVielfaches(zahlen, teiler) {
  let ergebnis = null;
  for (const zahl of zahlen) {
    if (zahl % teiler === 0) {
      ergebnis = zahl;
      break;
    }
  }
  return ergebnis;
}
