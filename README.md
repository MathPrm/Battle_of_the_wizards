🧙‍♂️ ##Duel de Sorciers - Simulateur de Combat##

Bienvenue dans le Duel de Sorciers, un simulateur de combat au tour par tour écrit en Python. Ce projet met en scène un affrontement épique entre deux puissants magiciens, utilisant des concepts clés de la Programmation Orientée Objet (POO).

📋 #Fonctionnalités#

- Combat au tour par tour : Les joueurs attaquent alternativement jusqu'à ce que les points de vie (PV) de l'un d'eux tombent à zéro.

- Système de classes :

    - WhiteWizard (Sorcier Blanc) : Spécialisé dans les éléments naturels (Tornade, Éclair).

    - WizardKing (Roi Sorcier) : Utilise des attaques émotionnelles et de feu.

- Mécaniques de jeu :

    - Aléatoire : Chaque sorcier possède un set de mouvements, et l'attaque utilisée est choisie aléatoirement à chaque tour.

    - Esquive : Chaque personnage a 20% de chances d'esquiver totalement une attaque.

    - Système d'XP : Gagner de l'expérience augmente les dégâts infligés aux adversaires (Bonus XP ajouté aux dégâts bruts).

    - Interface Console : Affichage clair avec emojis pour suivre l'état du combat, les PV et l'XP.

🛠️ #Structure Technique#

1. Ce projet est conçu pour démontrer une architecture logicielle propre :

2. Interface Personnage (Personnage.py) : Une classe abstraite (ABC) qui définit le contrat que tous les combattants doivent respecter (méthodes fighting_move, dodge, propriétés name, xp).

3. Classe Mère Wizard (Wizard.py) : Implémente la logique commune (gestion de la santé, calcul des dégâts, getters/setters avec validation).

4. Classes Filles : WhiteWizard et WizardKing héritent de Wizard et définissent leurs propres attaques spécifiques.

5. Gestionnaire de Jeu (ScoreManager.py) : Orchestre la boucle de jeu, gère les tours et l'affichage des scores.

📂 Structure du Projet

Pour que les importations fonctionnent correctement (telles que définies dans main.py), vos fichiers doivent être organisés comme suit :

mon_projet/
│
├── main.py                # Point d'entrée du programme
└── app/
    ├── __init__.py        # (Optionnel, vide)
    └── classes/
        ├── __init__.py    # (Optionnel, vide)
        ├── Personnage.py
        ├── Wizard.py
        ├── WhiteWizard.py
        ├── WizardKing.py
        └── ScoreManager.py


🚀 #Comment lancer le jeu#

1. Assurez-vous d'avoir Python 3.x installé.

2. Placez-vous à la racine du projet (là où se trouve main.py).

3. Exécutez la commande suivante :

```python main.py```


🎮 #Exemple de déroulement#

```🪄 LE COMBAT COMMENCE ! 🪄

🔔 Tour n°1 : C'est à Luc de jouer
joueur 1 : Luc lance Éclair Foudroyant ⚡ (Dégâts de l'attaque : 20)
> C'est un magnifique coup réussi! Luc gagne 4 XP!
Georges Le Malin subit 20 dégâts (dégâts subis: 20 + BONUS XP: 0)
État: Georges Le Malin n'a plus que 80 PV!
🧙 joueur 1 Luc: 100 PV | 4 XP
👑 joueur 2 Georges Le Malin: 80 PV | 0 XP

----------------------------------------------------------------------------------------------------

🔔 Tour n°2 : C'est à Georges Le Malin de jouer
joueur 2 : Georges Le Malin lance Boule de feu 🔥 (Dégâts de l'attaque : 12)
> Luc s'est bien défendu et a esquivé l'attaque !
...
```
