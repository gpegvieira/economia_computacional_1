# Exercício 6.13
"""A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista 
T = [ -10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor e a maior 
temperatura, assim como a temperatura média"""

T = [-10, -8, 0, 1, 2, 5, -2, -4]
minima = L[0]
maxima = L[0]
soma = 0
for e in T:
    if e < minima:
        minima = e
    if e > maxima:
        maxima = e
    soma = soma + e
media = soma/8
print(f"A temperatura máxima é {maxima}°C.")
print(f"A temperatura média é {media}°C.")
print(f"A temperatura mínima é {minima}°C.")