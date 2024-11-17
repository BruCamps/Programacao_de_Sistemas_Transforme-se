"""
Exercício: Conversão de Tipos

Descrição: Desenvolva uma função que receba uma lista de strings e 
converta cada elemento para inteiro. Utilize try/except para lidar com 
elementos que não podem ser convertidos, exibindo uma mensagem de erro 
para esses casos e ignorando-os.
"""

valoresInteiros = list()
valoresStrings = list()

print("\n[O valor pode ser um número ou uma palavra]\n")

for i in range(5):
    valor = input(f'Digite o {i+1}º valor: ')
    
    try:
        int(valor)
        valoresInteiros.append(valor)    
    except ValueError:
        valoresStrings.append(valor)
 
    if i == 4:
        print(f"\n\033[1m{' Convertendo para inteiro ':-^40}\033[m\n")
        if valoresInteiros:
            print(f"\033[0;32mConversões bem-sucedidas:\033[m {", ".join(valoresInteiros[:-1])} e {valoresInteiros[-1]}\n")
        if valoresStrings:
            print(f"\033[0;31m[ERRO: Não foi possível converter:\033[m {", ".join(valoresStrings[:-1])} e {valoresStrings[-1]}\033[0;31m]\033[m\n")
