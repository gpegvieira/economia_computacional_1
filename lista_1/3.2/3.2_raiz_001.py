"""
Programa Raiz
Descrição: Calcula a raiz quadrada a partir do algoritmo fornecido no enunciado.
Autor: GPV
Versão: 0.0.1
"""

a = float(input("Digite um número para extrair sua raiz quadrada: "))
xi = a/2
diferenca = 1
epsilon = 0.0000000000000000000000001
while diferenca > epsilon:
    xf = (xi + (a/xi))/2
    diferenca = xi - xf
    xi = xf

print(f"A raiz quadrada aproximada do número fornecido é {xf}.")