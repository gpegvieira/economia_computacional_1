"""
Programa Cubo e Raiz Cúbica
Descrição: Recebe 6 números e imprime o cubo e a raiz cúbica de cada um deles.
Autor: GPV
Versão: 0.0.1
"""

i = 0

while i < 6:
    x = int(input(f"Digite o {i+1}º número: "))
    cubo = x**3
    raiz_cubica = x**(1/3)
    print(f"O cubo do {i+1}º número é {cubo}.")
    print(f"A raiz cúbica do {i+1}º número é {raiz_cubica}.")
    i += 1

