# Exercício 5.11:
"""Escreva um programa que pergunte o depósito inicial e a taxa de 
juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. 
Escreva o total ganho com juros no período.
"""

deposito = float(input("Depósito inicial:"))
taxa = float(input("Taxa de juros da poupança:"))

valor = deposito
mes = 1
rendimento = valor*mes*taxa/100

while mes <= 24:
    print("O montante ao fim do mês %d é de %.2f reais." % (mes, valor+rendimento))
    mes = mes + 1
    valor = valor + rendimento
juros = deposito*24*taxa/100
print(f"O total ganho com juros é de %.2f reais." % juros)