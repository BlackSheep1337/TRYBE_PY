from figura_geometrica import FiguraGeometrica
from math import pi as PI

class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return f"The circle area is {round(PI * self.raio * self.raio, 2)}"

    def perimetro(self):
        return f"The circle perimeter is {round(2 * PI * self.raio, 2)}"


my_circle = Circulo(3)

print(my_circle.area())
print(my_circle.perimetro())