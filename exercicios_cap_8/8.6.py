# Exercício 8.6
"""Reescreva o programa da listagem 8.8 de forma a utilizar for em vez 
de while.
"""
def soma(L):
    total = 0
    x = 1
    for x in range(len(L)):
        total += L[x]
    return total
L = [1,7,2,9,15]
print(soma(L))
print(soma([7,9,12,3,100,20,4]))