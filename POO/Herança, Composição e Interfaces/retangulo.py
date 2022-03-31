from figura_geometrica import FiguraGeometrica

class Retangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return f"The area is {self.base * self.altura}²"

    def perimetro(self):
        return f"The parameter is {2 * (self.base + self.altura)}"

my_rectangle = Retangulo(12, 7)

print(my_rectangle.area())
print(my_rectangle.perimetro())