"""
Programa 1.11
Descrição: Este programa calcula a média aritmética de quatro números.
Autor: GPV
Versão: 0.0.2
Correção realizada: indica para o usuário a ordem em inteiros positivos não nulos dos números digitados.
Data: 20/04/2024
"""

a = 0
soma = 0
i = 0

while i < 4:
    a = float(input(f"Digite o {i+1}º número para cálculo da média aritmética simples: "))
    soma = soma + a
    i += 1

media = soma / 4

print(f"A média dos quatro números é {media}.")