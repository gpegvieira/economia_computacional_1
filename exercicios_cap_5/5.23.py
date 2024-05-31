# Exercício 5.23
"""Escreva um programa que leia um número e verifique se é ou não um número primo. Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido. Se o resto de uma dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é par."""

numero = int(input("Digite um número inteiro positivo para verificar se ele é primo: "))
i = 3

if numero <= 0:
    print("O número inserido não é válido.")

else:
    if numero == 1:
        print(f"O número {numero} não é primo.")
    elif numero == 2 or numero == 3:
        print(f"O número {numero} é primo.")
    elif numero % 2 == 1:
        while i < numero:
            if numero % i == 0:
                print(f"O número {numero} não é primo.")
                break
            else:
                i = i + 2
                if numero == i:
                    print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")