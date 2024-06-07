# Exercício 8.8
"""Usando a função mdc definida no exercício anterior, defina uma 
função para calcular o menor múltiplo comum (M.M.C.) entre dois números."""

def mdc(a,b):
    if b == 0:
        return a
    else:
        return mdc(b, a%b)
    
def mmc(a,b):
    return int(abs(a*b)/mdc(a,b))