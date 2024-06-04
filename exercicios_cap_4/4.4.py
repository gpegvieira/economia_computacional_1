# Exercício 4.4:
salario = float(input("Qual é o seu salário atual em reais?"))
if salario > 1250:
    aumento = salario*0.1
if salario <= 1250:
    aumento = salario*0.15
print("O seu salário será aumentado em R$ %.2f." % aumento)