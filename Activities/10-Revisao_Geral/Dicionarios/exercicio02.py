"""
Exercício: Crie um programa que permita cadastrar vários alunos com suas notas e, 
ao final, calcule a média das notas.
Instruções:
1.Use um dicionário para armazenar os nomes dos alunos como 
chaves e as notas como valores.
2.Permita que o usuário cadastre alunos até que ele digite "sair".
3.Calcule e exiba a média das notas ao final. 
"""

alunos = {}
 
while True:
    nome = input("Informe o nome do aluno: ")
 
    if nome == "sair":
        break
 
    nota = float(input("Informe a nota do aluno: "))
 
    alunos[nome] = nota
 
if alunos:
    media = sum(alunos.values()) / len(alunos)
    print(f"\nMédia: {media:.2f}")
else:
    print("\n[Nenhum aluno foi inserido]\n")
