""" Questionário 7 - Listas
----------------------
Escreva um programa que peça ao usuário para digitar nomes. 
Quando digitar 'fim', o programa deve mostrar todos os nomes 
na ordem inversa em que foram digitados.

Objetivo: Pedir ao usuário para digitar nomes até que ele digite "fim".
Depois, mostrar os nomes na ordem inversa em que foram digitados.

Como funciona:
1. O programa cria uma lista chamada `nomes` para armazenar os nomes.
2. Ele pede ao usuário para digitar nomes.
3. Se o nome for "fim", o programa para.
4. Caso contrário, o nome é adicionado à lista.
5. No final, o programa mostra os nomes na ordem inversa.
"""

nomes = []
while True:
    nome = input("Digite um nome (ou 'fim' para sair): ")
    if nome == 'fim':
        break
    nomes.append(nome)

print("Nomes na ordem inversa:")
for nome in reversed(nomes):
    print(nome)
