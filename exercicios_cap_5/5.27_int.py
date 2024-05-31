# Exercício 5.27.
"""Escreva um programa que verifique se um número é palíndromo. Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos. Exemplos: 454, 10501"""

# Caso em que n é int (solução do livro)

n = int(input("Digite um número para verificar se é um palíndromo: "))

i = 0
while int(n / 10**i) < 0:
    i = i + 1

print(i)