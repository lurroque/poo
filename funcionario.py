class Funcionario:
    
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostra_salario(self):
        return self.salario
    
    def mostra_nome(self):
        return self.nome

    def aumentar_salario(self, porcentagem):
        aumento = self.salario * porcentagem / 100
        novo_salario = self.salario + aumento
        return "Novo salário: R$ {}".format(novo_salario)