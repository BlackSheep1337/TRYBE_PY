import pyredis #fake database
from read_only_connector import ReadOnlyConnector
 
class RedisConnector(ReadOnlyConnector):
    def __init__(self, address: str, port: int):
        print(f"Connected to addres: {address}:{port}")
        self.db = pyredis.connect(address, port)

    def update_count(self, token):
        amount = self.get_count()
        if amount is None:
            self.db.insert({ token: 1 })
        else:
            self.db.insert({ token: amount + 1})