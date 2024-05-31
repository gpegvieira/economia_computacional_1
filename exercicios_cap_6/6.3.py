# Exercício 6.3
"""Faça um programa que percorra duas listas e gere uma terceira sem 
elementos repetidos"""

l = 0
m = 0
x = 0
l1 = []
l2 = []

while True:
    l = int(input("Digite um número não nulo para a primeira lista (0 para sair):"))
    if l == 0:
        break
    else:
        l1.append(l)
        x = x+1

x = 0
while True:
    m = int(input("Digite um número não nulo para a segunda lista (0 para sair):"))
    if m == 0:
        break
    else:
        l2.append(m)
        x = x+1

l3 = []
l3.extend(l1)
l3.extend(l2)
l3sr = []

x = 0
while x < len(l3):
    y = 0
    while y < len(l3sr):
        if l3[x] == l3sr[y]:
            break
        y = y + 1
    if y == len(l3sr):
        l3sr.append(l3[x])
        # adicionar o elemento l3[x] à l3sr se o elemento não for igual a l3sr[1], l3sr[2], ..., l3sr[y]
    x = x + 1

print(f"Lista com elementos não repetidos das listas 1 e 2: {l3sr}")