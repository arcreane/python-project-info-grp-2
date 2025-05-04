import random
import time
import json
import tkinter as tk
from tkinter import messagebox
import pygame
import os
import sys

# Assurer que les fichiers sont trouvés quel que soit le répertoire d'exécution
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# ===========================
# INTRODUCTION DU JEU
# ===========================

def introduction():
    print("\n[INTRODUCTION]")
    print("Tu ouvres les yeux dans un espace confiné. L'air est glacé, chargé d'électricité statique.")
    print("Devant toi, un miroir fêlé, des parois métalliques... et un écran rouge affichant \"ÉTAGE ???\".")
    print("Une voix métallique résonne: \"Bienvenue dans l'Ascenseur Infernal. Pour sortir, vous devrez résoudre une série d'énigmes.\"")
    print("\"Chaque réussite vous rapprochera de la liberté. Chaque échec... eh bien, vous verrez.\"")
    input("Appuie sur Entrée pour commencer ta première épreuve...")

# ===========================
# JEU 1 : SERRURE MUSICALE
# ===========================

notes = {1: "GRAVE", 2: "MOYEN", 3: "AIGU", 4: "TRÈS AIGU"}
frequences = {1: 262, 2: 440, 3: 660, 4: 880}

def jouer_note(bouton):
    try:
        import winsound
        winsound.Beep(frequences[bouton], 800)  # son plus long (800 ms)
    except:
        # Alternative si winsound n'est pas disponible
        print(f"BIP ({notes[bouton]})")
        time.sleep(0.8)

def jouer_sequence(sequence):
    print("\nLa mélodie :")
    for bouton in sequence:
        jouer_note(bouton)
        time.sleep(0.5)  # petite pause entre les notes
    print("\n")

def ecouter_notes():
    print("\nTu peux écouter les sons un par un.")
    print("Tape 1, 2, 3 ou 4 pour écouter, ou 'q' pour quitter l'écoute.")
    while True:
        choix = input("Quel son veux-tu écouter ? (1-4, q pour quitter) : ").strip().lower()
        if choix == "q":
            break
        try:
            bouton = int(choix)
            if bouton in notes:
                print(f"Bouton {bouton} : {notes[bouton]}")
                jouer_note(bouton)
            else:
                print("Choix invalide. Tape un numéro entre 1 et 4.")
        except ValueError:
            print("Choix invalide. Tape un numéro entre 1 et 4 ou 'q'.")

def serrure_musicale():
    print("\n[JEU 1 : LA SERRURE MUSICALE]")
    print("L'écran de l'ascenseur scintille. Un panneau s'ouvre, révélant quatre boutons colorés.")
    print("\"Pour avancer, vous devez reproduire la mélodie secrète. Écoutez attentivement...\"")
    
    print("Bienvenue dans la serrure musicale!")
    print("Écoute attentivement, chaque note est une clé différente...")
    print("\nAttention : tu as droit à 3 erreurs maximum par mélodie. Après 3 erreurs, la bonne réponse sera donnée!")
    print("\nCorrespondance des boutons :")
    for bouton, note in notes.items():
        print(f"Bouton {bouton} = {note}")

    while True:
        choix = input("\nVeux-tu écouter les notes ou commencer le jeu ? (e = écouter / c = commencer) : ").strip().lower()
        if choix == "e":
            ecouter_notes()
        elif choix == "c":
            break
        else:
            print("Choix invalide. Tape 'e' ou 'c'.")

    boutons_possibles = [1, 2, 3, 4]

    sequence_sons = [random.choice(boutons_possibles) for _ in range(3)]
    erreurs_consecutives = 0
    bonne_reponse = False

    while erreurs_consecutives < 3 and not bonne_reponse:
        jouer_sequence(sequence_sons)

        while True:
            choix_reponse = input("Veux-tu réécouter la mélodie ? (o = oui / n = non) : ").strip().lower()
            if choix_reponse == "o":
                jouer_sequence(sequence_sons)
            elif choix_reponse == "n":
                break
            else:
                print("Choix invalide. Tape 'o' ou 'n'.")

        reponse = input("Entre la séquence des numéros (exemple : 1 3 2) : ").strip()
        reponse_liste = reponse.split()

        try:
            reponse_joueur = [int(num) for num in reponse_liste]
        except ValueError:
            print("Erreur : entre seulement des chiffres entre 1 et 4.")
            continue

        if reponse_joueur == sequence_sons:
            print("Bravo! Tu as réussi à ouvrir la serrure!")
            print("Un mécanisme s'active. Tu entends un déclic sourd...")
            bonne_reponse = True
        else:
            erreurs_consecutives += 1
            print("Ce n'est pas la bonne mélodie...")
            if erreurs_consecutives >= 3:
                print("La bonne réponse était :", ' '.join(str(num) for num in sequence_sons))
                print("Malgré tes erreurs, la serrure clique et s'ouvre. La voix résonne: \"Premier défi complété... par chance.\"")

    print("\nLa serrure musicale est déverrouillée. Une nouvelle épreuve t'attend...")
    input("Appuie sur Entrée pour continuer...")

