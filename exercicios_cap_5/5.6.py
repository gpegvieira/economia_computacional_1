# Exercício 5.6:
"""Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2=4, ..."""

n = int(input("Tabuada do:"))
x = 1
while x <= 10:
    print(f"{n}x{x}={n*x}")
    x = x+1