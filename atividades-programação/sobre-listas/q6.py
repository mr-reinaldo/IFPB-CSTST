""" Questionário: 6 - Listas
----------------------
Faça um programa que leia números inteiros até o usuário digitar 0. 
Em seguida, calcule e exiba o produto (multiplicação) de todos os 
números digitados, excluindo o zero final.

Objetivo: Pedir ao usuário para digitar números inteiros até que ele digite 0.
Depois, calcular e mostrar o produto (multiplicação) de todos os números digitados, excluindo o zero final.

Como funciona:
1. O programa cria uma variável `produto` para armazenar o resultado da multiplicação e `contador` para contar os números digitados.
2. Ele pede ao usuário para digitar números.
3. Se o número for 0, o programa para.
4. Caso contrário, o número é multiplicado pelo valor de `produto`.
5. No final, o programa mostra o produto dos números digitados ou uma mensagem dizendo que nenhum número válido foi digitado.
"""

produto = 1
contador = 0
while True:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    if numero == 0:
        break
    produto *= numero
    contador += 1
if contador > 0:
    print("Produto dos números digitados:", produto)
else:
    print("Nenhum número válido foi digitado.")