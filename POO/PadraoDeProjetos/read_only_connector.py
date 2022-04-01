from abc import ABC, abstractmethod

class ReadOnlyConnector(ABC):
    @abstractmethod
    def get_count(token):
        pass