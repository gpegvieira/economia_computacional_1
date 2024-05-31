# Exercício 5.7:
"""Modifique o programa anterior de forma que o usuário também 
digite o início e o fim da tabuada, em vez de começar com 1 e 10."""

n = int(input("Tabuada do:"))
a = int(input("Iniciando com o fator:"))
b = int(input("E terminando com o fator:"))
x = a
while x <= b:
    print(f"{n}x{x}={n*x}")
    x = x+1