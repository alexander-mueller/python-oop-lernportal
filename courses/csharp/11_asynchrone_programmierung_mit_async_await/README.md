# C# 11: Asynchrone Programmierung mit Async/Await & Task.WhenAll ⚡

Willkommen zu **Modul 11**! In modernen Microservices und Cloud-Architekturen ist nicht-blockierende, asynchrone Ein-/Ausgabe (I/O) unverzichtbar für maximale Skalierbarkeit und Durchsatz.

---

## 💡 1. Das Wichtigste in Kürze

### Die Kernbausteine: `async`, `await` & `Task<T>`
- **`Task`**: Repräsentiert eine laufende oder geplante asynchrone Operation ohne Rückgabewert.
- **`Task<T>`**: Repräsentiert eine asynchrone Operation, die ein Ergebnis vom Typ `T` liefert.
- **`async`**: Markiert eine Methode, die den `await`-Operator nutzen darf und transformiert den Code in eine compilergenerierte State Machine.
- **`await`**: Unterbricht die Ausführung der aktuellen Methode, gibt den ausführenden Thread an den ThreadPool zurück und setzt die Ausführung fort, sobald das Ergebnis verfügbar ist.

### Parallelisierung mit `Task.WhenAll`
```csharp
var taskA = FetchStockDataAsync("MSFT", ct);
var taskB = FetchStockDataAsync("GOOGL", ct);

// Beide Tasks laufen gleichzeitig!
string[] results = await Task.WhenAll(taskA, taskB);
```

### Kooperativer Abbruch mit `CancellationToken`
```csharp
public async Task ProcessDataAsync(CancellationToken ct)
{
    while (!ct.IsCancellationRequested)
    {
        await DoWorkChunkAsync(ct);
    }
    ct.ThrowIfCancellationRequested();
}
```

---

## 🎯 Teilziele in `Aufgabe.cs`

1. **TODO 1: `FetchServiceDataAsync`**  
   Simuliere einen asynchronen API-Aufruf mit `Task.Delay(delayMs, ct)` und gib eine `ServiceResponse` zurück.

2. **TODO 2: `AggregateServicesAsync`**  
   Starte die Abrufe für alle übergebenen Endpunkte parallel mit `Task.WhenAll` und sammle die Antworten.

3. **TODO 3: `FetchFastestResponseAsync`**  
   Verwende `Task.WhenAny`, um das Ergebnis des am schnellsten antwortenden Endpunkts abzugreifen.

4. **TODO 4: `ExecuteWithTimeoutAsync<T>`**  
   Kapsele eine asynchrone Funktion mit einem harten Timeout mittels `CancellationTokenSource(TimeSpan timeout)`.
