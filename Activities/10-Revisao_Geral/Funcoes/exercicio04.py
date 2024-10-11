"""
Crie um programa que simule um sistema de login usando uma função. 
O usuário deve inserir seu nome de usuário e senha, 
e o programa deve verificar se as credenciais estão corretas.
Instruções:
1.Defina um nome de usuário e uma senha predefinidos (por exemplo, "usuario" e 
"senha123").
1.Crie uma função chamada login que recebe o nome de usuário e a senha como 
parâmetros.
1.A função deve verificar se as credenciais estão corretas e retornar uma 
mensagem de sucesso ou falha.
1.No programa principal, solicite ao usuário que insira seu nome de usuário e 
senha e chame a função.
"""


def login(usuario, senha):
    if usuario == "usuario" and senha == "senha123":
        return "Login efetuado com sucesso!"
    elif usuario != "usuario" and senha != "senha123":
        return "Nome de usuário e senha inválidos!"
    elif usuario != "usuario":
        return "Nome de usuário inválido!"
    elif senha != "senha123":
        return "Senha inválida!"

usuario = input("Informe seu nome de usuário: ")
senha = input("Insira sua senha: ")

print(login(usuario, senha))