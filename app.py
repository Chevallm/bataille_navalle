from random import randint

plateau = []

nb_ligne_col = 5
nb_tours = 4

for x in range(0, nb_ligne_col):
    plateau.append(["O"] * nb_ligne_col)

def afficher_plateau(plateau):
    for ligne in plateau:
        print " ".join(ligne)

afficher_plateau(plateau)

def alea_ligne(plateau):
    return randint(0, len(plateau) - 1)

def alea_col(plateau):
    return randint(0, len(plateau[0]) - 1)

bateau_x = alea_ligne(plateau)
bateau_y = alea_col(plateau)
print "Bateau en " + str(bateau_x) + ":" + str(bateau_y)

for tour in range(nb_tours):
    print("Tour n " + str(tour+1))
    print("- - - - - - -")
    tir_x = int(raw_input("Quelle ligne ?"))
    tir_y = int(raw_input("Quelle colonne ?"))

    if tir_x == bateau_x and tir_y == bateau_y:
        print "Bravo ! Vous avez eu mon bateau !"
        break
    else:
        if (tir_x < 0 or tir_x > nb_ligne_col-1) or (tir_y < 0 or tir_y > nb_ligne_col-1):
            print "Oups ! Vous devez viser l'ocean."
        elif(plateau[tir_x ][tir_y ] == "X"):
            print "Cette case est deja decouverte."
        else:
            print "Dommage !"
            plateau[tir_x ][tir_y ] = "X"
        # Affichez tour+1 ici !

        afficher_plateau(plateau)
