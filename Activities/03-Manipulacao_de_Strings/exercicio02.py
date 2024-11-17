# Crie um programa que o usuário digite duas notas e apareça uma 
# mensagem informando se ele foi:

# • APROVADO: nota superior a 7.0
# • RECUPERAÇÃO: nota entre 5.0 e 6.9
# • REPROVADO: nota abaixo de 5.0

# Variáveis das Notas
nota1 = float(input("\nDigite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))

# Variável do cálculo da Média
media = (nota1 + nota2) / 2

print(f"\n-------------\nNota 1 | {nota1}\nNota 2 | {nota2}\nMédia  | {media:.1f}\n-------------")
if media >= 7:                                               # Verifica se a média é maior ou igual a 7
    print(f"\nVocê foi \033[1;30;42m APROVADO! \033[m\n")
elif media >= 5:                                             # Verifica se a média é maior ou igual a 5
    print(f"\nVocê está em \033[1;30;43m RECUPERAÇÃO. \033[m\n")
else:
    print(f"\nVocê foi \033[1;30;41m REPROVADO. \033[m\n")   # Resultado para caso a média seja menor que 5
