# Exercício 8.7
"""Defina uma função recursiva que calcule o maior divisor comum
(M.D.C.) entre dois números a e b, onde a > b."""

def mdc(a,b):
    if b == 0:
        return a
    else:
        return mdc(b, a%b)