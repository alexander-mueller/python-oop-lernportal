#!/usr/bin/env python3
"""
🪪 ENTWICKLER-PROFIL & GAMIFICATION PASS 🪪
===========================================
Führe diesen Befehl im Terminal aus, um deinen aktuellen Level,
deine XP, deinen Fortschrittsbalken und deine Trophäen anzuzeigen:
    python3 profil.py
"""

import sys
from gamification import GamificationManager, BADGES_KATALOG

# ANSI Farbcodes für ansprechende Terminal-Optik
C_RESET = "\033[0m"
C_BOLD = "\033[1m"
C_CYAN = "\033[36m"
C_GREEN = "\033[32m"
C_YELLOW = "\033[33m"
C_BLUE = "\033[34m"
C_MAGENTA = "\033[35m"
C_RED = "\033[31m"


def erstelle_balken(prozent: int, breite: int = 30) -> str:
    """Erzeugt einen visuellen Unicode-Fortschrittsbalken."""
    gefuellt = int((prozent / 100) * breite)
    leer = breite - gefuellt
    return f"{C_GREEN}{'█' * gefuellt}{C_RESET}{'░' * leer}"


def main():
    manager = GamificationManager()
    state = manager.state
    xp = state.get("xp", 0)
    lvl_info = manager.get_level_info(xp)
    geloest = state.get("geloeste_kapitel", [])
    unlocked_badges = set(state.get("freigeschaltete_badges", []))
    streak = state.get("streak_tage", 1)
    name = state.get("spieler_name", "Python-Entwicklerin")
    titel = lvl_info["titel"]
    rang = lvl_info["rang"]
    tests_count = state.get("bestandene_tests", 0)
    kapitel_str = f"{len(geloest)} / 27 Kapiteln gelöst ({tests_count} Tests)"
    streak_str = f"{streak} Tag(e) in Folge aktiv!"

    print()
    print(f"{C_CYAN}╔══════════════════════════════════════════════════════════════════════╗{C_RESET}")
    print(f"{C_CYAN}║{C_RESET} {C_BOLD}🎮 PYTHON ENTWICKLER-PROFIL & MEISTERPASS{C_RESET}                            {C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╠══════════════════════════════════════════════════════════════════════╣{C_RESET}")
    print(f"{C_CYAN}║{C_RESET} 👤 {C_BOLD}Entwicklerin:{C_RESET}  {name:<48} {C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}║{C_RESET} 🏅 {C_BOLD}Titel:{C_RESET}         {titel:<48} {C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}║{C_RESET} ⭐ {C_BOLD}Rang:{C_RESET}          {rang:<48} {C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}║{C_RESET} 🔥 {C_BOLD}Lern-Streak:{C_RESET}   {streak_str:<48} {C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}║{C_RESET} 📚 {C_BOLD}Fortschritt:{C_RESET}   {kapitel_str:<48} {C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╠══════════════════════════════════════════════════════════════════════╣{C_RESET}")
    print(f"{C_CYAN}║{C_RESET} 📈 {C_BOLD}LEVEL {lvl_info['level']:2d} FORTSCHRITT:{C_RESET}                                              {C_CYAN}║{C_RESET}")
    
    balken = erstelle_balken(lvl_info["prozent"], breite=35)
    xp_text = f"{xp} / {lvl_info['naechste_stufe_xp']} XP ({lvl_info['prozent']}%)"
    print(f"{C_CYAN}║{C_RESET}    [{balken}] {xp_text:<17} {C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╠══════════════════════════════════════════════════════════════════════╣{C_RESET}")
    print(f"{C_CYAN}║{C_RESET} 🏆 {C_BOLD}TROPHÄENRAUM ({len(unlocked_badges)} von {len(BADGES_KATALOG)} freigeschaltet):{C_RESET}                           {C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╟──────────────────────────────────────────────────────────────────────╢{C_RESET}")

    # Badges auflisten
    for b_id, badge in BADGES_KATALOG.items():
        if b_id in unlocked_badges:
            status = f"{C_GREEN}[FREIGESCHALTET]{C_RESET}"
            icon = badge["icon"]
            name_colored = f"{C_YELLOW}{badge['name']}{C_RESET}"
        else:
            status = f"{C_RESET}[GESPERRT 🔒]{C_RESET}"
            icon = "🔒"
            name_colored = f"{badge['name']}"
            
        print(f"{C_CYAN}║{C_RESET}  {icon} {name_colored:<36} {status:>24} {C_CYAN}║{C_RESET}")
        print(f"{C_CYAN}║{C_RESET}     ↳ {badge['desc']:<63} {C_CYAN}║{C_RESET}")

    print(f"{C_CYAN}╚══════════════════════════════════════════════════════════════════════╝{C_RESET}")
    print(f"💡 {C_BOLD}Tipp:{C_RESET} Löse weitere Aufgaben in 'aufgabe.py' und teste sie mit 'python3 test_all.py'!")
    print()


if __name__ == "__main__":
    main()
