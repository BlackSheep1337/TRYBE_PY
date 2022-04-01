from audioop import add
from read_only_connector import ReadOnlyConnector
import pysql #fake database


class ReadOnlySqlConnector(ReadOnlyConnector):
    def __init__(self, address, port):
        print(f"Connection on address: {address}:{port}")
        self.db = pysql.connection(address, port)

    def get_count(self, token):
        query = f"SELECT count FROM access WHERE token={token};--"
        result = self.db.execute(query)
        return result