"""
Exercício: Crie um programa que permita ao usuário cadastrar um aluno com seu
nome e nota. O nome do aluno deve ser a chave em um dicionário, e a
nota deve ser o valor. Após o cadastro, exiba as informações do aluno.
Instruções:
1. Peça ao usuário para inserir o nome do aluno.
2. Peça ao usuário para inserir a nota do aluno.
3. Armazene essas informações em um dicionário.
4. Exiba as informações do aluno.
"""
 
infos = {}
nome = input("Informe seu nome: ")
nota = float(input("Informe a sua nota: "))
 
infos[nome] = nota
 
for aluno in infos:
    print(f'\nInformações:\nNome: {aluno}\nNota: {infos[aluno]}\n')