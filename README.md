# 🧙‍♂️ Duel de Sorciers - Simulateur de Combat

Bienvenue dans **Duel de Sorciers**, un simulateur de combat au tour par tour écrit en Python, illustrant des concepts fondamentaux de la programmation orientée objet.

---

## 📋 Fonctionnalités

- **Combat au tour par tour** : Les joueurs attaquent successivement jusqu'à ce que les PV d'un sorcier atteignent zéro.
- **Système de classes** :
  - **WhiteWizard** : Maîtrise les éléments naturels (Tornade, Éclair).
  - **WizardKing** : Utilise des attaques émotionnelles et de feu.
- **Mécaniques de jeu** :
  - **Aléatoire** : L'attaque utilisée est choisie de manière aléatoire parmi les mouvements du sorcier.
  - **Esquive** : 20 % de chances d'éviter totalement une attaque.
  - **Système d'XP** : L'expérience gagnée augmente les dégâts infligés.
  - **Interface console** : Suivi clair du combat via emojis, PV et XP.

---

## 🛠️ Structure Technique

1. **Personnage (Personnage.py)** : Classe abstraite définissant le contrat des combattants.
2. **Wizard (Wizard.py)** : Classe mère gérant la santé, les dégâts et les propriétés communes.
3. **WhiteWizard & WizardKing** : Classes filles définissant leurs attaques spécifiques.
4. **ScoreManager (ScoreManager.py)** : Gère la boucle du jeu et l'affichage des tours.

---

## 📂 Structure du Projet

```
mon_projet/
│
├── main.py                # Point d'entrée du programme
└── app/
    ├── __init__.py
    └── classes/
        ├── __init__.py
        ├── Personnage.py
        ├── Wizard.py
        ├── WhiteWizard.py
        ├── WizardKing.py
        └── ScoreManager.py
```

---

## 🚀 Comment lancer le jeu

1. Installer Python 3.x.
2. Se placer à la racine du projet.
3. Exécuter :

```
python main.py
```

---

## 🎮 Exemple de déroulement

```
🪄 LE COMBAT COMMENCE ! 🪄

🔔 Tour n°1 : C'est à Luc de jouer
joueur 1 : Luc lance Éclair Foudroyant ⚡ (Dégâts de l'attaque : 20)
> C'est un magnifique coup réussi! Luc gagne 4 XP!
Georges Le Malin subit 20 dégâts (dégâts subis: 20 + BONUS XP: 0)
État: Georges Le Malin n'a plus que 80 PV!
🧙 joueur 1 Luc: 100 PV | 4 XP
👑 joueur 2 Georges Le Malin: 80 PV | 0 XP

---------------------------------------------------------------

🔔 Tour n°2 : C'est à Georges Le Malin de jouer
joueur 2 : Georges Le Malin lance Boule de feu 🔥 (Dégâts de l'attaque : 12)
> Luc s'est bien défendu et a esquivé l'attaque !
...
