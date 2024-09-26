# Exercício: Que leia do teclado o NOME e IDADE de 5 pessoas, calcule e no final imprima (mostre no console):
# a) A soma de idade das pessoas.
# b) A média das idades lidas.

# Variáveis de array
arraynome = []
arrayidade = [] # (opcional)

# Variáveis que armazenam o nome da pessoa mais velha e mais nova (opcional)
maisvelha = ''
maisnova = ''

# Variáveis numéricas
i = 0             
soma = 0          
media = 0         
maior = 0         
menor = 100       

# Estrutura de repetição
while i < 5: 

    # Comandos de entrada para nome e idade
    nome = input(f"\n{i+1}ª pessoa \nNome: ")
    idade = int(input(f"Idade: "))

    # Armazenando os valores de nome e idade em seus respectivos arrays
    arrayidade.append(idade)
    arraynome.append(nome) # (opcional)

    # Condicionais para idade maior e menor (opcional)
    if arrayidade[i] > maior:
        maior = arrayidade[i]
        maisvelha = arraynome[i]
    if arrayidade[i] < menor:
        menor = arrayidade[i]
        maisnova = arraynome[i]

    # Adiciona +1 para o contador i
    i += 1

# Variáveis de cálculo
soma = sum(arrayidade)
media = soma / len(arrayidade) 


print(
# Mensagem com a soma e a média das idades
f'''
Soma das idades: {soma}
Média das idades: {media:.1f}
''',
# Mensagem com os nomes das pessoas e suas idades (opcional)
f'''
A pessoa mais velha é {maisvelha} com {maior} {maior == 1 and 'ano' or 'anos'}
A pessoa mais nova é {maisnova} com {menor} {menor == 1 and 'ano' or 'anos'}
'''
)
