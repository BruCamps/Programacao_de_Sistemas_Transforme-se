# Anotações (Notes):

# Comandos de Entrada e Saída
# input() -> Comando de Entrada que recebe o valor digitado pelo usuário
# print() -> Comando de Saída que exibe algo na tela

# NOTE: TUDO o que é digitado em um input() é uma STRING

# Tipos de Dados
# Str (String) -> Texto                                 (Ex.: 'Casa', "Ab", '2', "Menino")
# Int (Integer) -> Número inteiro                       (Ex.: 2, -3, 100, -500)
# Float -> Número real                                  (Ex.: 2.5, 3.444, 1.0, 80.7)
# Bool (Boolean) -> True (Verdadeiro) ou False (Falso)  (Ex.: True, False)

# Recursos de Formatação
# format() -> Método que pode ter uma variável como argumento e mostra seu valor a partir de {}
# vazias, com índices ou com parâmetros
# f-string -> Recurso que formata um texto e colocando as variáveis entre {}, recebe seus valores

# Comentário e DocString
# Comentário (usamos #) -> Linha de texto que é ignorada pelo interpretador usada para explicar o código
# DocString (usamos ''' ''' ou """ """) -> Não é um comentário, pois é lido pelo interpretador (só não é executado), mas podemos utilizar para fazer anotações
# Ex.:

'''
  Este é um exemplo de DocString com aspas simples :)
'''

"""
  Este é outro exemplo de DocString, mas com aspas duplas :)
"""

# Função de retorno do Tipo de Dado
# type() -> Função que retorna o tipo de dado de uma variável ou valor

# NOTE: Concatenação -> Juntar duas ou mais strings adicionando um + entre elas

# Funções de Coerção de Tipos
# str() -> Função que converte o tipo de um valor para STRING
# int() -> Função que converte o tipo de um valor para INT
# float() -> Função que converte o tipo de um valor para FLOAT
# bool() -> Função que converte o tipo de um valor para BOOL

# Conversão Implícita: Interpretador converte automaticamente
# Ex.:
num = 12
num = 15.4

# Conversão Explícita: Devs convertem manualmente
# Ex.:
valor = '145'      # -> <class 'str'>
print(int(valor))  # -> <class 'int'>
# Saída: 145       
