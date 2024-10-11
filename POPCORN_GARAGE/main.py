from PIL import Image

#Chemin vers la liste des films
chemin = "liste_films.txt"
#Liste des noms de films
base_films_list = []
#Liste des noms de films compactés en minuscules sans espaces
compact_films_list = []
#Réponse du joueur
player_input = ""
#Liste des films que le joueur a trouvé
valid_films = []
#Nombres de films à trouver
films_remaining = 0
#Nombre d'erreurs faites par le joueur
errors = 0
#Nombre maximum d'erreurs
max_errors = 3


#Ouvrir le fichier
with open(chemin, "r") as file :
    #Lire et mettres les noms des films dans une liste
    base_films_list = file.readlines()
    films_remaining = len(base_films_list)

#Enlever les sauts de lignes
base_films_list = [elt.strip() for elt in base_films_list]
#Enlever les majuscules et les espaces
compact_films_list = [elt.strip().lower().replace(" ", "") for elt in base_films_list]

#Ouvrir l'image
image = Image.open(f"img/background.png")
#Montrer l'image
image.show()



#Message de début
print(f"Vous devez essayer de trouver le nom des {films_remaining} films en regardant les images. Vous perdrez si vous atteignez {max_errors} erreurs. ")



#Tant qu'il y a des films à trouver et que le joueur à fais moins d'erreurs que le nombre maximum d'erreurs autorisé
while films_remaining > 0 and errors < max_errors :
    #Réponse du joueur
    player_input = input("Entrer le nom d'un film : ").strip().lower().replace(" ", "")
    #Si sa réponse est dans la liste
    if player_input in compact_films_list :
        #Si il n'a pas déjà trouvé ce film
        if player_input not in valid_films :
            #Ajout du film dans la liste de ceux trouvés
            valid_films.append(player_input)
            films_remaining -= 1
            print(f"Bravo, il reste {films_remaining} films à trouver !")
        #Si le joueur a déjà trouvé ce film
        else :
            print(f"Vous avez déjà trouvé {player_input}.")
    #Si le film n'est pas dans la liste de films à trouver
    else :
        errors += 1
        print(f"ERREUR ! Il vous reste {max_errors - errors} chances.")


#Si le joueur a fait le maximum d'erreurs
if errors == max_errors :
    print(f"Vous avez perdu ! {errors}/{max_errors} erreurs")
#Si le joueur à gagné
else :
    print("GAGNÉ ! Vous avez trouvé toute la liste de films :")
    print("\n".join(base_films_list))
