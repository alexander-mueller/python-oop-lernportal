package main

import (
	"fmt"
)

const (
	StatusStopped = iota
	StatusStarting
	StatusRunning
)

func GetServerConfig() (string, int, int, bool) {
	host := "localhost"
	port := 8080
	maxClients := 1000
	tlsEnabled := true
	return host, port, maxClients, tlsEnabled
}

func BerechneDurchschnitt(summe int, anzahl int) float64 {
	if anzahl <= 0 {
		return 0.0
	}
	return float64(summe) / float64(anzahl)
}

func FormatiereServerStatus(name string, port int, online bool) string {
	statusStr := "OFFLINE"
	if online {
		statusStr = "ONLINE"
	}
	return fmt.Sprintf("Server %s auf Port %d - Status: %s", name, port, statusStr)
}

func GetStatusName(status int) string {
	switch status {
	case StatusStopped:
		return "STOPPED"
	case StatusStarting:
		return "STARTING"
	case StatusRunning:
		return "RUNNING"
	default:
		return "UNKNOWN"
	}
}

func main() {
	host, port, maxC, tls := GetServerConfig()
	fmt.Printf("Config: %s:%d (Max: %d, TLS: %t)\n", host, port, maxC, tls)
	fmt.Printf("Avg: %.2f\n", BerechneDurchschnitt(150, 4))
	fmt.Println(FormatiereServerStatus("api-gw", 8080, true))
	fmt.Println("Status 2:", GetStatusName(StatusRunning))
}
