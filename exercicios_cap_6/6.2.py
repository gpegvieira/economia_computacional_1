# Exercício 6.2
"""Faça um programa que leia duas listas e que gere uma terceira com 
os elementos das duas primeiras."""

l = 0
m = 0
x = 0
L = []
M = []

while True:
    l = int(input("Digite um número não nulo para a primeira lista (0 para sair):"))
    if l == 0:
        break
    else:
        L.append(l)
        x = x+1

x = 0
while True:
    m = int(input("Digite um número não nulo para a segunda lista (0 para sair):"))
    if m == 0:
        break
    else:
        M.append(m)
        x = x+1

N = []
N.extend(L)
N.extend(M)
print(f"Terceira lista: {N}")