# Exercício 3.9
print("Este programa calcula a quantidade de segundos decorridos dado o tempo em dias, horas, minutos e segundos.")
d = int(input("Digite o número de dias: "))
h = int(input("Digite o número de horas: "))
m = int(input("Digite o número de minutos: "))
s = int(input("Digite o número de segundos: "))

s2 = 24*60*60*d + 60*60*h + 60*m + s

print("Este é o tempo equivalente em segundos: %d" % s2)