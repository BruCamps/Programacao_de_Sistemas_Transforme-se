# Exercício: Que leia do teclado o NOME e IDADE de 5 pessoas, calcule e no final imprima (mostre no console):
# a) A soma de idade das pessoas.
# b) A média das idades lidas.

nome = []
idade = []
maisvelha = ''
maisnova = ''
soma = 0
media = 0
maior = 0
menor = 100

for i in range(0, 5):
    nome.append(str(input("Nome: ")))
    idade.append(int(input("Idade: ")))
    soma += idade[i]

    if idade[i] > maior:
        maior = idade[i]
        maisvelha = nome[i]
    if idade[i] < menor:
        menor = idade[i]
        maisnova = nome[i]

media = soma / len(idade) 

print(f'''
Soma das idades: {soma}
Média das idades: {media:.1f}
A pessoa mais velha é {maisvelha} com {maior} {maior == 1 and 'ano' or 'anos'}
A pessoa mais nova é {maisnova} com {menor} {menor == 1 and 'ano' or 'anos'}
'''
)
 
