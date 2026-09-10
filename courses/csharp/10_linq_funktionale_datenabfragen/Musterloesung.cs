using System;
using System.Collections.Generic;
using System.Linq;

namespace CSharpKurs.Modul10;

public record OrderItem(int ProductId, string Title, string Category, decimal Price, int Quantity)
{
    public decimal LineTotal => Price * Quantity;
}

public record Order(int OrderId, int CustomerId, DateTime CreatedAt, List<OrderItem> Items)
{
    public decimal TotalAmount => Items.Sum(i => i.LineTotal);
}

public record CustomerSpending(int CustomerId, decimal TotalSpent);

public class SalesAnalyticsEngine
{
    // 🎯 LÖSUNG TODO 1: High-Value Orders filtern
    public List<Order> GetHighValueOrders(IEnumerable<Order> orders, decimal minTotal)
    {
        ArgumentNullException.ThrowIfNull(orders);

        return orders
            .Where(o => o.TotalAmount >= minTotal)
            .OrderByDescending(o => o.TotalAmount)
            .ToList();
    }

    // 🎯 LÖSUNG TODO 2: Eindeutige Produkt-IDs ermitteln
    public List<int> GetAllPurchasedProductIds(IEnumerable<Order> orders)
    {
        ArgumentNullException.ThrowIfNull(orders);

        return orders
            .SelectMany(o => o.Items)
            .Select(item => item.ProductId)
            .Distinct()
            .OrderBy(id => id)
            .ToList();
    }

    // 🎯 LÖSUNG TODO 3: Umsatz pro Kategorie berechnen
    public Dictionary<string, decimal> CalculateRevenueByCategory(IEnumerable<Order> orders)
    {
        ArgumentNullException.ThrowIfNull(orders);

        return orders
            .SelectMany(o => o.Items)
            .GroupBy(item => item.Category)
            .ToDictionary(
                group => group.Key,
                group => group.Sum(item => item.LineTotal)
            );
    }

    // 🎯 LÖSUNG TODO 4: Top-Kunden nach Umsatz
    public List<CustomerSpending> GetTopSpendingCustomers(IEnumerable<Order> orders, int topCount)
    {
        ArgumentNullException.ThrowIfNull(orders);

        return orders
            .GroupBy(o => o.CustomerId)
            .Select(group => new CustomerSpending(
                group.Key,
                group.Sum(o => o.TotalAmount)
            ))
            .OrderByDescending(c => c.TotalSpent)
            .Take(topCount)
            .ToList();
    }

    // 🎯 LÖSUNG TODO 5: Paginierte Bestellungen abrufen
    public List<Order> GetPaginatedOrders(IEnumerable<Order> orders, int pageNumber, int pageSize)
    {
        ArgumentNullException.ThrowIfNull(orders);

        if (pageNumber < 1)
            throw new ArgumentOutOfRangeException(nameof(pageNumber), "Page number must be >= 1.");

        if (pageSize < 1)
            throw new ArgumentOutOfRangeException(nameof(pageSize), "Page size must be >= 1.");

        return orders
            .Skip((pageNumber - 1) * pageSize)
            .Take(pageSize)
            .ToList();
    }
}
