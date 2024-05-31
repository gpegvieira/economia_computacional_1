# Exercício 5.12:
"""Altere o programa anterior de forma a perguntar também o valor 
depositado mensalmente. Esse valor será depositado no início de cada mês, e você 
deve considerá-lo para o cálculo de juros do mês seguinte."""

deposito = float(input("Depósito inicial:"))
taxa = float(input("Taxa de juros da poupança:"))
deposito_mes = float(input("Valor de depósito mensal, a partir do início do 2º mês:"))

saldo = deposito
mes = 1

while mes <= 24:
    saldo = saldo + saldo*taxa/100 + deposito_mes
    print("O montante ao fim do mês %d é de %.2f reais." % (mes, saldo))
    mes = mes + 1
juros = saldo - deposito - 23*deposito_mes
print(f"O total ganho com juros é de %.2f reais." % juros)