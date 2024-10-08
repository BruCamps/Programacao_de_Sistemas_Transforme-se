"""
Exercício: Crie um programa em python que possua 2 funções que receba 5 valores inteiros, determine e imprima:
a. Em uma função, a soma dos números positivos;
b. Em uma segunda função, a quantidade de valores negativos.
"""
 
listaPositivos = []
listaNegativos = []

for i in range(5):
    
    num = int(input(f"Digite o {i+1}° número: "))

    if num > 0:
        listaPositivos.append(num)
    elif num < 0:
        listaNegativos.append(num)
       
def somaPositivos(lista):
    return sum(lista)
 
def quantidadeNegativos(lista):
    return len(lista)

if listaPositivos: 
    print(f'\nNúmeros Positivos:\n{" + ".join(map(str, listaPositivos))} = {somaPositivos(listaPositivos)}\n')
if listaNegativos:
    print(f'\nNúmeros Negativos:\nHá {quantidadeNegativos(listaNegativos)} números negativos\n')
