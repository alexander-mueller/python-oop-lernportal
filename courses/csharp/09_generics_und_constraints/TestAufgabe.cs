using System;
using System.Collections.Generic;
using System.Linq;
using Xunit;

namespace CSharpKurs.Modul09.Tests;

public class GenericsTests
{
    // TEST: IEntity und Result<T> Success
    [Fact]
    public void Test_Result_Success_HoldsValueAndTrueStatus()
    {
        var customer = new Customer { Name = "Max Mustermann", Email = "max@enterprise.com" };
        var result = Result<Customer>.Success(customer);

        Assert.True(result.IsSuccess);
        Assert.NotNull(result.Value);
        Assert.Equal("Max Mustermann", result.Value.Name);
        Assert.Null(result.Error);
    }

    // TEST: Result<T> Failure
    [Fact]
    public void Test_Result_Failure_HoldsErrorMessage()
    {
        var result = Result<Product>.Failure("Produkt nicht gefunden!");

        Assert.False(result.IsSuccess);
        Assert.Null(result.Value);
        Assert.Equal("Produkt nicht gefunden!", result.Error);
    }

    // TEST: Generic Repository Add and GetById
    [Fact]
    public void Test_Repository_AddAndGetById_WorksCorrectly()
    {
        var repo = new InMemoryRepository<Product, int>();
        var p1 = new Product { Id = 101, Title = "Enterprise Cloud Server", Price = 4999.99m };
        var p2 = new Product { Id = 102, Title = "SSD Array 4TB", Price = 899.50m };

        repo.Add(p1);
        repo.Add(p2);

        Assert.Equal(2, repo.Count);
        var fetched = repo.GetById(101);
        Assert.NotNull(fetched);
        Assert.Equal("Enterprise Cloud Server", fetched.Title);

        var nonExistent = repo.GetById(999);
        Assert.Null(nonExistent);
    }

    // TEST: Generic Repository GetAll and Remove
    [Fact]
    public void Test_Repository_GetAllAndRemove_ModifiesCollection()
    {
        var repo = new InMemoryRepository<Customer, Guid>();
        var id1 = Guid.NewGuid();
        var id2 = Guid.NewGuid();

        repo.Add(new Customer { Id = id1, Name = "Alice GmbH" });
        repo.Add(new Customer { Id = id2, Name = "Bob AG" });

        Assert.Equal(2, repo.Count);
        var all = repo.GetAll();
        Assert.Equal(2, all.Count);

        bool removed = repo.Remove(id1);
        Assert.True(removed);
        Assert.Equal(1, repo.Count);
        Assert.Null(repo.GetById(id1));

        bool removedAgain = repo.Remove(id1);
        Assert.False(removedAgain);
    }

    // TEST: Generic Repository Constraint new() CreateDefault
    [Fact]
    public void Test_Repository_CreateDefault_InstantiatesNewEntity()
    {
        var repo = new InMemoryRepository<Product, int>();
        var defaultProduct = repo.CreateDefault();

        Assert.NotNull(defaultProduct);
        Assert.IsType<Product>(defaultProduct);
        Assert.Equal(0, defaultProduct.Id);
    }

    // TEST: GenericUtilities Swap Value Types
    [Fact]
    public void Test_GenericUtilities_Swap_SwapsValues()
    {
        int x = 10;
        int y = 20;
        GenericUtilities.Swap(ref x, ref y);

        Assert.Equal(20, x);
        Assert.Equal(10, y);

        string s1 = "Hello";
        string s2 = "World";
        GenericUtilities.Swap(ref s1, ref s2);

        Assert.Equal("World", s1);
        Assert.Equal("Hello", s2);
    }

    // TEST: GenericUtilities FindMatches Filter
    [Theory]
    [InlineData(10, 3)] // Zahlen > 10 in {5, 12, 8, 20, 15, 3} -> 12, 20, 15 (3 Treffer)
    public void Test_GenericUtilities_FindMatches_FiltersItems(int threshold, int expectedCount)
    {
        var numbers = new List<int> { 5, 12, 8, 20, 15, 3 };
        var matches = GenericUtilities.FindMatches(numbers, n => n > threshold);

        Assert.Equal(expectedCount, matches.Count);
        Assert.All(matches, n => Assert.True(n > threshold));
    }
}
