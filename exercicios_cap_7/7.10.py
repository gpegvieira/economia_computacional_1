# Exercício 7.10
"""Escreva um jogo da velha para dois jogadores. O jogo deve perguntar 
onde você quer jogar e alternar entre os jogadores. A cada jogada, verifique se a 
posição está livre. Verifique também quando um jogador venceu a partida. Um 
jogo da velha pode ser visto como uma lista de 3 elementos, onde cada elemento 
é outra lista, também com três elementos.
Exemplo do jogo:
 X | O |
---+---+---
   | X | X
---+---+---
   |   | O
Onde cada posição pode ser vista como um número. Confira abaixo um exemplo 
das posições mapeadas para a mesma posição de seu teclado numérico.
 7 | 8 | 9
---+---+---
 4 | 5 | 6
---+---+---
 1 | 2 | 3
"""

jogo_da_velha = """           
 7 | 8 | 9 
---+---+---
 4 | 5 | 6 
---+---+---
 1 | 2 | 3 
           """
jogo_lista = []
string = ''

for linha in jogo_da_velha.splitlines():
    jogo_lista.append(list(linha))

for i in jogo_lista:
    print("".join(i))
k = 0

while True:    
    x = int(input("Jogador 1, digite qual posição você quer marcar: "))
    
    if x == 1 and jogo_lista[5][1] == "1":
        jogo_lista[5][1] = "X"
    elif x == 2 and jogo_lista[5][5] == "2":
        jogo_lista[5][5] = "X"
    elif x == 3 and jogo_lista[5][9] == "3":
        jogo_lista[5][9] = "X"
    elif x == 4 and jogo_lista[3][1] == "4":
        jogo_lista[3][1] = "X"
    elif x == 5 and jogo_lista[3][5] == "5":
        jogo_lista[3][5] = "X"      
    elif x == 6 and jogo_lista[3][9] == "6":
        jogo_lista[3][9] = "X"       
    elif x == 7 and jogo_lista[1][1] == "7":
        jogo_lista[1][1] = "X"       
    elif x == 8 and jogo_lista[1][5] == "8":
        jogo_lista[1][5] = "X"      
    elif x == 9 and jogo_lista[1][9] == "9":
        jogo_lista[1][9] = "X"
    else:
        print("Jogada inválida.")
    
    k = k + 1
    
    if jogo_lista[1][1] == jogo_lista[1][5] == jogo_lista[1][9] == "X" or jogo_lista[3][1] == jogo_lista[3][5] == jogo_lista[3][9] == "X" or jogo_lista[5][1] == jogo_lista[5][5] == jogo_lista[5][9] == "X" or jogo_lista[1][1] == jogo_lista[3][1] == jogo_lista[5][1] == "X" or jogo_lista[1][5] == jogo_lista[3][5] == jogo_lista[5][5] == "X" or jogo_lista[1][9] == jogo_lista[3][9] == jogo_lista[5][9] == "X" or jogo_lista[1][1] == jogo_lista[3][5] == jogo_lista[5][9] == "X" or jogo_lista[1][9] == jogo_lista[3][5] == jogo_lista[5][1] == "X":
        print("Parabéns, jogador 1! Você venceu.")
        break
    else:
        for i in jogo_lista:
            print("".join(i))
        if k == 9:
            print("Deu velha (ou houve erro nas jogadas)!")
            break

    o = int(input("Jogador 2, digite qual posição você quer marcar: "))

    if o == 1 and jogo_lista[5][1] == "1":
        jogo_lista[5][1] = "O"
    elif o == 2 and jogo_lista[5][5] == "2":
        jogo_lista[5][5] = "O"
    elif o == 3 and jogo_lista[5][9] == "3":
        jogo_lista[5][9] = "O"
    elif o == 4 and jogo_lista[3][1] == "4":
        jogo_lista[3][1] = "O"
    elif o == 5 and jogo_lista[3][5] == "5":
        jogo_lista[3][5] = "O"      
    elif o == 6 and jogo_lista[3][9] == "6":
        jogo_lista[3][9] = "O"       
    elif o == 7 and jogo_lista[1][1] == "7":
        jogo_lista[1][1] = "O"       
    elif o == 8 and jogo_lista[1][5] == "8":
        jogo_lista[1][5] = "O"      
    elif o == 9 and jogo_lista[1][9] == "9":
        jogo_lista[1][9] = "O"
    else:
        print("Jogada inválida.")
        
    k = k + 1
        
    if jogo_lista[1][1] == jogo_lista[1][5] == jogo_lista[1][9] == "O" or jogo_lista[3][1] == jogo_lista[3][5] == jogo_lista[3][9] == "O" or jogo_lista[5][1] == jogo_lista[5][5] == jogo_lista[5][9] == "O" or jogo_lista[1][1] == jogo_lista[3][1] == jogo_lista[5][1] == "O" or jogo_lista[1][5] == jogo_lista[3][5] == jogo_lista[5][5] == "O" or jogo_lista[1][9] == jogo_lista[3][9] == jogo_lista[5][9] == "O" or jogo_lista[1][1] == jogo_lista[3][5] == jogo_lista[5][9] == "O" or jogo_lista[1][9] == jogo_lista[3][5] == jogo_lista[5][1] == "O":
        print("Parabéns, jogador 2! Você venceu.")
        break
    else:
        for i in jogo_lista:
            print("".join(i))