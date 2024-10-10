class Conta:
    def __init__(self, nome, cpf, saldo=0):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
        self.deposito = 0
        self.saque = 0
        self.saldoFinal = 0

    def msgFinal(self):
        if len(str(self.cpf)) < 11:
            msgCPF = f'{self.cpf:0>11}'
        else:
            msgCPF = f'{str(self.cpf)[:11]}'

        print(f'\nCliente: \033[1;35m{self.nome}\033[m')
        print(f'CPF: \033[1;35m{msgCPF}\033[m')
        print(f'Saldo: \033[1;35mR${self.saldo:.2f}\033[m\n')

    def exibeDeposito(self):
        print(f'Depósito: \033[1;35mR${self.deposito:.2f}\033[m')
        print(f'Saldo: \033[1;35mR${self.saldo:.2f}\033[m')

    def exibeSaque(self):
        print(f'Saque: \033[1;35mR${self.saque:.2f}\033[m')
        print(f'Saldo: \033[1;35mR${self.saldo:.2f}\033[m')
