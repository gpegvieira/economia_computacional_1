"""
Programa 1.9
Descrição: Este programa resolve a equação quadrática ax^2+bx+c=0.
Autor: GPV
Versão: 0.0.1
Data: 19/04/2024
"""

a = float(input("Determine valor não nulo para o coeficiente a em ax^2+bx+c=0:"))
b = float(input("Determine valor para b em ax^2+bx+c=0:"))
c = float(input("Determine valor para c em ax^2+bx=c=0:"))

delta = b^2 - 4*a*c

x1 = (-b + sqrt(delta))/(2*a)
x2 = (-b - sqrt(delta))/(2*a)

if x1 != x2:
    print(f"As raízes da equação são {x1} e {x2}.")

else:
    print(f"A raiz dupla é {x1}.")