# Crie um programa que calcule o índice de massa corporal de uma pessoa.

# Variáveis principais
nome = input("\nInforme seu nome: ")
altura = float(input("Informe sua altura: "))
peso = float(input("Informe seu peso:  "))
imc = peso / (altura ** 2)

# Variáveis de mensagem
divisoria = f'{"-"*6} Resultado do IMC {"-"*6}'
mensagem = f'\n{divisoria}\n\nOlá, {nome}!\n\nAltura: {altura}\nPeso: {peso}\nIMC: {imc:,.2f}\n'

# Função de saída
print(mensagem)
