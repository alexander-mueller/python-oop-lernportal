using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using Xunit;

namespace CSharpKurs.Modul11.Tests;

public class AsyncTests
{
    private readonly CloudDataAggregator _aggregator = new();

    // TEST: FetchServiceDataAsync Returns Data
    [Fact]
    public async Task Test_FetchServiceDataAsync_ReturnsValidResponse()
    {
        var endpoint = new ServiceEndpoint("BillingService", "https://api.internal/billing", 10);
        var response = await _aggregator.FetchServiceDataAsync(endpoint);

        Assert.True(response.Success);
        Assert.Equal("BillingService", response.EndpointName);
        Assert.Equal("Data from https://api.internal/billing", response.Payload);
    }

    // TEST: FetchServiceDataAsync Respects CancellationToken
    [Fact]
    public async Task Test_FetchServiceDataAsync_ThrowsOnCancellation()
    {
        using var cts = new CancellationTokenSource();
        cts.Cancel(); // Sofortiger Abbruch

        var endpoint = new ServiceEndpoint("SlowService", "https://api.internal/slow", 500);

        await Assert.ThrowsAnyAsync<OperationCanceledException>(async () =>
        {
            await _aggregator.FetchServiceDataAsync(endpoint, cts.Token);
        });
    }

    // TEST: AggregateServicesAsync Runs In Parallel With Task.WhenAll
    [Fact]
    public async Task Test_AggregateServicesAsync_FetchesAllEndpointsConcurrently()
    {
        var endpoints = new List<ServiceEndpoint>
        {
            new("AuthService", "https://api.internal/auth", 20),
            new("CatalogService", "https://api.internal/catalog", 20),
            new("InventoryService", "https://api.internal/inventory", 20)
        };

        var responses = await _aggregator.AggregateServicesAsync(endpoints);

        Assert.Equal(3, responses.Count);
        Assert.Contains(responses, r => r.EndpointName == "AuthService");
        Assert.Contains(responses, r => r.EndpointName == "CatalogService");
        Assert.Contains(responses, r => r.EndpointName == "InventoryService");
    }

    // TEST: FetchFastestResponseAsync Returns First Completed
    [Fact]
    public async Task Test_FetchFastestResponseAsync_ReturnsQuickestService()
    {
        var endpoints = new List<ServiceEndpoint>
        {
            new("SlowBackup", "https://api.backup/data", 100),
            new("FastCache", "https://api.cache/data", 10),
            new("MediumMain", "https://api.main/data", 50)
        };

        var fastest = await _aggregator.FetchFastestResponseAsync(endpoints);

        Assert.Equal("FastCache", fastest.EndpointName);
    }

    // TEST: ExecuteWithTimeoutAsync Returns Result When Finished In Time
    [Fact]
    public async Task Test_ExecuteWithTimeoutAsync_ReturnsResultOnSuccess()
    {
        var result = await _aggregator.ExecuteWithTimeoutAsync(async ct =>
        {
            await Task.Delay(10, ct);
            return 42;
        }, TimeSpan.FromMilliseconds(500));

        Assert.Equal(42, result);
    }

    // TEST: ExecuteWithTimeoutAsync Throws TimeoutException When Exceeded
    [Fact]
    public async Task Test_ExecuteWithTimeoutAsync_ThrowsTimeoutException()
    {
        await Assert.ThrowsAsync<TimeoutException>(async () =>
        {
            await _aggregator.ExecuteWithTimeoutAsync(async ct =>
            {
                await Task.Delay(500, ct);
                return "Too late";
            }, TimeSpan.FromMilliseconds(20));
        });
    }
}
