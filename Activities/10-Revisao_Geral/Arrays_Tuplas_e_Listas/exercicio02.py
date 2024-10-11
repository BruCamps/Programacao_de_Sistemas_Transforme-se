"""
Exercício: Crie um programa que permita ao usuário inserir números em uma lista
e, em seguida, calcule e exiba a média dos números.
Instruções:
1. Crie uma lista vazia.
2. Use um loop para permitir que o usuário adicione números até
que ele digite "sair".
3. Calcule a média dos números inseridos e exiba o resultado.
"""
 
lista = []
 
while True:
    num = input("Digite um número: ")
 
    if num == "sair":
        break
 
    lista.append(float(num))
   
media = sum(lista) / len(lista)
 
print(f"Média: {media:.2f}")