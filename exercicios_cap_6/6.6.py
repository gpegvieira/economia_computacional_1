# Exercício 6.6
"""Modifique o programa para trabalhar com duas filas. Para facilitar 
seu trabalho, considere o comando A para atendimento da fila 1; e B, para atendimento da fila 2. O mesmo para a chegada de clientes: F para fila 1; e G, para fila 2."""

último1 = 10
último2 = 10
fila1 = list(range(1, último1 + 1))
fila2 = list(range(1, último2 + 1))
while True:
    print("\nExistem %d clientes na fila 1" % len(fila1))
    print("\nExistem %d clientes na fila 2" % len(fila2))
    print("Fila 1 atual:", fila1)
    print("Fila 2 atual:", fila2)
    print("Digite F para adicionar um cliente ao fim da fila 1,")
    print("ou G para adicionar um cliente ao fim da fila 2,")
    print("ou A para realizar o atendimento de um cliente da fila 1")
    print("ou B para realizar o atendimento de um cliente da fila 2.")
    print("S para sair.")
    operação = input("Operação (F, G, A, B e/ou S):")
    i = 0
    while i < len(operação):
        operacao = operação[i]
    
        if operacao == "A":
            if (len(fila1)) > 0:
                atendido1 = fila1.pop(0)
                print("Cliente %d atendido" % atendido1)
            else:
                print("Fila vazia! Ninguém para atender nesta fila.")
        elif operacao == "B":
            if (len(fila2)) > 0:
                atendido2 = fila2.pop(0)
                print("Cliente %d atendido" % atendido2)
            else:
                print("Fila vazia! Ninguém para atender nesta fila.")
        elif operacao == "F":
            último1 += 1
            fila1.append(último1)
        elif operacao == "G":
            último2 += 1
            fila2.append(último2)
        elif operacao == "S":
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S!")
        i = i + 1