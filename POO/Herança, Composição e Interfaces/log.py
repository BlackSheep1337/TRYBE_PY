from datetime import datetime
from log_em_tela import LogEmTela

class Log:
    def __init__(self, manipuladores):
        self._manipuladores = set(manipuladores)

    def adicionar_manipulador(self, manipulador):
        self._manipuladores.add(manipulador)

    def info(self, msg):
        self._log("INFO", msg)
    
    def alerta(self, msg):
        self._log("ALERTA", msg)

    def erro(self, msg):
        self._log("ERRO", msg)

    def debug(self, msg):
        self._log("DEBUG", msg)
    
    def _log(self, nivel, msg):
        for manipulador in self._manipuladores:
            manipulador.log(self.__formatar(nivel, msg))

    def __formatar(self, nivel, msg):
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return f"[{nivel} - {data}]: {msg}"
    
my_log = Log(["Dado 1", "Dado 2", "Dado 3"])

my_log._log(123, "funf?")