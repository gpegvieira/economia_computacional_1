# Exercício 4.3:
a = int(input("Digite um número:"))
b = int(input("Digite mais um número:"))
c = int(input("Digite outro número:"))

if a<b<c:
    print("%d é o menor número entre os três" % a)
    print("%d é o maior número entre os três" % c)

elif a<c<b:
    print("%d é o menor número entre os três" % a)
    print("%d é o maior número entre os três" % b)
    
elif b<c<a:
    print("%d é o menor número entre os três" % b)
    print("%d é o maior número entre os três" % a)

elif b<a<c:
    print("%d é o menor número entre os três" % b)
    print("%d é o maior número entre os três" % c)
    
elif c<a<b:
    print("%d é o menor número entre os três" % c)
    print("%d é o maior número entre os três" % b)

elif c<b<a:
    print("%d é o menor número entre os três" % c)
    print("%d é o maior número entre os três" % a)

elif a==b<c or a<b==c:
     print("%d é o menor número entre os três" % a)
     print("%d é o maior número entre os três" % c)

elif c<a==b or c==a<b:
     print("%d é o menor número entre os três" % c)
     print("%d é o maior número entre os três" % b)

elif b==c<a or b<c==a:
     print("%d é o menor número entre os três" % b)
     print("%d é o maior número entre os três" % a)

elif a==b==c:
     print("%d é o único número entre os três" % a)