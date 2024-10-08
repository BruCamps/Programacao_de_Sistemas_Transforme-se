"""
Exercício: Crie um programa em python que solicite um número qualquer. Nele, criem
duas funções, uma para calcular o quadrado do número digitado e outra para
imprimir o resultado.
"""
 
def calculo(num):
    return num ** 2
 
def resultado(num):
    print(f'\n{num}² = {num} x {num} = {exp(num)}\n')
 
numero = int(input("Digite um número: "))
resultado(numero)
