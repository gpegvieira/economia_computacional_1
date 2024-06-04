# Exercício 7.2
"""
Escreva um programa que leia duas strings e gere uma terceira com 
os caracteres comuns às duas strings lidas.
1ª string: AAACTBF
2ª string: CBT
Resultado: CBT
A ordem dos caracteres da string gerada não é importante, mas deve conter todas 
as letras comuns a ambas.
"""

str1 = input("Primeira string: ")
str2 = input("Segunda string: ")
list3 = []

if len(str2)>len(str1):
    for caractere in str1:
        if caractere in str2:
            list3.extend(caractere)

if len(str1)>len(str2):
    for caractere in str2:
        if caractere in str1:
            list3.extend(caractere)

str3 = "".join(list3)
print(str3)