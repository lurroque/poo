class Conta:

    def __init__(self, numero, titular, limite, saldo = 0):
        self.__numero = numero
        self.__titular = titular
        self.__limite = limite
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return """Titular: {}
                  Saldo: {}""".format(self.__titular, self.__saldo)

    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        if(valor <= (self.__saldo + self.__limite)):
            self.__saldo -= valor
        else:
            return "Saldo insuficiente."

    def transferir(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)

    @staticmethod
    def codigos_bancos():
        return {'BB' : '001', 'Caixa' : '104', 'Bradesco' : '237'}