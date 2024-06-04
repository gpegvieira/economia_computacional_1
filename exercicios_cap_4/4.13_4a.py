# Exercício 4.13 (4ª ed.):
a = int(input("a ="))
b = int(input("b ="))

if not a <= b:
    print("a é maior que b")
elif not a >= b:
    print("b é maior que a")
else:
    print("a é igual a b")