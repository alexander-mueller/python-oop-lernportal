using System;
using System.Collections.Generic;
using System.Linq;
using Xunit;

namespace CSharpKurs.Modul10.Tests;

public class LinqTests
{
    private readonly SalesAnalyticsEngine _engine = new();

    private List<Order> CreateSampleOrders()
    {
        return new List<Order>
        {
            new Order(1, 101, DateTime.UtcNow.AddDays(-5), new List<OrderItem>
            {
                new OrderItem(1, "Laptop Pro", "Electronics", 1200m, 1),
                new OrderItem(2, "Wireless Mouse", "Accessories", 40m, 2)
            }), // Total: 1280m
            new Order(2, 102, DateTime.UtcNow.AddDays(-4), new List<OrderItem>
            {
                new OrderItem(3, "Desk Lamp", "Furniture", 60m, 1),
                new OrderItem(2, "Wireless Mouse", "Accessories", 40m, 1)
            }), // Total: 100m
            new Order(3, 101, DateTime.UtcNow.AddDays(-3), new List<OrderItem>
            {
                new OrderItem(4, "4K Monitor", "Electronics", 450m, 2)
            }), // Total: 900m (Customer 101 Total: 1280 + 900 = 2180m)
            new Order(4, 103, DateTime.UtcNow.AddDays(-2), new List<OrderItem>
            {
                new OrderItem(5, "Ergonomic Chair", "Furniture", 350m, 1),
                new OrderItem(1, "Laptop Pro", "Electronics", 1200m, 2)
            }), // Total: 2750m (Customer 103 Total: 2750m)
            new Order(5, 104, DateTime.UtcNow.AddDays(-1), new List<OrderItem>
            {
                new OrderItem(6, "USB-C Hub", "Accessories", 30m, 3)
            })  // Total: 90m
        };
    }

    // TEST: GetHighValueOrders Filters and Orders Descending
    [Fact]
    public void Test_GetHighValueOrders_ReturnsOrdersAboveThresholdSorted()
    {
        var orders = CreateSampleOrders();
        var highValue = _engine.GetHighValueOrders(orders, 500m);

        Assert.Equal(3, highValue.Count);
        Assert.Equal(4, highValue[0].OrderId); // 2750m
        Assert.Equal(1, highValue[1].OrderId); // 1280m
        Assert.Equal(3, highValue[2].OrderId); // 900m
    }

    // TEST: GetAllPurchasedProductIds Distinct and Ordered
    [Fact]
    public void Test_GetAllPurchasedProductIds_ReturnsUniqueSortedIds()
    {
        var orders = CreateSampleOrders();
        var productIds = _engine.GetAllPurchasedProductIds(orders);

        Assert.Equal(new List<int> { 1, 2, 3, 4, 5, 6 }, productIds);
    }

    // TEST: CalculateRevenueByCategory
    [Fact]
    public void Test_CalculateRevenueByCategory_CalculatesSumPerCategory()
    {
        var orders = CreateSampleOrders();
        var revenue = _engine.CalculateRevenueByCategory(orders);

        // Electronics: 1200 (Order 1) + 900 (Order 3) + 2400 (Order 4) = 4500m
        // Accessories: 80 (Order 1) + 40 (Order 2) + 90 (Order 5) = 210m
        // Furniture: 60 (Order 2) + 350 (Order 4) = 410m
        Assert.Equal(4500m, revenue["Electronics"]);
        Assert.Equal(210m, revenue["Accessories"]);
        Assert.Equal(410m, revenue["Furniture"]);
    }

    // TEST: GetTopSpendingCustomers
    [Fact]
    public void Test_GetTopSpendingCustomers_ReturnsRankedSpenders()
    {
        var orders = CreateSampleOrders();
        var top2 = _engine.GetTopSpendingCustomers(orders, 2);

        Assert.Equal(2, top2.Count);
        Assert.Equal(103, top2[0].CustomerId); // 2750m
        Assert.Equal(2750m, top2[0].TotalSpent);

        Assert.Equal(101, top2[1].CustomerId); // 2180m
        Assert.Equal(2180m, top2[1].TotalSpent);
    }

    // TEST: GetPaginatedOrders Pagination Logic
    [Theory]
    [InlineData(1, 2, 2)] // Page 1 with size 2 -> Orders 1 and 2
    [InlineData(2, 2, 2)] // Page 2 with size 2 -> Orders 3 and 4
    [InlineData(3, 2, 1)] // Page 3 with size 2 -> Order 5
    public void Test_GetPaginatedOrders_PaginatesCorrectly(int pageNumber, int pageSize, int expectedCount)
    {
        var orders = CreateSampleOrders();
        var page = _engine.GetPaginatedOrders(orders, pageNumber, pageSize);

        Assert.Equal(expectedCount, page.Count);
    }

    // TEST: GetPaginatedOrders Throws On Invalid Arguments
    [Fact]
    public void Test_GetPaginatedOrders_ThrowsOnInvalidPage()
    {
        var orders = CreateSampleOrders();
        Assert.Throws<ArgumentOutOfRangeException>(() => _engine.GetPaginatedOrders(orders, 0, 10));
        Assert.Throws<ArgumentOutOfRangeException>(() => _engine.GetPaginatedOrders(orders, 1, 0));
    }
}
