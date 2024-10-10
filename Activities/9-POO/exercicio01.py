"""
Exercício: Crie um programa em python simulando uma conta bancaria. O
programa deve armazenar o nome do cliente, cpf e saldo em conta. 
O programa deve dar a possibilidade do cliente exibir o saldo, depositar na
conta e sacar da conta.
"""

from conta import Conta

try: 
    nome = input("Digite seu nome: ") or "Anônimo"
    cpf = int(input("Digite seu CPF: "))
    saldo = float(input("Digite seu saldo: "))

    conta = Conta(nome, cpf, saldo)
    print(f"\nOlá! Bem-vindx, \033[1;35m{nome}\033[m!\nO que deseja fazer hoje?")

    while True:
        opcao = int(input(f"\n[1] Depositar\n[2] Sacar\n[3] Sair\n\n\033[0;35mEscolha uma das opções:\033[m "))

        if opcao == 1:
            conta.deposito = float(input("\n\033[0;35mDigite o valor do depósito:\033[m "))
            conta.saldo += conta.deposito
            conta.exibeDeposito()

        elif opcao == 2:
            conta.saque = float(input("\n\033[0;35mDigite o valor do saque:\033[m "))
            conta.saldo -= conta.saque
            conta.exibeSaque()

        else:
            conta.msgFinal()
            break

except ValueError:
    print("\n\033[1;31m[ERRO: O valor informado não é um número! Tente novamente]\033[m\n")
