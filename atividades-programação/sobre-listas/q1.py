""" Questionário 1 - Listas
----------------------
Faça um programa que peça ao usuário para digitar preços 
de produtos até que ele digite um valor negativo. Ao final, 
exiba o total da compra e todos os preços digitados.
"""

# Objetivo: Pedir ao usuário para digitar preços de produtos até que ele digite um valor negativo.
# Depois, mostrar o total da compra e todos os preços digitados.

# Como funciona:
# 1. O programa cria uma lista chamada `precos` para armazenar os preços.
# 2. Ele pede ao usuário para digitar o preço de um produto.
# 3. Se o preço for negativo, o programa para de pedir preços.
# 4. Caso contrário, o preço é adicionado à lista.
# 5. No final, o programa soma todos os preços e exibe o total e a lista de preços digitados.

precos = []

while True:
    preco = float(input("Digite o preço do produto (ou um valor negativo para sair): "))
    if preco < 0:
        break
    precos.append(preco)
    
total = sum(precos)
print("Total da compra:", total)
print("Preços digitados:", precos)