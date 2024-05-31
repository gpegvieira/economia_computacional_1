# Exercício 5.26
"""Escreva um programa que calcule o resto da divisão inteira entre dois números. Utilize apenas as operações de soma e subtração para calcular o resultado."""

n = int(input("Informe o dividendo: "))
b = int(input("Informe o divisor: "))
ni = n

while n > b:
    n = n - b

r = n
print(f"O resto da divisão de {ni} por {b} é {r}.")