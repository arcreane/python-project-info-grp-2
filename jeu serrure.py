import random
import json
import winsound
import time

notes = {
    1: "GRAVE",
    2: "MOYEN",
    3: "AIGU",
    4: "TRÈS AIGU"
}

frequences = {
    1: 262,  # grave
    2: 440,  # moyen
    3: 660,  # aigu
    4: 880   # très aigu
}

fichier_sauvegarde = "progression_serrure.json"

indice = "Écoute attentivement, chaque note est une clé différente..."

def jouer_note(bouton):
    winsound.Beep(frequences[bouton], 800)  # son plus long (800 ms)

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

def sauvegarder_etat(reussi):
    etat = {"serrure_musicale_reussie": reussi}
    with open(fichier_sauvegarde, "w") as f:
        json.dump(etat, f)

def serrure_musicale():
    print("Bienvenue dans la serrure musicale!")
    print(indice)
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
            bonne_reponse = True
        else:
            erreurs_consecutives += 1
            print("Ce n'est pas la bonne mélodie...")
            if erreurs_consecutives >= 3:
                print("La bonne réponse était :", ' '.join(str(num) for num in sequence_sons))

    if bonne_reponse:
        sauvegarder_etat(True)
    else:
        print("Tu as échoué à ouvrir la serrure.")
        sauvegarder_etat(False)

if __name__ == "__main__":
    serrure_musicale()
