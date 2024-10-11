"""
Crie uma função que recebe um e-mail como parâmetro, 
verifica se ele contém o símbolo @ e informa se o e-mail foi enviado. 
Instruções:
1. Defina uma função chamada verifica_email que aceita um e-mail como parâmetro.
1. A função deve verificar se o e-mail contém o símbolo @.
1. Se o e-mail for válido, exiba uma mensagem dizendo que o e-mail foi enviado. Caso contrário, informe que o e-mail é inválido.
"""

def verifica_email(email):
    if "@" in email:
        print("[O e-mail foi enviado]")
    else:
        print("[O e-mail é inválido]")

email = input("Insira o seu e-mail: ")
verifica_email(email)