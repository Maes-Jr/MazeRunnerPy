class Cellule:
    def __init__(self):
        self.murs = {"N": True, "S": True, "E": True, "O": True}
        self.visited = False

def initialiser_grille(n, m):
    return [[Cellule() for _ in range(m)] for _ in range(n)]

def casser_murs(cellule1, cellule2, direction):
    oppose = {"N": "S", "S": "N", "E": "O", "O": "E"}
    cellule1.murs[direction] = False
    cellule2.murs[oppose[direction]] = False

def cellule_pleine(cellule):
    return all(cellule.murs.values())

def afficher_labyrinthe(grille, chemin=None):
    n = len(grille)
    m = len(grille[0])
    print("+" + "---+" * m)
    for i in range(n):
        ligne_haut = "|"
        ligne_bas = "+"
        for j in range(m):
            if chemin and (i, j) in chemin:
                ligne_haut += " . "
            else:
                ligne_haut += "   "
            ligne_haut += "|" if grille[i][j].murs["E"] else " "
        for j in range(m):
            ligne_bas += "---+" if grille[i][j].murs["S"] else "   +"
        print(ligne_haut)
        print(ligne_bas)

if __name__ == "__main__":
    n, m = 5, 5
    labyrinthe = initialiser_grille(n, m)
    casser_murs(labyrinthe[0][0], labyrinthe[0][1], "E")
    casser_murs(labyrinthe[0][1], labyrinthe[1][1], "S")
    afficher_labyrinthe(labyrinthe)
