from abc import ABC, abstractclassmethod

class EstrategiaImposto(ABC):
    @abstractclassmethod
    def calcular(self):
        raise NotImplementedError

class ISS(EstrategiaImposto):
    @classmethod
    def calcular(self, valor):
        return valor * 0.1

class ICMS(EstrategiaImposto):
    @classmethod
    def calcular(self, valor):
        return valor * 0.06

class PIS(EstrategiaImposto):
    @classmethod
    def calcular(self, valor):
        return valor * 0.0065

class COFINS(EstrategiaImposto):
    @classmethod
    def calcular(self, valor):
        return valor * 0.03

class Orcamento:
    def __init__(self, valor):
        self.valor = valor

    def calcular_imposto(self, imposto):
        return imposto.calcular(self.valor)

orcamento = Orcamento(1000)

print(f"ISS: {orcamento.calcular_imposto(ISS)}")
print(f"ICMS: {orcamento.calcular_imposto(ICMS)}")
print(f"PIS: {orcamento.calcular_imposto(PIS)}")
print(f"COFINS: {orcamento.calcular_imposto(COFINS)}")