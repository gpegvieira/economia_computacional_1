"""
Programa Par ou Ímpar (2.2)
Descrição: Este programa recebe um número e informa se ele é par ou ímpar, caso seja inteiro não negativo.
Autor: GPV
Versão: 0.0.1
Data: 20/04/2024
"""

n = float(input("Digite um número para saber se ele é par ou ímpar: "))

if n >= 0 and n % 2 == 0:
    print(f"O número {n:.0f} é par.")
elif n > 0 and n % 2 == 1:
    print(f"O número {n:.0f} é ímpar.")
else:
    print("Este número não é válido.")