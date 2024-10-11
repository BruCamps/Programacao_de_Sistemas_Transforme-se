"""
Exercício: Crie um programa que peça ao usuário para inserir uma frase e uma
palavra. O programa deve substituir todas as ocorrências da palavra na
frase por outra palavra de sua escolha.
Instruções:
1.Peça ao usuário para inserir uma frase.
2.Peça ao usuário para inserir a palavra a ser substituída.
3.Peça ao usuário para inserir a nova palavra.
4.Use o método replace() para realizar a substituição.
5.Exiba a frase modificada.
"""
 
frase = input("Insira uma frase: ")
palavra = input("Insira a palavra a ser substituída: ")
novaPalavra = input("Insira a nova palavra: ")
 
fraseModificada = frase.replace(palavra, novaPalavra)
 
print(fraseModificada)