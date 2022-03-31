from figura_geometrica import FiguraGeometrica

class Quadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado * self.lado
    
    def perimetro(self):
        return self.lado * 4


my_squad = Quadrado(2)

print(my_squad.area())
print(my_squad.perimetro())