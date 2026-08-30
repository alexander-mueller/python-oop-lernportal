package main

import (
	"fmt"
)

// ============================================================================
// 💡 GO 10: MUSTERLÖSUNG (Channels & Streaming Pipelines)
// ============================================================================

// LogRecord repräsentiert ein strukturiertes Log-Ereignis.
type LogRecord struct {
	ID      int
	Level   string
	Message string
	Source  string
}

// ProduceLogs generiert einen Channel-Stream aus einer Log-Liste.
func ProduceLogs(records []LogRecord) <-chan LogRecord {
	bufSize := len(records)
	if bufSize < 1 {
		bufSize = 1
	}
	out := make(chan LogRecord, bufSize)

	go func() {
		defer close(out)
		for _, rec := range records {
			out <- rec
		}
	}()

	return out
}

// FilterLogs filtert einen eingehenden Log-Stream nach dem gewünschten Level.
func FilterLogs(in <-chan LogRecord, targetLevel string) <-chan LogRecord {
	out := make(chan LogRecord, 10)

	go func() {
		defer close(out)
		for record := range in {
			if record.Level == targetLevel {
				out <- record
			}
		}
	}()

	return out
}

// CountLogsByLevel aggregiert die Anzahl aller Logs gruppiert nach Log-Level.
func CountLogsByLevel(in <-chan LogRecord) map[string]int {
	counts := make(map[string]int)

	for record := range in {
		counts[record.Level]++
	}

	return counts
}

func main() {
	fmt.Println("=== Go 10: Musterlösung ===")

	sampleLogs := []LogRecord{
		{ID: 1, Level: "INFO", Message: "Service gestartet", Source: "gateway"},
		{ID: 2, Level: "WARN", Message: "Hohe Speicherauslastung", Source: "db"},
		{ID: 3, Level: "ERROR", Message: "Verbindungsabbruch", Source: "db"},
		{ID: 4, Level: "INFO", Message: "User Login", Source: "auth"},
		{ID: 5, Level: "ERROR", Message: "Timeout bei Zahlung", Source: "payment"},
	}

	// Pipeline: Produce -> Filter -> Output
	stream := ProduceLogs(sampleLogs)
	errorsOnly := FilterLogs(stream, "ERROR")

	fmt.Println("Gefilterte ERROR-Logs:")
	for errLog := range errorsOnly {
		fmt.Printf("  🚨 [%d] %s: %s (Source: %s)\n", errLog.ID, errLog.Level, errLog.Message, errLog.Source)
	}
}
