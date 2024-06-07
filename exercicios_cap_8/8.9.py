# Exercício 8.9
"""Rastreie o programa da listagem 8.12 e compare o resultado com o 
apresentado na listagem 8.13."""

def fatorial(n):
    print("Calculando o fatorial de %d" % n)
    if n==0 or n==1:
        print("Fatorial de %d = 1" % n)
        return 1
    else:
        fat = n*fatorial(n-1)
        print(" fatorial de %d = %d" % (n, fat))
    return fat
fatorial(4)

# Calculando o fatorial de 4
# Calculando o fatorial de 3
# Calculando o fatorial de 2
# Calculando o fatorial de 1
# Fatorial de 1 = 1
#  fatorial de 2 = 2
#  fatorial de 3 = 6
#  fatorial de 4 = 24