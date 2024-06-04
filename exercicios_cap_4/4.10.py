# Exercício 4.10 (2ª ed.)/4.12 (4ª ed.):
consumo = float(input("Informe seu consumo em kWh:"))
tipo = str(input("Qual o seu tipo de instalação? Informe R para residencial, I para industrial ou C para comercial."))

preco = 0

if tipo == "R":
    if consumo <= 500:
        preco = 0.4
    elif consumo > 500:
        preco = 0.65

if tipo == "C":
    if consumo <= 1000:
        preco = 0.55
    elif consumo > 1000:
        preco = 0.6

if tipo == "I":
    if consumo <= 5000:
        preco = 0.55
    elif consumo > 5000:
        preco = 0.6

valor_final = preco*consumo

if consumo >= 0:
    print(f"O valor final a pagar é de R$ {valor_final:.2f}.")
    
else:
    print("Consumo inválido")