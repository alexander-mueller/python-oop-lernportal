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

-- 1. Elektronik > 100
SELECT * FROM shop_artikel WHERE kategorie = 'Elektronik' AND preis > 100.0;

-- 2. BETWEEN & IN
SELECT * FROM shop_artikel WHERE preis BETWEEN 20.0 AND 150.0 AND kategorie IN ('Zubehör', 'Audio');

-- 3. LIKE Suche
SELECT * FROM shop_artikel WHERE titel LIKE 'Smart%' OR titel LIKE '%Pro%';

-- 4. IS NULL & lagerbestand > 0
SELECT * FROM shop_artikel WHERE rabatt_code IS NULL AND lagerbestand > 0;

-- 5. NOT Elektronik & Top 3 teuerste
SELECT * FROM shop_artikel WHERE ist_verfuegbar = 1 AND kategorie != 'Elektronik' ORDER BY preis DESC LIMIT 3;
