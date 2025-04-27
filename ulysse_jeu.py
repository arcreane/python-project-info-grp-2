import pygame
import random

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

dalle_image = pygame.image.load("images/dalle.jpg")
dalle_image = pygame.transform.scale(dalle_image, (TAILLE_CASE, TAILLE_CASE))

tnt_image = pygame.image.load("images/tnt.jpg")
tnt_image = pygame.transform.scale(tnt_image, (TAILLE_CASE, TAILLE_CASE))

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

    def toggle_flag(self, x, y):
        if not self.revelees[y][x]:
            self.flags[y][x] = not self.flags[y][x]

    def afficher(self):
        for y in range(self.taille):
            for x in range(self.taille):
                rect = pygame.Rect(x * TAILLE_CASE, y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE)

                fenetre.blit(dalle_image, rect.topleft)

                pygame.draw.rect(fenetre, NOIR, rect, 2)

                if self.flags[y][x]:
                    pygame.draw.circle(fenetre, JAUNE, rect.center, TAILLE_CASE // 4)
                elif self.revelees[y][x] or (self.game_over and self.grille[y][x] == "X"):
                    if self.grille[y][x] == "X":
                        fenetre.blit(tnt_image, rect.topleft)
                    elif self.grille[y][x] != ".":
                        font = pygame.font.Font(None, 36)
                        texte = font.render(self.grille[y][x], True, BLANC)
                        fenetre.blit(texte, (x * TAILLE_CASE + 10, y * TAILLE_CASE + 5))

def dessiner_bouton_rejouer():
    bouton = pygame.Rect(LARGEUR // 2 - 60, HAUTEUR + 20, 120, 40)
    pygame.draw.rect(fenetre, VERT, bouton)
    pygame.draw.rect(fenetre, NOIR, bouton, 2)
    font = pygame.font.Font(None, 32)
    texte = font.render("Rejouer", True, NOIR)
    fenetre.blit(texte, (LARGEUR // 2 - 40, HAUTEUR + 30))
    return bouton

niveau = 0
jeu = TourDemineur(niveau)
clock = pygame.time.Clock()
running = True

while running:
    fenetre.fill(NOIR)
    jeu.afficher()

    rect_bouton_rejouer = None
    if jeu.game_over:
        font = pygame.font.Font(None, 48)
        texte = font.render("Perdu !", True, ROUGE)
        fenetre.blit(texte, (LARGEUR // 2 - 60, HAUTEUR // 2 - 30))
        rect_bouton_rejouer = dessiner_bouton_rejouer()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not jeu.game_over and event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0] // TAILLE_CASE
            y = event.pos[1] // TAILLE_CASE
            if x < jeu.taille and y < jeu.taille:
                if event.button == 1:
                    jeu.reveler_case(x, y)
                elif event.button == 3:
                    jeu.toggle_flag(x, y)
        elif jeu.game_over and event.type == pygame.MOUSEBUTTONDOWN:
            if rect_bouton_rejouer and rect_bouton_rejouer.collidepoint(event.pos):
                jeu = TourDemineur(niveau)

    clock.tick(30)

pygame.quit()
pygame.quit()
