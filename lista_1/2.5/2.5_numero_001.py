"""
Programa Número
Descrição: Avalia e informa se o número fornecido pelo usuário é negativo, nulo ou positivo.
Autor: GPV
Versão: 0.0.1
"""

numero = float(input("Digite um número para avaliar se ele é negativo, nulo ou positivo: "))

if numero < 0:
    print(f"O número {numero} é negativo.")

elif numero == 0:
    print(f"O número {numero} é nulo.")
    
else:
    print(f"O número {numero} é positivo.")