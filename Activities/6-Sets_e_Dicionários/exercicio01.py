# Exercício: Faça um dicionário com as 5 pessoas mais perto de você, 
# tendo o nome como chave e a cor da camisa que está usando como valor.
 
pessoas = {
    "Ruth": "Lilás",
    "Pedro": "Azul",
    "Juan": "Preta",
    "Vitor": "Branca",
    "Milly": "Verde"
}

print("\n\033[1mNome\033[m\t|  \033[1mCamisa\033[m", end="\n")

for pessoa in pessoas:
    print(f'{pessoa}\t|  {pessoas[pessoa]}')
print(end="\n")
