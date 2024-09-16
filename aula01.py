# Exercício 1: Faça um algoritmo que siga os seguintes passos ->
# 1- Recebe o valor de nome, idade, altura e cidade
# 2- No final mostre todas as informações dadas pelo usuário

name = input("\nWrite your name: ")
age = int(input("Type your age: "))
height = input("Type your height (with dot '.'): ")
city = input("Write where you from: ")
message = f"\nYour name's {name}\nYou are {age} years old\nYour height is {height}m\nYou are from {city}\n"
print(message)

# Exercício 2: Faça um algoritmo que receba 2 números e some eles
num1 = int(input("\nDigite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
soma = f"\n{num1} + {num2} = {num1+num2}"
print(soma, end="\n")
