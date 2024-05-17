"""
Programa PA
Descrição: Imprime os dez primeiros termos de uma PA de razão dada pelo usuário.
Autor: GPV
Versão: 0.0.1
"""

a0 = int(input("Digite o primeiro termo da PA:"))
r = int(input("Digite a razão da PA:"))
i = 0
a_i = a0

print(a0)

while i < 9:
    a_i = a_i + r
    print(a_i)
    i+=1