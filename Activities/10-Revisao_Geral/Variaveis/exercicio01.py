"""
Exercício: Crie um programa que peça ao usuário para inserir dois números e, em
seguida, calcule e exiba a soma, a subtração, a multiplicação e a divisão
desses números.
1. Peça ao usuário para inserir o primeiro número.
2. Peça ao usuário para inserir o segundo número.
3. Calcule a soma, subtração, multiplicação e divisão dos dois números.
4. Exiba os resultados de forma legível.
"""
 
numero1 = int(input("Digite o 1º número: "))
numero2 = int(input("Digite o 2º número: "))
 
def soma(num1, num2):
    return num1 + num2
def subtracao(num1, num2):
    return num1 - num2
def multiplicacao(num1, num2):
    return num1 * num2
def divisao(num1, num2):
    return num1 / num2
 
print(f"\nSoma: {numero1} + {numero2} = {soma(numero1, numero2)}")
print(f"Subtração: {numero1} - {numero2} = {subtracao(numero1, numero2)}")
print(f"Multiplicação: {numero1} * {numero2} = {multiplicacao(numero1, numero2)}")
print(f"Divisão: {numero1} / {numero2} = {divisao(numero1, numero2):.2f}\n")
