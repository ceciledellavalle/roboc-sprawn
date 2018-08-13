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
import random

import socket
import select

from mouvement import Mouvement
from labyrinthe import Labyrinthe
from actions import deplacer
from actions import question_fermee
from actions import sortir

#########################################################################################
##    CLASSE
#########################################################################################



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

##### GESTION DE LA CONNECTION
# Contruction du socket
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connection du socket
nom_hote=""
port = 12800
connexion_principale.bind((nom_hote, port))

# Faire écouter le socket
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))



##### DEBUT DU JEU 
continuer_jouer = True # bool() -- Vaut True tant que le Master est connecté
clients_connectes = [] # list() -- Liste des sockets des clients connectés

while continuer_jouer: # On commence à jouer

##### NOUVELLE PARTIE

    # Le joueur commence une nouvelle partie
    partie = True
    print(" ")
    print("~*~ Nouvelle partie ~*~")
    print(" ")

    # Le Master choisit une carte
    choix_labyrinthe = """
    Labyrinthes existants :
        1 - facile 
        2 - prison
        3 - hyperloop
        """
    print(choix_labyrinthe)
    print("Entrez un numéro de labyrinthe : ")
    numero_carte = input(">")
    print(" ")

    # La carte est chargée dans mon_labyrinthe
    mon_labyrinthe = Labyrinthe() # initialisation du labyrinthe de la class Labyrinthe
    mon_labyrinthe = dict_labyrinthe[numero_carte]
    # La console affiche la carte
    mon_labyrinthe.afficher_carte()


    while partie:

        # Le joueur entre un déplacment mvt_str

        instruction_ok = True # bool() -- Vaut True tant que le serveur ne reçoit pas de déplacement des joueurs

        while instruction_ok :

            # On va vérifier que de nouveaux clients ne demandent pas à se conncerter
            # Pour cela, on écoute la connection_principale en lecture
            # On attend au maximum 500ms
            connexions_demandees, wlist, xlist = select.select([connexion_principale], [], [], 1)

            for connexion in connexions_demandees:
                # Accepter la connexion client
                # méthode accept qui bloque le programme tant qu'aucun client n'est connecté
                # renvoie le socket connecté ET un tuple présentant l'adresse IP et le port de connexion client
                connexion_avec_client, infos_connexion = connexion.accept()
                # On ajoute le socket connecté à la liste des clients
                clients_connectes.append(connexion_avec_client)

            # On attend là encore 500ms max
            # On enferme l'appel à select.select dans un bloc try
            # En effet, si la liste des clients connectés est vide, une exception peut être levée
            clients_a_lire = []
            try:
                clients_a_lire, wlist, xlist = select.select(clients_connectes, [], [], 1)
            except select.error:
                pass
            else:
            #   On parcourt la liste des clients à lire
                for index, client in enumerate(clients_a_lire):

                    # On reçoit l'instruction de déplacement du joueur
                    msg_recu = client.recv(1024)

                    # peut planter si le message contient des caractères spéciaux
                    msg_recu = msg_recu.decode()
                    print("Le joueur numéro {0} a choisi de déplacer son robot de {1}".format(index,msg_recu))
                    mvt_str = str(msg_recu)
            
                    # On crée l'objet de la classe Mouvement correspondant au déplacement entré par le joueur
                    mvt = Mouvement(mvt_str)

                    # Le robot est déplacé
                    deplacer(mon_labyrinthe, mvt)

                    # On affiche de nouveau la carte
                    mon_labyrinthe.afficher_carte()

                    # On envoie le labyrinthe au client
                    msg_a_envoyer = str(mon_labyrinthe).encode()
                    client.send(msg_a_envoyer) 
                 


        # Test est-ce que le robot est sorti
        if sortir(mon_labyrinthe):
            print("Bravo, tu es sorti du labyrinthe !!")
            print(" ")
            partie = False
    
    # Le joueur peut commencer une nouvelle partie
    print("Lancer une nouvelle partie au jeu du labyrinthe ? ")
    print(" ")
    continuer_jouer = question_fermee()
    
print("Fermeture de la connexion. ")

# Fermer les connexions clients
for client in clients_connectes:
     client.close()

# Fermer la connexion principales
connexion_principale.close()






















