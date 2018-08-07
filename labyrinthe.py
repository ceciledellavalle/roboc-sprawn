#########################################################################################
##                                                                                     ##
##                              LE JEU DU LABYRINTHE                                   ##
##                          Création de ma classe Labyrinthe                           ##
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

class Labyrinthe:
    """ Le labyrinthe contient trois attributs :
        carte -- dictionnaire carte
        numero -- numéro du labyrinthe donné au joueur
        longueur -- entier correspondant à la longueur du labyrinthe
        largeur -- entier correspondant à la largeur du bayrinthe
        robot -- coordonnées du robot sous la forme d'une liste de deux int
        sortie -- coordonnées de la sortie sous la forme d'une liste de deux int

    La carte est un dictionnaire labyrinthe à partir d'un str.
    La clé du dictionnaire est une liste composé de 2 int qui désigne les coordonnées
    La valeur associée à une clé est un str qui peut être :
    " " -- vide
    "0" -- mur
    "." -- porte
    "X" -- robot
    "U" -- sortie
    """
    def __init__(self):
        """ Le labyrinthe initialisé par une carte vide, un robot à la position [0,0] et 
        une sortie à la position [100,100]
        """
        self.carte = {}
        self.numero = 0
        self.longueur = 0
        self.largeur  = 0
        self.robot = [0,0]
        self.sortie = [100, 100]
    
    def __repr__(self):
        """Méthode spéciale de Labyrinthe pour fabriquer un str
        Quand on rentre l'objet dans l'interpreteur ou qu'on utilise print"""
        carte_str = str()
        for i in range(1,self.longueur):
            for j in range(1,self.largeur):
                carte_str += self.carte[str(i),str(j)]
            carte_str += "\n"
        return carte_str
        
    def afficher_carte(self):
        """Fonction sans argument qui affiche un labyrinthe"""
        print(self)

    def telecharger(self, path, numero_lab):
        """Cette fonction de la classe des Labyrinthe permet d'initialiser un labyrinthe à partir 
        d'un fichier txt et du numéro de la carte associé.
        Elle reçoit les arguments :
        path -- chemin vers le fichier txt
        numero_lab -- le numéro du labyrinthe correspondant qui sera donné au joueur.
        """

        with open(path,"r") as f :
            # on initialise les compteurs pour remplir la carte
            i  = 1
            ii = str(i)
            j  = 1
            jj = str(j)

            # on parcourt un à un les caractères du fichier txt qui contient le labyrinthe
            for line in f.readlines():
                for letter in line :

                    # on teste si la lettre est bien un caractère prévu
                    if re.search(r"^[ O.XU]$", letter) is None:
                        break
                    else:
                        self.carte[ii,jj] = letter
                        if letter == "X":
                            self.robot = [i,j]
                        elif letter == "U":
                            self.sortie = [i,j]
                        j += 1
                        jj = str(j)
                self.largeur = j
                i += 1
                ii = str(i)
                j =1
                jj = str(j)

            self.longueur = i

        self.numero = numero_lab
    
    def enregistrer(self, dir_path, nom_du_fichier):
        """Cette fonction permet si le joueur le souhaite d'enregistrer le labyrinthe et
        de le charger à la prochaine partie.
        Elle enregistre le labyrinthe dans le dossier cartes situé dans le doccier de travail.
        """
        path = dir_path + "/cartes/{}.txt".format(nom_du_fichier)
        with open(path,"w") as labyrinthe_en_cours :
            labyrinthe_en_cours.write(str(self))
