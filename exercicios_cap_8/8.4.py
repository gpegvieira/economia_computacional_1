# Exercício 8.4
"""
Escreva uma função que receba a base e a altura de um triângulo e 
retorne sua área (A = (base x altura)/2).
Valores esperados:
área_triângulo(6, 9) == 27
área_triângulo(5, 8) == 20
"""

def area_triangulo(b,h):
    return(b*h/2)

print(area_triangulo(6,9))
print(area_triangulo(5,8))