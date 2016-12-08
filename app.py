# Importer le random
from random import randint

exit = False

# Création du plateau
plateau = []

nb_ligne_col = 10 # Nombre de ligne et de colonnes
nb_tours = 4 # Nombre de tours
espace = " " # Caractère espace

# Retourne une ligne aléatoire
def alea_ligne(plateau):
    return randint(0, len(plateau) - 1)
# Retourne une colonne aléatoire
def alea_col(plateau):
    return randint(0, len(plateau[0]) - 1)

# Remplir le tableau de O
def initPlateau(plateau):
    for x in range(0, nb_ligne_col):
        plateau.append(["O"] * nb_ligne_col)

# Vide le tableau


# Afficher le tableau
def afficher_plateau(plateau):
    for ligne in plateau:
        print(espace.join(ligne)) # Afficher des espace entre chaque cellule

def afficher_le_numero_du_tour():
    print("Tour N "+ str(tour+1))

def faire_tirer_le_joueur():
    return {
        "tx": int(input("Quelle ligne ?"))-1,
        "ty": int(input("Quelle colonne ?"))-1
    }

def flatten(lignes_du_plateau):
    r = []
    for ligne in lignes_du_plateau:
        for n in ligne:
            r.append(n)
    return r

def vider_le_plateau(plateau):
    flatten(plateau)
    for value in plateau:
        plateau.remove(value)
    return plateau

def est_fini(nb_tours):
    return nb_tours > 0

def demander_nombre_de_tour():
    return int(input("Combien de tours voulez-vous ?"))-1

def afficher_le_titre():
    print("**************************************************")
    print("*                     BATAILLE                   *")
    print("*                      NAVALE                    *")
    print("**************************************************")
    print()
    print("Ecrit par: MCP <maxime.chevallier_pichon@yahoo.fr>")
    print("Open source 2016")
    print()
    print()

afficher_le_titre()
while(exit == False):

    nb_tours = demander_nombre_de_tour()+1

    vider_le_plateau(plateau)
    initPlateau(plateau)
    afficher_plateau(plateau)

    # Placement du bateau aléatoirement
    bateau_x = alea_ligne(plateau)
    bateau_y = alea_col(plateau)

    # Affiche la localisation du bateau
    #print("Bateau en " + str(bateau_x) + ":" + str(bateau_y))

    # Boucle du jeu

    for tour in range(0,nb_tours):
        afficher_le_numero_du_tour()
        coordonnees_du_tir = faire_tirer_le_joueur();

        if coordonnees_du_tir["tx"] == bateau_x and coordonnees_du_tir["ty"] == bateau_y:
            print("Bravo ! Vous avez eu mon bateau !")
            break
        else:
            if (coordonnees_du_tir["tx"] < 0 or coordonnees_du_tir["tx"] > nb_ligne_col-1) or (coordonnees_du_tir["ty"] < 0 or coordonnees_du_tir["ty"] > nb_ligne_col-1):
                print("Oups ! Vous devez viser l'ocean.")
            elif(plateau[coordonnees_du_tir["tx"] ][coordonnees_du_tir["ty"] ] == "X"):
                print("Cette case est deja decouverte.")
            else:
                print("Dans l'eau !")
                plateau[coordonnees_du_tir["tx"] ][coordonnees_du_tir["ty"] ] = "X"

            print(est_fini(nb_tours))
