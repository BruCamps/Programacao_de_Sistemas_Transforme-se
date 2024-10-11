"""
Exercício: Crie um programa que exiba a tabuada de um número fornecido pelo
usuário.
Instruções:
1.Peça ao usuário para inserir um número.
2.Use um loop for com range para gerar a tabuada de 1 a 10.
3.Exiba a tabuada.
"""
 
numero = int(input("Insira um número: "))
 
print(f"Tabuada do {numero}")
 
for i in range(1, 11):
    resultado = i * numero
    print(f"{i} x {numero} = {resultado}")