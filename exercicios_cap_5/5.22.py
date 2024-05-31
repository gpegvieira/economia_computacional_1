# Exercício 5.22
"""Escreva um programa que exiba uma lista de opções (menu): adição, 
subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida. 
Repita até que a opção saída seja escolhida."""

while True:
    operacao = int(input("Este programa fornece a tabuada de uma operação. Digite 1 para adição, 2 para subtração, 3 para multiplicação, 4 para divisão ou 0 para sair."))
    if operacao == 0:
        break
    elif operacao > 0 and operacao < 5:
        tabuada = 1
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                if operacao == 1:
                    print(f"{tabuada} + {numero} = {tabuada+numero}")
                elif operacao == 2:
                    print(f"{tabuada} - {numero} = {tabuada-numero}")
                elif operacao == 3:
                    print(f"{tabuada} x {numero} = {tabuada*numero}")
                elif operacao == 4:
                    print(f"{tabuada} / {numero} = {tabuada/numero}")
                numero += 1
            tabuada += 1