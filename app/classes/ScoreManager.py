from .Wizard import Wizard  # On importe Wizard car on sait qu'on gère des sorciers
import time

class ScoreManager:
    
    def __init__(self, player1: Wizard, player2: Wizard):
        self.player1 = player1
        self.player2 = player2

    def display_stats(self) -> None:
        '''
        Display player's stats at the end of the turn
        '''
        p1_hp = max(0, self.player1.health - self.player1.damages)
        p2_hp = max(0, self.player2.health - self.player2.damages)
        
        print(f"🧙 {self.player1.turn} {self.player1.name}: {p1_hp} PV | {self.player1.xp} XP")
        print(f"👑 {self.player2.turn} {self.player2.name}: {p2_hp} PV | {self.player2.xp} XP")
        print("-" * 100)
        
    def battle(self) -> None:
        print("🪄 LE COMBAT COMMENCE ! 🪄\n")
        
        attacker = self.player1
        defender = self.player2
        turn_count = 1
        game_over = False
        
        while not game_over:
            print(f"\n🔔 Tour n°{turn_count} : C'est à {attacker.name} de jouer")
            attacker.fighting_move(defender)
            self.display_stats()
            
            if defender.health - defender.damages <= 0:
                print(f"\n☠️ {defender.name} ({defender.turn}) est tombé au combat !")
                print(f"🏆 LE VAINQUEUR EST {attacker.turn.upper()} ({attacker.name}) avec {attacker.xp} XP !")
                game_over = True
            else:
                attacker, defender = defender, attacker
                turn_count += 1
                time.sleep(1)