""" Questão 2: Números Pares
----------------------
Faça um programa que peça ao usuário para digitar números inteiros. 
O programa deve parar quando o usuário digitar 0. Ao final, exiba 
quantos números pares foram digitados e exiba os números pares.
"""

# Objetivo: Pedir ao usuário para digitar números inteiros até que ele digite 0.
# Depois, mostrar quantos números pares foram digitados e quais são esses números.

# Como funciona:
# 1. O programa cria uma lista chamada `numeros_pares` para armazenar os números pares.
# 2. Ele pede ao usuário para digitar números.
# 3. Se o número for 0, o programa para.
# 4. Se o número for par, ele é adicionado à lista.
# 5. No final, o programa mostra a quantidade de números pares, os números pares digitados e o total de números digitados.

numeros_pares = []
contador = 0

while True:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    if numero == 0:
        break
    if numero % 2 == 0:
        numeros_pares.append(numero)
    contador += 1

print("Quantidade de números pares digitados:", len(numeros_pares))
print("Números pares digitados:", numeros_pares)
print("Total de números digitados:", contador)