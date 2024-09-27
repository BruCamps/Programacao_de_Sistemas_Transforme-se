"""
Exercício: Crie um algoritmo que possua 3 listas. 

A primeira você irá armazenar 10 números. 
A segunda, apenas os números pares dos 10 números lidos.
A terceira, apenas os números ímpares. 
Depois imprima os números pares e os números ímpares.

"""
 
lista = []
lista2 = []
lista3 = []
 
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))

    lista.append(num)
 
    if lista[i] % 2 == 0:
        lista2.append(num)
    else:
        lista3.append(num)
 
print(f"\nNúmeros pares: {lista2}\nNúmeros ímpares: {lista3}\n")
