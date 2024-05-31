# Exercício 5.8:
"""Escreva um programa que leia dois números. Imprima o resultado da 
multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e 
subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5 
+ 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4."""

x = int(input())
y = int(input())
a = 1
b = 0
while a <= x:
    b = b + y
    a = a + 1
print(f"{x} x {y} = {b}")