class Car:
    def __init__(self, speed, year, on):
        self.speed = speed
        self.year = year
        self.on = on

opala = Car(220, 1970, False)
# marea = Car()
# fusca = Car()


print(f"Velocidade maxima: {opala.speed}")
print(f"Ligado: {opala.on}")