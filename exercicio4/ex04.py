class CaixaEletronico:
    '''Classe para realizar operações do caixa'''
    def __init__(self, sacar, depositar, saldo, saldoAtual):
        self.sacar = sacar
        self.depositar = depositar
        self.saldo = saldo
        self.saldoAtual = saldoAtual
    # Fim def __init__(self, sacar, depositar, saldo)

    def saque (self, sacar, saldo):
        self.saldo = self.saldo - self.sacar

        return self.saldo
    # Fim def saque (self, sacar, saldo)

    def deposito (self, depositar, saldo):
        self.saldo = self.saldo + self.depositar

        return self.saldo
    # Fim def deposito (self, depositar, saldo)