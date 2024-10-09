class Estoque:
    
    def __init__(self):
        self.produtos = list()
        self.codigos = list()
        self.precos = list()
        self.quantidade = list()

    def alterar(self, produto):        
        index = self.produtos.index(produto)

        if produto in self.produtos:
            self.produtos[index] = input("Novo nome do produto: ")
            print(f'\033[0;33m["{produto}" foi alterado para "{self.produtos[index]}"]\033[m')
        else:
            print(f'\033[0;31m[O produto "{produto}" não está no estoque]\033[m]')

    def retirar(self, produto):
        index = self.produtos.index(produto)

        if produto in self.produtos:
            self.produtos.pop(index)
            self.codigos.pop(index)
            self.precos.pop(index)
            self.quantidade.pop(index)
            print(f'\033[0;33m[O produto "{produto}" foi removido do estoque]\033[m')
        else:
            print(f'\033[0;31m[O produto "{produto}" não está no estoque]\033[m]')

    def verificar(self, produto):
        if produto in self.produtos:
            print(f'\033[0;33m[O produto "{produto}" está no estoque]\033[m')
        else:
            print(f'\033[0;31m[O produto "{produto}" não está no estoque]\033[m]')

    def relatorio(self):
        for i in range(len(self.produtos)):
            print(f"\nProduto: \033[1;32m{self.produtos[i]}\033[m")
            print(f"Código: \033[1;32m{self.codigos[i]:0>5}\033[m")
            print(f"Preço: \033[1;32mR${self.precos[i]:.2f}\033[m")
            print(f"Quant.: \033[1;32m{self.quantidade[i]}\033[m")

estoque = Estoque()
