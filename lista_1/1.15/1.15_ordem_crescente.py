"""
Programa Ordem Crescente (1.15)
Descrição: Este programa recebe três números e ordena-os em ordem crescente.
Autor: GPV
Versão: 0.0.1
Data: 20/04/2024
"""

print("Este programa recebe três números e ordena-os em ordem crescente.")

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a <= b <= c:
    print(a, b, c)
elif a <= c <= b:
    print(a, c, b)
elif b <= a <= c:
    print(b, a, c)
elif b <= c <= a:
    print(b, c, a)
elif c <= a <= b:
    print(c, a, b)
elif c <= b <= a:
    print(c, b, a)