# ===========================
# JEU 2 : MESSAGE CODÉ
# ===========================

# Dictionnaire pour convertir les lettres latines en lettres grecques
greek_alphabet = {
    'f': 'α', 'h': 'β', 't': 'γ', 'r': 'δ', 'z': 'ε', 'a': 'ζ', 'n': 'η', 'l': 'θ',
    'b': 'ι', 'o': 'κ', 'j': 'λ', 'e': 'μ', 'c': 'ν', 'd': 'ξ', 'g': 'ο', 's': 'π',
    'm': 'ρ', 'i': 'σ', 'p': 'τ', 'q': 'υ', 'y': 'φ', 'u': 'χ', 'v': 'ψ', 'w': 'ω'
}

# Liste des messages à déchiffrer
messages = [
    "chat", "pomme", "arbre", "bleu", "maison", "livre", "fleur", "etoile", "ciel", "train",
    "ballon", "soleil", "lune", "mer", "velo", "sucre", "four", "porte", "cle", "table"
]

# Indices sous forme de calculs pour chaque lettre grecque
indices = {
    'α': '3*2', 'β': '2*4', 'γ': '5*4', 'δ': '9*2', 'ε': '13*2', 'ζ': '1*1',
    'η': '7*2', 'θ': '3*4', 'ι': '2*1', 'κ': '5*3', 'λ': '30/3', 'μ': '25/5',
    'ν': '120/40', 'ξ': '16/4', 'ο': '21/3', 'π': '38/2', 'ρ': '130/10', 'σ': '27/9',
    'τ': '4*4', 'υ': '34/2', 'φ': '100/4', 'χ': '3*7', 'ψ': '11*2', 'ω': '69/3'
}

def convertir_en_grec(message):
    """Fonction pour convertir un message en lettres grecques."""
    return ''.join([greek_alphabet.get(char, char) for char in message.lower()])

def afficher_indice(message_grec):
    """Afficher un indice basé sur les lettres grecques du message."""
    indices_message = []
    for char in message_grec:
        if char in indices:
            indices_message.append(f"{char} = {indices[char]}")
    return "\n".join(indices_message)

def message_code():
    """Fonction principale du jeu."""
    print("\n[JEU 2 : LE MESSAGE CODÉ]")
    print("L'écran de l'ascenseur scintille à nouveau. Des symboles étranges y apparaissent.")
    print("\"De mystérieux caractères grecs dissimulent un message. Déchiffrez-le pour continuer votre ascension...\"")
    
    message_original = random.choice(messages)  # Choisir un message aléatoire
    message_grec = convertir_en_grec(message_original)  # Convertir le message en grec

    print("\nVoici le message à déchiffrer en lettres grecques:")
    print(message_grec)

    # Afficher les indices pour aider à déchiffrer
    print("\nIndices pour les lettres grecques :")
    print(afficher_indice(message_grec))

    # Lancement de la boucle de jeu
    essais = 0
    while True:
        reponse = input("\nQuel est le message original? ").lower().strip()
        essais += 1

        if reponse == message_original:
            print(f"Bravo! Vous avez trouvé le message après {essais} essai(s).")
            print("L'écran clignote en vert. Un mécanisme se débloque dans l'ascenseur.")
            break
        else:
            print("Ce n'est pas le bon message, essayez encore!")
            if essais >= 5:
                print("Indice supplémentaire: Le message est un nom commun simple.")
            if essais >= 10:
                print(f"Indice final: Le mot commence par '{message_original[0]}'")

    print("\nL'énigme du message codé est résolue! L'ascenseur tremble légèrement...")
    input("Appuie sur Entrée pour continuer vers la prochaine épreuve...")

