# Exercício: Escreva em Python um algoritmo que receba do teclado um número e escreva o seu fatorial.

# Variável do Número
num = int(input("\nDigite um número: "))

# Variáveis do Fatorial
resultado = 1
fatores = [] # Lista dos fatores (números que compõe a multiplicação do fatorial)

for i in range(num, 0, -1):  # Laço de repetição com range

    # Armazena o resultado da multiplicação com o i
    resultado *= i

    # Adiciona o contador i aos fatores (números da multiplicação)
    fatores.append(i)


# Une os fatores colocando x entre eles
multiplicacao = ' x '.join(map(str, fatores))

# Imprime o cálculo e o resultado
print(f"\n{num}! = {multiplicacao} = {resultado}\n")
