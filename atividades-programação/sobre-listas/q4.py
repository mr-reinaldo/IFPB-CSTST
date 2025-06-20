""" Questionário: 4 - Listas
----------------------
Escreva um programa que peça ao usuário para digitar 
palavras até que ele digite 'fim'. O programa deve 
contar quantas e exibir palavras começam com a letra A ou a.
"""

# Objetivo: Pedir ao usuário para digitar palavras até que ele digite "fim".
# Depois, contar e mostrar as palavras que começam com a letra "A" ou "a".

# Como funciona:
# 1. O programa cria duas listas: `palavras` para armazenar todas as palavras e `palavras_com_a` para armazenar as palavras que começam com "A" ou "a".
# 2. Ele pede ao usuário para digitar palavras.
# 3. Se a palavra for "fim", o programa para.
# 4. Caso contrário, a palavra é adicionada à lista `palavras`.
# 5. O programa verifica quais palavras começam com "A" ou "a" e as adiciona à lista `palavras_com_a`.
# 6. No final, ele mostra a quantidade e as palavras que começam com "A" ou "a".

palavras = []
palavras_com_a = []

while True:
    palavra = input("Digite uma palavra (ou 'fim' para sair): ")
    if palavra == 'fim':
        break
    palavras.append(palavra)

for palavra in palavras:
    if palavra[0] == 'A' or palavra[0] == 'a':
        palavras_com_a.append(palavra)

print("Quantidade de palavras que começam com 'A' ou 'a':", len(palavras_com_a))
print("Palavras que começam com 'A' ou 'a':", palavras_com_a)