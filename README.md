MazeRunnerPy

MazeRunnerPy est un projet Python destiné à la création, la résolution et la visualisation de labyrinthes. Il vise à fournir un ensemble d’outils modulaires pour générer différents types de labyrinthes, implémenter des algorithmes de résolution classiques, et visualiser le chemin parcouru par l’algorithme.

Fonctionnalités principales

- Génération de labyrinthes de différentes tailles et formes.
- Implémentation de plusieurs algorithmes de résolution (DFS, BFS, A*, etc.).
- Visualisation en temps réel ou en images du processus de résolution.
- Interface en ligne de commande simple d’utilisation.

Installation

1. Clonez ce dépôt :
   bash
   git clone https://github.com/Maes-Jr/MazeRunnerPy.git
   cd MazeRunnerPy
  
   

2. Installez les dépendances :
   bash
   pip install -r requirements.txt
   

Utilisation

Exemple d’exécution d’une génération et résolution de labyrinthe :
bash
python main.py --generate --solve --visualize --size 20x20

Options courantes

- generate : Générer un nouveau labyrinthe.
- size WxH : Spécifier la taille du labyrinthe (ex : 20x20).
- solve : Résoudre le labyrinthe généré.
- algorithm [dfs|bfs|astar] : Choisir l’algorithme de résolution.
- visualize : Afficher la visualisation du processus de résolution.

Structure du projet

MazeRunnerPy/
├── maze/             Modules de génération et de gestion des labyrinthes
├── solver/           Algorithmes de résolution
├── visualizer/       Visualisation (console, graphique, images)
├── main.py           Point d’entrée principal
├── requirements.txt  Dépendances Python
└── README.md


Contributeur

David Shimatu Allegresse
Diantezulua Makani Makanda Jordy
Dibay Lubamba Emmanuel
Dimercia Masala Ipanga
Dipa Tshipamba Valence

**Auteur** : [Maes-Jr](https://github.com/Maes-Jr)
