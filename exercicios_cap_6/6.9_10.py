# Exercício 6.9 (com indicação da ordem em que os números foram encontrados)
# Exercício 6.10 (pesquisa em toda a lista)
"""Modifique o programa do exercício 6.9 de forma a pesquisar p e v
em toda a lista e informando o usuário a posição onde p e a posição onde v foram 
encontrados."""

L = [15, 7, 27, 39]
p = int(input("Digite o primeiro valor a ser procurado: "))
v = int(input("Digite o segundo valor a ser procurado: "))

achou_p = -1
achou_v = -1
x = 0

while x < len(L):
    if L[x] == p:
        achou_p = x
    if L[x] == v:
        achou_v = x
    x += 1

if achou_p >= 0:
    print("%d achado na posição %d" % (p, achou_p))
else:
    print("%d não encontrado" % p)
if achou_v >= 0:
    print("%d achado na posição %d" % (v, achou_v))
else:
    print("%d não encontrado" % v)

if achou_p >=0 and achou_v >= 0:
    if achou_p < achou_v:
        print(f"{p} foi encontrado antes de {v}")
    elif achou_p == achou_v:
        print(f"{p} foi encontrado concomitantemente a {v}, pois têm o mesmo valor")
    else:
        print(f"{v} foi encontrado antes de {p}")