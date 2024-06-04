# Exercício 7.1
"""
Escreva um programa que leia duas strings. Verifique se a segunda 
ocorre dentro da primeira e imprima a posição de início.
1ª string: AABBEFAATT
2ª string: BE
Resultado: BE encontrado na posição 3 de AABBEFAATT
"""

str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string, a ser encontrada na primeira: ")

posicao = str1.find(str2)

if posicao == -1:
    print(f"{str2} não foi encontrado em {str1}.")
else:
    print(f"{str2} encontrado na posição {posicao} de {str1}.")