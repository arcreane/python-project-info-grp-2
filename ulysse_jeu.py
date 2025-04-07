import random
import pygame
pygame.init()

TAILLE_CASE = 60  
TAILLE_GRILLE = 8  
LARGEUR = HAUTEUR = TAILLE_CASE * TAILLE_GRILLE  

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
GRIS_CLAIR = (200, 200, 200)
BLEU = (0, 0, 255)

fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Démineur de la Tour")

def generer_mines(taille):
    mines = []
    nb_mines = (taille ** 2) // 5    # on a taille = 8, donc 8^2=64 et 64//5 = à 12, ya 12 mines en tout a chaque fois
    while len(mines) < nb_mines:
        x = random.randint(0, taille - 1)
        y = random.randint(0, taille - 1)
        if (x, y) not in mines:      #verifie que le couple x,y n'est pas dans la liste mines avant de l'ajouter
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


