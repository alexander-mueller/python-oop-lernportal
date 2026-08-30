package main

import (
	"testing"
)

func TestGetServerConfig(t *testing.T) {
	host, port, maxClients, tls := GetServerConfig()
	if host != "localhost" {
		t.Errorf("GetServerConfig() Host = %s; erwartet 'localhost'", host)
	}
	if port != 8080 {
		t.Errorf("GetServerConfig() Port = %d; erwartet 8080", port)
	}
	if maxClients != 1000 {
		t.Errorf("GetServerConfig() MaxClients = %d; erwartet 1000", maxClients)
	}
	if tls != true {
		t.Errorf("GetServerConfig() TlsEnabled = %t; erwartet true", tls)
	}
}

func TestBerechneDurchschnitt(t *testing.T) {
	cases := []struct {
		summe    int
		anzahl   int
		expected float64
	}{
		{150, 4, 37.5},
		{10, 3, 3.3333333333333335},
		{0, 5, 0.0},
		{100, 0, 0.0},
		{50, -2, 0.0},
	}

	for _, c := range cases {
		result := BerechneDurchschnitt(c.summe, c.anzahl)
		diff := result - c.expected
		if diff < -0.0001 || diff > 0.0001 {
			t.Errorf("BerechneDurchschnitt(%d, %d) = %f; erwartet %f", c.summe, c.anzahl, result, c.expected)
		}
	}
}

func TestFormatiereServerStatus(t *testing.T) {
	s1 := FormatiereServerStatus("api-gw", 8080, true)
	expected1 := "Server api-gw auf Port 8080 - Status: ONLINE"
	if s1 != expected1 {
		t.Errorf("FormatiereServerStatus() = %q; erwartet %q", s1, expected1)
	}

	s2 := FormatiereServerStatus("auth-service", 9000, false)
	expected2 := "Server auth-service auf Port 9000 - Status: OFFLINE"
	if s2 != expected2 {
		t.Errorf("FormatiereServerStatus() = %q; erwartet %q", s2, expected2)
	}
}

func TestGetStatusName(t *testing.T) {
	if GetStatusName(StatusStopped) != "STOPPED" {
		t.Errorf("GetStatusName(StatusStopped) = %q; erwartet 'STOPPED'", GetStatusName(StatusStopped))
	}
	if GetStatusName(StatusStarting) != "STARTING" {
		t.Errorf("GetStatusName(StatusStarting) = %q; erwartet 'STARTING'", GetStatusName(StatusStarting))
	}
	if GetStatusName(StatusRunning) != "RUNNING" {
		t.Errorf("GetStatusName(StatusRunning) = %q; erwartet 'RUNNING'", GetStatusName(StatusRunning))
	}
	if GetStatusName(99) != "UNKNOWN" {
		t.Errorf("GetStatusName(99) = %q; erwartet 'UNKNOWN'", GetStatusName(99))
	}
}
