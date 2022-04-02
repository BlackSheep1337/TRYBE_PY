class Order:
    def __init__(
        self,
        items,
        cred_card
    ):
        self.items = items
        self.cred_card = cred_card
    # ...

class CredCard:
    def __init__(self, name, number, month, year, security_code):
        self.name, self.number = name, number
        self.month, self.year = month, year
        self.security_code = security_code