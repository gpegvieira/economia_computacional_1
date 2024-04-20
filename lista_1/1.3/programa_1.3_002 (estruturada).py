"""
Programa 1.3
Descrição: Este programa lê dois números do teclado, calcula a sua soma e imprime na tela o resultado. Esta versão utiliza a linguagem estruturada.
Autor: GPV
Versão: 0.0.2
Correção realizada: mudança de paradigma de linguagem (de sequencial para estruturada).
Data: 12/04/2024
"""

i = 0
numero = 0
soma = 0
while i < 2:
    numero = int(input(f"Digite o {i+1}º número:"))
    i += 1
    soma = soma + numero
print(f"A soma dos dois números é {soma}.")
