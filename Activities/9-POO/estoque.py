class Estoque:
    
    def __init__(self):
        self.produtos = list()
        self.codigos = list()
        self.precos = list()
        self.quantidade = list()

    def alterar(self, opcao, produto):
        index = self.produtos.index(produto)
        
        if produto in self.produtos:
            if opcao == "nome":
                self.produtos[index] = input("\033[0;32mNovo nome do produto: \033[m")
            elif opcao == "código":
                self.codigos[index] = int(input("\033[0;32mNovo código: \033[m"))
            elif opcao == "preço":
                self.precos[index] = float(input("\033[0;32mNovo preço: \033[m"))
            elif opcao == "quantidade":
                self.quantidade[index] = int(input("\033[0;32mNova quantidade: \033[m"))
        else:
            print(f'\033[0;31m[O produto "{produto}" não está no estoque]\033[m')

    def retirar(self, produto):
        index = self.produtos.index(produto)
        
        if produto in self.produtos:
            self.produtos.pop(index)
            self.codigos.pop(index)
            self.precos.pop(index)
            self.quantidade.pop(index)

            print(f'[O produto \033[0;32m"{produto}"\033[m foi removido do estoque]')
        else:
            print(f'\033[0;31m[O produto "{produto}" não está no estoque]\033[m')

    def verificar(self, produto):
        if produto in self.produtos:
            print(f'\033[0;33m[O produto "{produto}" está no estoque]\033[m')
        else:
            print(f'\033[0;31m[O produto "{produto}" não está no estoque]\033[m')

    def relatorio(self):
        print("\n\033[1;33mRelatório de estoque:\033[m\n")
        for i in range(len(self.produtos)):
            if len(str(self.codigos[i])) < 5:
                msgCodigo = f"{self.codigos[i]:0>5}"
            else:
                msgCodigo = f"{str(self.codigos[i])[:5]}"

            print(f"Produto: \033[1;33m{self.produtos[i].title()}\033[m")
            print(f"Código: \033[1;33m{msgCodigo}\033[m")
            print(f"Preço: \033[1;33mR${self.precos[i]:.2f}\033[m")
            print(f"Quant.: \033[1;33m{self.quantidade[i]}\033[m")

estoque = Estoque()
