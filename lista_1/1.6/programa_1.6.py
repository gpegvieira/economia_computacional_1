"""
Programa 1.6
Descrição: Este programa calcula a soma dos termos e o n-ésimo termo de uma PA, dados o primeiro termo, a razão e o número de termos.
Autor: GPV
Versão: 0.0.1
Data: 19/04/2024
"""

a_1 = int(input("Determine o primeiro termo: "))
r = int(input("Determine a razão da progressão aritmética: "))
n = int(input("Determine o número de termos: "))

S = a_1
a_i = a_1
i = 1

while i < n:
    a_i = a_i + r
    S = S + a_i
    i += 1

print(f"Soma dos termos: {S}")
print(f"n-ésimo termo: {a_i}")