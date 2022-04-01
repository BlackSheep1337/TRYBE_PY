from sales_report import SalesReport
from csv import DictWriter

class SalesReportCSV(SalesReport):
    def serialize(self):
        with open(self.export_file + ".csv", "w") as file:
            headers = ["Coluna 1", "Coluna 2", "Coluna 3"]
            csv_writer = DictWriter(file, headers)
            csv_writer.writeheader()
            for item in self.build():
                csv_writer.writerow(item)
    
    def get_length(self):
        return len(self.build())

sales_report = SalesReportCSV('my_report')
sales_report.serialize()
print(sales_report.get_length())