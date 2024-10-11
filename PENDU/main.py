from random import choice
import unidecode

#Ouvrir le fichier
with open('mots_mysteres.txt', 'r') as file:
    words = file.read().splitlines()

#Filtrer les mots de plus de 6 lettres et sans accents au cas où il y en aurait
valid_words = [word for word in words if len(word) >= 6 and word.isalpha()]
valid_words = [unidecode.unidecode(word) for word in valid_words]

#Choisir un mot au hasard et le mettre en majuscule
chosen_word = choice(valid_words).upper()

#Chaque tiret représente une lettre
display_word = ['_'] * len(chosen_word)
#Nombre d'essaies
attempts = 0
#Nombre d'essaies maximum
max_attempts = 10
#Stocker les lettres déjà utilisées
used_letters = set()

#Afficher le mot mystère
def display_current_progress():
    print(" ".join(display_word))

#Tant que le joueur a des essais
while attempts < max_attempts:
    display_current_progress()
    player_input = input("Entrez une lettre: ").upper()

    #Vérifier que l'input du joueur est bien une seule lettre
    if not player_input.isalpha() or len(player_input) != 1:
        print("Veuillez entrer une lettre valide.")
        continue
    #Vérifier si la lettres choisie du joueur est dans les lettres déjà utilisées
    if player_input in used_letters:
        print("Vous avez déjà choisi cette lettre.")
        continue
    #Ajouter la lettre aux lettres utilisées
    used_letters.add(player_input)

    #Vérifier si la lettre est dans le mot
    if player_input in chosen_word:
        #Pour toutes les lettres et index dans le mot mystère
        for index, letter in enumerate(chosen_word):
            #Si la lettre est la même que celle choisie par le joueur
            if letter == player_input:
                #On remplace le tiret correspondant avec la bonne lettre
                display_word[index] = player_input
        #Si il n'y a plus de tiret (-)
        if '_' not in display_word:
            print(f"Bravo ! Vous avez trouvé le mot : {chosen_word}")
            break
    #Si ce n'est pas la bonne lettre
    else:
        attempts += 1
        print(f"Lettre incorrecte. Il vous reste {max_attempts - attempts} essais.")

#Si le joueur a atteint son maximum de tentatives
if attempts == max_attempts:
    print(f"Game over ! Le mot était : {chosen_word}")
