"""
Exercício: Crie um programa que peça ao usuário para inserir uma frase e faça as
seguintes operações:
Converta toda a frase para letras minúsculas e converta toda a frase
para letras maiúsculas.
Instruções:
1.Peça ao usuário para inserir uma frase.
2.Utilize os métodos lower() e upper().
3.Exiba os resultados.
"""
 
frase = input("Escreva uma frase: ")
 
fraseMaiusculas = frase.upper()
fraseMinusculas = frase.lower()
 
print(f"\nFrase em maiúsculo: {fraseMaiusculas}\nFrase em minúsculo: {fraseMinusculas}\n")
