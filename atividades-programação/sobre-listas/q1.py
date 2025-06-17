#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Questão 1: Faça um programa que peça ao usuário para digitar preços de produtos 
até que ele digite um valor negativo. Ao final, exiba o total da compra e todos 
os preços digitados.
"""

precos = []
somatorio = 0.0

while True:
    preco = float(input("Digite o preço do produto (ou um valor negativo para sair): "))
    if preco < 0:
        break
    precos.append(preco)
    somatorio += preco
print("*" * 60)
print("Preços dos produtos:")
for p in precos:
    print(f"R$ {p:.2f}")
print("+-" * 30)
print(f"Total da compra: R$ {somatorio:.2f}")
print("+-" * 30)