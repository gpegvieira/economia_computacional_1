"""
Programa Polinômio
Descrição: Calcula o valor de um polinômio a partir dos valores dos coeficientes e de x.
Autor: GPV
Versão: 0.0.1
"""

n = int(input("Digite o grau do polinômio: "))
x = float(input("Digite um valor numérico para x: "))
i = 0
polinomio = 0

while i <= n:
    coef = float(input(f"Qual é o coeficiente do termo de grau {i}? "))
    termo = coef*(x**i)
    polinomio = polinomio + termo
    i += 1

print(f"O valor do polinômio é {polinomio}.")