palavra = input("Digite uma palavra: ").lower()
palavraAoContrario = palavra[::-1]

if(palavra == palavraAoContrario):
    print(f"\n'{palavra}' é um palíndromo pois é o mesmo que a sua forma reversa '{palavraAoContrario}'\n")
else:
    print(f"\n'{palavra}' não é um palíndromo pois não é o mesmo que a sua forma reversa '{palavraAoContrario}\n'")
