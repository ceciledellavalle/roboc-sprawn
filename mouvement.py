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

#########################################################################################
##     MA CLASSE
#########################################################################################

class Mouvement:
    """Le Mouvement est un objet qui contient une lettre référant aux quatre points
    cardinaux et un chiffre référant aux nombre de pass à faire dans cette 
    direction pour un déplacement."""

    def __init__(self, mvt_str):
        """L'objet mouvement est créé à partir d'une chaine de caractère (string).
        Il contient deux attributs :
        direction -- str - lettre désignant la direction du mouvement 
                            "n" pour Nord, "s" pour Sud, "e" pour Est, "o" pour Ouest
        nb_pas -- int - le nombre de pas (ou de case) à réaliser
        Attention, le format de la chaine caractère doit être respecté à l'initialisation !
        """
        liste_intermediaire = list(mvt_str)
        self.direction = liste_intermediaire[0]
        self.nb_pas = int(liste_intermediaire[1])