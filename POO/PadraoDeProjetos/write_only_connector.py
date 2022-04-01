from abc import ABC, abstractmethod

class FullConnector(ABC):
    @abstractmethod
    def count_requires(self, token):
        pass