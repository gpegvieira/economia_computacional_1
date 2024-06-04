# Exercício 3.14
distancia = float(input("Digite a distância percorrida, em km, com o veículo alugado:"))
dias = float(input("Digite o número de dias do aluguel do veículo:"))

preco = 60*dias + 0.15*distancia

print("O preço a pagar pelo aluguel do veículo é R$ %.2f." % preco)