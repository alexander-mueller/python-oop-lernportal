package main

import (
	"fmt"
	"sort"
	"sync"
	"time"
)

// ============================================================================
// 🚀 GO 09: GOROUTINES & SYNC.WAITGROUP
// ============================================================================

// 🎯 TODO 1: Definiere das Struct 'ServerMetric'
// Felder:
// - ServerID   string    (z.B. "srv-eu-central-1")
// - LatencyMs  int       (z.B. 42)
// - Status     string    (z.B. "ONLINE", "DEGRADED", "OFFLINE")
// - Timestamp  time.Time (Zeitpunkt der Prüfung)
type ServerMetric struct {
	// TODO: Ergänze die Struct-Felder
	ServerID  string
	LatencyMs int
	Status    string
	Timestamp time.Time
}

// 🎯 TODO 2: Implementiere die Worker-Funktion 'CheckServer'
// Parameter:
// - serverID: Die ID des zu prüfenden Servers
// - wg: Zeiger auf die sync.WaitGroup (*sync.WaitGroup)
// - out: Sende-Kanal (chan<- ServerMetric), in den das Ergebnis geschrieben wird
//
// Anforderungen:
// 1. Rufe sofort per 'defer' wg.Done() auf.
// 2. Simuliere eine Status-Ermittlung:
//    - Status ist "OFFLINE", wenn serverID mit "offline-" beginnt (LatencyMs = 999).
//    - Status ist "DEGRADED", wenn serverID mit "slow-" beginnt (LatencyMs = 250).
//    - Sonst Status "ONLINE" (LatencyMs = 15).
// 3. Sende die erstellte ServerMetric in den Channel 'out'.
func CheckServer(serverID string, wg *sync.WaitGroup, out chan<- ServerMetric) {
	// TODO: wg.Done() via defer aufrufen, Metrik ermitteln und in out schreiben
}

// 🎯 TODO 3: Implementiere 'BatchHealthCheck'
// Führt für eine Liste von Server-IDs nebenläufige Checks aus.
//
// Anforderungen:
// 1. Erstelle eine sync.WaitGroup und einen gepufferten Channel mit der Kapazität len(servers).
// 2. Iteriere über 'servers', rufe wg.Add(1) auf und starte 'CheckServer' als Goroutine.
// 3. Verwende eine separate Goroutine, die wg.Wait() aufruft und anschließend den Channel schließt (close(out)).
// 4. Lese alle Metriken mit einer 'for m := range out' Schleife in einen Slice ein.
// 5. Sortiere die Metriken aufsteigend nach 'ServerID'.
// 6. Gib den sortierten Slice zurück.
func BatchHealthCheck(servers []string) []ServerMetric {
	// TODO: Parallele Checks mit sync.WaitGroup und Channel ausführen
	return nil
}

// 🎯 TODO 4: Implementiere 'ParallelTaskRunner'
// Führt eine Liste generischer Tasks (Funktionen func() string) parallel aus.
//
// Anforderungen:
// 1. Initialisiere einen Ergebnis-Slice der Länge len(tasks): results := make([]string, len(tasks)).
// 2. Starte für jeden Task (Index i und Funktion task) eine Goroutine mit 'wg.Add(1)'.
// 3. Jede Goroutine führt ihren Task aus und schreibt das Ergebnis direkt an results[i] (Index-Isolation).
// 4. Warte mit wg.Wait() auf alle Tasks und gib 'results' zurück.
func ParallelTaskRunner(tasks []func() string) []string {
	// TODO: Tasks nebenläufig ausführen und indexbasiert synchronisieren
	return nil
}

func main() {
	fmt.Println("=== Go 09: Goroutines & sync.WaitGroup ===")

	serverList := []string{"srv-01", "slow-node-02", "srv-03", "offline-backup"}
	metrics := BatchHealthCheck(serverList)

	fmt.Printf("Ergebnis des Health-Checks (%d Server):\n", len(metrics))
	for _, m := range metrics {
		fmt.Printf("  • %-15s => Status: %-8s (Latenz: %3d ms) @ %s\n",
			m.ServerID, m.Status, m.LatencyMs, m.Timestamp.Format("15:04:05.000"))
	}
}
