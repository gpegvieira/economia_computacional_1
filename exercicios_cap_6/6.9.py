# Exercício 6.9
"""Modifique o exemplo para pesquisar dois valores. Em vez de apenas 
p, leia outro valor v que também será procurado. Na impressão, indique qual dos 
dois valores foi achado primeiro."""

L = [15, 7, 27, 39]
p = int(input("Digite o primeiro valor a ser procurado: "))
v = int(input("Digite o segundo valor a ser procurado: "))
achou_p = False
x = 0
while x < len(L):
    if L[x] == p:
        achou_p = True
        break
    x += 1
    
achou_v = False
y = 0
while y < len(L):
    if L[y] == v:
        achou_v = True
        break
    y += 1

if achou_p:
    print("%d achado na posição %d" % (p, x))
else:
    print("%d não encontrado" % p)
if achou_v:
    print("%d achado na posição %d" % (v, y))
else:
    print("%d não encontrado" % v)