# Exercício 5.14
""" Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, 
exiba a quantidade de números digitados, assim como a soma e a média aritmética. """

s = 0
while True:
    x = int(input("Digite um número inteiro não nulo para somar, ou 0 para obter a soma e sair: "))
    s = s + x
    if x == 0:
        break
print(f"A soma dos números digitados é {s}.")