package main

import (
	"fmt"
)

// 🧪 GO 10 TESTSUITE: Channels & Datenfluss

func assertEquals[T comparable](actual, expected T, msg string) {
	if actual != expected {
		panic(fmt.Sprintf("❌ Test fehlgeschlagen: %s (Erwartet: '%v', Erhalten: '%v')", msg, expected, actual))
	}
}

// TEST: TestLogRecordStruct - Überprüft Struct-Definition
func TestLogRecordStruct() {
	fmt.Println("=== RUN   TestLogRecordStruct")
	rec := LogRecord{
		ID:      101,
		Level:   "ERROR",
		Message: "Database timeout",
		Source:  "db-primary",
	}
	assertEquals(rec.ID, 101, "ID muss übereinstimmen")
	assertEquals(rec.Level, "ERROR", "Level muss ERROR sein")
	assertEquals(rec.Source, "db-primary", "Source muss db-primary sein")
	fmt.Println("--- PASS: TestLogRecordStruct")
}

// TEST: TestProduceLogsStream - Prüft den Log-Generator
func TestProduceLogsStream() {
	fmt.Println("=== RUN   TestProduceLogsStream")
	records := []LogRecord{
		{ID: 1, Level: "INFO", Message: "A", Source: "app"},
		{ID: 2, Level: "WARN", Message: "B", Source: "app"},
		{ID: 3, Level: "ERROR", Message: "C", Source: "app"},
	}

	ch := ProduceLogs(records)
	var received []LogRecord
	for item := range ch {
		received = append(received, item)
	}

	assertEquals(len(received), 3, "Generator muss genau 3 Records liefern")
	assertEquals(received[0].ID, 1, "Erster Eintrag muss ID 1 haben")
	assertEquals(received[2].ID, 3, "Dritter Eintrag muss ID 3 haben")
	fmt.Println("--- PASS: TestProduceLogsStream")
}

// TEST: TestFilterLogsPipeline - Prüft das Filtern im Channel-Stream
func TestFilterLogsPipeline() {
	fmt.Println("=== RUN   TestFilterLogsPipeline")
	records := []LogRecord{
		{ID: 1, Level: "INFO", Message: "A", Source: "app"},
		{ID: 2, Level: "ERROR", Message: "B", Source: "app"},
		{ID: 3, Level: "WARN", Message: "C", Source: "app"},
		{ID: 4, Level: "ERROR", Message: "D", Source: "app"},
	}

	stream := ProduceLogs(records)
	filtered := FilterLogs(stream, "ERROR")

	var errors []LogRecord
	for rec := range filtered {
		errors = append(errors, rec)
	}

	assertEquals(len(errors), 2, "Filter muss genau 2 ERROR-Logs zurückgeben")
	assertEquals(errors[0].ID, 2, "Erstes gefiltertes Log muss ID 2 haben")
	assertEquals(errors[1].ID, 4, "Zweites gefiltertes Log muss ID 4 haben")
	fmt.Println("--- PASS: TestFilterLogsPipeline")
}

// TEST: TestCountLogsByLevel - Prüft das Aggregieren von Events
func TestCountLogsByLevel() {
	fmt.Println("=== RUN   TestCountLogsByLevel")
	records := []LogRecord{
		{ID: 1, Level: "INFO", Message: "A", Source: "app"},
		{ID: 2, Level: "INFO", Message: "B", Source: "app"},
		{ID: 3, Level: "WARN", Message: "C", Source: "app"},
		{ID: 4, Level: "ERROR", Message: "D", Source: "app"},
		{ID: 5, Level: "INFO", Message: "E", Source: "app"},
	}

	stream := ProduceLogs(records)
	counts := CountLogsByLevel(stream)

	assertEquals(counts["INFO"], 3, "INFO-Anzahl muss 3 sein")
	assertEquals(counts["WARN"], 1, "WARN-Anzahl muss 1 sein")
	assertEquals(counts["ERROR"], 1, "ERROR-Anzahl muss 1 sein")
	assertEquals(counts["DEBUG"], 0, "Nicht existierende Keys müssen 0 liefern")
	fmt.Println("--- PASS: TestCountLogsByLevel")
}

func main() {
	fmt.Println("🧪 Starte Go 10 Testsuite...")
	TestLogRecordStruct()
	TestProduceLogsStream()
	TestFilterLogsPipeline()
	TestCountLogsByLevel()
	fmt.Println("\n✅ Alle Tests in Go 10 erfolgreich bestanden!")
}
