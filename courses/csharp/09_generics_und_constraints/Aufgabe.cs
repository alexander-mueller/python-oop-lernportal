using System;
using System.Collections.Generic;
using System.Linq;

namespace CSharpKurs.Modul09;

// ============================================================================
// 🎯 TODO 1: Generic Entity Interface
// Definiere das Interface IEntity<TId>, das eine get/set Property 'Id' vom Typ TId verlangt.
// ============================================================================
public interface IEntity<TId>
{
    // TODO 1: Property 'TId Id { get; set; }' hier definieren
}

// Beispiel-Entities zur Verwendung mit dem Repository
public class Customer : IEntity<Guid>
{
    public Guid Id { get; set; } = Guid.NewGuid();
    public string Name { get; set; } = string.Empty;
    public string Email { get; set; } = string.Empty;
}

public class Product : IEntity<int>
{
    public int Id { get; set; }
    public string Title { get; set; } = string.Empty;
    public decimal Price { get; set; }
}

// ============================================================================
// 🎯 TODO 2: Result<T> Generic Container
// Kapselt das Ergebnis einer Operation (Erfolg oder Fehler) typsicher ein.
// ============================================================================
public sealed class Result<T>
{
    public bool IsSuccess { get; }
    public T? Value { get; }
    public string? Error { get; }

    // Privater Konstruktor für Erfolg / Fehler
    private Result(bool isSuccess, T? value, string? error)
    {
        IsSuccess = isSuccess;
        Value = value;
        Error = error;
    }

    public static Result<T> Success(T value)
    {
        // TODO 2a: Gibt ein erfolgreiches Result<T> mit dem übergebenen Wert zurück.
        throw new NotImplementedException();
    }

    public static Result<T> Failure(string error)
    {
        // TODO 2b: Gibt ein fehlgeschlagenes Result<T> mit der übergebenen Fehlermeldung zurück.
        throw new NotImplementedException();
    }
}

// ============================================================================
// 🎯 TODO 3: Generic Repository mit Constraints
// Implementiere das generische InMemoryRepository<TEntity, TId> mit den Constraints:
// - where TEntity : class, IEntity<TId>, new()
// - where TId : notnull
// ============================================================================
public interface IRepository<TEntity, TId> 
    where TEntity : class, IEntity<TId>, new()
    where TId : notnull
{
    void Add(TEntity entity);
    TEntity? GetById(TId id);
    IReadOnlyList<TEntity> GetAll();
    bool Remove(TId id);
    int Count { get; }
    TEntity CreateDefault();
}

public class InMemoryRepository<TEntity, TId> : IRepository<TEntity, TId>
    where TEntity : class, IEntity<TId>, new()
    where TId : notnull
{
    private readonly Dictionary<TId, TEntity> _storage = new();

    public int Count => _storage.Count;

    public void Add(TEntity entity)
    {
        // TODO 3a: Speichere die Entity anhand ihrer Id im Dictionary _storage.
        // Wenn entity null ist, wirf eine ArgumentNullException.
        throw new NotImplementedException();
    }

    public TEntity? GetById(TId id)
    {
        // TODO 3b: Suche die Entity anhand der Id im Dictionary und gib sie zurück (oder null falls nicht gefunden).
        throw new NotImplementedException();
    }

    public IReadOnlyList<TEntity> GetAll()
    {
        // TODO 3c: Gib alle im Dictionary gespeicherten Entities als IReadOnlyList zurück.
        throw new NotImplementedException();
    }

    public bool Remove(TId id)
    {
        // TODO 3d: Entferne die Entity mit der angegebenen Id aus _storage und gib true zurück, falls sie existierte.
        throw new NotImplementedException();
    }

    public TEntity CreateDefault()
    {
        // TODO 3e: Erzeuge eine neue Instanz von TEntity via 'new TEntity()' und gib sie zurück.
        throw new NotImplementedException();
    }
}

// ============================================================================
// 🎯 TODO 4: Generische Hilfsmethoden
// ============================================================================
public static class GenericUtilities
{
    // TODO 4a: Tausche die Werte von zwei Variablen per Referenz (ref T a, ref T b)
    public static void Swap<T>(ref T a, ref T b)
    {
        throw new NotImplementedException();
    }

    // TODO 4b: Filtert eine IEnumerable<T> anhand eines Predicates und liefert eine neue Liste zurück.
    public static List<T> FindMatches<T>(IEnumerable<T> items, Predicate<T> filter)
    {
        throw new NotImplementedException();
    }
}
