# Exercício: Crie um programa que calcule o índice de massa corporal de uma pessoa.

# Mensagem de Introdução
print("\nCálculo do IMC (Índice de Massa Corpórea)\n\n[Atenção! Utilize ponto no lugar de vírgula para separar as casas decimais]\n")

# Variáveis principais
nome = input("Informe seu nome: ")
altura = float(input("Informe sua altura: "))  # Transforma a resposta do usuário em um número real (com casas decimais)
peso = float(input("Informe seu peso: "))      # Transforma a resposta do usuário em um número real (com casas decimais)
imc = peso / (altura ** 2)                     # Realiza o cálculo do IMC (Índice de Massa Corpórea)

"""
  O ** é usado na potenciação (exponenciação).
  Ex.: 
    ---------------------------------------------
    Python      |     3 ** 2     |    12 ** 3   |
    Matemática  |     3²         |    12³       |  
    ---------------------------------------------
"""

# Variáveis de mensagem
divisoria = f'{"-"*4} Dados Pessoais {"-"*4}'
mensagem = f'\n{divisoria}\n\nNome: {nome}\nAltura: {altura:.2f}m\nPeso: {peso:.2f}kg\nIMC: {imc:.2f}\n'

"""
  O :.[número_inteiro]f controla a exibição de números float, definindo quantas casas decimais devem 
  ser mostradas e arrendonda para cima quando a última casa decimal é maior ou igual a 5.
  
  Ex.: 
    pi = 3.1415926535
    formatacao = f'{pi:.4f}'
    print(formatacao)
    # Saída: 3.1416
"""

# Função de saída
print(mensagem)

# Função de saída
print(mensagem)
