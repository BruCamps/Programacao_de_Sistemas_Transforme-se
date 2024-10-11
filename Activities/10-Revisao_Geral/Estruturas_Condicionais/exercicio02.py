"""
Exercício: Crie um programa que peça ao usuário para inserir uma nota de 0 a 10 e
classifique a nota como "Aprovado" (7 a 10), "Recuperação" (4 a 6) ou
"Reprovado" (menos de 4).
1. Peça ao usuário para inserir a nota.
2. Use if, elif e else, utilizando and para verificar os intervalos.
3. Exiba a classificação correspondente.
"""
 
nota = float(input("Insira uma nota (0 a 10): "))
 
if nota < 11:
    if nota >= 7:
        print("Aprovado!")
    elif nota >= 4:
        print("Recuperação!")
    else:
        print("Reprovado!")