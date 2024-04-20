"""
Programa 1.12
Descrição: Este programa calcula a área de um círculo e o comprimento de sua circunferência a partir da medida do raio, dada pelo usuário.
Autor: GPV
Versão: 0.0.2
Correção realizada: limita o número de casas decimais a serem exibidas nas variáveis na saída de dados.
Data: 20/04/2024
"""
import math # importar módulo math para utilizar pi (math.pi)

raio = float(input("Digite o valor do raio, em unidades de comprimento: "))
area = math.pi * raio**2
circunferencia = 2 * math.pi * raio

print(f"A área do círculo é de {area:.2f} unidade(s) de área.")
print(f"O comprimento da circunferência é de {circunferencia:.2f} unidade(s) de comprimento.")