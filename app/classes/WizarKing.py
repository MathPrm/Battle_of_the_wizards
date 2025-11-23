from .Wizard import Wizard

class WizardKing(Wizard):
    
    def fighting_move(self, opponent: str, attack_strength: int) -> None:
        return super().fighting_move(opponent, attack_strength)
    
    def dodge(self) -> None:
        return super().dodge()
    
    def damages_taken(self, opponent: str, attack_strength: int) -> None:
        return super().damages_taken(opponent, attack_strength)