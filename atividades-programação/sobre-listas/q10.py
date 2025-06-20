""" Questionário: 10 - Listas
----------------------
Escreva um programa que peça ao usuário para digitar palavras até que ele digite 'fim'. 
Depois disso, exiba quantas letras 'E' ou 'e' apareceram no total das palavras digitadas.
"""

# Objetivo: Pedir ao usuário para digitar palavras até que ele digite "fim".
# Depois, contar quantas letras "E" ou "e" apareceram no total das palavras digitadas.

# Como funciona:
# 1. O programa cria duas variáveis: `contador_e_minusculo` para contar as letras "e" e `contador_e_maiusculo` para contar as letras "E".
# 2. Ele pede ao usuário para digitar palavras.
# 3. Se a palavra for "fim", o programa para.
# 4. Caso contrário, o programa conta quantas vezes "e" e "E" aparecem na palavra e atualiza os contadores.
# 5. No final, o programa mostra o total de letras "e" e "E".

contador_e_minusculo = 0
contador_e_maiusculo = 0
while True:
    palavra = input("Digite uma palavra (ou 'fim' para sair): ")
    if palavra == 'fim':
        break
    
    if 'e' in palavra:
        contador_e_minusculo += palavra.count('e')
    if 'E' in palavra:
        contador_e_maiusculo += palavra.count('E')

print("Total de letras 'e':", contador_e_minusculo)
print("Total de letras 'E':", contador_e_maiusculo)