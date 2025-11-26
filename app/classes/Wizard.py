from .Personnage import Personnage
from random import choice

class Wizard(Personnage):
    
    def __init__(self, name: str, fighting_moves: list[dict], turn: str):
        self.__name = name
        self.__health = 100
        self.__damages = 0  
        self.__xp = 0
        self.__fighting_moves = fighting_moves
        self.turn = turn 

        
    # getter / setter
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        if name:
            self.__name = name
        else:
            raise ValueError("Name shouldn't be empty")
        
    @property
    def fighting_moves(self) -> list[dict]:
        return self.__fighting_moves
    
    @fighting_moves.setter
    def fighting_moves(self, fighting_moves: list[dict]) -> None:
        if fighting_moves:
            self.__fighting_moves = fighting_moves
        else:
            raise ValueError("Fighting moves shouldn't be empty")
        
    @property
    def xp(self) -> int:
        return self.__xp
    
    @xp.setter
    def xp(self, xp: int) -> None:
        # Validation si l'XP est un entier positif
        if isinstance(xp, int) and xp >= 0:
            self.__xp = xp
        else:
            raise ValueError("Experience must be a non-negative integer.")
        
    @property
    def damages(self) -> int:
        return self.__damages
    
    @damages.setter
    def damages(self, value: int) -> None:
        if value < 0:
            raise ValueError("Damages can't be negative.")
        self.__damages = value
        
    @property
    def health(self) -> int:
        return self.__health
    
    @health.setter
    def health(self, health: int) -> None:
        # Validation si la santé est un entier positif
        if isinstance(health, int) and health > 0:
            self.__health = health
        else:
            raise ValueError("Health must be a positive integer.")
        
    # abtract methods from Personnage interface
    def fighting_move(self, opponent: Personnage, attack_strength: int = 0) -> None:
        """
        Choose a random attack from `self.fighting_moves` and apply it to the opponent.
        If the chosen move contains a damage/strength value, use it; otherwise fall back
        to the `attack_strength` parameter.
        """
        random_move = choice(self.fighting_moves)
        move_name = random_move.get('name', 'Coup de bâton')
        damage_to_deal = random_move.get('damage', 5)
        xp_to_gain = random_move.get('xp_gain', 1)
        print(f"{self.turn} : {self.name} lance {move_name} (Dégâts de l'attaque : {damage_to_deal})")
        
        # case where the opponent dodge the attack
        if opponent.dodge():
            print(f"> {opponent.name} s'est bien défendu et a esquivé l'attaque !")
        else:
            # case where the opponent suffers from the attack
            print(f"> C'est un magnifique coup réussi! {self.name} gagne {xp_to_gain} XP!")
            self.xp += xp_to_gain
            opponent.damages_taken(self, damage_to_deal)
        
    def dodge(self) -> bool:
        """
        Attempt to dodge an attack.
        Returns True if dodged, False otherwise.
        """
        # 20% chance to dodge
        is_dodging = choice([True, False, False, False, False])
        return is_dodging

    def damages_taken(self, opponent: Personnage, attack_strength: int) -> None:
        """
        Apply damages to the wizard's health.
        """
        opponent_xp = opponent.xp
        total_damages = attack_strength + opponent_xp
        self.damages += total_damages
        print(f"{self.name} subit {total_damages} dégâts (dégâts subis: {attack_strength} + BONUS XP: {opponent_xp})")
        print(f"État: {self.name} n'a plus que {self.health - self.damages} PV!")