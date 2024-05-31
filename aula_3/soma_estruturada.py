"""
Programa soma estruturada 2
Descrição: Este programa soma dois números usando o paradigma de programação estruturada.
Autor: alunos e professor de Economia Computacional I
Data: 05/04/2024
Versão: 0.0.1
"""

# Alocação de memória
parcela = 0
soma = 0
sum = 0

# Entrada e processamento de dados
while parcela < 2:
    num = int(input(f"\nInforme a parcela {parcela + 1} "))
    soma = soma + num
    parcela += 1 # isso é o mesmo que parcela = parcela + 1

# Saída de dados
print(f"A soma dos números é igual a {soma}.")