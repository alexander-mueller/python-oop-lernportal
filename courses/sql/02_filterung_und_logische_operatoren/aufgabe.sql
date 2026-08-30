-- 🗄️ SQL 02: FILTERUNG MIT WHERE, LIKE & BETWEEN 🗄️
-- ====================================================

-- 🎯 TEILZIEL 1 (TODO 1): Erstelle die Tabelle `shop_artikel` und füge die Testdaten ein.
CREATE TABLE IF NOT EXISTS shop_artikel (
    id INTEGER PRIMARY KEY,
    titel TEXT NOT NULL,
    kategorie TEXT NOT NULL,
    preis REAL NOT NULL,
    lagerbestand INTEGER NOT NULL,
    rabatt_code TEXT,
    ist_verfuegbar INTEGER NOT NULL DEFAULT 1
);

INSERT INTO shop_artikel (id, titel, kategorie, preis, lagerbestand, rabatt_code, ist_verfuegbar) VALUES
    (1, 'Smartphone Pro Max', 'Elektronik', 1199.99, 15, 'SALE10', 1),
    (2, 'Kabellose Maus', 'Zubehör', 29.99, 50, NULL, 1),
    (3, 'Smart TV 55 Zoll', 'Elektronik', 649.00, 8, NULL, 1),
    (4, 'Bluetooth Kopfhörer Pro', 'Audio', 129.50, 25, 'AUDIO5', 1),
    (5, 'Ergonomische Tastatur', 'Zubehör', 89.90, 0, NULL, 0),
    (6, 'Smart Speaker Mini', 'Audio', 49.99, 40, NULL, 1),
    (7, 'Gaming Laptop X', 'Elektronik', 1499.00, 5, 'GAMER', 1),
    (8, 'USB-C Schnellladekabel', 'Zubehör', 14.99, 120, 'CABLE', 1);


-- 🎯 TEILZIEL 2 (TODO 2): Schreibe eine Abfrage für alle Artikel aus 'Elektronik', die teurer als 100.0 Euro sind.
-- SELECT ... FROM shop_artikel WHERE ...;
SELECT * FROM shop_artikel WHERE kategorie = 'Elektronik' AND preis > 100.0;


-- 🎯 TEILZIEL 3 (TODO 3): Finde alle Artikel, deren Preis zwischen 20.0 und 150.0 Euro liegt (inklusive)
-- und die zur Kategorie 'Zubehör' ODER 'Audio' gehören (Nutze BETWEEN und IN).
-- SELECT ...;
SELECT * FROM shop_artikel WHERE preis BETWEEN 20.0 AND 150.0 AND kategorie IN ('Zubehör', 'Audio');


-- 🎯 TEILZIEL 4 (TODO 4): Finde alle Artikel, deren Titel mit 'Smart' beginnt ODER das Wort 'Pro' enthält (Nutze LIKE).
-- SELECT ...;
SELECT * FROM shop_artikel WHERE titel LIKE 'Smart%' OR titel LIKE '%Pro%';


-- 🎯 TEILZIEL 5 (TODO 5): Finde alle Artikel, die KEINEN Rabattcode besitzen (NULL) und deren Lagerbestand größer als 0 ist.
-- SELECT ...;
SELECT * FROM shop_artikel WHERE rabatt_code IS NULL AND lagerbestand > 0;


-- 🎯 TEILZIEL 6 (TODO 6): Finde die Top 3 teuersten verfügbaren Artikel (ist_verfuegbar = 1),
-- die NICHT zur Kategorie 'Elektronik' gehören. Sortiere absteigend nach Preis (LIMIT 3).
-- SELECT ...;
SELECT * FROM shop_artikel WHERE ist_verfuegbar = 1 AND kategorie != 'Elektronik' ORDER BY preis DESC LIMIT 3;
