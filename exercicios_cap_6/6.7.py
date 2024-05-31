# Exercício 6.7
"""Faça um programa que leia uma expressão com parênteses. Usando 
pilhas, verifique se os parênteses foram abertos e fechados na ordem correta. 
Exemplo:
(()) OK
()()(()()) OK
()) Erro"""

# Formação de uma pilha de parênteses abertos, que são retirados da lista quando são fechados.
# Quando parênteses são fechados indevidamente, eles também são adicionados 

parenteses = input("Digite uma sequência de parênteses abertos e fechados para saber se está correta: ")
pilha_abertos = []
i = 0
while i < len(parenteses):
    if parenteses[i]=="(":
        pilha_abertos.append(parenteses[i])
    elif parenteses[i]==")":
        if len(pilha_abertos) > 0:
            pilha_abertos.pop(-1)
            a = len(pilha_abertos)
        else:
            a = 1
            break
    i = i + 1

if a == 0:
    print("OK")
else:
    print("Erro")