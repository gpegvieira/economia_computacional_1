# Exercício 8.14
"""Altere o programa da listagem 7.45, o jogo da forca. Escolha a palavra 
a adivinhar utilizando números aleatórios."""

lista_de_palavras = [
    'Adam Smith',
    'David Ricardo',
    'John Stuart Mill',
    'Karl Marx',
    'Léon Walras',
    'Alfred Marshall',
    'John Maynard Keynes',
    'Friedrich List',
    'Joan Robinson',
    'Thorstein Veblen',
    'Friedrich Hayek',
    'Milton Friedman',
    'John Nash',
    'Vilfredo Pareto',
]

import random
indice = random.randint(1,len(lista_de_palavras))

palavra = lista_de_palavras[indice].lower()
digitadas = []
acertos = []
erros = 0
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else " "
    print(senha)
    if senha == palavra.lower():
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX  :  ")
    print("X  O  " if erros >=1 else "X")
    linha2=""
    if erros == 2:
        linha2 = "  |  "
    elif erros == 3:
        linha2 = " \|  "
    elif erros == 4:
        linha2 = " \|/ "
    print("X%s" % linha2)
    linha3 = ""    
    if erros == 5:
        linha3 += " /   "
    elif erros >= 6:
        linha3 += " / \ "
    print("X%s" % linha3)
    if erros == 6:
        print(f"Enforcado! O nome correto é {palavra}.")
        break