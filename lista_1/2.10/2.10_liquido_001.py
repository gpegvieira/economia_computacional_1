"""
Programa Salário Líquido
Descrição: Calcula o salário líquido (deduzido o IR) de um trabalhador com salário fixo por hora trabalhada e número variável de horas trabalhadas.
Autor: GPV
Versão: 0.0.1
"""

horas = int(input("Digite o número de horas trabalhadas: "))
ir = 0
bruto = 20*horas

if bruto > 1000:
    ir = 0.1*(bruto-1000)

if bruto > 2500:
    ir = ir + 0.2*(bruto-2500)

if bruto > 5000:
    ir = ir + 0.35*(bruto-5000)

liquido = bruto - ir
print(f"O salário líquido é R$ {liquido:.2f}.")