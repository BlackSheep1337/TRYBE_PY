from random import randint

class Soldier:
    def __init__(self, level):
        self.level = level
    
    def attack(self):
        return self.level * randint(self.level, self.level * 10) #Number between 5 - 50 * 5
    