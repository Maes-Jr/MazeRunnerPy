from maze_model import initialiser_grille, afficher_labyrinthe
from maze_generator import generer_labyrinthe
from dfs_solver import resoudre_labyrinthe
from bfs_solver import bfs

def menu():
    print("\n=== MazeRunnerPy ===")
    print("1. Générer un nouveau labyrinthe")
    print("2. Afficher le labyrinthe")
    print("3. Résoudre avec DFS")
    print("4. Résoudre avec BFS")
    print("5. Quitter")
    print("====================")

def main():
    labyrinthe = None
    n, m = 0, 0

    while True:
        menu()
        choix = input("Votre choix : ")

        if choix == "1":
            n = int(input("Hauteur du labyrinthe : "))
            m = int(input("Largeur du labyrinthe : "))
            labyrinthe = initialiser_grille(n, m)
            generer_labyrinthe(labyrinthe, 0, 0)
            print("✅ Labyrinthe généré !")

        elif choix == "2":
            if labyrinthe:
                afficher_labyrinthe(labyrinthe)
            else:
                print("⚠️ Aucun labyrinthe généré.")

        elif choix == "3":
            if labyrinthe:
                print("🔍 Résolution avec DFS...")
                resoudre_labyrinthe(labyrinthe, 0, 0, n-1, m-1)
            else:
                print("⚠️ Aucun labyrinthe généré.")

        elif choix == "4":
            if labyrinthe:
                print("🔍 Résolution avec BFS...")
                chemin = bfs(labyrinthe, 0, 0, n-1, m-1)
                if chemin:
                    afficher_labyrinthe(labyrinthe, chemin)
                else:
                    print("Aucun chemin trouvé.")
            else:
                print("⚠️ Aucun labyrinthe généré.")

        elif choix == "5":
            print("👋 À bientôt !")
            break

        else:
            print("Option invalide, réessaie.")

if __name__ == "__main__":
    main()
