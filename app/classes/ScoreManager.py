class ScoreManager:
    
    def __init__(self, white_wizard_score: int, wizard_king_score: int):
        self.__white_wizard_score = white_wizard_score
        self.__wizard_king_score = wizard_king_score
    
    def score(self) -> None:
        print(f"Scores:\nWhite Wizard: {self.__white_wizard_score}\nWizardKing: {self.__wizard_king_score}")