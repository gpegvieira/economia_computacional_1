# Exercício 5.16
"""Execute o programa (Listagem 5.14) para os seguintes valores: 501, 745, 384, 2, 7 e 1 """

valor=int(input("Digite o valor a pagar:"))
cédulas=0
atual=50
apagar=valor
while True:
    if atual<=apagar:
        apagar-=atual
        cédulas+=1
    else:
        print("%d cédula(s) de R$%d" % (cédulas, atual))
        if apagar == 0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cédulas = 0

# Exercício 5.17
"""O que acontece se digitarmos 0 (zero) no valor a pagar?"""
# O programa imprime "0 cédula(s) de R$50", visto que o atual é 50.