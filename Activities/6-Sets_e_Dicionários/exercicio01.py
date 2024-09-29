# Exercício: Faça um dicionário com as 5 pessoas mais perto de você, 
# tendo o nome como chave e a cor da camisa que está usando como valor.
 
pessoas = {
    "Ruth": "Lilás",
    "Pedro": "Azul",
    "Juan": "Preta",
    "Vitor": "Branca",
    "Milly": "Verde"
}

print(f"\n\033[1mNome\033[m\t|  \033[1mCamisa\033[m\n{'—'*20}")

for pessoa in pessoas:
    print(f'{pessoa}\t|  {pessoas[pessoa]}\n{'—'*20}')
print(end="\n")
