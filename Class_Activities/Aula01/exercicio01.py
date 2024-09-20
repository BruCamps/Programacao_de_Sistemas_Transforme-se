# Exercício: Faça um algoritmo que siga os seguintes passos ->
# 1- Recebe o valor de nome, idade, altura e cidade
# 2- No final mostre todas as informações dadas pelo usuário

nome = input("\nEscreva seu nome: ")
idade = int(input("Digite a sua idade: "))
altura = float(input("Informe a sua altura (com '.', não ','): "))
cidade = input("De onde você é: ")
mensagem = f"\n[ Dados Pessoais de {nome} ]\n\nIdade: {idade} anos\nAltura: {altura}m\nCidade: {cidade}\n"
print(mensagem)
