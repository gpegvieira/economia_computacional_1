"""
Programa Distância no Plano (1.14)
Descrição: Este programa calcula a distância entre dois pontos no plano cartesiano.
Autor: GPV
Versão: 0.0.1
Data: 20/04/2024
"""

import math

x_1 = float(input("Digite a abscissa (x) do ponto A: "))
y_1 = float(input("Digite a ordenada (y) do ponto A: "))
x_2 = float(input("Digite a abscissa (x) do ponto B: "))
y_2 = float(input("Digite a ordenada (y) do ponto B: "))

d = math.sqrt((x_1-x_2)**2+(y_1-y_2)**2)

print("A distância entre os pontos A e B é %f." % d)