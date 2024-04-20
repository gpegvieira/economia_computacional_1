"""
Programa Dobro ou Metade (2.1)
Descrição: Este programa recebe um número e indica o seu dobro, caso o número seja menor que 10, ou a sua metade, caso seja maior que ou igual a 10 ou menor que ou igual a 20. Se for maior que 20, o programa considera inválido o número de entrada.
Autor: GPV
Versão: 0.0.1
Data: 20/04/2024
"""

n = float(input("Digite um número: "))

if n < 10:
    print(2*n)
elif n >= 10 and n <= 20:
    print(n/2)
else:
    print("Este número não é válido.")