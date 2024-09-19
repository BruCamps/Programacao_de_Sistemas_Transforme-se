# Exercício: Condicional Simples
# Objetivo: Verificar se uma pessoa pode entrar em uma sessão de cinema com base na idade.

# Descrição: Escreva um programa que peça a idade do usuário e imprima "Você pode assistir ao filme" se 
# a idade for 12 anos ou mais. Caso contrário, imprima "Você não pode assistir ao filme".


# Variável da Mensagem Inicial
introducao = f'\n{"-"*14} CINECAT - Spider-Man No Way Home {"-"*14}\n\nAntes de prosseguir, por favor, informe sua idade: '

# Variável da Idade
idade = int(input(introducao))

# Condicionais do tipo Simples
if idade >= 12: # Condição para assistir ao filme (verifica se é maior ou igual a 12)
    print("\n[ Que massa! Você pode assistir ao filme. Aproveite! :) ]")

if idade < 12: # Condição para não assistir ao filme (verifica se é menor que 12)
    print("\n[ Você não tem idade suficiente para assistir ao filme. :'( ]\n[ Confira outros filmes em nosso site! :D ]")

# Funções de Mensagens Finais
print("\n[CINECAT: O melhor do cinema, sempre com você!]\n")
print("    /\\_/\\ \n", "  (-'^'-) \n", "\\ /  ^^ \\ \n") # ASCII art de um gatinho
