# Exercício: Faça um algoritmo que receba 2 números e mostre o resultado da soma entre ambos

# Variáveis dos Números
num1 = float(input("\nDigite o 1º número: "))
num2 = float(input("Digite o 2º número: "))

# Variável da Soma 
soma = num1 + num2 

# Variável da Mensagem
MsgSoma = f"\n{num1} + {num2} = {soma}"

print(MsgSoma)                                                  # Saída: 2.0 + 5.5 = 7.5
print('A soma entre', num1, 'e', num2, 'é', soma)               # Saída: A soma entre 2.0 e 5.5 é 7.5
print('A soma entre {} e {} é: {}'.format(num1, num2, soma))    # Saída: A soma entre 2.0 e 5.5 é 7.5
print('A soma entre {1} e {0} é: {2}'.format(num1, num2, soma)) # Saída: A soma entre 5.5 e 2.0 é 7.5

# Os números são as posições das variáveis dentro do format. Então é basicamente assim: 
# Variáveis     Posição
# num1          0
# num2          1
# num3          2
