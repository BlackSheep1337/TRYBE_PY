class Address:
    def __init__(self, street, number, district):
        self.street = street
        self.number = number
        self.district = district
    
    def items(self):
        return [
            self.number,
            self.street,
            self.district
        ]


class User:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_full_data(self):
           for info in self.address.items():
               return f"User info:\n{info}"


user = User('Ale', Address('andre luiz', 42, 'brotas'))

print(user.get_full_data())