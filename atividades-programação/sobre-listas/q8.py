""" Questionário: 8 - Listas
----------------------
Escreva um programa que peça ao usuário para digitar números 
inteiros até que ele digite -1. Ao final, exiba o maior número digitado.
"""

# Objetivo: Pedir ao usuário para digitar números inteiros até que ele digite -1.
# Depois, mostrar o maior número digitado.

# Como funciona:
# 1. O programa cria uma variável `maior_numero` para armazenar o maior número.
# 2. Ele pede ao usuário para digitar números.
# 3. Se o número for -1, o programa para.
# 4. Caso contrário, o programa verifica se o número é maior que `maior_numero` e, se for, atualiza o valor de `maior_numero`.
# 5. No final, o programa mostra o maior número digitado ou uma mensagem dizendo que nenhum número válido foi digitado.

maior_numero = 0

while True:
    numero = int(input("Digite um número inteiro (-1 para sair): "))
    if numero == -1:
        break
    if numero > maior_numero:
        maior_numero = numero
if maior_numero != 0:
    print("O maior número digitado foi:", maior_numero)
else:
    print("Nenhum número válido foi digitado.")