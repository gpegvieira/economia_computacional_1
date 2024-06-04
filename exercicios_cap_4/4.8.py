# Exercício 4.8 (2ª ed.)/4.10 (4ª ed.):
a = float(input("Digite o primeiro número:"))
b = float(input("Digite o segundo número:"))
c = input("Que operação você deseja realizar: adição, subtração, multiplicação ou divisão?")

if c == "Soma" or c == "soma" or c == "Adição" or c == "adição" or c == "Mais" or c == "mais":
    print(a+b)
elif c == "Subtração" or c == "subtração" or c == "Menos" or c == "menos":
    print(a-b)
elif c == "Multiplicação" or c == "multiplicação" or c == "Vezes" or c == "vezes":
    print(a*b)
elif c == "Divisão" or c == "divisão":
    print(a/b)
else:
    print("Operação inválida")