# Exercício 5.13:
"""Escreva um programa que pergunte o valor inicial de uma dívida e 
o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número 
de meses para que a dívida seja paga, o total pago e o total de juros pago."""

pv = float(input("Valor inicial da dívida: "))
i = float(input("Taxa de juros mensal: "))
pmt = float(input("Valor mensal a ser pago: "))

saldo = pv
juro_mensal = pv*i/100

i = 0
juros_pagos = 0

if juro_mensal > pmt:
    print("Pagamento insuficiente para quitar a dívida.")
else:
    while saldo > pmt:
        saldo = saldo + juro_mensal - pmt
        juros_pagos = juros_pagos + juro_mensal
        i = i + 1

    print(f"Número de meses até o pagamento da dívida: {i}")
    print(f"Total pago: R$ {pv+juros_pagos:.2f}")
    print(f"Total de juros pago: R$ {juros_pagos:.2f}")
    print(f"Saldo residual: R$ {saldo:.2f}")