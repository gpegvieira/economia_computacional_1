# Exercício 6.5
"""Altere o programa da listagem 6.21 de forma a poder trabalhar com 
vários comandos digitados de uma só vez. Atualmente, apenas um comando pode 
ser inserido por vez. Altere-o de forma a considerar operação como uma string.
Exemplo: FFFAAAS significaria três chegadas de novos clientes, três atendimentos 
e, finalmente, a saída do programa."""

último = 10
fila = list(range(1, último + 1))
while True:
    print("\nExistem %d clientes na fila" % len(fila))
    print("Fila atual:", fila)
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operação = input("Operação (F, A e/ou S):")
    i = 0
    while i < len(operação):
        operacao = operação[i]
    
        if operacao == "A":
            if (len(fila)) > 0:
                atendido = fila.pop(0)
                print("Cliente %d atendido" % atendido)
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao == "F":
            último += 1  # Increnta o ticket do novo cliente
            fila.append(último)
        elif operacao == "S":
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S!")
        i = i + 1