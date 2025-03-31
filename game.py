import random

# Dictionnaire pour convertir les lettres latines en lettres grecques
greek_alphabet = {
    'f': 'α', 'h': 'β', 't': 'γ', 'r': 'δ', 'z': 'ε', 'a': 'ζ', 'n': 'η', 'l': 'θ',
    'b': 'ι', 'o': 'κ', 'j': 'λ', 'e': 'μ', 'c': 'ν', 'd': 'ξ', 'g': 'ο', 's': 'π',
    'm': 'ρ', 'i': 'σ', 'p': 'τ', 'q': 'υ', 'y': 'φ', 'u': 'χ', 'v': 'ψ', 'w': 'ω'
}

# Liste des messages à déchiffrer
messages = [
    "chat", "pomme", "arbre", "bleu", "maison", "livre", "fleur", "etoile", "ciel", "train",
    "ballon", "soleil", "lune", "mer", "velo", "sucre", "four", "porte", "cle", "table",
    "nuit", "fer", "pluie", "vent", "musique", "reve", "banc", "glace", "route", "bois",
    "cle", "phare", "orage", "neige", "paix", "glace", "vent", "sac", "ballon", "camion",
    "neige", "porte", "fleur", "ciel", "verre", "soupe", "coupe", "chien", "pomme", "crayon",
    "maison", "chat", "style", "jumeau", "pont", "miroir", "papa", "poule", "carte", "sucre",
    "gateau", "fleur", "chaise", "vent", "cle", "onde", "ciel", "bleu", "rouge", "jardin",
    "rame", "ruisseau", "rue", "bois", "tapis", "jus", "miroir", "botte", "table", "tombe",
    "soir", "minuit", "nuage", "sable", "monnaie", "lune", "meche", "moche", "rayon", "porte",
    "livre", "ours", "fauteuil", "lever", "porter", "jeter", "pause", "reveil", "maree"
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


def jeu():
    """Fonction principale du jeu."""
    message_original = random.choice(messages)  # Choisir un message aléatoire
    message_grec = convertir_en_grec(message_original)  # Convertir le message en grec

    print("Voici le message à déchiffrer en lettres grecques:")
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
            break
        else:
            print("Ce n'est pas le bon message, essayez encore!")


# Lancer le jeu
jeu()


