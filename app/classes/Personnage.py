# interface that defines a contract for characters classes

from abc import ABC, abstractmethod

class Personnage(ABC):
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Méthode getter pour le nom"""
        ...
        
    @property
    @abstractmethod
    def xp(self) -> int:
        """Méthode getter pour l'expérience"""
        ...
    
    @abstractmethod
    def fighting_move(self, opponent: 'Personnage', attack_strength: int) -> None:
        '''
        This function allow the character to use a fighting move.
        Args:
            - opponent (str): name of the opponent against whom the player is attacking.
            - attack_strength (int): strength of the attack.
        '''
        ...
        
    @abstractmethod
    def dodge(self) -> bool:
        '''
        This function allow the character to dodge an attack.
        '''
        ...
        
    @abstractmethod
    def damages_taken(self, opponent: 'Personnage', attack_strength: int) -> None:
        '''
        This function calculate the damages taken by the character.
        Args:
            - opponent (str): name of the opponent against whom the player is attacking.
            - attack_strength (int): strength of the attack.
        '''
        ...