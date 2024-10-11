"""
Exercício: Crie uma função que recebe um número e verifica se ele é par ou ímpar, 
utilizando o operador de módulo %.
Instruções:
1.Defina uma função chamada verifica_paridade que 
aceita um número como parâmetro.
2.A função deve retornar uma string informando se o 
número é "par" ou "ímpar".
3.No programa principal, peça ao usuário para inserir 
um número e exiba o resultado da verificação.
"""

def verifica_paridade(num):
    if num % 2 == 0:
        return "par"
    else:
        return "ímpar"

num = int(input("Insira um número: "))
print(f'\nO número {num} é {verifica_paridade(num)}')