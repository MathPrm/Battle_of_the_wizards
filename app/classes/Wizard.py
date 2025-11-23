from .Personnage import Personnage

class Wizard(Personnage):
    
    def __init__(self, name: str, fightings_moves: list[str], xp: int, damages: int, turn: str, health: int =100):
        self.__name = name
        self.__fighting_moves = fightings_moves
        self.__xp = xp
        self.__damages = damages
        self.turn = turn
        self.__health = health
        
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
    def fighting_moves(self) -> list[str]:
        return self.__fighting_moves
    
    @fighting_moves.setter
    def fighting_moves(self, fighting_moves: list[str]) -> None:
        if fighting_moves:
            self.__fighting_moves = fighting_moves
        else:
            raise ValueError("Fighting moves shouldn't be empty")
        
    @property
    def xp(self) -> int:
        return self.__xp
    
    @xp.setter
    def xp(self, xp: int) -> None:
        if xp:
            self.__xp = xp
        else:
            raise ValueError("Experience shouldn't be empty")
        
    @property
    def damages(self) -> int:
        return self.__damages
    
    @damages.setter
    def damages (self, damages: int) -> None:
        if damages:
            self.__damages = damages
        else:
            raise ValueError("Damages shouldn't be empty")
        
    @property
    def health(self) -> int:
        return self.__health
    
    @health.setter
    def health(self, health) -> None:
        if health:
            self.__health = health
        else:
            raise ValueError("Health shouldn't be empty")
        
    # abtract methods from Personnage interface
    def fighting_move(self, opponent: str, attack_strength: int) -> None:
        print(f"{self.name} a lancé une attaque basique de {attack_strength} dégâtssur {opponent}.\n")
        
    def dodge(self) -> None:
        print(f"attaque esquivée !\n")
        
    def damages_taken(self, opponent: str, attack_strength: int) -> None:
        print(f"{opponent} a subi {attack_strength} dégâts.")