"""
Exercício: Crie um programa em python simulando um controle de estoque. O
programa deve ter a possibilidade de armazenar seus produtos, códigos,
preços e quantidades. 
Crie um menu, que dê também a possibilidade de
alterar o preço de um produto, retirar item do estoque, verificar se
produto existe no estoque e mostrar relatório (lista de todos os produtos,
seus respectivos códigos, preços e quantidade no estoque)
"""

from estoque import estoque

menu = f"\n\033[1;34mControle de estoque\033[m\n[1] Cadastrar produto\t[4] Verificar estoque\n[2] Alterar produto\t[5] Exibir Estoque/Sair\n[3] Excluir produto\n"

try:
    while True:
        opcaoMenu = int(input(f"{menu}\n\033[0;34mEscolha uma opção:\033[m "))

        if opcaoMenu == 1:
            produto = input("\n\033[0;34mNome do produto:\033[m ").strip()
            codigo = int(input("\033[0;34mCódigo:\033[m "))
            preco = float(input("\033[0;34mPreço:\033[m "))
            quantidade = int(input("\033[0;34mQuantidade:\033[m "))

            estoque.produtos.append(produto)
            estoque.codigos.append(codigo)
            estoque.precos.append(preco)
            estoque.quantidade.append(quantidade)

        elif opcaoMenu == 2:
            buscaNome = input("\033[0;34mNome do buscaNome:\033[m ").strip()
            opcao = int(input(f"\n\033[0;34mO que deseja alterar?\033[m\n[1] Alterar nome\t[3] Alterar código\n[2] Alterar preço\t [4] Alterar quantidade\n\n\033[0;34mEscolha uma opção:\033[m "))
            
            if opcao == 1:
                estoque.alterar("nome", buscaNome)
            elif opcao == 2:
                estoque.alterar("preço", buscaNome)
            elif opcao == 3:
                estoque.alterar("código", buscaNome)
            elif opcao == 4:
                estoque.alterar("quantidade", buscaNome)

        elif opcaoMenu == 3:
            produto = input("\033[0;34mNome do produto:\033[m ").strip()
            estoque.retirar(produto)

        elif opcaoMenu == 4:
            produto = input("\033[0;34mNome do produto:\033[m ").strip()
            estoque.verificar(produto)

        elif opcaoMenu == 5:
            estoque.relatorio()
            break
except ValueError:
    print("\n\033[1;31m[ERRO: O valor informado não é um número! Tente novamente]\033[m\n")
