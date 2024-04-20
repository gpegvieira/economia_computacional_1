"""
Programa Quantidade Demandada (1.13)
Descrição: Este programa calcula a quantidade demandada (em números inteiros) a partir da renda do consumidor e do preço do bem analisado.
Autor: GPV
Versão: 0.0.1
Data: 20/04/2024
"""

renda = float(input("Qual é a renda do consumidor? "))
preco = float(input("Qual é o preço do bem em questão? "))
qd = renda / preco

print(f"A quantidade demandada do bem em questão é de {qd:.0f} unidades.")