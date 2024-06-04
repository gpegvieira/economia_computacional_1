# Exercício 4.6:
distancia = float(input("Que distância, em km, você deseja percorrer?"))
if distancia <= 200:
    preco = distancia*0.5
else:
    preco = distancia*0.45
print(f"O preço a ser pago é R$ {preco:.2f}.")