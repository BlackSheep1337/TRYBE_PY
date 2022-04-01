from abc import ABC, abstractmethod

class Connector(ABC):
    @abstractmethod
    def get_count(token):
        pass
    
    @abstractmethod
    def update_count():
        pass