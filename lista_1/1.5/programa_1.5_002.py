"""
Programa 1.5
Descrição: Este programa calcula o salário mensal bruto e líquido e os descontos salariais referentes a impostos de um professor horista a partir do número de horas trabalhadas, com imposto a 30% e valor da hora-aula a R$ 40,00.
Autor: GPV
Versão: 0.0.2
Correção realizada: explicita a unidade de medida de tempo na entrada de dados.
Data: 19/04/2024
"""

# Entrada de dados
horas = int(input("Qual é a jornada de trabalho mensal em horas? "))

# Processamento de dados
salario_bruto = horas*40
salario_liquido = salario_bruto - 0.3*salario_bruto
total_de_descontos = salario_bruto-salario_liquido

# Saída de dados
print(f"Salário bruto mensal: R$ {salario_bruto:.2f}")
print(f"Salário líquido mensal: R$ {salario_liquido:.2f}")
print(f"Impostos totais por mês: R$ {total_de_descontos:.2f}")
