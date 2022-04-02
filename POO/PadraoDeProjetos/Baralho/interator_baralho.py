from collections.abc import Iterator

class InteratorDoBaralho(Iterator):
    def __init__(self, cards):
        self._cards = cards
        self._pos = 0
    
    def __next__(self):
        try:
            card = self._cards[self._pos]
        except IndexError:
            raise StopIteration()
        else:
            self._pos += 1
            return card