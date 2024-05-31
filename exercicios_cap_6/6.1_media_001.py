"""
Programa Média (6.1)
Descrição: O programa, desenvolvido com base na listagem 6.6, recebe sete notas e calcula a média.
Autor: GPV
Versão: 0.0.1
Data: 26/04/2024
"""

notas = [0,0,0,0,0,0,0]
soma = 0
x = 0

while x < 7:
    notas[x] = float(input("Nota %d: " % x))
    soma += notas[x]
    x += 1
x = 0

while x < 7:
    print("Nota %d: %6.2f" % (x, notas[x]))
    x += 1

print("Média: %5.2f" % (soma/x))