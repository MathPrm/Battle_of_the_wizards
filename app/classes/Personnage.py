# interface that defines a contract for characters classes

from abc import ABC, abstractmethod

class Personnage(ABC):
    
    @abstractmethod
    def fighting_move(self, opponent: str, attack_strength: int) -> None:
        '''
        This function allow the character to use a fighting move.
        Args:
            - opponent (str): name of the opponent against whom the player is attacking.
            - attack_strength (int): strength of the attack.
        '''
        ...
        
    @abstractmethod
    def dodge(self) -> None:
        '''
        This function allow the character to dodge an attack.
        '''
        ...
        
    @abstractmethod
    def damages_taken(self, opponent: str, attack_strength: int) -> None:
        '''
        This function calculate the damages taken by the character.
        Args:
            - opponent (str): name of the opponent against whom the player is attacking.
            - attack_strength (int): strength of the attack.
        '''
        ...