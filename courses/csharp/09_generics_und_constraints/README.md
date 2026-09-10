# C# 09: Generics & Generic Constraints 🧬

Willkommen zu **Modul 09** des C# Masterkurses! In diesem Kapitel lernst du, wie du flexible, hochgradig wiederverwendbare und typsichere Datenstrukturen in C# 12 entwickelst.

---

## 💡 1. Das Wichtigste in Kürze

### Warum Generics?
Generics eliminieren die Notwendigkeit von Type-Casts und Boxing/Unboxing:
- **Typsicherheit:** Fehler werden bereits vom Roslyn-Compiler zur Build-Zeit erkannt.
- **Performance:** Wertetypen (wie `int`, `struct`) landen direkt auf dem Stack bzw. in typspezifischen Arrays – keine teure Heap-Allokation.
- **Code-Wiederverwendung:** Ein einzelner Algorithmus funktioniert für beliebig viele Typen.

### Generic Constraints (`where T : ...`)
Mit Constraints sagst du dem Compiler, welche Fähigkeiten der Typ `T` mitbringen muss:
```csharp
public class Repository<TEntity, TId> 
    where TEntity : class, IEntity<TId>, new()
    where TId : notnull
{
    // Hier können wir:
    // - entity.Id aufrufen (durch IEntity<TId>)
    // - TEntity instanziieren mit new TEntity() (durch new())
    // - null zurückgeben (durch class)
}
```

### Der `Result<T>` Typ (Functional Error Handling)
Statt Ausnahmen für reguläre Fehlerflüsse zu werfen, kapselt `Result<T>` Erfolg oder Misserfolg:
```csharp
var result = Result<Customer>.Success(new Customer { Name = "Alice" });
if (result.IsSuccess)
{
    Console.WriteLine($"Kunde geladen: {result.Value.Name}");
}
```

---

## 🎯 Teilziele in `Aufgabe.cs`

1. **TODO 1: `IEntity<TId>` Interface**  
   Definiere ein generisches Entity-Interface mit `TId Id { get; set; }`.

2. **TODO 2: `Result<T>` Wrapper-Klasse**  
   Implementiere einen unmodifizierbaren Result-Container mit `IsSuccess`, `Value`, `Error` sowie statischen Factory-Methoden `Success(T)` und `Failure(string)`.

3. **TODO 3: `InMemoryRepository<TEntity, TId>`**  
   Erstelle ein In-Memory Repository mit den Constraints `where TEntity : class, IEntity<TId>, new()` und `where TId : notnull`. Implementiere `Add`, `GetById`, `GetAll`, `Remove`, `Count` und `CreateDefault()`.

4. **TODO 4: Generische Hilfsmethoden**  
   Implementiere `Swap<T>(ref T a, ref T b)` und `FindMatches<T>(IEnumerable<T> items, Predicate<T> filter)`.
