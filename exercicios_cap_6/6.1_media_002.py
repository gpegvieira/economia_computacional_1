"""
Programa Média (6.1)
Descrição: O programa, desenvolvido com base na listagem 6.6, recebe sete notas e calcula a média.
Autor: GPV
Versão: 0.0.2
Alteração realizada: contagem das notas em números inteiros positivos.
Data: 26/04/2024
"""

notas = [0,0,0,0,0,0,0]
soma = 0
x = 0

while x < 7:
    notas[x] = float(input("Nota %d: " % (x+1)))
    soma += notas[x]
    x += 0
x = 0

while x < 7:
    print("Nota %d: %6.2f" % ((x+1), notas[x]))
    x += 1

print("Média: %5.2f" % (soma/x))