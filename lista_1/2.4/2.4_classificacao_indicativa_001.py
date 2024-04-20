"""
Programa Classificação Indicativa (2.4)
Descrição: Este programa informa caso determinado espectador não possa assistir a um filme com restrição de idade.
Autor: GPV
Versão: 0.0.1
Data: 20/04/2024
"""

nome = input("Qual é o nome do espectador? ")
idade = int(input(f"Qual é a idade de {nome} (em anos)? "))

if idade < 18:
    print(f"{nome} não pode assistir a esse filme.")