numeros = []
media = 0

for i in range(0, 5):
    num = int(input(f"Escreva o {i+1}º número: "))
    numeros.append(num)

media = sum(numeros) / 5
soma = ' + '.join(map(str, numeros))

print(f"\nMédia Arimética:\n{soma} / 5 = {media:.1f}\n")

