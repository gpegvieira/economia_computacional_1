# Exercício 7.3
"""
Escreva um programa que leia duas strings e gere uma terceira apenas 
com os caracteres que aparecem em uma delas.
1ª string: CTA
2ª string: ABC
3ª string: BT
A ordem dos caracteres da terceira string não é importante.
"""

str1 = input("Primeira string: ")
str2 = input("Segunda string: ")
str3 = ""

for caractere in str1:
    if caractere not in str2:
        str3 = str3 + caractere

for caractere in str2:
    if caractere not in str1:
        str3 = str3 + caractere


print(str3)