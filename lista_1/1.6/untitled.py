# 1.6

a_1 = int(input("Determine o primeiro termo:"))
r = int(input("Determine a razão da progressão aritmética:"))
n = int(input("Determine o número de termos:"))

a_n = a_1 + (n-1)*r
S = a_1
i = 0

while i < n:
    i += 1
    S = S + a_i

print(f"Soma dos termos: {S}")
print(f"n-ésimo termo: {a_n}")