#########################################################################################
##                                                                                     ##
##                              LE JEU DU LABYRINTHE                                   ##
##                                                                                     ##
#########################################################################################

#########################################################################################
##     IMPORTATION
#########################################################################################
import sys
import re
import os
<<<<<<< HEAD
import tkinter as tk
=======
>>>>>>> 577296e... Ajout d'un affichage graphique des règles du jeu avec Tkinter (sans mise en forme du texte)

from mouvement import Mouvement
from labyrinthe import Labyrinthe
from actions import deplacer
from actions import question_fermee
from actions import sortir

#########################################################################################
##    TELECHARGEMENT DES CARTES
#########################################################################################

##### A REMPLIR A LA MAIN
nombre_cartes = 3
liste_labyrinthe = ["facile", "prison", "hyperloop"]

##### RECUPERATION DU CHEMIN
dict_labyrinthe = {} # dict() -- dictionnaire des labyrinthes de la bibliothèque, la cle est le numero du labyrinthe
dir_path = os.path.dirname(os.path.realpath(__file__))

##### TELECHARGEMENT
for i, elt in enumerate(liste_labyrinthe):
    path = dir_path + "/cartes/{}.txt".format(liste_labyrinthe[i])
    i += 1
    mon_labyrinthe_1 = Labyrinthe()
    mon_labyrinthe_1.telecharger(path, str(i)) 
    dict_labyrinthe[str(i)] = mon_labyrinthe_1

#########################################################################################
##     ALGORITHME DE JEU
#########################################################################################

##### INITIALISATION
continuer_jouer = bool() # bool -- vaut True tant que le joueur souhaite jouer
partie = bool() # bool -- vaut True tant que le robot n'est pas sorti du labyrinthe


##### DEBUT DU JEU
print(" ")
print("Souhaites-tu jouer au jeu du labyrinthe ? ")
continuer_jouer = question_fermee()

if not continuer_jouer: # si le joueur ne souhgaite pas jouer on quitte immédiatement la partie
    sys.exit("Très bien, au revoir et à bientôt !")

print(" ")
print("As-tu une partie déjà entamée ? ")
partie_en_cours = question_fermee()
print(" ")




##### AFFICHAGE DES REGLES
regles_du_jeu = """ 
Bienvenu l'ami dans le jeu du labyrinthe !
Voici quelques règles avant de commencer à jouer. 
Un labyrinthe est composé des éléments suivants :
        -- une case vide
      O -- un mur
      . -- une porte
      X -- ton robot
      U -- la sortie
Le but du jeu est d'amener le robot sur la sortie. Pour cela tu peux le diriger en lui envoyant
des instructions sous la forme d'une lettre n, s, e, o pour indiquer la direction :
      n -- nord
      s -- sud
      e -- est
      o -- ouest
suivie d'un chiffre entre 1 et 9 pour le nombre de pas que le robot doit faire dans cette direction.

Allez, c'est parti !

"""
print(regles_du_jeu)



while continuer_jouer: # On commence à jouer

##### OPTION 1 : ENCIENNE PARTIE CHARGEE
    if partie_en_cours:
        partie = True
        path = dir_path + "/cartes/labyrinthe_en_cours.txt"
        mon_labyrinthe = Labyrinthe()
        mon_labyrinthe.telecharger(path, "0") 

##### OPTION 2 : NOUVELLE PARTIE
    else:
    # Le joueur commence une nouvelle partie
        partie = True
        print(" ")
        print("~*~ Nouvelle partie ~*~")
        print(" ")

        # Le joueur choisit une carte
        choix_labyrinthe = """
        Labyrinthes existants :
            1 - facile 
            2 - prison
            3 - hyperloop
        """
        print(choix_labyrinthe)
        instruction_ok = True
    
        while instruction_ok:
            numero_carte = input("Entrez un numéro de labyrinthe : ")
            print(" ")
            if numero_carte not in dict_labyrinthe:
                print("Je n'ai pas ce labyrinthe dans ma bibliothèque.")
            else:
                instruction_ok = False

        # La carte est chargée dans mon_labyrinthe
        mon_labyrinthe = Labyrinthe() # initialisation du labyrinthe de la class Labyrinthe
        mon_labyrinthe = dict_labyrinthe[numero_carte]

    

    # La console affiche la carte
    mon_labyrinthe.afficher_carte()



    while partie:

        # Le joueur entre un déplacment mvt_str
        # On vérifie qu'il a saisit le mouvement au bon format une lettre puis un nombre
        expression = r"^[nseo]{1}[1-9]{1}$"
        instruction_ok = True

        while instruction_ok:
            mvt_str = input("Entrer un déplacement pour votre robot X ou q pour quitter : ")
            print(" ")
            
            if mvt_str == "q" :
                sys.exit("On se quitte là-dessus alors, à bientôt !")
                
            if re.search(expression, mvt_str) is None:
                print("L'expression n'est pas valide.")
                print("Le premier caractère doit être un point cardinal n, s, e ou o. ")
                print("le deuxième caractère doit être un entier entre 1 et 9.")

            else:
                instruction_ok = False

                    
        # On crée l'objet de la classe Mouvement correspondant au déplacement entré par le joueur
        mvt = Mouvement(mvt_str)

        # Le robot est déplacé
        deplacer(mon_labyrinthe, mvt)
 
        # On enregistre la nouvelle carte
        mon_labyrinthe.enregistrer(dir_path, "labyrinthe_en_cours")

        # On affiche de nouveau la carte
        mon_labyrinthe.afficher_carte()

        # Test est-ce que le robot est sorti
        if sortir(mon_labyrinthe):
            print("Bravo, tu es sorti du labyrinthe !!")
            print(" ")
            partie = False


    # Le joueur peut commencer une nouvelle partie
    print("Souhaites-tu jouer une nouvelle partie au jeu du labyrinthe ? ")
    print(" ")
    continuer_jouer = question_fermee()
    if not continuer_jouer: # si le joueur ne souhgaite pas jouer on quitte immédiatement la partie
        sys.exit("Très bien, au revoir et à bientôt !")



















