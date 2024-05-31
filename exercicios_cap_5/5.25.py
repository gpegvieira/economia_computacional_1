# Exercício 5.25.
"""Escreva um programa que calcule a raiz quadrada de um número. 
Utilize o método de Newton para obter um resultado aproximado. Sendo n o número a obter a raiz quadrada, considere a base b=2. Calcule p usando a fórmula p=(b+(n/b))/2. Agora, calcule o quadrado de p. A cada passo, faça b=p e recalcule p usando a fórmula apresentada. Pare quando a diferença absoluta entre n e o quadrado de p for menor que 0,0001."""

n = float(input("Digite um número para extrair a raiz quadrada aproximada dele: "))
b = 2
epsilon = 0.0001
diferenca = 1

while diferenca > 0.00001:
    p = (b+(n/b))/2
    b = p
    diferenca = p**2 - n
    
print(f"A raiz quadrada aproximada de {n} é {p:.4f}.")