from reserva import Reserva
from operator import attrgetter

class Hotel:
    def __init__(self, nome, quartos, reservas):
        self.nome = nome
        self.quartos = quartos
        self.reservas = reservas
    
    def check_in(self, *hospedes):
        try:
            quarto = self.quartos_disponiveis(len(hospedes))[0]
        except (IndexError):
            raise IndexError(
                'Não há quartos disponíveis para essa quantidade de hospedes'
            )
        else:
            quarto.reservado = True
            for hospede in hospedes:
                self.reservas.append(Reserva(quarto, hospede))
    
    def check_out(self, quarto):
        quarto.reservado = False
        self.reservas = [
            reserva
            for reserva in self.reservas
            if reserva.quarto != quarto
        ]

    def quartos_disponiveis(self, quantidade_de_hospedes):
        return sorted(
            [
                quarto
                for quarto in self.quartos
                if not quarto.reservado and
                quantidade_de_hospedes <= quarto.quantidade_de_hospedes
            ],
            key=attrgetter('quantidade_de_hospedes')
        )