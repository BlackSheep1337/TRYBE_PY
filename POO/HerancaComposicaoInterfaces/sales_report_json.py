from sales_report import SalesReport
from json import dump

class SalesReportJSON(SalesReport):
    def serialize(self):
        with open(self.export_file + ".json", 'w') as file:
            dump(self.build(), file)

    def get_length(self):
        return len(self.build())


sales_report = SalesReportJSON('my_report')
sales_report.serialize()

print(sales_report.get_length())