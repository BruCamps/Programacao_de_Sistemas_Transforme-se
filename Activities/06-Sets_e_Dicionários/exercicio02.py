# Exercício: Crie um dicionário vazio filmes = {}. Utilize o nome de um filme como chave. 
# E, como valor, outro dicionário contendo o vilão e o ano em que o filme foi lançado. 
# Preencha o dicionário com 5 filmes.

filmes =  dict()
infos = dict()
tituloInvalido = '\033[1;31m[Insira um título válido!]\033[m'                                   # (opcional)
anoInvalido = '\033[1;31m[Ano inválido! Válido somente a partir de 1880]\033[m'                 # (opcional)
numeroInvalido = '\033[1;31m[Valor válido! Insira números]\033[m'                               # (opcional)
nomeInvalido = '\033[1;31m[Valor válido! Insira um nome]\033[m'                                 # (opcional)
cont = 0                                                                                        # (opcional)

print('\n\033[1;4;34mCadastro de 5 Filmes\033[m')

for i in range(5):

    titulo = input(f'\n{i+1}º filme: ').title().strip()
    while not titulo or titulo.isnumeric():                                                     # (opcional)
        titulo = input(f'{tituloInvalido}\nNome do {i+1}º filme: ').title().strip()             # (opcional)

    ano = input('Ano: ')
    while not ano or not ano.isnumeric() or int(ano) < 1880:                                    # (opcional)
        if not ano.isnumeric() or not ano:                                                      # (opcional)
            print(numeroInvalido)                                                               # (opcional)
        else:                                                                                   # (opcional)
            print(anoInvalido)                                                                  # (opcional)
        ano = input('Ano: ')                                                                    # (opcional)

    vilao = input('Vilão: ').title().strip()

    while not vilao or vilao.isnumeric():                                                       # (opcional)
        vilao = input(f'{nomeInvalido}\nVilão: ').title().strip()                               # (opcional)

    infos = {'Ano': ano, 'Vilão': vilao}
    filmes[titulo] = infos

for filme in filmes:
    cont += 1 # (opcional)
    print(f'\n\033[1;34m{cont}{'º Filme \033[m':-<30}\033[m\nTítulo: \033[0;34m{filme}\033[m\nAno: \033[0;34m{filmes[filme]["Ano"]}\033[m\nVilão: \033[0;34m{filmes[filme]["Vilão"]}\033[m') 
print(end='\n') # (opcional)
