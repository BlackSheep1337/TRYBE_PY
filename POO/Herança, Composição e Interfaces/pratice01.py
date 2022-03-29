import json
from csv import DictWriter

class SalesReport():
    def __init__(self, export_file):
        self.export_file = export_file + '.json'

    def build(self):
        return [{
            'Coluna 1': 'Dado 1',
            'Coluna 2': 'Dado 2',
            'Coluna 3': 'Dado 3',
        },
        {
            'Coluna 1': 'Dado A',   
            'Coluna 2': 'Dado B',   
            'Coluna 3': 'Dado C',   
        }]

    def serialize_json(self):
        with open(self.export_file, 'w') as file:
            json.dump(self.build(), file)

    def serialize_cvs(self):
        with open('my_report.csv', 'w') as file:
            headers = ["Coluna 1", "Coluna 2", "Coluna 3"]
            csv_writer = DictWriter(file, headers)
            csv_writer.writeheader()
            for item in self.build():
                csv_writer.writerow(item)


sales_report = SalesReport('my_report')

sales_report.serialize_json()
sales_report.serialize_cvs()