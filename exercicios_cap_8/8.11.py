# Exercício 8.11
"""Escreva uma função para validar uma variável string. Essa função 
recebe como parâmetro a string, o número mínimo e máximo de caracteres. Retorne 
verdadeiro se o tamanho da string estiver entre os valores de máximo e mínimo, 
e falso em caso contrário."""

def faixa_str(string, minimo, maximo):
    if len(string) >= minimo and len(string) <= maximo:
        return True
    else:
        return False