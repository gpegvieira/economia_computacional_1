"""
Programa IMC
Descrição: A partir da altura e do peso fornecidos pelo usuário, o programa calcula o Índice de Massa Corporal (IMC) e informa a condição apresentada.
Autor: GPV
Versão: 0.0.1
"""

print("Este programa informa a sua condição conforme indicada pelo Índice de Massa Corporal, calculado a partir do seu peso e da sua altura.")
peso = float(input("Qual é o seu peso (em kg)? "))
altura = float(input("Qual é a sua altura (em m)? "))

imc = peso / altura**2

if peso < 0 or altura < 0:
    print("Peso e/ou altura inválido.")
elif imc <= 18.5:
    print(f'Seu IMC é {imc} e está na faixa "extremamente magro".')
elif imc <= 25 and imc > 18.5:
    print(f'Seu IMC é {imc} e está na faixa de peso normal.')
elif imc > 25 and imc <= 30:
    print(f'Seu IMC é {imc} e está na faixa "sobrepeso".')
elif imc > 30:
    print(f'Seu IMC é {imc} e está na faixa "obesidade".')
    