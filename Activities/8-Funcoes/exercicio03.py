"""
Exercício: Crie um programa em python que recebe do teclado uma palavra, e 2
caracteres (um que exista na palavra e outro que vai substituir ele), e através
de uma função chamada substituir_caracteres irá receber a string e os dois
caracteres, substituindo todas as ocorrências do primeiro caractere pelo
segundo.
"""
 
palavra = input("Digite uma palavra: ")
caractere1 = input("Digite uma letra: ")
caractere2 = input("Digite outra letra: ")
 
def substituir_caracteres(string, c1, c2):
    print(f'\nPalavra original: {string}\nPalabra modificada: {string.replace(c1, c2)}\n')
 
substituir_caracteres(palavra, caractere1, caractere2)
