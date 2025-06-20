from maze_model import afficher_labyrinthe
from maze_generator import initialiser_grille, generer_labyrinthe

def dfs(grille, x, y, sortie_x, sortie_y, chemin):
    if (x, y) == (sortie_x, sortie_y):
        chemin.append((x, y))
        return True
    grille[x][y].visited = True
    chemin.append((x, y))
    directions = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "O": (0, -1)}
    for direction, (dx, dy) in directions.items():
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grille) and 0 <= ny < len(grille[0]):
            if not grille[x][y].murs[direction] and not grille[nx][ny].visited:
                if dfs(grille, nx, ny, sortie_x, sortie_y, chemin):
                    return True
    chemin.pop()
    return False

def resoudre_labyrinthe(grille, depart_x, depart_y, sortie_x, sortie_y):
    for ligne in grille:
        for cellule in ligne:
            cellule.visited = False
    chemin = []
    trouve = dfs(grille, depart_x, depart_y, sortie_x, sortie_y, chemin)
    if trouve:
        print("\nChemin trouvé !")
        afficher_labyrinthe(grille, chemin)
    else:
        print("Aucun chemin trouvé.")
    return chemin

if __name__ == "__main__":
    n, m = 10, 10
    labyrinthe = initialiser_grille(n, m)
    generer_labyrinthe(labyrinthe, 0, 0)
    afficher_labyrinthe(labyrinthe)
    chemin = resoudre_labyrinthe(labyrinthe, 0, 0, n-1, m-1)
