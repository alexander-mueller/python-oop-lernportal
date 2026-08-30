package main

import (
	"fmt"
)

// ============================================================================
// 🚀 GO 10: CHANNELS & DATENFLUSS (STREAMING PIPELINES)
// ============================================================================

// 🎯 TODO 1: Definiere das Struct 'LogRecord'
// Felder:
// - ID      int    (Eindeutige fortlaufende ID)
// - Level   string ("INFO", "WARN", "ERROR", "FATAL")
// - Message string (Beschreibung des Ereignisses)
// - Source  string (z.B. "auth-service", "payment-api")
type LogRecord struct {
	// TODO: Ergänze die Struct-Felder
	ID      int
	Level   string
	Message string
	Source  string
}

// 🎯 TODO 2: Implementiere den Generator 'ProduceLogs'
// Parameter:
// - records: Ein Slice von LogRecords
// Rückgabe:
// - Ein Receive-Only Channel (<-chan LogRecord)
//
// Anforderungen:
// 1. Erstelle einen Channel 'out' mit Puffergröße len(records) (mindestens 1).
// 2. Starte eine Goroutine, die:
//    - Mit 'defer close(out)' sicherstellt, dass der Channel nach getaner Arbeit geschlossen wird.
//    - Über 'records' iteriert und jedes Element in 'out' sendet.
// 3. Gib den Channel 'out' sofort an den Aufrufer zurück.
func ProduceLogs(records []LogRecord) <-chan LogRecord {
	// TODO: Generator-Goroutine starten und out-Channel zurückgeben
	return nil
}

// 🎯 TODO 3: Implementiere die Pipeline-Stufe 'FilterLogs'
// Parameter:
// - in: Receive-Only Channel (<-chan LogRecord)
// - targetLevel: Der gesuchte Log-Level (z.B. "ERROR")
// Rückgabe:
// - Ein Receive-Only Channel (<-chan LogRecord) mit gefilterten Einträgen
//
// Anforderungen:
// 1. Erstelle einen Ausgangskanal 'out' (z.B. Puffergröße 10).
// 2. Starte eine Goroutine, die:
//    - 'defer close(out)' aufruft.
//    - Mit 'for record := range in' über alle eingehenden Logs iteriert.
//    - Wenn 'record.Level == targetLevel' ist, sende 'record' in 'out'.
// 3. Gib 'out' zurück.
func FilterLogs(in <-chan LogRecord, targetLevel string) <-chan LogRecord {
	// TODO: Filter-Goroutine starten und gefilterten out-Channel zurückgeben
	return nil
}

// 🎯 TODO 4: Implementiere den Consumer 'CountLogsByLevel'
// Parameter:
// - in: Receive-Only Channel (<-chan LogRecord)
// Rückgabe:
// - Eine Map mit der Anzahl der Logs pro Level, z.B. {"INFO": 5, "ERROR": 2}
//
// Anforderungen:
// 1. Initialisiere eine Map: counts := make(map[string]int).
// 2. Iteriere mit 'for record := range in' bis der Channel geschlossen wird.
// 3. Erhöhe für jedes Level den entsprechenden Zähler.
// 4. Gib 'counts' zurück.
func CountLogsByLevel(in <-chan LogRecord) map[string]int {
	// TODO: Channel auslesen und Vorkommen aggregieren
	return nil
}

func main() {
	fmt.Println("=== Go 10: Channels & Datenfluss ===")

	sampleLogs := []LogRecord{
		{ID: 1, Level: "INFO", Message: "Service gestartet", Source: "gateway"},
		{ID: 2, Level: "WARN", Message: "Hohe Speicherauslastung", Source: "db"},
		{ID: 3, Level: "ERROR", Message: "Verbindungsabbruch", Source: "db"},
		{ID: 4, Level: "INFO", Message: "User Login", Source: "auth"},
		{ID: 5, Level: "ERROR", Message: "Timeout bei Zahlung", Source: "payment"},
	}

	// 1. Pipeline aufbauen: Produce -> Filter -> Collect
	stream := ProduceLogs(sampleLogs)
	errorsOnly := FilterLogs(stream, "ERROR")

	fmt.Println("Gefilterte ERROR-Logs:")
	for errLog := range errorsOnly {
		fmt.Printf("  🚨 [%d] %s: %s (Source: %s)\n", errLog.ID, errLog.Level, errLog.Message, errLog.Source)
	}
}
