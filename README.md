# 🐍 Python OOP Übungsreihe: Der Einstieg in Klassen & Objekte

Willkommen zu deiner Übungsreihe für **Objektorientierte Programmierung (OOP)** in Python! 🎉

Hier lernst du Schritt für Schritt, wie man mit Klassen arbeitet, warum sie die Programmierung übersichtlicher machen und wie du deine eigenen, mächtigen Objekte baust.

---

## 🗺️ Der Lernpfad

Die Übungen sind so aufgebaut, dass jedes Kapitel auf dem vorherigen aufbaut:

| Kapitel | Thema | Was du lernst |
| :--- | :--- | :--- |
| **[01. Einstieg in Klassen](./01_einstieg_klassen/)** | Warum Klassen? | Bauplan vs. Objekt, Instanziierung & Attribute |
| **[02. Konstruktor & self](./02_init_und_self/)** | `__init__` & `self` | Objekte sauber mit Startwerten initialisieren |
| **[03. Methoden & Verhalten](./03_methoden_und_verhalten/)** | Methoden & Interaktion | Objekte können handeln & miteinander interagieren |
| **[04. Schöne Textausgabe](./04_str_und_darstellung/)** | `__str__` Dunder-Methode | Wie Objekte lesbar mit `print()` ausgegeben werden |
| **[05. Objekte kombinieren](./05_objekte_kombinieren/)** | Komposition | Listen von Objekten & komplexe Datenstrukturen |
| **[06. Abschlussprojekt](./06_abschlussprojekt_tamagotchi/)** | Mini-Projekt: Tamagotchi | Ein interaktives Konsolenspiel mit allem Gelernten |

---

## 📁 Aufbau eines Kapitels

In jedem Kapitelordner findest du:
1. **`README.md`**: Eine verständliche Erklärung mit Analogien aus dem Alltag und Codebeispielen.
2. **`aufgabe.py`**: Dein Arbeitsblatt! Hier steht der Starter-Code mit klaren `TODO`-Kommentaren.
3. **`test_aufgabe.py`**: Automatische Tests, mit denen du deine Lösung jederzeit überprüfen kannst.
4. **`musterloesung.py`**: Eine ausführlich kommentierte Beispiellösung (falls du mal nicht weiterkommst oder vergleichen möchtest).

---

## 🚀 Wie du vorgehst

1. Öffne den Ordner des aktuellen Kapitels (z.B. `01_einstieg_klassen`).
2. Lies dir die Erklärung in der jeweiligen `README.md` durch.
3. Öffne `aufgabe.py` und bearbeite die nummerierten `TODO`s.
4. Führe die Tests aus, um deine Lösung zu prüfen:
   ```bash
   # Aus dem Hauptverzeichnis:
   python3 -m unittest 01_einstieg_klassen/test_aufgabe.py

   # Oder direkt im Ordner:
   cd 01_einstieg_klassen
   python3 test_aufgabe.py
   ```
5. Wenn alle Tests mit einem grünen `OK` durchlaufen: **Herzlichen Glückwunsch!** Du bist bereit für das nächste Kapitel! 🏆

---

## 💡 Tipp zum Lernen
Versuche zuerst selbst eine Lösung zu finden. Wenn ein Fehler auftritt, lies die Fehlermeldung der Tests aufmerksam durch – sie gibt dir oft schon den entscheidenden Hinweis! Wenn du gar nicht weiterkommst, wirf einen Blick in `musterloesung.py` und versuche zu verstehen, wie das Problem gelöst wurde.
