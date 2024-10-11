"""
Exercício: Crie um programa que tenha um array de nomes já definida e exiba
todos os nomes na lista.
Instruções:
1. Defina uma lista com pelo menos 5 nomes.
2. Exiba todos os nomes da lista.
3. Use a função enumerate()
"""
 
lista = ["Diego", "Pedro", "Graham", "Eduarda", "Bianca"]
 
for i, item in enumerate(lista, start=1):
    print(f"{i}- {item}")