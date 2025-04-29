import tkinter as tk
from tkinter import messagebox
import random
import time

TAILLE_LABYRINTHE = 6
TOP_RECORDS = 10
records = []

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

labyrinthe = generer_labyrinthe()
commandes = {'O': (-1, 0), 'K': (0, -1), 'L': (0, 1), 'M': (1, 0)}

def afficher_labyrinthe(position):

    for i, ligne in enumerate(labyrinthe):
        for j, case in enumerate(ligne):
            if (i, j) == position:
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
    messagebox.showinfo("Victoire", f"Félicitations ! Tu as trouvé la sortie en {temps:.2f} secondes !\n\nTop 10 des records :\n" + "\n".join(f"{i+1}. {t:.2f}s" for i, t in enumerate(records)))
    labyrinthe = generer_labyrinthe()
    root.destroy()

def afficher_indice(texte):
 
    indice_fenetre = tk.Toplevel(root)
    indice_fenetre.title("Indice")
    label = tk.Label(indice_fenetre, text=texte)
    label.pack(pady=10)
    bouton_ok = tk.Button(indice_fenetre, text="OK", command=indice_fenetre.destroy)
    bouton_ok.pack(pady=5)

def verifier_inactivite(position_initiale):
    root.after(120000, lambda: afficher_indice("Indice : Avance au calme, chaque pas compte…") if position_initiale == position else None)
    root.after(240000, lambda: afficher_indice("Indice : Je suis à l'opposé de ZQSD") if position_initiale == position else None)
    root.after(300000, lambda: afficher_indice("Indice : Ceux qui te permettent d'avancer est l'acronyme de Au Calme") if position_initiale == position else None)

def jouer_labyrinthe(nouveau_jeu=True):
    global position, debut_temps
    if nouveau_jeu:
        debut_temps = time.time()
    position = [0, 0]

   
    def debut_jeu():
        messagebox.showinfo("Bienvenue", "Bienvenue dans le jeu !\n\nLes commandes pour avancer sont à découvrir par toi-même.\nEssaie d'explorer et de trouver comment te déplacer.")

    debut_jeu()

    def rejouer():
       
        global position
        position = [0, 0]
        afficher_labyrinthe(tuple(position))
        jeu_frame.pack_forget()  
        jeu_frame.pack()  

    jeu_frame = tk.Frame(root)
    jeu_frame.pack()

    while True:
        afficher_labyrinthe(tuple(position))
        verifier_inactivite(position[:])
        mouvement = input("Entre un déplacement : ").upper()

        if mouvement not in commandes:
            print("Mouvement invalide, essaie encore.")
            continue

        nouvelle_position = [position[0] + commandes[mouvement][0], position[1] + commandes[mouvement][1]]

        if not (0 <= nouvelle_position[0] < len(labyrinthe) and 0 <= nouvelle_position[1] < len(labyrinthe[0])):
            print("Impossible de sortir du labyrinthe.")
            continue

        if labyrinthe[nouvelle_position[0]][nouvelle_position[1]] == "piège":
            print("Tu es mort ! Tu dois recommencer.")
            print("Tu retournes à ta position initiale.")
            rejouer() 
            break

        position[:] = nouvelle_position

        if labyrinthe[position[0]][position[1]] == "sortie":
            gagner(time.time() - debut_temps)
            break

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  
    jouer_labyrinthe()

