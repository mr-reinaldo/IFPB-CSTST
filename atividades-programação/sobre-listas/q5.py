""" Questionário: 5 - Listas
----------------------
Escreva um programa que peça ao usuário para digitar números 
até que ele digite -999. Crie uma nova lista substituindo os 
números negativos por zero e exiba essa lista ao final.

Objetivo: Pedir ao usuário para digitar números até que ele digite -999.
Depois, criar uma nova lista onde os números negativos são substituídos por zero.

Como funciona:
1. O programa cria uma lista chamada `numeros` para armazenar os números digitados.
2. Ele pede ao usuário para digitar números.
3. Se o número for -999, o programa para.
4. Caso contrário, o número é adicionado à lista.
5. O programa cria uma nova lista chamada `nova_lista`, onde os números negativos são substituídos por zero.
6. No final, ele mostra a lista original e a nova lista.
"""
numeros = []
while True:
    numero = int(input("Digite um número (-999 para sair): "))
    
    if numero == -999:
        break
    numeros.append(numero)

nova_lista = [max(0, n) for n in numeros]
print("Lista original:", numeros)
print("Nova lista (negativos substituídos por zero):", nova_lista)