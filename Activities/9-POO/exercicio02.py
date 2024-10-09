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

menu = f"\n\033[1;32mControle de estoque\033[m\n[1] Cadastrar produto\t[4] Verificar estoque\n[2] Alterar produto\t[5] Exibir Estoque/Sair\n[3] Excluir produto\n"

try:
    while True:
        opcao = int(input(f"{menu}\n\033[0;32mEscolha uma opção:\033[m "))

        if opcao == 1:
            produto = input("\n\033[0;32mNome do produto:\033[m ").strip().title()
            codigo = int(input("\033[0;32mCódigo:\033[m "))
            preco = float(input("\033[0;32mPreço:\033[m "))
            quantidade = int(input("\033[0;32mQuantidade:\033[m "))

            estoque.produtos.append(produto)
            estoque.codigos.append(codigo)
            estoque.precos.append(preco)
            estoque.quantidade.append(quantidade)

        elif opcao == 2:
            produto = input("\033[0;32mNome do produto:\033[m").strip().title()
            estoque.alterar(produto)
        elif opcao == 3:
            produto = input("\033[0;32mNome do produto:\033[m").strip().title()
            estoque.retirar(produto)
        elif opcao == 4:
            produto = input("\033[0;32mNome do produto:\033[m").strip().title()
            estoque.verificar(produto)
        elif opcao == 5:
            estoque.relatorio()
            break
except ValueError:
    print("\n\033[1;31m[ERRO: O valor informado não é um número! Tente novamente]\033[m\n")
