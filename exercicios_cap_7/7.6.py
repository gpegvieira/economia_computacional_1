# Exercício 7.6 (solução adaptada conforme a do livro)
"""
Escreva um programa que leia três strings. Imprima o resultado da 
substituição na primeira, dos caracteres da segunda pelos da terceira.
1ª string: AATTCGAA
2ª string: TG
3ª string: AC
Resultado: AAAACCAA
"""

str1 = input("Primeira string: ")
str2 = input("Segunda string: ")
str3 = input("Terceira string (com mesmo nº de caracteres da segunda): ")
str_final = ""

if len(str2) == len(str3):
    for caractere in str1:
        posicao = str2.find(caractere)
        if posicao >= 0:
            str_final = str_final + str3[posicao]
        else:
            str_final = str_final + caractere
    print("Os caracteres da segunda string foram substituídos pelos da terceira na primeira string, resultando em %s." % str_final)
        
else:
    print("A terceira string deve ter o mesmo número de caracteres da segunda.")