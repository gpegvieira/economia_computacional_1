"""
Programa Múltiplo de Três (2.3)
Descrição: Este programa recebe um número e informa se ele é ou não múltiplo de 3.
Autor: GPV
Versão: 0.0.1
Data: 20/04/2024
"""

n = float(input("Digite um número para saber se ele é ou não múltiplo de 3: "))

if n % 3 == 0:
    print(f"O número {n:0f} é múltiplo de 3.")
else:
    print(f"O número {n} não é múltiplo de 3.")