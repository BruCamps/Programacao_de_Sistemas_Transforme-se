# Comando de Entrada
nome = input("Digite seu nome: ") # Sempre atribua o input a uma variável
print(nome)
# Saída: Beatrice

# Comando de Saída
print("Olá, Mundo!")
# Saída: Olá, Mundo!

# Concatenação de textos
saudacao = 'Olá,' + 'mundo!'
print(saudacao)
# Saída: Olá, mundo!

# Concatenação de números
print('2' + '2')
# Saída: 22

# Conversão da resposta no input para nº inteiro usando int()
idade = int(input('Digite sua idade: '))
print('A sua idade é: ', idade) 
# Saída: A sua idade é: 15

# Formas de exibir na tela a variável nome

# Vírgula: Separa o texto da variável
print('Seu nome é: ', nome) 
# Concatenação: Junta o texto e a variável
print('Seu nome é: ' + nome)
# F-string: Recebe o valor do nome ao colocá-lo entre {}
print(f'Seu nome é: {nome}')
# Format(): Recebe o valor do nome nas {} pois a variável foi passada como argumento no método
print('Seu nome é: {}'.format(nome))

# Retorno do Tipo de Dado

num1 = int(input('Digite um número: '))
print(num1)
# Saída: 10
print(type(num1))
# Saída: <class 'int'>

num2 = float(input('Digite um número: '))
print(num2)
# Saída: 2.5
print(type(num2))
# Saída: <class 'float'>

num3 = bool(input('Digite um número: ')) # Se tiver uma resposta será True, caso não False
print(num3)
# Saída: True
print(type(num3))
# Saída: <class 'bool'>

text = 'Recife é uma boa cidade'
print(text)
# Saída: Recife é uma boa cidade
print(type(text))
# Saída: <class 'str'>
