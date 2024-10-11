"""
Exercício: Crie um programa que peça ao usuário para inserir uma palavra e, em
seguida, conte e exiba quantas letras essa palavra possui.
1. Peça ao usuário para inserir uma palavra.
2. Calcule o número de letras na palavra.
3. Exiba o resultado.
Obs.: Use a função len()
"""
 
palavra = input("Informe uma palavra: ").strip()
totalLetras = len(palavra.replace(' ', ''))
 
print(f'"{palavra}" possui {totalLetras} letras')