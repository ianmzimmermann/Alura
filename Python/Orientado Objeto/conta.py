class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo Objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposito(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        if (self.__limite_saque(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite".format(valor))

    def __limite_saque(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def transferencia(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def cod_banco():
        return "001"
