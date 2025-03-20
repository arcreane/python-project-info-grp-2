import random

# Dictionnaire pour convertir les lettres latines en lettres grecques
greek_alphabet = {
    'f': 'α', 'h': 'β', 't': 'γ', 'r': 'δ', 'z': 'ε', 'a': 'ζ', 'n': 'η', 'l': 'θ',
    'b': 'ι', 'o': 'κ', 'j': 'λ', 'e': 'μ', 'c': 'ν', 'd': 'ξ', 'g': 'ο', 's': 'π',
    'm': 'ρ', 'i': 'σ', 'p': 'τ', 'q': 'υ', 'y': 'φ', 'u': 'χ', 'v': 'ψ', 'w': 'ω'
}

# Liste des messages à déchiffrer
messages = [
    "bonjour",
    "salut",
    "code",
    "python",
    "jeu"
]

def convertir_en_grec(message):
    """Fonction pour convertir un message en lettres grecques."""
    return ''.join([greek_alphabet.get(char, char) for char in message.lower()])

def jeu():
    """Fonction principale du jeu."""
    message_original = random.choice(messages)  # Choisir un message aléatoire
    message_grec = convertir_en_grec(message_original)  # Convertir le message en grec

    print("Voici le message à déchiffrer en lettres grecques:")
    print(message_grec)

    # Lancement de la boucle de jeu
    essais = 0
    while True:
        reponse = input("Quel est le message original? ").lower().strip()
        essais += 1

        if reponse == message_original:
            print(f"Bravo! Vous à présent accéder au niveau superieur.")
            break
        else:
            print("Ce n'est pas le bon message, essayez encore!")
            # Changer le message si la réponse est incorrecte
            message_original = random.choice(messages)
            message_grec = convertir_en_grec(message_original)
            print("Nouveau message à déchiffrer en grec:")
            print(message_grec)

# Lancer le jeu
jeu()
