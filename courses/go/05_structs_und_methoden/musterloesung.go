package main

import (
	"fmt"
)

type User struct {
	ID       int
	Username string
	Email    string
	Active   bool
}

func NewUser(id int, username, email string) *User {
	return &User{
		ID:       id,
		Username: username,
		Email:    email,
		Active:   true,
	}
}

func (u User) Info() string {
	return fmt.Sprintf("User #%d: %s <%s> (Aktiv: %t)", u.ID, u.Username, u.Email, u.Active)
}

func (u *User) Deactivate() {
	if u != nil {
		u.Active = false
	}
}

func (u *User) UpdateEmail(newEmail string) {
	if u != nil && newEmail != "" {
		u.Email = newEmail
	}
}

type AdminUser struct {
	User
	Role       string
	SuperAdmin bool
}

func NewAdminUser(id int, username, email, role string, superAdmin bool) *AdminUser {
	return &AdminUser{
		User: User{
			ID:       id,
			Username: username,
			Email:    email,
			Active:   true,
		},
		Role:       role,
		SuperAdmin: superAdmin,
	}
}

func (a *AdminUser) Permissions() []string {
	if a != nil && a.SuperAdmin {
		return []string{"READ", "WRITE", "DELETE", "ADMIN"}
	}
	return []string{"READ", "WRITE"}
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
