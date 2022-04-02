from carta import Carta
from collections.abc import Iterable
from interator_baralho import InteratorDoBaralho

class Baralho(Iterable):
    naipes = 'copas ouros espadas paus'.split()
    valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()

    def __init__(self):
        self._cartas = [
            Carta(valor, naipe)
            for valor in self.valores
            for naipe in self.naipes
        ]

    def __len__(self):
        return len(self._cartas)

    def __iter__(self):
        return InteratorDoBaralho(self._cartas)

for game in Baralho.items():
    print(game)
