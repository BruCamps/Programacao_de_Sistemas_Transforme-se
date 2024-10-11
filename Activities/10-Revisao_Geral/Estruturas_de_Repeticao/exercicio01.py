"""
Exercício: Crie um programa que peça ao usuário para inserir uma palavra e conte
quantas letras "a" existem nessa palavra.
Instruções:
1.Peça ao usuário para inserir uma palavra.
2.Use um loop for para contar as letras "a".
3.Exiba o total de letras "a".
"""
 
palavra = input("Digite uma palavra: ").lower()
contA = 0
 
for letra in palavra:
    if letra in "a":
        contA += 1
 
print(f"Total de letras 'a': {contA}")