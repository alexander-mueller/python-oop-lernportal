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
    // ========================================================================
    // 🎯 TODO 1: Asynchroner Einzelabruf
    // Simuliere einen asynchronen HTTP-Aufruf mit await Task.Delay(endpoint.LatencyMs, ct).
    // Gib eine erfolgreiche ServiceResponse zurück:
    // EndpointName = endpoint.Name, Payload = "Data from " + endpoint.Url, Success = true.
    // Falls ct.IsCancellationRequested ist, soll Task.Delay eine OperationCanceledException werfen.
    // ========================================================================
    public async Task<ServiceResponse> FetchServiceDataAsync(ServiceEndpoint endpoint, CancellationToken ct = default)
    {
        throw new NotImplementedException();
    }

    // ========================================================================
    // 🎯 TODO 2: Parallele Aggregation mit Task.WhenAll
    // Starte für jeden Endpunkt in der Liste einen Task über FetchServiceDataAsync.
    // Führe alle Tasks parallel mit Task.WhenAll aus und gib die Liste aller Responses zurück.
    // ========================================================================
    public async Task<List<ServiceResponse>> AggregateServicesAsync(IEnumerable<ServiceEndpoint> endpoints, CancellationToken ct = default)
    {
        throw new NotImplementedException();
    }

    // ========================================================================
    // 🎯 TODO 3: Schnellste Antwort mit Task.WhenAny
    // Starte Tasks für alle Endpunkte.
    // Verwende await Task.WhenAny(tasks), um den zuerst fertigen Task zu identifizieren.
    // Gib das Ergebnis (ServiceResponse) dieses schnellsten Tasks zurück.
    // Falls endpoints leer ist, wirf eine ArgumentException.
    // ========================================================================
    public async Task<ServiceResponse> FetchFastestResponseAsync(IEnumerable<ServiceEndpoint> endpoints, CancellationToken ct = default)
    {
        throw new NotImplementedException();
    }

    // ========================================================================
    // 🎯 TODO 4: Timeout-Wrapper
    // Führe die asynchrone Operation 'operation' aus.
    // Wenn die Operation nicht innerhalb von 'timeout' fertig wird, bricht die CancellationTokenSource ab
    // und die Methode wirf eine TimeoutException mit der Meldung "Operation timed out.".
    // ========================================================================
    public async Task<T> ExecuteWithTimeoutAsync<T>(Func<CancellationToken, Task<T>> operation, TimeSpan timeout)
    {
        throw new NotImplementedException();
    }
}
