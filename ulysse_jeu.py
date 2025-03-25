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
    nb_mines = (taille ** 2) // 5    # on a taille = 8, donc 8^2=64 et 64//5 environ = à 12, ya 12 mines en tout a chaque fois
    while len(mines) < nb_mines:
        x = random.randint(0, taille - 1)
        y = random.randint(0, taille - 1)
        if (x, y) not in mines:
            mines.append((x, y))
    return mines

