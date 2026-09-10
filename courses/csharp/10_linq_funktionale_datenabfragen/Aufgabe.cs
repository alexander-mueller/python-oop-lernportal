using System;
using System.Collections.Generic;
using System.Linq;

namespace CSharpKurs.Modul10;

// Domain-Modelle
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
    // ========================================================================
    // 🎯 TODO 1: High-Value Orders filtern
    // Filtere alle Bestellungen mit TotalAmount >= minTotal.
    // Sortiere das Ergebnis absteigend nach TotalAmount.
    // ========================================================================
    public List<Order> GetHighValueOrders(IEnumerable<Order> orders, decimal minTotal)
    {
        throw new NotImplementedException();
    }

    // ========================================================================
    // 🎯 TODO 2: Eindeutige Produkt-IDs ermitteln
    // Verwende SelectMany, um über alle Items aller Orders zu iterieren.
    // Liefere eine sortierte Liste aller eindeutigen (Distinct) ProductId-Werte zurück.
    // ========================================================================
    public List<int> GetAllPurchasedProductIds(IEnumerable<Order> orders)
    {
        throw new NotImplementedException();
    }

    // ========================================================================
    // 🎯 TODO 3: Umsatz pro Kategorie berechnen
    // Extrahiere alle Items aller Orders, gruppiere sie nach Category und 
    // berechne die Summe von (Price * Quantity) pro Kategorie.
    // Gib das Ergebnis als Dictionary<string, decimal> zurück.
    // ========================================================================
    public Dictionary<string, decimal> CalculateRevenueByCategory(IEnumerable<Order> orders)
    {
        throw new NotImplementedException();
    }

    // ========================================================================
    // 🎯 TODO 4: Top-Kunden nach Umsatz
    // Gruppiere alle Bestellungen nach CustomerId.
    // Berechne für jeden Kunden den Gesamtausgabenbetrag (Summe der TotalAmounts).
    // Sortiere absteigend nach TotalSpent und nimm die ersten 'topCount' Einträge.
    // ========================================================================
    public List<CustomerSpending> GetTopSpendingCustomers(IEnumerable<Order> orders, int topCount)
    {
        throw new NotImplementedException();
    }

    // ========================================================================
    // 🎯 TODO 5: Paginierte Bestellungen abrufen
    // Überspringe (pageNumber - 1) * pageSize Elemente und nimm pageSize Elemente.
    // Falls pageNumber < 1 oder pageSize < 1, wirf eine ArgumentOutOfRangeException.
    // ========================================================================
    public List<Order> GetPaginatedOrders(IEnumerable<Order> orders, int pageNumber, int pageSize)
    {
        throw new NotImplementedException();
    }
}
