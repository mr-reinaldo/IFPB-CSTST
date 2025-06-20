""" Questionário 3 - Listas
----------------------
Escreva um programa que peça ao usuário para digitar 
as notas de uma turma. O programa deve parar quando o 
usuário digitar uma nota negativa. Em seguida, calcule 
e exiba a média e todas as notas que estão acima da média.

"""
# Objetivo: Pedir ao usuário para digitar notas de alunos até que ele digite uma nota negativa.
# Depois, calcular a média das notas e mostrar as notas que estão acima da média.

# Como funciona:
# 1. O programa cria uma lista chamada `notas` para armazenar as notas.
# 2. Ele pede ao usuário para digitar notas.
# 3. Se a nota for negativa, o programa para.
# 4. Caso contrário, a nota é adicionada à lista.
# 5. No final, o programa calcula a média das notas e exibe as notas que são maiores que a média.

notas = []
while True:
    nota = float(input("Digite a nota do aluno (ou uma nota negativa para sair): "))
    if nota < 0:
        break
    notas.append(nota)

if notas:
    media = sum(notas) / len(notas)
    print("Média da turma:", media)
    print("Notas acima da média:")
    for nota in notas:
        if nota > media:
            print(f"Nota: {nota:.2f}")
else:
    print("Nenhuma nota válida foi digitada.")