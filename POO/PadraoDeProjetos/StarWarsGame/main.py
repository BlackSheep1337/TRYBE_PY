from jedi import Jedi
from soldier import Soldier
from jedi_adpter import JediAdpter

class StarWarsGame:
    def __init__(self, character):
        self.character = character

    def start_game(self):
        print(f"You caused {self.character.attack()} damage to the enemy")


StarWarsGame(Soldier(5)).start_game()
StarWarsGame(JediAdpter(Jedi(5))).start_game()