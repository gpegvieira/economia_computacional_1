# Exercício 6.11 (substituir while por for, onde for possível)
"""Modifique o programa da listagem 6.15 usando for. Explique por 
que nem todos os while podem ser transformados em for."""

L = []
while True:
    n = int(input("Digite um número (0 sai):"))
    if n == 0:
        break
    L.append(n)
# Para substituir esse while por for, seria preciso saber o número de "n"s de antemão.

for x in L:
    print(x)