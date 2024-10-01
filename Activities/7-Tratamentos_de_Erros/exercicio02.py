"""
Exercício: Operações com Dicionários

Descrição: Desenvolva um programa que contenha um dicionário com 
nomes de alunos como chaves e suas respectivas notas como valores. Peça 
ao usuário para digitar o nome de um aluno e exiba a nota correspondente. 
Utilize try/except para capturar KeyError caso o nome inserido não exista no 
dicionário.
"""

titulo = f"\033[1m Pesquisa | Notas de Estudantes \033[m"
msgErro = "\n[ERRO: Este nome não está em nosso Banco de Dados]\n"
relacaoNotas = {
    'Ana': { 
      'N1': 9.5, 'N2': 9.0, 'N3': 10.0 
    },
    'Pedro': { 
      'N1': 5.0, 'N2': 6.5, 'N3': 7.0 
    },
    'João': { 
      'N1': 10.0, 'N2': 9.0, 'N3': 8.0 
    },
    'Alice': { 
      'N1': 7.0, 'N2': 8.0, 'N3': 7.5 
    }
}

try:
    nome = input(f"{titulo:-^60}\nDigite o nome: ").strip().title()
    notasAluno = relacaoNotas[nome]
    media = sum(notasAluno.values()) / len(notasAluno)

    print(f'\n\033[1mEstudante\tNota 1\tNota 2\tNota 3\tMédia\033[m')
    print(f'{nome}\t\t{notasAluno["N1"]}\t{notasAluno["N2"]}\t{notasAluno["N3"]}\t{media:.1f}\n')
except KeyError:
    print(f"\n\033[0;31m{msgErro}\033[m\n")

