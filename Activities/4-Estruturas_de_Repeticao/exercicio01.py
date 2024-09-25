# Exercício: Escreva em Python um algoritmo que receba do teclado um número e escreva o seu fatorial.

# Variável do Número
num = int(input("\nDigite um número: "))

# Variáveis do Fatorial
fat = 1
fatores = [] # Lista dos fatores (números que compõe a multiplicação do fatorial)

for i in range(1, num+1):  # Laço de repetição com range (1 -> Começa em 1, num+1 -> Vai até o número informado)
    fat = fat * i
    fatores.append(i)
    join = ' x '.join(map(str, fatores))

print("\n{}! = {} = {}\n".format(num, join[::-1], fat)) # Imprime o cálculo e o resultado

# OBS.: O join[::-1] inverte a ordem da lista de fatores
