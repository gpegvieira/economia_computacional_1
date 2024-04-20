"""
Programa 1.7
Descrição: Este programa calcula a soma dos termos e o n-ésimo termo de uma PG, dados o primeiro termo, a razão e o número de termos.
Autor: GPV
Versão: 0.0.1
Data: 19/04/2024
"""

a_1 = int(input("Determine o primeiro termo: "))
q = int(input("Determine a razão da progressão geométrica: "))
n = int(input("Determine o número de termos: "))

S = 0
a_i = a_1
i = 0

while i < n:
    a_i = a_1*q**i
    S = S + a_i
    i += 1

print(f"Soma dos termos: {S}")
print(f"n-ésimo termo: {a_i}")