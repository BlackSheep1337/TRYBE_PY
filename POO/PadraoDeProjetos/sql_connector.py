import pysql #fake database
from connector import Connector

class SqlConnector(Connector):
    def __init__(self, address: str, port: int):
        print(f"Connection created at {address}:{port}")
        self.db = pysql.connect(address, port)

    def get_count(self, token):
        query = f"SELECT count FROM access WHERE token={token};--"
        result = self.db.execute(query)
        return result
    
    def count_request(self, token):
        query = f"UPDATE access SET count = count+=1 WHERE token={token};--"
        self.db.execute(query)
