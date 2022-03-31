from abc import ABC, abstractmethod
import json
import gzip

class SalesReport(ABC):
    def __init__(self, export_file):
        self.export_file = export_file

    def build(self):
        return [{
        'Coluna 1': 'Dado 1',
        'Coluna 2': 'Dado 2',
        'Coluna 3': 'Dado 3'
        },
        {
        'Coluna 1': 'Dado A',
        'Coluna 2': 'Dado B',
        'Coluna 3': 'Dado C'
        }]

    def compress(self):
        binary_content = json.dumps(self.build()).encode('utf-8')

        with gzip.open(self.export_file + '.gz', 'wb') as compress_file:
            compress_file.write(binary_content)

    @abstractmethod
    def serialize(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_length(self):
        raise NotImplementedError

# my_report = SalesReport()