# Exercício 7.5
"""
Escreva um programa que leia duas strings e gere uma terceira, na 
qual os caracteres da segunda foram retirados da primeira.
1ª string: AATTGGAA
2ª string: TG
3ª string: AAAA
"""

str1 = input("Digite a primeira string, da qual os caracteres da segunda string serão retirados: ")
str2 = input("Digite a segunda string: ")
str3 = ""

for l in str1:
    if l not in str2:
        str3 = str3 + l

if str3 == "":
    print("Terceira string: (nula)")
else:
    print("Terceira string: %s" % str3)