"""
🌿 GIT-MITMACH-ÜBUNG 🌿
=======================
Diese Datei ist für dein erstes Git-Experiment da!

ANLEITUNG:
1. Ändere die Variable 'dein_name' unten zu deinem echten Vornamen.
2. Füge eine neue Lieblingsprogrammiersprache oder ein Hobby zur Liste hinzu.
3. Speichere die Datei mit Strg + S (Mac: Cmd + S).
4. Öffne links in VS Code den Quellcodeverwaltungs-Tab (Strg + Shift + G).
5. Klicke auf 'git_uebung.py', um die roten/grünen Änderungen zu sehen!
6. Gib oben eine Nachricht ein wie: "Update git_uebung mit meinem Namen"
7. Klicke auf das blaue Häkchen (Commit).
"""

dein_name = "Nachhilfe-Schülerin"
lieblings_sprachen = ["Python", "HTML", "CSS"]
lieblings_feature_in_python = "Objektorientierte Programmierung mit Klassen!"


def begruessung():
    return f"Hallo! Ich bin {dein_name} und lerne gerade Git & Versionskontrolle! 🎉"


if __name__ == "__main__":
    print("=" * 60)
    print(begruessung())
    print("Meine Sprachen:", ", ".join(lieblings_sprachen))
    print("Mein Lieblings-Feature:", lieblings_feature_in_python)
    print("=" * 60)
