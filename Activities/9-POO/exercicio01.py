"""
Exercício: Crie um programa em python simulando uma conta bancaria. O
programa deve armazenar o nome do cliente, cpf e saldo em conta. 
O programa deve dar a possibilidade do cliente exibir o saldo, depositar na
conta e sacar da conta.
"""

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

try: 
    nome = input("Digite seu nome: ") or "Anônimo"
    cpf = int(input("Digite seu CPF: "))
    saldo = float(input("Digite seu saldo: "))

    objeto = Conta(nome, cpf, saldo)
    print(f"\nOlá! Bem-vindx, {nome}!\nO que deseja fazer hoje?")

    while True:

        opcao = int(input(f"\nEscolha uma das opções:\n[1] Depositar\n[2] Sacar\n[3] Sair\n"))

        if opcao == 1:
            objeto.deposito = float(input("Digite o valor do depósito: "))
            objeto.saldo += objeto.deposito
            objeto.exibeDeposito()

        elif opcao == 2:
            objeto.saque = float(input("Digite o valor do saque: "))
            objeto.saldo -= objeto.saque
            objeto.exibeSaque()

        else:
            objeto.msgFinal()
            break

except ValueError:
    print("\n[ERRO: O valor informado não é um número! Tente novamente]\n")
