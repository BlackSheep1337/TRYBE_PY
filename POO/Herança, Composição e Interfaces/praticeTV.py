class TV:
    def __init__(self, tamanho):
        self._volume = 50
        self._canal = 1
        self._tamanho = tamanho
        self._ligada = False

    def aumentar_volume(self):
        if self._volume <= 99:
            self._volume += 1
    
    def diminuir_volume(self):
        if self._volume >= 0:
            self._volume -= 1
    
    def modificar_canal(self, canal):
        if canal < 1 or canal > 99:
            raise ValueError('Canal indisponivel')
        self._canal = canal
    
    def ligar_desligar(self):
        self._ligada = not self._ligada

my_tv = TV(45)

my_tv.ligar_desligar()
my_tv.diminuir_volume()
my_tv.modificar_canal(13)
# my_tv.aumentar_volume()

print(my_tv._ligada)
print(my_tv._volume)
print(my_tv._canal)
