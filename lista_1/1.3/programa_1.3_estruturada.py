# 1.3 (estruturada)
i = 0
numero = 0
soma = 0
while i < 2:
    numero = int(input(f"Digite o {i+1}º número:"))
    i += 1
    soma = soma + numero
print(f"A soma dos dois números é {soma}.")