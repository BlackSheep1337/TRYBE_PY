from random import randint


class Jedi:
    def __init__(self, level):
        self.level = level

    def attackWithSaber(self):
        return self.level * randint(self.level, self.level * 100)
