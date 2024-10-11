"""
Exercício: Crie um programa que continue pedindo ao usuário para inserir um
número até que ele digite "0". Quando "0" for digitado, o programa deve
exibir a soma de todos os números inseridos.
Instruções:
1.Use um loop while True para continuar recebendo números.
2.Se o usuário digitar "0", saia do loop.
3.Exiba a soma total dos números.
"""
 
soma = 0
 
while True:
    num = int(input("Insira um número: "))
    soma += num
 
    if num == 0:
        break
 
print(f"Soma: {soma}")