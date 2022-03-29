from sales_report import SalesReport
from csv import DictWriter

class SalesReportCsv(SalesReport):
    def serialize(self):
        with open(self.export_file + ".csv", "w") as file:
            headers = ["Coluna 1", "Coluna 2", "Coluna 3"]
            csv_writer = DictWriter(file, headers)
            csv_writer.writeheader()
            for item in self.build():
                csv_writer.writerow(item)

sales_report = SalesReportCsv('my_report')
sales_report.serialize()