from app.classes.WhiteWizard import WhiteWizard
from app.classes.WizardKing import WizardKing
from app.classes.ScoreManager import ScoreManager

def main():

    gandalf = WhiteWizard("Luc", "joueur1")
    sauron = WizardKing("Georges Le Malin", "joueur 2")

    game_manager = ScoreManager(gandalf, sauron)

    game_manager.battle()

if __name__ == "__main__":
    main()