# SQL 02: Filterung mit WHERE, LIKE & BETWEEN 🔍

Willkommen zu **Modul 02** des SQL & Datenbanken Kurses!

In realen relationalen Datenbanken liegen oft Millionen von Datensätzen. Niemand möchte unstrukturierte Datenberge ungefiltert abfragen. Mit der `WHERE`-Klausel steuerst du präzise, welche Zeilen zurückgegeben werden.

---

## 💡 1. Das Wichtigste in Kürze

### Vergleichsoperatoren
| Operator | Bedeutung | Beispiel |
| :--- | :--- | :--- |
| `=` | Ist gleich | `WHERE kategorie = 'Elektronik'` |
| `!=` oder `<>` | Ungleich | `WHERE status != 'inaktiv'` |
| `<`, `>` | Kleiner als, Größer als | `WHERE preis > 99.99` |
| `<=`, `>=` | Kleiner/Größer oder gleich | `WHERE lagerbestand >= 10` |

### Logische Operatoren (`AND`, `OR`, `NOT`)
```sql
-- Beide Bedingungen müssen wahr sein (AND)
SELECT * FROM produkte WHERE kategorie = 'Elektronik' AND preis < 500;

-- Mindestens eine Bedingung muss wahr sein (OR)
SELECT * FROM produkte WHERE kategorie = 'Audio' OR kategorie = 'Zubehör';

-- Bedingung umkehren (NOT)
SELECT * FROM produkte WHERE NOT (kategorie = 'Möbel');
```

### Wertebereiche mit `BETWEEN` & Mengenauswahl mit `IN`
```sql
-- Inklusive Grenzen [20.0, 100.0]
SELECT * FROM produkte WHERE preis BETWEEN 20.0 AND 100.0;

-- Prüfung gegen eine feste Wertemenge (ersetzt langes OR)
SELECT * FROM produkte WHERE kategorie IN ('Elektronik', 'Audio', 'Gaming');
```

### Textsuche mit Mustern (`LIKE`)
- `%` steht für **beliebig viele** Zeichen (0 bis unendlich).
- `_` steht für **genau ein** beliebiges Zeichen.
```sql
SELECT * FROM produkte WHERE titel LIKE 'Smart%';   -- Beginnt mit 'Smart'
SELECT * FROM produkte WHERE titel LIKE '%Pro%';     -- Enthält irgendwo 'Pro'
SELECT * FROM produkte WHERE code LIKE 'DE___';      -- 'DE' gefolgt von exakt 3 Zeichen
```

### Die Nullwert-Falle (`IS NULL` vs `= NULL`)
In SQL ist `NULL` kein Wert, sondern die **Abwesenheit eines Wertes**. Vergleiche mit `= NULL` ergeben immer `UNKNOWN` (falsch)!
```sql
-- ❌ FALSCH: Ergibt niemals Treffer!
SELECT * FROM produkte WHERE rabatt_code = NULL;

-- ✅ RICHTIG:
SELECT * FROM produkte WHERE rabatt_code IS NULL;
SELECT * FROM produkte WHERE rabatt_code IS NOT NULL;
```

---

## 🎯 Aufgaben in `aufgabe.sql`

1. **TODO 1**: Tabelle `shop_artikel` erstellen und vorgegebene Testartikel einfügen.
2. **TODO 2**: Alle Artikel aus `'Elektronik'` mit `preis > 100.0` filtern.
3. **TODO 3**: Artikel filtern mit `preis BETWEEN 20.0 AND 150.0` und `kategorie IN ('Zubehör', 'Audio')`.
4. **TODO 4**: Textmustersuche mit `LIKE` nach Titeln, die mit `'Smart'` beginnen oder `'Pro'` enthalten.
5. **TODO 5**: Artikel finden ohne Rabattcode (`rabatt_code IS NULL`) und mit `lagerbestand > 0`.
6. **TODO 6**: Top 3 teuerste verfügbare Artikel (`ist_verfuegbar = 1`), die **nicht** aus `'Elektronik'` stammen (`ORDER BY preis DESC LIMIT 3`).

---

## 🚀 Ausführung
Klicke in der Web-IDE auf **Code ausführen** oder **Tests ausführen**, um deine Abfragen mit der SQLite WebAssembly Engine zu testen.
