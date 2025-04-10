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

    def reveler_case(self, x, y):
        if self.revelees[y][x] or self.flags[y][x]:
            return
        self.revelees[y][x] = True
        if self.grille[y][x] == "X":
            self.game_over = True
        elif self.grille[y][x] == ".":
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1),
                           (0, -1),         (0, 1),
                           (1, -1), (1, 0), (1, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.taille and 0 <= ny < self.taille:
                    self.reveler_case(nx, ny)
