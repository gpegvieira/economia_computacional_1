# Exercício 7.4
"""
Escreva um programa que leia uma string e imprima quantas vezes 
cada caractere aparece nessa string.
String: TTAAC
Resultado:
T: 2x
A: 2x
C: 1x
"""

string = input("Digite uma string: ")
letras_contadas = ""

for l in string:
    a = string.count(l)
    if l not in letras_contadas:
        print(f"{l}: {a}x")
    letras_contadas += l