"""
Exercício: Conversão de Tipos

Descrição: Desenvolva uma função que receba uma lista de strings e 
converta cada elemento para inteiro. Utilize try/except para lidar com 
elementos que não podem ser convertidos, exibindo uma mensagem de erro 
para esses casos e ignorando-os.
"""

valoresInteiros = list()

print("\n[O valor pode ser um número ou uma palavra]\n")

for i in range(5):
    valor = input(f'Digite o {i+1}º valor: ')
    valoresInteiros.append(valor)
    
print(f"\n\033[1m{' Convertendo para inteiro ':-^40}\033[m\n")

for item in valoresInteiros:
    try:
        int(item)
        print(f"Conversão bem-sucedida: {int(item)}\n")  
    except ValueError:
        print(f"[Erro: Não foi possível converter '{item}']\n")
        
