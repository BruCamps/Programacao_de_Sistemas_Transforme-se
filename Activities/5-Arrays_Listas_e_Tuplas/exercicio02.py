"""
Exercício: Crie um algoritmo que possua uma lista vazia, na qual você irá nomes de animais 
a está lista. 

Ao final deve mostrar os itens em ordem inversa 
(do ultimo adicionado até o primeiro adicionado).

"""
 
lista = []
 
for i in range(5):
    animal_nome = input(f"Digite o nome do {i+1}º animal: ")
    lista.append(animal_nome)

print(f'\nLista de Animais: {', '.join(reversed(lista)).capitalize()}\n')
