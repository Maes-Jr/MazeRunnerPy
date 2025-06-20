
from collections import deque
from typing import List, Tuple, Optional, Dict
from maze_model import Labyrinthe  # Supposant que le module 1 s'appelle Labyrinthe

class ResolveurBFS:
    """
    Implémentation de l'algorithme BFS pour résoudre un labyrinthe
    avec des fonctions de visualisation optionnelles.
    """
    
    def __init__(self, labyrinthe: Labyrinthe):
        """
        Initialise le résolveur avec un labyrinthe.
        
        Args:
            labyrinthe (Labyrinthe): Instance du labyrinthe généré
        """
        self.labyrinthe = labyrinthe
        self.largeur = labyrinthe.largeur
        self.hauteur = labyrinthe.hauteur
        self.visites = [[False for _ in range(self.largeur)] for _ in range(self.hauteur)]
        self.parents = [[None for _ in range(self.largeur)] for _ in range(self.hauteur)]
        self.chemin_solution = []
    
    def resoudre(self, depart: Tuple[int, int], arrivee: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        """
        Résout le labyrinthe en utilisant BFS (parcours en largeur).
        
        Args:
            depart (Tuple[int, int]): Position de départ (x, y)
            arrivee (Tuple[int, int]): Position d'arrivée (x, y)
            
        Returns:
            Optional[List[Tuple[int, int]]]: Le chemin solution ou None si non trouvé
        """
        file = deque()
        file.append(depart)
        self.visites[depart[1]][depart[0]] = True
        
        while file:
            cellule_actuelle = file.popleft()
            
            # Si on a atteint l'arrivée
            if cellule_actuelle == arrivee:
                self.chemin_solution = self._reconstruire_chemin(arrivee)
                return self.chemin_solution
            
            # Explorer les voisins
            for voisin in self._obtenir_voisins_valides(cellule_actuelle):
                if not self.visites[voisin[1]][voisin[0]]:
                    self.visites[voisin[1]][voisin[0]] = True
                    self.parents[voisin[1]][voisin[0]] = cellule_actuelle
                    file.append(voisin)
        
        return None  # Aucun chemin trouvé
    
    def visualiser_recherche(self, depart: Tuple[int, int], arrivee: Tuple[int, int], pas_a_pas: bool = False) -> None:
        """
        Visualise le processus de recherche BFS.
        
        Args:
            depart (Tuple[int, int]): Position de départ
            arrivee (Tuple[int, int]): Position d'arrivée
            pas_a_pas (bool): Si True, affiche chaque étape
        """
        file = deque([depart])
        self.visites[depart[1]][depart[0]] = True
        
        print("\nDébut de la visualisation BFS...")
        
        while file:
            cellule_actuelle = file.popleft()
            
            if pas_a_pas:
                self._afficher_etat_actuel(cellule_actuelle, arrivee)
                input("Appuyez sur Entrée pour continuer...")
            
            if cellule_actuelle == arrivee:
                self.chemin_solution = self._reconstruire_chemin(arrivee)
                print("\nSolution trouvée!")
                self._afficher_solution()
                return
            
            for voisin in self._obtenir_voisins_valides(cellule_actuelle):
                if not self.visites[voisin[1]][voisin[0]]:
                    self.visites[voisin[1]][voisin[0]] = True
                    self.parents[voisin[1]][voisin[0]] = cellule_actuelle
                    file.append(voisin)
        
        print("\nAucun chemin trouvé entre le départ et l'arrivée!")
    
    def _obtenir_voisins_valides(self, cellule: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Retourne les voisins accessibles depuis une cellule donnée.
        
        Args:
            cellule (Tuple[int, int]): Position (x, y)
            
        Returns:
            List[Tuple[int, int]]: Liste des positions voisines accessibles
        """
        x, y = cellule
        voisins = []
        
        # Vérification des murs dans chaque direction
        if not self.labyrinthe.contient_mur(x, y, 'N') and y > 0:
            voisins.append((x, y - 1))
        if not self.labyrinthe.contient_mur(x, y, 'S') and y < self.hauteur - 1:
            voisins.append((x, y + 1))
        if not self.labyrinthe.contient_mur(x, y, 'O') and x > 0:
            voisins.append((x - 1, y))
        if not self.labyrinthe.contient_mur(x, y, 'E') and x < self.largeur - 1:
            voisins.append((x + 1, y))
            
        return voisins
    
    def _reconstruire_chemin(self, arrivee: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Reconstruit le chemin solution à partir des parents enregistrés.
        
        Args:
            arrivee (Tuple[int, int]): Position d'arrivée
            
        Returns:
            List[Tuple[int, int]]: Chemin du départ à l'arrivée
        """
        chemin = []
        cellule = arrivee
        
        while cellule is not None:
            chemin.append(cellule)
            x, y = cellule
            cellule = self.parents[y][x]
        
        chemin.reverse()
        return chemin
    
    def _afficher_etat_actuel(self, cellule_actuelle: Tuple[int, int], arrivee: Tuple[int, int]) -> None:
        """
        Affiche l'état actuel de la recherche.
        
        Args:
            cellule_actuelle (Tuple[int, int]): Position actuelle
            arrivee (Tuple[int, int]): Position d'arrivée
        """
        print(f"\nÉtat actuel - Position: {cellule_actuelle}")
        for y in range(self.hauteur):
            ligne = "|"
            for x in range(self.largeur):
                if (x, y) == cellule_actuelle:
                    ligne += "A|"  # Actuelle
                elif (x, y) == arrivee:
                    ligne += "B|"  # But/Arrivée
                elif self.visites[y][x]:
                    ligne += ".|"  # Visitée
                else:
                    ligne += " |"  # Non visitée
            print(ligne)
            print("+" + "-+" * self.largeur)
    
    def _afficher_solution(self) -> None:
        """
        Affiche le labyrinthe avec le chemin solution.
        """
        print("\nLabyrinthe avec solution:")
        for y in range(self.hauteur):
            ligne = "|"
            for x in range(self.largeur):
                if (x, y) in self.chemin_solution:
                    if (x, y) == self.chemin_solution[0]:
                        ligne += "D|"  # Départ
                    elif (x, y) == self.chemin_solution[-1]:
                        ligne += "A|"  # Arrivée
                    else:
                        ligne += "*|"  # Chemin
                else:
                    ligne += " |"  # Case vide
            print(ligne)
            print("+" + "-+" * self.largeur)
        print(f"Longueur du chemin: {len(self.chemin_solution)} cases")
```

## Intégration avec les autres modules

1. **Compatibilité avec `maze_model.py` (Module 1)**:
   - Utilise les méthodes `contient_mur()` pour vérifier les murs
   - Suppose que le labyrinthe a des attributs `largeur` et `hauteur`

2. **Pour le contrôleur principal (Module 5)**:
   ```python
   # Exemple d'utilisation dans game_controller.py
   from bfs_solver_visualizer import ResolveurBFS
   
   def resoudre_bfs(labyrinthe, depart, arrivee):
       resolveur = ResolveurBFS(labyrinthe)
       chemin = resolveur.resoudre(depart, arrivee)
       if chemin:
           print("Solution trouvée par BFS!")
           resolveur._afficher_solution()
       else:
           print("Aucun chemin trouvé.")
       return chemin
   ```

3. **Visualisation optionnelle**:
   ```python
   # Pour une visualisation pas à pas
   resolveur.visualiser_recherche(depart, arrivee, pas_a_pas=True)
   ```

## Points clés de cette implémentation

1. **Conventions françaises**:
   - Noms de variables et méthodes en français
   - Documentation en français
   - Respect des bonnes pratiques PEP8

2. **Fonctionnalités complètes**:
   - Résolution BFS standard
   - Visualisation étape par étape
   - Affichage clair du chemin solution

3. **Extensibilité**:
   - Facile à intégrer avec une interface graphique future
   - Possibilité d'ajouter des animations

Cette implémentation correspond bien aux spécifications du projet tout en restant claire et maintenable
