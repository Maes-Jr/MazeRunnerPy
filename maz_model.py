# maz_model. py
from doctest import master


class cellule:
    def __init__(self):
        # Chaque cellule a 4 murs au depart: Nord, Sud, Est, Ouest
        self.murs={"N":True, "S":True, "E":True, "O": True}
        self.visited = False # utile pour le générateur et le Solveur

def initialiser_grille(n,m):
    """
    Crée  une grille n x m avec toute les cellule ayant tous leurs murs.
    """
    grille=[[cellule() for _ in range(m)] for _ in range (n)]
    return grille
def casser_mur(cellule1,cellule2, direction):
    """
    Casse le mur entre deux cellules voisines dans une direction donnée.
    direction : 'N', 'S', 'E', 'O'
    """
    opposé = {"N": "S", "S": "E", "E": "O", "O": "E"}
    cellule1.murs[direction]= False
    cellule2.murs[opposé [direction]]= False

def cellule_pleine(cellule):
    """
    Verifie si une cellule a encore tous ses murs.
    """
    return all(cellule.murs.values())

def Afficher_labyrinthe (grille, chemin=None):
    """
    Affiche le labyrinthe en mode texte avec des caractères ASCII.
    Optionnel: Pour afficher un chemin sous forme de points.
    """
    n=len(grille)
    m=len(grille[0])
    
    print ("+"+"---+"*m)

    for i in range(n):
        ligne_haut = "|"
        ligne_bas = "+"

        for j in range(m):
            if chemin and (i, j)in chemin :
                ligne_haut += " . "
            else:
                ligne_haut += "  "
            ligne_haut += "|" if grille[i][j].murs["E"] else " "
        for j in range(m):
            ligne_bas += "---+" if grille[i][j].murs["S"] else "   +"
        print(ligne_haut)
        print(ligne_bas)

if __name__=="__main__":
    n,m=4, 4
    labyrinthe = initialiser_grille(n,m)
    # Exemple : casser un murs entre (0,0) et (0,1)
    casser_mur(labyrinthe[0][0], labyrinthe[0][1], "E")
    casser_mur(labyrinthe[0][1], labyrinthe[1][1], "S")
    
    Afficher_labyrinthe (labyrinthe) 
