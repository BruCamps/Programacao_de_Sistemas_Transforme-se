# Exercício 1: Faça um algoritmo que siga os seguintes passos ->
# 1- Recebe o valor de nome, idade, altura e cidade
# 2- No final mostre todas as informações dadas pelo usuário

nome = input("\nEscreva seu nome: ")
idade = int(input("Digite a sua idade: "))
altura = float(input("Informe a sua altura (com '.', não ','): "))
cidade = input("Write where you from: ")
mensagem = f"\nSeus Dados Pessoais:\n\n Nome:{nome}\nIdade:{idade} anos\nAltura: {altura} m\nCidade: {cidade}\n"
print(mensagem)

# Exercício 2: Faça um algoritmo que receba 2 números e mostre o resultado da soma entre ambos
num1 = int(input("\nDigite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
sumMsg = f"\n{num1} + {num2} = {num1+num2}"
print(sumMsg, end="\n")

# Aprendendo a usar a função type()
resultSum = 1 + 5
username = "Kiera"
print(type(resultSum)) # Retorna o tipo de dado recebido na variável -> Será do tipo Integer (Número Inteiro)
# Saída: <class 'int'>
print(type(username)) # Retorna o tipo de dado recebido na variável -> Será do tipo String (Texto)
# Saída: <class 'str'>