# Exercício 3.10
salario_i = float(input("Salário atual: R$ "))
aumento_percentual = float(input("Aumento percentual: "))

valor_do_aumento = salario_i * aumento_percentual/100
salario_f = salario_i * (1 + aumento_percentual/100)

print("Valor do aumento: R$ %.2f" % valor_do_aumento)
print("Valor do novo salário: R$ %.2f" % salario_f)
