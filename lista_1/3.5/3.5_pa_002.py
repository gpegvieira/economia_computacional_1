"""
Programa PA
Descrição: Imprime os dez primeiros termos de uma PA de razão dada pelo usuário.
Autor: GPV
Versão: 0.0.2
"""

a0 = int(input("Digite o primeiro termo da PA:"))
r = int(input("Digite a razão da PA:"))
i = 0
a_i = a0

while i < 10:
    print(a_i)
    a_i = a_i + r
    i+=1