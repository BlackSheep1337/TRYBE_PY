# class Item:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
    
#     def __repr__(self):
#         return f"Hello {self.name} your age is {self.age} and grade {self.grade}"


# mug = Item("Doe", "12", "7")

# print(mug)

class Item:
    pay_rate = 0.8 #The pay rate after 20% of discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        #Run validation to the received arguments
        assert price >= 0, f"Price {price} must be greater or equal than zero"
        assert quantity >= 0,  f"Quantity {quantity} must be greater or equal than zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
    def calculate_total_price(self) -> int:
        self.quantity = 1 if self.quantity == 0 else self.quantity
        return self.price * self.quantity

    def apply_discount(self) -> float:
        self.price = self.price * self.pay_rate

    def __repr__(self) -> str:
        return f"Item('{self.name}, {self.price}, {self.quantity}')"

# item1 = Item("Phone", 100, 2)
# item1.apply_discount()

# print(item1.price)

# item2 = Item("Notbook", 1000, 5)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

item1 = Item("IPhone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)