using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

namespace CSharpKurs.Modul11;

public record ServiceEndpoint(string Name, string Url, int LatencyMs);
public record ServiceResponse(string EndpointName, string Payload, bool Success);

public class CloudDataAggregator
{
    // 🎯 LÖSUNG TODO 1: Asynchroner Einzelabruf
    public async Task<ServiceResponse> FetchServiceDataAsync(ServiceEndpoint endpoint, CancellationToken ct = default)
    {
        ArgumentNullException.ThrowIfNull(endpoint);

        await Task.Delay(endpoint.LatencyMs, ct);

        return new ServiceResponse(
            EndpointName: endpoint.Name,
            Payload: $"Data from {endpoint.Url}",
            Success: true
        );
    }

    // 🎯 LÖSUNG TODO 2: Parallele Aggregation mit Task.WhenAll
    public async Task<List<ServiceResponse>> AggregateServicesAsync(IEnumerable<ServiceEndpoint> endpoints, CancellationToken ct = default)
    {
        ArgumentNullException.ThrowIfNull(endpoints);

        var tasks = endpoints.Select(ep => FetchServiceDataAsync(ep, ct));
        var results = await Task.WhenAll(tasks);

        return results.ToList();
    }

    // 🎯 LÖSUNG TODO 3: Schnellste Antwort mit Task.WhenAny
    public async Task<ServiceResponse> FetchFastestResponseAsync(IEnumerable<ServiceEndpoint> endpoints, CancellationToken ct = default)
    {
        ArgumentNullException.ThrowIfNull(endpoints);

        var taskList = endpoints.Select(ep => FetchServiceDataAsync(ep, ct)).ToList();
        if (taskList.Count == 0)
        {
            throw new ArgumentException("Endpoints collection must not be empty.", nameof(endpoints));
        }

        var completedTask = await Task.WhenAny(taskList);
        return await completedTask;
    }

    // 🎯 LÖSUNG TODO 4: Timeout-Wrapper
    public async Task<T> ExecuteWithTimeoutAsync<T>(Func<CancellationToken, Task<T>> operation, TimeSpan timeout)
    {
        ArgumentNullException.ThrowIfNull(operation);

        using var cts = new CancellationTokenSource(timeout);

        try
        {
            return await operation(cts.Token);
        }
        catch (OperationCanceledException) when (cts.IsCancellationRequested)
        {
            throw new TimeoutException("Operation timed out.");
        }
    }
}
