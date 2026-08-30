package main

import (
	"fmt"
)

// 🎯 TEILZIEL 4 (TODO 4): Definiere die Server-Status-Konstanten mit iota
// StatusStopped = 0, StatusStarting = 1, StatusRunning = 2
const (
	StatusStopped = iota
	StatusStarting
	StatusRunning
)

// 🎯 TEILZIEL 1 (TODO 1): Gib Server-Konfigurationsdaten zurück
// Rückgabewerte: host (string), port (int), maxClients (int), tlsEnabled (bool)
// Erwartet: "localhost", 8080, 1000, true
func GetServerConfig() (string, int, int, bool) {
	// TODO: Deklariere die Variablen und gib sie zurück
	return "", 0, 0, false
}

// 🎯 TEILZIEL 2 (TODO 2): Berechne den genauen Durchschnitt als float64
// Falls anzahl <= 0 ist, soll 0.0 zurückgegeben werden.
// Achte auf explizite Typkonvertierung von int zu float64!
func BerechneDurchschnitt(summe int, anzahl int) float64 {
	// TODO: Konvertiere summe und anzahl zu float64 und führe die Division durch
	return 0.0
}

// 🎯 TEILZIEL 3 (TODO 3): Formatiere den Serverstatus als String
// Format: "Server [name] auf Port [port] - Status: [ONLINE/OFFLINE]"
// Beispiel: FormatiereServerStatus("api-gw", 8080, true) -> "Server api-gw auf Port 8080 - Status: ONLINE"
// Beispiel: FormatiereServerStatus("auth", 9000, false) -> "Server auth auf Port 9000 - Status: OFFLINE"
func FormatiereServerStatus(name string, port int, online bool) string {
	// TODO: Verwende fmt.Sprintf und prüfe das online-Flag
	return ""
}

// 🎯 TEILZIEL 4 (TODO 4): Gib den Textnamen für den Status-Code zurück
// 0 -> "STOPPED", 1 -> "STARTING", 2 -> "RUNNING", sonst -> "UNKNOWN"
func GetStatusName(status int) string {
	// TODO: Prüfe den status-Wert gegen die iota-Konstanten
	return ""
}

func main() {
	host, port, maxC, tls := GetServerConfig()
	fmt.Printf("Config: %s:%d (Max: %d, TLS: %t)\n", host, port, maxC, tls)
	fmt.Printf("Avg: %.2f\n", BerechneDurchschnitt(150, 4))
	fmt.Println(FormatiereServerStatus("api-gw", 8080, true))
	fmt.Println("Status 2:", GetStatusName(StatusRunning))
}
