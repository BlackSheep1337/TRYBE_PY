class ReportAnalyzer:
    def __init__(self, loader):
        self.loader = loader

    def avarage(self):
        data = self.loader.load_data()

        total = sum([order['final_price'] for order in data])

        return total / len(data)