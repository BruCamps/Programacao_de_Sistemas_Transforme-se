class Conta:
    def __init__(self, nome, cpf, saldo=0):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
        self.deposito = 0
        self.saque = 0
        self.saldoFinal = 0

    def msgFinal(self):
        print(f'\nCliente: {self.nome}\nCPF: {self.cpf:0<11}\nSaldo: R${self.saldo:.2f}\n')

    def exibeDeposito(self):
        print(f'Depósito: R${self.deposito:.2f}\nSaldo: R${self.saldo:.2f}')

    def exibeSaque(self):
        print(f'Saque: R${self.saque:.2f}\nSaldo: R${self.saldo:.2f}')
