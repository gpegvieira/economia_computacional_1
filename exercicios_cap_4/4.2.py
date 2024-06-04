# Exercício 4.2
velocidade = float(input("Qual é a velocidade, em km/h, a que você estava transitando?"))
multa = 5 * (velocidade - 80)

if velocidade > 80:
    print("Você foi multado em R$ %.2f." % multa)

if velocidade <= 80:
    print("Você está dentro do limite de velocidade. Parabéns pela sua conduta.")