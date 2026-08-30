package main

import (
	"fmt"
	"sort"
	"strings"
	"sync"
	"time"
)

// ============================================================================
// 💡 GO 09: MUSTERLÖSUNG (Goroutines & sync.WaitGroup)
// ============================================================================

// ServerMetric repräsentiert das Ergebnis eines Server-Health-Checks.
type ServerMetric struct {
	ServerID  string
	LatencyMs int
	Status    string
	Timestamp time.Time
}

// CheckServer prüft einen Server asynchron und meldet das Ergebnis via Channel.
func CheckServer(serverID string, wg *sync.WaitGroup, out chan<- ServerMetric) {
	defer wg.Done()

	status := "ONLINE"
	latency := 15

	if strings.HasPrefix(serverID, "offline-") {
		status = "OFFLINE"
		latency = 999
	} else if strings.HasPrefix(serverID, "slow-") {
		status = "DEGRADED"
		latency = 250
	}

	metric := ServerMetric{
		ServerID:  serverID,
		LatencyMs: latency,
		Status:    status,
		Timestamp: time.Now(),
	}

	out <- metric
}

// BatchHealthCheck führt nebenläufige Server-Checks durch und synchronisiert sie via sync.WaitGroup.
func BatchHealthCheck(servers []string) []ServerMetric {
	if len(servers) == 0 {
		return []ServerMetric{}
	}

	var wg sync.WaitGroup
	out := make(chan ServerMetric, len(servers))

	for _, srv := range servers {
		wg.Add(1)
		go CheckServer(srv, &wg, out)
	}

	// Goroutine zum Schließen des Channels nach Abschluss aller Worker
	go func() {
		wg.Wait()
		close(out)
	}()

	var results []ServerMetric
	for metric := range out {
		results = append(results, metric)
	}

	// Sortieren nach ServerID für deterministische Ausgabe
	sort.Slice(results, func(i, j int) bool {
		return results[i].ServerID < results[j].ServerID
	})

	return results
}

// ParallelTaskRunner führt generische Tasks parallel aus und sammelt Ergebnisse indexgetreu.
func ParallelTaskRunner(tasks []func() string) []string {
	if len(tasks) == 0 {
		return []string{}
	}

	results := make([]string, len(tasks))
	var wg sync.WaitGroup

	for i, task := range tasks {
		wg.Add(1)
		go func(idx int, t func() string) {
			defer wg.Done()
			results[idx] = t()
		}(i, task)
	}

	wg.Wait()
	return results
}

func main() {
	fmt.Println("=== Go 09: Musterlösung ===")

	serverList := []string{"srv-01", "slow-node-02", "srv-03", "offline-backup"}
	metrics := BatchHealthCheck(serverList)

	fmt.Printf("Ergebnis des Health-Checks (%d Server):\n", len(metrics))
	for _, m := range metrics {
		fmt.Printf("  • %-15s => Status: %-8s (Latenz: %3d ms) @ %s\n",
			m.ServerID, m.Status, m.LatencyMs, m.Timestamp.Format("15:04:05.000"))
	}
}
