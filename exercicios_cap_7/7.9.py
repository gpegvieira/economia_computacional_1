# Exercício 7.9
"""Modifique o programa para utilizar listas de strings para desenhar 
o boneco da forca. Você pode utilizar uma lista para cada linha e organizá-las em 
uma lista de listas. Em vez de controlar quando imprimir cada parte, desenhe 
nessas listas, substituindo o elemento a desenhar.
Exemplo:
>>> linha = list("X------")
>>> linha
['X', '-', '-', '-', '-', '-', '-']
>>> linha[6] = "|"
>>> linha
['X', '-', '-', '-', '-', '-', '|']
>>> "".join(linha)
'X-----|'
"""

palavra = input("Digite a palavra secreta: ").lower().strip()
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0

linhas_string = """
X==:==
X  :  
X     
X     
X     
X     
=======
"""
linhas_list = []

for linha_string in linhas_string.splitlines():
    linhas_list.append(list(linha_string))

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
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
    linhas_list[3][3] = "O" if erros >=1 else ""
    if erros == 2:
        linhas_list[4][3] = "|"
    elif erros == 3:
        linhas_list[4][2] = "\\"
    elif erros == 4:
        linhas_list[4][4] = "/"
    elif erros == 5:
        linhas_list[5][2] += "/"
    elif erros >= 6:
        linhas_list[5][4] += "\\"
        
    for letra in linhas_list:
        print("".join(letra))
    
    if erros == 6:
        print(f"Enforcado! A palavra correta é {palavra}.")
        break