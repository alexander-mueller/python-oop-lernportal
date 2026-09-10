using System;
using System.Collections.Generic;
using System.Linq;

namespace CSharpKurs.Modul09;

// 🎯 LÖSUNG TODO 1: Generic Entity Interface
public interface IEntity<TId>
{
    TId Id { get; set; }
}

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

// 🎯 LÖSUNG TODO 2: Result<T> Generic Container
public sealed class Result<T>
{
    public bool IsSuccess { get; }
    public T? Value { get; }
    public string? Error { get; }

    private Result(bool isSuccess, T? value, string? error)
    {
        IsSuccess = isSuccess;
        Value = value;
        Error = error;
    }

    public static Result<T> Success(T value)
    {
        return new Result<T>(true, value, null);
    }

    public static Result<T> Failure(string error)
    {
        return new Result<T>(false, default, error);
    }
}

// 🎯 LÖSUNG TODO 3: Generic Repository mit Constraints
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
        ArgumentNullException.ThrowIfNull(entity);
        _storage[entity.Id] = entity;
    }

    public TEntity? GetById(TId id)
    {
        return _storage.GetValueOrDefault(id);
    }

    public IReadOnlyList<TEntity> GetAll()
    {
        return _storage.Values.ToList().AsReadOnly();
    }

    public bool Remove(TId id)
    {
        return _storage.Remove(id);
    }

    public TEntity CreateDefault()
    {
        return new TEntity();
    }
}

// 🎯 LÖSUNG TODO 4: Generische Hilfsmethoden
public static class GenericUtilities
{
    public static void Swap<T>(ref T a, ref T b)
    {
        (a, b) = (b, a);
    }

    public static List<T> FindMatches<T>(IEnumerable<T> items, Predicate<T> filter)
    {
        ArgumentNullException.ThrowIfNull(items);
        ArgumentNullException.ThrowIfNull(filter);

        var result = new List<T>();
        foreach (var item in items)
        {
            if (filter(item))
            {
                result.Add(item);
            }
        }
        return result;
    }
}
