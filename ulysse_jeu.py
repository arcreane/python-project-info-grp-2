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


