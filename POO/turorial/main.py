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
    def calculate_total_price(self, x ,y):
        return x * y

item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))


item2 = Item()
item2.name = "Notbook"
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))

