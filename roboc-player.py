#########################################################################################
##                                 JEU DU LABYRINTHE                                   ##
##                                    PLAYER CODE                                      ##
#########################################################################################

#########################################################################################
###  IMPORTATION
#########################################################################################

import sys
import re
import os
import random

import socket
import select

from mouvement import Mouvement
from labyrinthe import Labyrinthe
from actions import deplacer
from actions import question_fermee
from actions import sortir

#########################################################################################
###  CONNEXION
#########################################################################################

# Création du client
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecter le client
# On utilise le même numéro de port que la connexion établie par le serveur
port = 12800

connexion_avec_serveur.connect(("localhost", port))
print("Connexion établie avec le serveur sur le port {}".format(port))

#########################################################################################
###  JEU DU LABYRINTHE
#########################################################################################

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


##### INITIALISATION
msg_a_envoyer =b"" #
expression = r"^[nseo]{1}[1-9]{1}$"

##### DEBUT DU JEU

while msg_a_envoyer != b"q":

    #On demande le déplacement
    instruction_ok = True

    # Avant d'envoyer le déplacement, on vérifie le format rentré par le joueur
    while instruction_ok:
        print("Entrer un déplacement pour votre robot X ou q pour quitter : ")
        mvt_str = input(">") # On reçoit le déplacement sous forme de str
        print(" ")
        
        if re.search(r"q", mvt_str) is not None: # Si le joueur rentre "q", on quitte le jeu
            msg_a_envoyer = b"q"
            instruction_ok = False
            
        elif re.search(expression, mvt_str) is None: # On vérifie avec l'expression régulière que l'instruction est au bon format
            print("L'expression n'est pas valide.")
            print("Le premier caractère doit être un point cardinal n, s, e ou o. ")
            print("le deuxième caractère doit être un entier entre 1 et 9.")

        else:
            # on encode l'instruction
            msg_a_envoyer = mvt_str.encode()
            instruction_ok = False

    # On envoie le message correspondant au serveur
    connexion_avec_serveur.send(msg_a_envoyer) 

    # On reçoit la nouvelle carte du labyrinthe
    msg_recu = connexion_avec_serveur.recv(1024)
    print(msg_recu.decode()) # Là, encore, peut planter avec des accents
    

print("Fermeture de la connexion")
#Fermer la connexion
connexion_avec_serveur.close()
