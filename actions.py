#########################################################################################
##                                                                                     ##
##                              LE JEU DU LABYRINTHE                                   ##
##                        Les fonctions utilisées dans roboc                           ##
##                                                                                     ##
#########################################################################################

#########################################################################################
##     IMPORTATION
#########################################################################################
import sys
import re
import os

#########################################################################################
##     LES FONCTIONS
#########################################################################################


def deplacer(un_labyrinthe, mvt):
    """ Fonction de déplacement du robot dans le labyrinthe
    reçoit une instruction sous la forme d'une lettre cardinale:
    n -- nord
    s -- sud
    e -- est
    o -- ouest
    Il renvoit la nouvelle carte du laryrinthe avec le robot déplacé"""
    # on traduit le cardinal par un vecteur
    if mvt.direction =="n":
        vecteur = [-1,0]
    elif mvt.direction =="s":
        vecteur = [1,0]
    elif mvt.direction =="e":
        vecteur = [0,1]
    elif mvt.direction =="o":
        vecteur = [0,-1]

    # notre robot exécute un pas après l'autre
    for k in range(0,mvt.nb_pas):
        a_robot = [un_labyrinthe.robot[0],un_labyrinthe.robot[1]] # ancienne position du robot
        n_robot = [un_labyrinthe.robot[0]+vecteur[0],un_labyrinthe.robot[1]+vecteur[1]] # nouvelle position du robot

        # notre robot teste s'il ne s'agit pas d'un mur
        # l'avantage c'est qu'il y a toujours un mur qui encadre le labyrinthe
        # le robot ne risque donc pas de se volatilier
        if un_labyrinthe.carte[str(n_robot[0]),str(n_robot[1])] == "O":
            mvt.nb_pas = k
            break

        # et si on atterri sur la sorite en milieu de parcours, on arrete tout.
        elif un_labyrinthe.carte[str(n_robot[0]),str(n_robot[1])] == "U":
            un_labyrinthe.carte[str(a_robot[0]),str(a_robot[1])] = " "
            un_labyrinthe.carte[str(n_robot[0]),str(n_robot[1])] = "X"
            un_labyrinthe.robot = n_robot
            break

        # sinon, le robot avance et laisse un vide derrière lui
        # dans mon jeu le robot ouvre les portes
        else :
            un_labyrinthe.carte[str(a_robot[0]),str(a_robot[1])] = " "
            un_labyrinthe.carte[str(n_robot[0]),str(n_robot[1])] = "X"
            un_labyrinthe.robot = n_robot




def sortir(un_labyrinthe):
    """ Fonction de test pour la sortie du labyrinthe
    il renvoit le booléen suivant :
    True -- les coordonnées du robot sont les mêmes que celles de la sortie
    False -- les coordonnées du robot sont différentes de la sortie
    """
    if un_labyrinthe.robot == un_labyrinthe.sortie :
        return True
    else :
        return False




def question_fermee():
    """Fonction qui demande OUI/NON et qui renvoit le booléen correspondant
    True -- réponse OUI
    False -- réponse non
    """
    instruction_ok = True
    while instruction_ok:
        print("OUI / NON")
        continuer = input(">")
        if continuer == "OUI" :
            reponse_bool = True
            instruction_ok = False
        elif continuer == "NON":
            reponse_bool = False
            instruction_ok = False
        else:
            print("Pardon, je n'ai pas bien compris. Souhaites-tu jouer au jeu du labyrinthe ? \n \
Tu dois me répondre en tapant OUI ou NON avec ton clavier.")
    return reponse_bool


