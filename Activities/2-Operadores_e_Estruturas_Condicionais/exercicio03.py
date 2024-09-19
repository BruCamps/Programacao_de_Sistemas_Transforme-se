# Exercício: Condicional Encadeada
# Objetivo: Classificar uma nota em categorias de desempenho.

# Descrição: Escreva um programa que peça a nota de um aluno 
# (entre 0 e 100) e classifique a nota como "Excelente", "Bom", 
# "Regular" ou "Insuficiente". Use as seguintes faixas:
# • "Excelente" para notas 90 ou mais
# • "Bom" para notas entre 70 e 89
# • "Regular" para notas entre 50 e 69
# • "Insuficiente" para notas abaixo de 50

# Variável da Mensagem Inicial
introducao = f"\n{"-"*14} SISTEMA DE INCENTIVO {"-"*14}\n\nEscreva uma nota sobre o seu desempenho no curso\nInforme a sua nota (0-100): "

# Variável da Nota
nota = float(input(introducao))

if nota >= 90:                                                                                                          # Condição para nota maior ou igual a 90
    print("\n[Parabéns!]\nSua dedicação é excelente; continue brilhando e\ndando o melhor de si! :D\n")
elif nota >= 70:                                                                                                        # Condição para nota maior ou igual a 70
    print("\n[Ótimo trabalho!]\nUm desempenho bom mostra que seu esforço está\nvalendo a pena! OwO\n")
elif nota >= 50:                                                                                                        # Condição para nota maior ou igual a 50
    print("\n[Muito bem!]\nVocê está no caminho certo! Continue assim! :)\n")
else:                             
    print("\n[Não desanime!]\nO importante é persistir e buscar melhorar.\nVocê é capaz de muito mais! ÒwÓ\n")          # Mensagem para nota abaixo de 50