# ===========================
# JEU 3 : LABYRINTHE PIÉGÉ
# ===========================

TAILLE_LABYRINTHE = 6
commandes = {'O': (-1, 0), 'K': (0, -1), 'L': (0, 1), 'M': (1, 0)}  # OKLM - Au calme

def generer_labyrinthe():
    lab = [["piège" for _ in range(TAILLE_LABYRINTHE)] for _ in range(TAILLE_LABYRINTHE)]
    x, y = 0, 0
    lab[x][y] = "entrée"
    while (x, y) != (TAILLE_LABYRINTHE - 1, TAILLE_LABYRINTHE - 1):
        lab[x][y] = "chemin"
        direction = random.choice([(0, 1), (1, 0)])  
        nx, ny = x + direction[0], y + direction[1]
        if 0 <= nx < TAILLE_LABYRINTHE and 0 <= ny < TAILLE_LABYRINTHE:
            x, y = nx, ny
    lab[x][y] = "sortie"
    return lab

def afficher_labyrinthe(lab, position):
    for i, ligne in enumerate(lab):
        for j, case in enumerate(ligne):
            if (i, j) == position:
                print("[X]", end=" ")
            else:
                print("[ ]" if case != "piège" else "[ ]", end=" ")
        print()

def labyrinthe_piege():
    print("\n[JEU 3 : LE LABYRINTHE PIÉGÉ]")
    print("Un pan de mur coulisse. Un écran tactile apparaît, affichant une grille mystérieuse.")
    print("\"Ce labyrinthe renferme de nombreux pièges. Trouvez les commandes cachées et rejoignez la sortie...\"")
    print("\"Attention: chaque pas compte. Au calme...\"")
    
    labyrinthe = generer_labyrinthe()
    position = [0, 0]
    tentative_count = 0
    
    print("\nBienvenue dans le labyrinthe piégé!")
    print("Tu dois trouver ton chemin jusqu'à la sortie.")
    print("Les commandes pour se déplacer sont à découvrir...")
    
    while True:
        print("\nVoici l'état actuel du labyrinthe:")
        afficher_labyrinthe(labyrinthe, tuple(position))
        
        mouvement = input("Entre un déplacement : ").upper()
        tentative_count += 1
        
        if mouvement not in commandes:
            print("Mouvement invalide, essaie encore.")
            if tentative_count == 5:
                print("Indice : Avance au calme, chaque pas compte…")
            continue
        
        nouvelle_position = [position[0] + commandes[mouvement][0], position[1] + commandes[mouvement][1]]
        
        if not (0 <= nouvelle_position[0] < len(labyrinthe) and 0 <= nouvelle_position[1] < len(labyrinthe[0])):
            print("Impossible de sortir du labyrinthe.")
            continue
        
        if labyrinthe[nouvelle_position[0]][nouvelle_position[1]] == "piège":
            print("Tu es tombé dans un piège ! Tu dois recommencer.")
            position = [0, 0]
            continue
        
        position = nouvelle_position
        
        if labyrinthe[position[0]][position[1]] == "sortie":
            print("Félicitations ! Tu as trouvé la sortie du labyrinthe !")
            print("Une lumière verte s'allume sur le panneau de l'ascenseur.")
            break
        
        if tentative_count == 15:
            print("Indice : Je suis à l'opposé de ZQSD")
        elif tentative_count == 20:
            print("Indice : Les touches qui te permettent d'avancer forment l'acronyme de 'Au Calme'")
    
    print("\nLe labyrinthe est résolu! L'ascenseur semble réagir...")
    input("Appuie sur Entrée pour continuer vers la dernière épreuve...")

