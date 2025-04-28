import random
import json
import winsound

notes = {
    1: "DO",
    2: "RE",
    3: "MI",
    4: "FA"
}

fichier_sauvegarde = "progression_serrure.json"

indice = "Ecoute attentivement, chaque note est une clé..."

def jouer_note(bouton):
    if bouton == 1:
        winsound.Beep(262, 300)
    elif bouton == 2:
        winsound.Beep(294, 300)
    elif bouton == 3:
        winsound.Beep(330, 300)
    elif bouton == 4:
        winsound.Beep(349, 300)

def jouer_sequence(sequence):
    print("\nLa mélodie :")
    for bouton in sequence:
        jouer_note(bouton)
    print("\n")

def ecouter_notes():
    print("\nVoici les sons disponibles :")
    for bouton in notes:
        print(f"Bouton {bouton} : {notes[bouton]}")
        jouer_note(bouton)

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
    tours_reussis = 0

    while tours_reussis < 3:
        sequence_sons = [random.choice(boutons_possibles) for _ in range(3)]
        erreurs_consecutives = 0

        while True:
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
                print("Bravo! Tu as reproduit la mélodie!")
                tours_reussis += 1
                print(f"Tours réussis : {tours_reussis}/3")
                break
            else:
                erreurs_consecutives += 1
                print("Ce n'est pas la bonne mélodie...")
                if erreurs_consecutives >= 3:
                    print("La bonne réponse était :", ' '.join(str(num) for num in sequence_sons))
                    break

    print("Félicitations! Tu as réussi 3 mélodies de suite!")
    sauvegarder_etat(True)

if __name__ == "__main__":
    serrure_musicale()