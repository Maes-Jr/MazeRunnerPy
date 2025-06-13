import random
from maze_model import initialiser_grille, casser_murs, afficher_labyrinthe

def generer_labyrinthe(grille, x, y):
    grille[x][y].visited = True
    directions = [("N", (-1, 0)), ("S", (1, 0)), ("E", (0, 1)), ("O", (0, -1))]
    random.shuffle(directions)
    for direction, (dx, dy) in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grille) and 0 <= ny < len(grille[0]) and not grille[nx][ny].visited:
            casser_murs(grille[x][y], grille[nx][ny], direction)
            generer_labyrinthe(grille, nx, ny)

if __name__ == "__main__":
    n, m = 10, 10
    labyrinthe = initialiser_grille(n, m)
    generer_labyrinthe(labyrinthe, 0, 0)
    afficher_labyrinthe(labyrinthe)
