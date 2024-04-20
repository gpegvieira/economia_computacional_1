"""
Programa Classificação Indicativa (2.4)
Descrição: Este programa informa caso determinado espectador não possa assistir a um filme com restrição de idade.
Autor: GPV
Versão: 0.0.2
Correção realizada: adição de informação para idade inválida ou para caso não haja restrição de idade ao espectador.
Data: 20/04/2024
"""

nome = input("Qual é o nome do espectador? ")
idade = int(input(f"Qual é a idade de {nome} (em anos)? "))

if idade < 18 and idade >= 0:
    print(f"{nome} não pode assistir a esse filme.")
elif idade > 18:
    print(f"Não há restrição de idade que impeça que {nome} assista a esse filme.")
else:
    print("Idade inválida.")