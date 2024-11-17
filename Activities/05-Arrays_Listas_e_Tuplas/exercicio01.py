"""
Exercicio: Crie um algoritmo que possua uma lista vazia, na qual você irá adicionar 5 
números inteiros a está lista. 

Ao final deve mostrar a soma desses números.

"""
 
lista = []
 
for i in range(5):
    int_num = int(input(f"Digite o {i+1}º número: "))
    lista.append(int_num)
   
soma = ' + '.join(map(str, lista))
resultado = sum(lista)
 
print(f"\nSoma:\n{soma} = {resultado}\n")
