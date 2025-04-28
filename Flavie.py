import tkinter as tk
from tkinter import messagebox
import threading
import random
import time

TAILLE_LABYRINTHE = 6
TOP_RECORDS = 10
records = []

def generer_labyrinthe():
    lab = [["piège" for _ in range(TAILLE_LABYRINTHE)] for _ in range(TAILLE_LABYRINTHE)]
    x, y = 0, 0
    lab[x][y] = "entrée"
    while (x, y) != (TAILLE_LABYRINTHE - 1, TAILLE_LABYRINTHE - 1):
        lab[x][y] = "chemin"
        direction = random.choice([(0, 1), (1, 0)])  # Droite ou Bas
        nx, ny = x + direction[0], y + direction[1]
        if 0 <= nx < TAILLE_LABYRINTHE and 0 <= ny < TAILLE_LABYRINTHE:
            x, y = nx, ny
    lab[x][y] = "sortie"
    return lab

labyrinthe = generer_labyrinthe()
commandes = {'O': (-1,0), 'K': (0,-1), 'L': (0,1), 'M': (1,0)}

def afficher_labyrinthe(position):
    for i, ligne in enumerate(labyrinthe):
        for j, case in enumerate(ligne):
            if (i, j) == position:
                print("[X]", end=" ")
            else:
                print("[ ]" if case != "piège" else "[ ]", end=" ")
        print()
def perdre():
    reponse = messagebox.askretrycancel("Défaite", "Oh non ! Tu es tombé dans un piège ! Recommencer ?")
    if reponse:
        jouer_labyrinthe(False)
    else:
        root.destroy()
def gagner(temps):
    global records, labyrinthe
    records.append(temps)
    records = sorted(records)[:TOP_RECORDS]
    messagebox.showinfo("Victoire", f"Félicitations ! Tu as trouvé la sortie en {temps:.2f} secondes !\n\nTop 10 des records :\n" + "\n".join(f"{i+1}. {t:.2f}s" for i, t in enumerate(records)))
    labyrinthe = generer_labyrinthe()
    root.destroy()
