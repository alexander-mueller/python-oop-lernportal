# C# 10: Language Integrated Query (LINQ) & Fluent Chaining 📊

Willkommen zu **Modul 10**! Hier lernst du LINQ (Language Integrated Query) – eines der beliebtesten und mächtigsten Features von C# und .NET für die deklarative Datenverarbeitung.

---

## 💡 1. Das Wichtigste in Kürze

### Was ist LINQ?
LINQ erlaubt es dir, Abfragen auf Collections (`IEnumerable<T>`, `IQueryable<T>`) genauso intuitiv wie in SQL zu formulieren, jedoch voll typsicher und mit IntelliSense-Unterstützung:

```csharp
// Imperativ (Alt & umständlich):
var result = new List<string>();
foreach (var o in orders)
{
    if (o.TotalAmount > 100)
        result.Add(o.CustomerName);
}

// Deklarativ mit LINQ (Modern & elegant):
var result = orders
    .Where(o => o.TotalAmount > 100)
    .Select(o => o.CustomerName)
    .ToList();
```

### Die wichtigsten LINQ-Methoden
- **Filtern:** `.Where(predicate)`
- **Transformieren (Mapping):** `.Select(selector)`
- **Flachklopfen verschachtelter Listen:** `.SelectMany(collectionSelector)`
- **Sortieren:** `.OrderBy(...)`, `.OrderByDescending(...)`, `.ThenBy(...)`
- **Gruppieren:** `.GroupBy(keySelector)`
- **Aggregieren:** `.Sum()`, `.Average()`, `.Min()`, `.Max()`, `.Count()`
- **Paginieren:** `.Skip(n).Take(m)`
- **Materialisieren:** `.ToList()`, `.ToArray()`, `.ToDictionary(k => ..., v => ...)`

---

## 🎯 Teilziele in `Aufgabe.cs`

1. **TODO 1: `GetHighValueOrders`**  
   Filtere alle Bestellungen mit `TotalAmount >= minTotal`, sortiert nach `TotalAmount` absteigend.

2. **TODO 2: `GetAllPurchasedProductIds`**  
   Extrahiere alle eindeutigen (`Distinct`) Produkt-IDs über alle Bestellpositionen hinweg mit `SelectMany`.

3. **TODO 3: `CalculateRevenueByCategory`**  
   Gruppiere alle Items nach ihrer Produktkategorie (`Category`) und summiere den Gesamtumsatz (`Price * Quantity`) pro Kategorie in ein `Dictionary<string, decimal>`.

4. **TODO 4: `GetTopSpendingCustomers`**  
   Gruppiere die Bestellungen nach `CustomerId`, summiere den Gesamtumsatz pro Kunde und gib die Top `N` Kunden (sortiert nach Umsatz absteigend) zurück.

5. **TODO 5: `GetPaginatedOrders`**  
   Implementiere Paginierung mit `.Skip((pageNumber - 1) * pageSize).Take(pageSize)`.
