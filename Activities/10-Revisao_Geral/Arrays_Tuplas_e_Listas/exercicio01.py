"""
Exercício: Crie um programa que permita ao usuário adicionar números a uma lista
e, em seguida, exiba todos os números inseridos.
Instruções:
1.Crie uma lista vazia.
2.Use um loop para permitir que o usuário adicione números até que ele digite "sair".
3.Exiba todos os números que foram inseridos.
"""
 
lista = []
 
while True:
    num = input("Digite um número: ")
 
    if num == "sair":
        break
 
    lista.append(num)
 
print(f'Números inseridos: {", ".join(lista)}')