# ===========================
# JEU 4 : DÉMINEUR
# ===========================

def jouer_demineur():
    print("\n[JEU 4 : LE DÉMINEUR]")
    print("L'écran principal de l'ascenseur s'illumine. Une grille apparaît avec des cases numérotées.")
    print("\"Pour votre dernier défi, désamorcez les explosifs cachés. Les chiffres indiquent le nombre de bombes adjacentes.\"")
    print("Appuie sur Entrée pour lancer l'interface du démineur...")
    input()
    
    pygame.init()

    TAILLE_CASE = 60
    TAILLE_GRILLE = 8
    LARGEUR = HAUTEUR = TAILLE_CASE * TAILLE_GRILLE

    BLANC = (255, 255, 255)
    NOIR = (0, 0, 0)
    ROUGE = (255, 0, 0)
    VERT = (0, 255, 0)
    GRIS_CLAIR = (200, 200, 200)
    JAUNE = (255, 255, 0)
    VIOLET_FONCE = (60, 0, 90)

    fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR + 80))
    pygame.display.set_caption("Démineur de la Tour")

    # Essayer de charger les images, sinon créer des substituts
    try:
        dalle_image = pygame.image.load("images/dalles.jpg")
        dalle_image = pygame.transform.scale(dalle_image, (TAILLE_CASE, TAILLE_CASE))
    except:
        dalle_image = pygame.Surface((TAILLE_CASE, TAILLE_CASE))
        dalle_image.fill(GRIS_CLAIR)
        
    try:
        tnt_image = pygame.image.load("images/tnt.jpg")
        tnt_image = pygame.transform.scale(tnt_image, (TAILLE_CASE, TAILLE_CASE))
    except:
        tnt_image = pygame.Surface((TAILLE_CASE, TAILLE_CASE))
        tnt_image.fill(ROUGE)
        font = pygame.font.Font(None, 36)
        texte = font.render("TNT", True, NOIR)
        tnt_image.blit(texte, (10, 20))
        
    try:
        tntsweeper_image = pygame.image.load("images/tntsweeper.png")
        tntsweeper_image = pygame.transform.scale(tntsweeper_image, (LARGEUR, HAUTEUR + 80))
    except:
        tntsweeper_image = pygame.Surface((LARGEUR, HAUTEUR + 80))
        tntsweeper_image.fill(VIOLET_FONCE)
        font = pygame.font.Font(None, 48)
        texte = font.render("TNT SWEEPER", True, BLANC)
        tntsweeper_image.blit(texte, (LARGEUR//2 - 150, HAUTEUR//2))

    def generer_mines(taille):
        mines = []
        nb_mines = (taille ** 2) // 5
        while len(mines) < nb_mines:
            x = random.randint(0, taille - 1)
            y = random.randint(0, taille - 1)
            if (x, y) not in mines:
                mines.append((x, y))
        return mines

    def placer_indices(grille, mines, taille):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),         (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        for y in range(taille):
            for x in range(taille):
                if (x, y) in mines:
                    grille[y][x] = "X"
                else:
                    compteur = 0
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < taille and 0 <= ny < taille and (nx, ny) in mines:
                            compteur += 1
                    if compteur > 0:
                        grille[y][x] = str(compteur)

    class TourDemineur:
        def __init__(self, niveau=0):
            self.niveau = niveau
            self.taille = TAILLE_GRILLE + niveau
            self.mines = generer_mines(self.taille)
            self.grille = [["." for _ in range(self.taille)] for _ in range(self.taille)]
            placer_indices(self.grille, self.mines, self.taille)
            self.revelees = [[False for _ in range(self.taille)] for _ in range(self.taille)]
            self.flags = [[False for _ in range(self.taille)] for _ in range(self.taille)]
            self.game_over = False
            self.victoire = False
            self.case_non_mines = (self.taille * self.taille) - len(self.mines)
            self.case_revelees = 0

        def reveler_case(self, x, y):
            if self.revelees[y][x] or self.flags[y][x]:
                return
            self.revelees[y][x] = True
            self.case_revelees += 1
            
            if self.grille[y][x] == "X":
                self.game_over = True
            elif self.grille[y][x] == ".":
                for dx, dy in [(-1, -1), (-1, 0), (-1, 1),
                               (0, -1),         (0, 1),
                               (1, -1), (1, 0), (1, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.taille and 0 <= ny < self.taille:
                        self.reveler_case(nx, ny)
                        
            # Vérifier la victoire
            if self.case_revelees >= self.case_non_mines:
                self.victoire = True

        def toggle_flag(self, x, y):
            if not self.revelees[y][x]:
                self.flags[y][x] = not self.flags[y][x]

        def afficher(self):
            for y in range(self.taille):
                for x in range(self.taille):
                    rect = pygame.Rect(x * TAILLE_CASE, y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE)

                    pygame.draw.rect(fenetre, NOIR, rect, 2)

                    if self.flags[y][x]:
                        fenetre.blit(dalle_image, rect.topleft)
                        pygame.draw.circle(fenetre, JAUNE, rect.center, TAILLE_CASE // 4)
                    elif self.revelees[y][x] or (self.game_over and self.grille[y][x] == "X"):
                        if self.grille[y][x] == "X":
                            fenetre.blit(tnt_image, rect.topleft)
                        elif self.grille[y][x] != ".":
                            font = pygame.font.Font(None, 36)
                            texte = font.render(self.grille[y][x], True, BLANC)
                            fenetre.blit(texte, (x * TAILLE_CASE + 20, y * TAILLE_CASE + 15))
                    else:
                        fenetre.blit(dalle_image, rect.topleft)

    def dessiner_bouton_rejouer():
        bouton = pygame.Rect(LARGEUR // 2 - 60, HAUTEUR + 20, 120, 40)
        pygame.draw.rect(fenetre, VERT, bouton)
        pygame.draw.rect(fenetre, NOIR, bouton, 2)
        font = pygame.font.Font(None, 32)
        texte = font.render("Rejouer", True, NOIR)
        fenetre.blit(texte, (LARGEUR // 2 - 40, HAUTEUR + 30))
        return bouton

    def afficher_intro():
        fenetre.blit(tntsweeper_image, (0, 0))
        pygame.display.flip()
        pygame.time.delay(2000)  # 2 secondes

    niveau = 0
    jeu = None
    clock = pygame.time.Clock()
    running = True
    etat = "intro"  # "intro", "accueil", "jeu"
    resultat = False
    
    while running:
        if etat == "intro":
            afficher_intro()
            etat = "jeu"
            jeu = TourDemineur(niveau)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
            elif etat == "jeu":
                if not jeu.game_over and not jeu.victoire and event.type == pygame.MOUSEBUTTONDOWN:
                    x = event.pos[0] // TAILLE_CASE
                    y = event.pos[1] // TAILLE_CASE
                    if x < jeu.taille and y < jeu.taille:
                        if event.button == 1:  # Clic gauche
                            jeu.reveler_case(x, y)
                        elif event.button == 3:  # Clic droit
                            jeu.toggle_flag(x, y)
                elif (jeu.game_over or jeu.victoire) and event.type == pygame.MOUSEBUTTONDOWN:
                    if rect_bouton_rejouer and rect_bouton_rejouer.collidepoint(event.pos):
                        if jeu.victoire:
                            resultat = True
                            running = False
                        else:
                            jeu = TourDemineur(niveau)
    
        if etat == "jeu":
            fenetre.fill(NOIR)
            jeu.afficher()
    
            rect_bouton_rejouer = None
            if jeu.game_over:
                font = pygame.font.Font(None, 48)
                texte = font.render("Perdu !", True, ROUGE)
                fenetre.blit(texte, (LARGEUR // 2 - 60, HAUTEUR // 2 - 30))
                rect_bouton_rejouer = dessiner_bouton_rejouer()
            elif jeu.victoire:
                font = pygame.font.Font(None, 48)
                texte = font.render("Victoire !", True, VERT)
                fenetre.blit(texte, (LARGEUR // 2 - 80, HAUTEUR // 2 - 30))
                rect_bouton_rejouer = dessiner_bouton_rejouer()
    
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()
    return resultat or jeu.victoire

# ===========================
# CONCLUSION
# ===========================

def conclusion(toutes_reussites):
    print("\n[CONCLUSION]")
    if toutes_reussites:
        print("Une lumière blanche t'aveugle alors que les portes de l'ascenseur s'ouvrent enfin...")
        print("\"Félicitations. Vous avez prouvé votre valeur en résolvant toutes les énigmes.\"")
        print("Tu franchis les portes et découvres un long couloir menant vers une lumière au loin.")
        print("Tu es libre... ou peut-être est-ce seulement le début d'une nouvelle série d'épreuves?")
    else:
        print("Malgré quelques difficultés, les portes de l'ascenseur finissent par s'ouvrir.")
        print("\"Vous avez survécu. C'est... acceptable.\"")
        print("Tu franchis les portes avec prudence, soulagé·e d'avoir survécu à cette épreuve étrange.")
        print("Mais au fond de toi, tu te demandes si cela est vraiment terminé...")
    
    print("\nFIN")

# ===========================
# PROGRAMME PRINCIPAL
# ===========================

def attendre_entree():
    def lancer_jeu():
        fenetre.destroy()
        jeu_principal()

    fenetre = tk.Tk()
    fenetre.title("L'Ascenseur Infernal")
    fenetre.geometry("500x300")
    fenetre.configure(bg="black")

    label = tk.Label(fenetre, text="Bienvenue dans\nL'ASCENSEUR INFERNAL", 
                    font=("Arial", 20), bg="black", fg="red", pady=30)
    label.pack()

    sous_titre = tk.Label(fenetre, text="Un escape game numérique", 
                        font=("Arial", 12), bg="black", fg="white")
    sous_titre.pack()

    bouton = tk.Button(fenetre, text="ENTRER", command=lancer_jeu, 
                      font=("Arial", 14), bg="red", fg="white", 
                      padx=20, pady=10, relief=tk.RAISED, bd=5)
    bouton.pack(pady=40)

    fenetre.mainloop()

def jeu_principal():
    # Variables pour suivre les réussites
    reussites = []
    
    # Introduction
    introduction()
    
    # Jeu 1: Serrure musicale
    print("\n==========================================================")
    print("TRANSITION: L'ascenseur tremble. Un premier défi apparaît.")
    print("==========================================================\n")
    serrure_musicale()
    reussites.append(True)  # Toujours considéré comme réussi pour progresser
    
    # Jeu 2: Message codé
    print("\n==========================================================")
    print("TRANSITION: L'ascenseur descend brusquement d'un étage.")
    print("L'écran affiche maintenant: \"ÉTAGE ?? - DÉCODAGE REQUIS\"")
    print("==========================================================\n")
    message_code()
    reussites.append(True)  # Toujours considéré comme réussi
    
    # Jeu 3: Labyrinthe piégé
    print("\n==========================================================")
    print("TRANSITION: L'ascenseur grince et bascule. Un mur coulisse.")
    print("\"ÉTAGE ?? - NAVIGATION REQUISE\"")
    print("==========================================================\n")
    labyrinthe_piege()
    reussites.append(True)  # Toujours considéré comme réussi
    
    # Jeu 4: Démineur avec interface graphique 
    print("\n==========================================================")
    print("TRANSITION: L'ascenseur s'arrête net. L'écran clignote en rouge.")
    print("\"ÉTAGE FINAL - DÉSAMORÇAGE REQUIS\"")
    print("==========================================================\n")
    reussite_demineur = jouer_demineur()
    reussites.append(reussite_demineur)
    
    # Conclusion
    print("\n==========================================================")
    print("TRANSITION: L'ascenseur s'active une dernière fois...")
    print("==========================================================\n")
    conclusion(all(reussites))

if __name__ == "__main__":
    try:
        # Lancer le jeu
        attendre_entree()
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")
        input("Appuyez sur Entrée pour quitter...")