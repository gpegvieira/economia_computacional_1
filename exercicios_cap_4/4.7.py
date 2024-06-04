# Exercício 4.7/Listagem 4.4:
salario = float(input("Qual é o seu salário-base para cálculo do IR?"))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + (base - 3000) * 0.35
    base = 3000
if base > 1000:
    imposto = imposto + (base - 1000) * 0.2
print("Salário: R$ %.2f Imposto a pagar: R$ %.2f" % (salario, imposto))