"""
Exercício: Crie um programa que peça ao usuário para inserir dois números e realize a 
divisão do primeiro pelo segundo. 
Utilize try-except para tratar possíveis erros, como divisão por zero e entrada 
inválida.
Instruções:
1.Peça ao usuário para inserir o primeiro número.
2.Peça ao usuário para inserir o segundo número.
3.Realize a divisão e trate as exceções.
4.Exiba o resultado ou uma mensagem de erro.
"""

try:
    num1 = int(input("Insira o primeiro número: "))
    num2 = int(input("Insira o segundo número: "))
    divisao = num1 / num2
    print(f'\n{num1} / {num2} = {divisao}')

except ZeroDivisionError:
    print("[Erro: Não é possível realizar uma divisão por zero]\n")

except ValueError:
    print("[Erro: Entrada inválida! O valor digitado não é um número inteiro]\n")