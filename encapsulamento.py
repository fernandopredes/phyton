class Conta:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.__saldo = saldo
    def consulta_saldo(self):
        return self.__saldo

contaNova = Conta(10, 75.90)
print(contaNova.numero)
contaNova.__saldo = 10
print(contaNova._Conta__saldo)
print(dir(contaNova))
print(contaNova.consulta_saldo())
