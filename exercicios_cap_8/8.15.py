# Exercício 8.15 (da solução do livro)
"""Utilizando a função type, escreva uma função recursiva que imprima 
os elementos de uma lista. Cada elemento deve ser impresso separadamente, um 
por linha. Considere o caso de listas dentro de listas, como L=[1, [2,3,4,[5,6,7]]]. 
A cada nível, imprima a lista mais à direita, como fazemos ao indentar blocos 
em Python. Dica: envie o nível atual como parâmetro e utilize-o para calcular a 
quantidade de espaços em branco à esquerda de cada elemento.
"""

import types

def print_lista(L, n_recuos=0):
    recuo_de_paragrafo = "    "
    recuos = recuo_de_paragrafo*n_recuos
    if type(L)==list:
        print(recuos, '[')
        for elemento in L:
            print_lista(elemento, n_recuos+1)
        print(recuos, ']')
    else:
        print(recuos, L)