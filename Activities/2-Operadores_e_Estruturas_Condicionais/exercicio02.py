# Exercício: Condicional Composta
# Objetivo: Verificar se um número é positivo ou negativo.

# Descrição: Escreva um programa que peça um número ao usuário e imprima "Número positivo" se o número 
# for maior que zero. Caso contrário, imprima "Número negativo"

# Variável do Número
num = float(input("\nDigite qualquer número: "))

if num > 0:                                    # Condição para o número ser positivo (verifica se o número é maior que 0)
    print(f"\nO número {num} é positivo\n") 
elif num < 0:                                  # Condição para o número ser negativo (verifica se o número é menor que 0)
    print(f"\nO número {num} é negativo\n")
else:                                           
    print(f"\nO número {num} é neutro\n")      # Resulado para o caso do número ser neutro (opcional)
