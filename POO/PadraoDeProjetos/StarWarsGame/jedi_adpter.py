class JediAdpter:
    def __init__(self, character):
        self.character = character

    def attack(self):
        return self.character.attackWithSaber()