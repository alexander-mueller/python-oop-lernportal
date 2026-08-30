package main

import (
	"reflect"
	"testing"
)

func TestNewUser(t *testing.T) {
	u := NewUser(42, "tester", "test@domain.com")
	if u == nil {
		t.Fatalf("NewUser lieferte nil")
	}
	if u.ID != 42 || u.Username != "tester" || u.Email != "test@domain.com" || u.Active != true {
		t.Errorf("NewUser() Felder nicht korrekt initialisiert: %+v", *u)
	}
}

func TestUserInfoValueReceiver(t *testing.T) {
	u := User{ID: 10, Username: "alex", Email: "alex@go.dev", Active: true}
	info := u.Info()
	expected := "User #10: alex <alex@go.dev> (Aktiv: true)"
	if info != expected {
		t.Errorf("u.Info() = %q; erwartet %q", info, expected)
	}
}

func TestUserPointerReceiver(t *testing.T) {
	u := NewUser(1, "bob", "bob@old.com")
	u.UpdateEmail("bob@new.com")
	if u.Email != "bob@new.com" {
		t.Errorf("u.UpdateEmail() hat Email nicht auf 'bob@new.com' gesetzt, sondern %q", u.Email)
	}

	// Leere Email darf nichts ändern
	u.UpdateEmail("")
	if u.Email != "bob@new.com" {
		t.Errorf("u.UpdateEmail('') sollte alte Email beibehalten")
	}

	u.Deactivate()
	if u.Active != false {
		t.Errorf("u.Deactivate() hat Active nicht auf false gesetzt")
	}
}

func TestAdminUserEmbedding(t *testing.T) {
	admin := NewAdminUser(99, "super_admin", "admin@sec.org", "SecurityLead", true)
	if admin == nil {
		t.Fatalf("NewAdminUser lieferte nil")
	}

	// Test auf Promoted Fields
	if admin.Username != "super_admin" || admin.ID != 99 {
		t.Errorf("Promoted Field admin.Username = %s; erwartet 'super_admin'", admin.Username)
	}

	superPerms := admin.Permissions()
	expectedSuper := []string{"READ", "WRITE", "DELETE", "ADMIN"}
	if !reflect.DeepEqual(superPerms, expectedSuper) {
		t.Errorf("Permissions() für SuperAdmin = %v; erwartet %v", superPerms, expectedSuper)
	}

	standardAdmin := NewAdminUser(100, "mod_bob", "mod@sec.org", "Moderator", false)
	standardPerms := standardAdmin.Permissions()
	expectedStandard := []string{"READ", "WRITE"}
	if !reflect.DeepEqual(standardPerms, expectedStandard) {
		t.Errorf("Permissions() für StandardAdmin = %v; erwartet %v", standardPerms, expectedStandard)
	}
}
