"""
Programa Potência
Descrição: Lê dois números a e b e calcula a potência a^b sem utilizar função nativa do Python.
Autor: GPV
Versão: 0.0.1
"""

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

soma = 0
parcela = a
i = 0
k = 1

while k < b:
    while i < a:
        soma = soma + parcela
        i = i + 1
    parcela = soma
    k = k + 1
    i = 1

print(f"O valor de a^b é {soma}.")