# Crie um programa que o usuário calcule o valor a ser pago na loja 
# de acordo com as condições de pagamento:

# • À vista (dinheiro/pix): 10% de desconto
# • À vista (cartão): 5% de desconto
# • 2x no cartão: 5% de acréscimo
# • 3x até 10x no cartão: 10% de acréscimo

# Variáveis do Início
hifens = "\033[1;31m-\033[m"*14
divisoria = f'{hifens} Loja \033[1;34mC&A\033[m {hifens}'

# Variável do Valor das Compras
valor = float(input(f"{divisoria}\nValor das compras: R$ "))

# Variáveis de Mensagem
titulo = '\033[1;34mFORMAS DE PAGAMENTO\033[m'
opcsPagamento = '''
[\033[1;31m 1 \033[m] à vista em dinheiro/pix \033[1;32m(10% de desconto)\033[m
[\033[1;31m 2 \033[m] à vista no cartão \033[1;32m(5% de desconto)\033[m
[\033[1;31m 3 \033[m] 2x no cartão \033[1;33m(5% de acréscimo)\033[m
[\033[1;31m 4 \033[m] 3x até 10x no cartão \033[1;33m(10% de acréscimo)\033[m
'''
pergunta = '\n\033[1;37mQual será a forma de pagamento?\033[m '

# Variável da Opção de Pagamento (1, 2, 3 ou 4)
opcao = int(input(f"\n{titulo}{opcsPagamento}{pergunta}"))
 
if opcao == 1:                                                                 # Verifica se a Opção de Pagamento é 1 e calcula o valor com 10% de desconto
    print(f"O total da compra será de \033[1;32mR${valor*0.9:.2f}\033[m\n") 
elif opcao == 2:                                                               # Verifica se a Opção de Pagamento é 2 e calcula o valor com 5% de desconto
    print(f"O total da compra será de \033[1;32mR${valor*0.95:.2f}\033[m\n") 
elif opcao == 3:                                                               # Verifica se a Opção de Pagamento é 3 e calcula o valor com 5% de acréscimo
    print(f"O total da compra será de \033[1;33mR${valor*1.05:.2f}\033[m\n")
elif opcao == 4:                                                               # Verifica se a Opção de Pagamento é 4 e calcula o valor com 10% de acréscimo
    print(f"O total da compra será de \033[1;33mR${valor*1.1:.2f}\033[m\n")
else:
    print("\033[1;31m[Opção inválida! Tente novamente.]\033[m\n")              # Resultado para Opção inválida
