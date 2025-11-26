from .Wizard import Wizard
from .Personnage import Personnage

class WizardKing(Wizard):
    
    def __init__(self, name: str, turn: str):
        # Wizard King specific attacks
        moves = [
            {"name": "Boule de feu 🔥", "damage": 12, "xp_gain": 2},
            {"name": "Coup de Bâton 🪵", "damage": 5, "xp_gain": 1},
            {"name": "Tempête Émotionnelle : AAAAAH! Rends-moi mon anneau!!! 💫", "damage": 20, "xp_gain": 4}
        ]
        super().__init__(name, moves, turn)
    
    def fighting_move(self, opponent: Personnage, attack_strength: int = 0) -> None:
        return super().fighting_move(opponent, attack_strength)
    
    def dodge(self) -> bool:
        return super().dodge()
    
    def damages_taken(self, opponent: Personnage, attack_strength: int) -> None:
        return super().damages_taken(opponent, attack_strength)