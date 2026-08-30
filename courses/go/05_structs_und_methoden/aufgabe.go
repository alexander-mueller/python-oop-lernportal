package main

import (
	"fmt"
)

// 🎯 TEILZIEL 1 (TODO 1): Definiere das Struct User und die Konstruktor-Funktion NewUser
// Felder in User:
// - ID (int)
// - Username (string)
// - Email (string)
// - Active (bool)
type User struct {
	ID       int
	Username string
	Email    string
	Active   bool
}

// NewUser initialisiert einen neuen User mit Active = true und gibt einen Zeiger (*User) zurück.
func NewUser(id int, username, email string) *User {
	// TODO: Initialisiere das Struct und gib den Pointer zurück
	return nil
}

// 🎯 TEILZIEL 2 (TODO 2): Implementiere die Methode Info() mit einem Value-Receiver (u User)
// Rückgabe-Format: "User #[ID]: [Username] <[Email]> (Aktiv: [true/false])"
// Beispiel: "User #1: gopher <gopher@golang.org> (Aktiv: true)"
func (u User) Info() string {
	// TODO: Formatiere den String mit fmt.Sprintf
	return ""
}

// 🎯 TEILZIEL 3 (TODO 3): Implementiere Methoden mit Pointer-Receiver (u *User)
// 1. Deactivate(): Setzt u.Active auf false.
// 2. UpdateEmail(newEmail string): Aktualisiert u.Email nur dann, wenn newEmail nicht leer ist ("").
func (u *User) Deactivate() {
	// TODO: u.Active auf false setzen
}

func (u *User) UpdateEmail(newEmail string) {
	// TODO: u.Email aktualisieren falls newEmail nicht leer
}

// 🎯 TEILZIEL 4 (TODO 4): Struct Embedding & AdminUser
// Definiere AdminUser mit:
// - User (eingebettetes anonymes Struct)
// - Role (string)
// - SuperAdmin (bool)
type AdminUser struct {
	User
	Role       string
	SuperAdmin bool
}

// NewAdminUser initialisiert einen AdminUser und gibt den Pointer zurück.
func NewAdminUser(id int, username, email, role string, superAdmin bool) *AdminUser {
	// TODO: AdminUser instanziieren und Pointer zurückgeben
	return nil
}

// Permissions() gibt ein Slice von Berechtigungen zurück:
// Ist SuperAdmin true: []string{"READ", "WRITE", "DELETE", "ADMIN"}
// Ist SuperAdmin false: []string{"READ", "WRITE"}
func (a *AdminUser) Permissions() []string {
	// TODO: Permissions basierend auf SuperAdmin zurückgeben
	return nil
}

func main() {
	u := NewUser(1, "gopher", "gopher@golang.org")
	if u != nil {
		fmt.Println(u.Info())
		u.UpdateEmail("dev@golang.org")
		u.Deactivate()
		fmt.Println("Nach Update:", u.Info())
	}

	admin := NewAdminUser(2, "admin_alice", "alice@cloud.io", "DevOpsLead", true)
	if admin != nil {
		fmt.Printf("Admin: %s, Rolle: %s, Rechte: %v\n", admin.Username, admin.Role, admin.Permissions())
	}
}
