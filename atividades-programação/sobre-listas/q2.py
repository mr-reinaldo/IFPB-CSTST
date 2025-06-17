#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Questão 2: Faça um programa que peça ao usuário para digitar números inteiros. 
O programa deve parar quando o usuário digitar 0. Ao final, exiba quantos números 
pares foram digitados e exiba os números pares.
"""

numeros_pares = []
while True:
    num = int(input("Digite um número inteiro (ou 0 para sair): "))
    if num == 0:
        break
    if num % 2 == 0:
        numeros_pares.append(num)

print(f"Quantidade de números pares digitados: {len(numeros_pares)}")
print("Números pares:")

for pares in numeros_pares:
    print(pares)
