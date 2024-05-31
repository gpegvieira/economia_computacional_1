#Exercício 5.15
"""Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade 
comprada. Utilize a tabela de códigos abaixo para obter o preço de cada produto:
Código Preço
1      0,50
2      1,00
3      4,00
5      7,00
9      8,00
Seu programa deve exibir o total das compras depois que o usuário digitar 0. 
Qualquer outro código deve gerar a mensagem de erro “Código inválido”
"""

s = 0
while True:
    code = int(input("Digite o código do próximo produto: "))
    if code == 1:
        s = s + 0.5
    elif code == 2:
        s = s + 1
    elif code == 3:
        s = s + 4
    elif code == 5:
        s = s + 7
    elif code == 9:
        s = s + 8
    elif code == 0:
        break
print(f"O valor total da compra é R$ {s:.2f}.")