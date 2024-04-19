# 1.5
horas = int(input("Qual é a jornada de trabalho mensal?"))

salario_bruto = horas*40
salario_liquido = salario_bruto - 0.3*salario_bruto
total_de_descontos = salario_bruto-salario_liquido

print(f"Salário bruto mensal: R$ {salario_bruto:.2f}")
print(f"Salário líquido mensal: R$ {salario_liquido:.2f}")
print(f"Impostos totais por mês: R$ {total_de_descontos:.2f}")