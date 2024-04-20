"""
Programa 1.10
Descrição: Este programa solicita o valor de um capital, o prazo de investimento e a taxa de juros e calcula e imprime na tela o valor capitalizado no regime de juros simples.
Autor: GPV
Versão: 0.0.2
Correção realizada: permite a entrada de prazos não inteiros.
Data: 20/04/2024
"""

capital = float(input("Digite o capital: "))
prazo = float(input("Digite o prazo do investimento: "))
taxa = float(input("Digite a taxa de juros (em %): "))

juros_t = capital*taxa/100
i = 0
montante = capital

while i < prazo:
    montante = montante + juros_t
    i += 1

montante = montante + juros_t * (prazo - i)

print(f"O valor capitalizado é de R$ {montante:.2f}.")