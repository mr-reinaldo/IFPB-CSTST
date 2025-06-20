""" Questionário: 9 - Listas
----------------------
Escreva um programa que peça ao usuário para digitar números 
inteiros até que ele digite -1. O programa deve exibir duas 
listas: uma com os números pares e outra com os ímpares.

Objetivo: Pedir ao usuário para digitar números inteiros até que ele digite -1.
Depois, mostrar duas listas: uma com os números pares e outra com os ímpares.

Como funciona:
1. O programa cria duas listas: `numeros_pares` para armazenar os números pares e `numeros_impares` para armazenar os ímpares.
2. Ele pede ao usuário para digitar números.
3. Se o número for -1, o programa para.
4. Caso contrário, o programa verifica se o número é par ou ímpar e o adiciona à lista correspondente.
5. No final, o programa mostra as duas listas.
"""

numeros_pares = []
numeros_impares = []

while True:
    numero = int(input("Digite um número inteiro (-1 para sair): "))
    if numero == -1:
        break
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print("Números pares:", numeros_pares)
print("Números ímpares:", numeros_impares)