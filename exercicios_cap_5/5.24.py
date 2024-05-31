# Exercício 5.24
"""Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos."""

n = int(input("Digite um número inteiro positivo n, para que o programa forneça os n primeiros números primos: "))
numero = 1
j = 0

if n <= 0:
    print("O número inserido não é válido.")

else:
    while j < n:
        i = 3
        if numero == 1:
            primalidade = "O número {numero} não é primo."
        elif numero == 2 or numero == 3:
            primalidade = "O número {numero} é primo."
        elif numero % 2 == 1:
            while i < numero:
                if numero % i == 0:
                    primalidade = "O número {numero} não é primo."
                    break
                else:
                    i = i + 2
                    if numero == i:
                        primalidade = "O número {numero} é primo."
        else:
            primalidade = "O número {numero} não é primo."
        if primalidade == "O número {numero} é primo.":
            print(numero)
            j = j + 1
        numero = numero + 1    