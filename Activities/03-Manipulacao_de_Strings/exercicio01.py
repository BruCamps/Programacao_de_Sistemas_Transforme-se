# Crie um programa que diga ao usuário se o número é: 
# PAR ou ÍMPAR

# Variável do Número
num = int(input("\nDigite um número: "))

if num % 2 == 0:                                 # Verifica se o resto da divisão do número por 2 é 0
    print(f"O número {num} é Par!\n")
else:
    print(f"O número {num} é Ímpar!\n")          # Resultado para caso a condição do if não for satisfeita
