import random
import time
import json
import winsound
import tkinter as tk
from tkinter import messagebox
import pygame

# ===========================
# INTRODUCTION DU JEU
# ===========================

def introduction():
    print("\n[INTRODUCTION]")
    print("Tu ouvres les yeux dans un espace confiné. L'air est glacé, chargé d'électricité statique.")
    print("Devant toi, un miroir fêlé, des parois métalliques... et un écran rouge affichant \"ÉTAGE ???\".")
    input("Appuie sur Entrée pour continuer...")

# ===========================
# JEU 1 : SERRURE MUSICALE
# ===========================

notes = {1: "GRAVE", 2: "MOYEN", 3: "AIGU", 4: "TRÈS AIGU"}
frequences = {1: 262, 2: 440, 3: 660, 4: 880}


def serrure_musicale():
    print("\n[DÉFI 1 : La Serrure Musicale]")
    print("Écoute attentivement, chaque note est une clé différente...")
    boutons_possibles = [1, 2, 3, 4]
    sequence_sons = [random.choice(boutons_possibles) for _ in range(3)]
    erreurs_consecutives = 0
    bonne_reponse = False

    while erreurs_consecutives < 3 and not bonne_reponse:
        print("\nLa mélodie :")
        for bouton in sequence_sons:
            winsound.Beep(frequences[bouton], 500)
            time.sleep(0.3)

        reponse = input("Entre la séquence des numéros (ex : 1 3 2) : ").strip().split()
        try:
            reponse_joueur = [int(num) for num in reponse]
        except ValueError:
            print("Erreur de saisie.")
            continue

        if reponse_joueur == sequence_sons:
            print("Bravo, la serrure est ouverte !")
            bonne_reponse = True
        else:
            erreurs_consecutives += 1
            print("Mauvaise séquence...")
            if erreurs_consecutives >= 3:
                print("La bonne séquence était :", sequence_sons)

    return bonne_reponse

# ===========================
# JEU 2 : LABYRINTHE PIÉGÉ
# ===========================

TAILLE_LABYRINTHE = 6
labyrinthe = [["piège" for _ in range(TAILLE_LABYRINTHE)] for _ in range(TAILLE_LABYRINTHE)]


def generer_labyrinthe():
    x, y = 0, 0
    labyrinthe[x][y] = "entrée"
    while (x, y) != (TAILLE_LABYRINTHE - 1, TAILLE_LABYRINTHE - 1):
        labyrinthe[x][y] = "chemin"
        direction = random.choice([(0, 1), (1, 0)])
        nx, ny = x + direction[0], y + direction[1]
        if 0 <= nx < TAILLE_LABYRINTHE and 0 <= ny < TAILLE_LABYRINTHE:
            x, y = nx, ny
    labyrinthe[x][y] = "sortie"

def labyrinthe_piege():
    print("\n[DÉFI 2 : Le Labyrinthe Piégé]")
    commandes = {'O': (-1, 0), 'K': (0, -1), 'L': (0, 1), 'M': (1, 0)}
    generer_labyrinthe()
    position = [0, 0]
    tentative = 0

    while True:
        mouvement = input("O (haut), K (gauche), L (droite), M (bas) : ").upper()
        if mouvement not in commandes:
            print("Commande invalide.")
            continue
        tentative += 1
        move = commandes[mouvement]
        new_x, new_y = position[0] + move[0], position[1] + move[1]
        if 0 <= new_x < TAILLE_LABYRINTHE and 0 <= new_y < TAILLE_LABYRINTHE:
            position = [new_x, new_y]
            case = labyrinthe[new_x][new_y]
            if case == "piège":
                print("Piège ! Retour à la case départ.")
                position = [0, 0]
            elif case == "sortie":
                print(f"Bravo, sortie trouvée en {tentative} déplacements !")
                return True
        else:
            print("Impossible de sortir du labyrinthe.")

# ===========================
# JEU 3 : MESSAGE CODÉ
# ===========================

greek_alphabet = {
    'f': 'α', 'h': 'β', 't': 'γ', 'r': 'δ', 'z': 'ε', 'a': 'ζ', 'n': 'η', 'l': 'θ',
    'b': 'ι', 'o': 'κ', 'j': 'λ', 'e': 'μ', 'c': 'ν', 'd': 'ξ', 'g': 'ο', 's': 'π',
    'm': 'ρ', 'i': 'σ', 'p': 'τ', 'q': 'υ', 'y': 'φ', 'u': 'χ', 'v': 'ψ', 'w': 'ω'
}
messages = ["chat", "pomme", "arbre", "livre", "ciel"]

def message_code():
    print("\n[DÉFI 3 : Le Message Codé]")
    original = random.choice(messages)
    message_grec = ''.join([greek_alphabet.get(c, c) for c in original])
    print("Message codé en grec :", message_grec)

    essais = 0
    while True:
        guess = input("Quelle est la traduction ? ").lower().strip()
        essais += 1
        if guess == original:
            print(f"Correct ! Trouvé en {essais} essai(s).")
            return True
        else:
            print("Mauvaise réponse.")

# ===========================
# CONCLUSION DU JEU
# ===========================

def conclusion():
    print("\n[CONCLUSION]")
    print("Après avoir bravé tous les défis, les portes de l'ascenseur s'ouvrent enfin...")
    print("La lumière t'aveugle, mais tu es libre ! Bravo aventurier.")

# ===========================
# PROGRAMME PRINCIPAL
# ===========================

def main():
    introduction()

    if serrure_musicale():
        print("\nTu descends à l'étage suivant...")
        if labyrinthe_piege():
            print("\nEncore un étage plus bas...")
            if message_code():
                conclusion()
            else:
                print("Tu es resté bloqué sur un message mystérieux...")
        else:
            print("Le labyrinthe a eu raison de toi...")
    else:
        print("La serrure musicale t'a vaincu...")

if __name__ == "__main__":
    main()
