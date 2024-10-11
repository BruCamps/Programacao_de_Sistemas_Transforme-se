"""
Exercício: Crie uma função que recebe dois números como parâmetros e retorna a soma 
deles.
Instruções:
1. Defina uma função chamada soma que aceita dois parâmetros.
2. A função deve retornar a soma dos dois números.
3. No programa principal, peça ao usuário para inserir dois números 
e exiba o resultado da soma.
"""

def soma(n1, n2):
    return n1 + n2

num1 = int(input("Insira o 1 número: "))
num2 = int(input("Insira o 2 número: "))
 
print(f'\n{num1} + {num2} = {soma(num1, num2)}\n')