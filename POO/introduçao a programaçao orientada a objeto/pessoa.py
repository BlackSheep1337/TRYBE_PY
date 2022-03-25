class People:
    def __init__(self, name, cpf, gender, active):
        self.name = name
        self.cpf = cpf
        self.gender = gender
        self.active = active

    def desativate(self):
        self.active = False


if __name__ == "__main__":
    person = People("Alexandre", "123456789", "M", True)
    print(person.name)
    print(person.gender)
    print(person.cpf)
    print("Ativado: " + str(person.active))
    person.desativate()
    print("Desativando...")
    print("Ativado: " + str(person.active))