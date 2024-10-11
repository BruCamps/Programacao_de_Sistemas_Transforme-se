"""
Exercício: Crie um programa que peça ao usuário para inserir a sua idade e
determine se a pessoa é maior de idade (18 anos ou mais) ou menor de
idade.
1. Peça ao usuário para inserir a idade.
2. Use if e else para verificar se a idade é maior ou igual a 18.
3. Exiba uma mensagem informando se a pessoa é maior ou menor de idade.
"""
 
idade = int(input("Insira sua idade: "))
 
if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")