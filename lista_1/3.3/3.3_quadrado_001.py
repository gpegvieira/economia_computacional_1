"""
Programa Quadrado
Descrição: Recebe cinco números e imprime o quadrado de cada um deles.
Autor: GPV
Versão: 0.0.1
"""

i = 0

while i < 5:
    x = float(input(f"Digite o {i+1}º número: "))
    quadrado = x**2
    print(f"O quadrado do {i+1}º número é {quadrado}.")
    i+=1