frase = input("Escreva uma frase: ")
CountVogais = 0
Vogais = []

for letra in frase:
    if(letra.lower() in 'aãáeéiíoóu'):
        CountVogais += 1
        Vogais.append(letra)

if(CountVogais == 0):
    print(f"\nFrase: {frase}\nQtd_Vogais: {CountVogais}\n")
else:
    print(f"\nFrase: {frase}\nQtd_Vogais: {CountVogais}\nVogais: {', '.join(Vogais)}\n")