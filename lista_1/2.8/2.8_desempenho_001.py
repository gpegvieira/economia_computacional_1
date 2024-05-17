"""
Programa Desempenho em Economia Computacional I
Descrição: A partir das notas obtidas nas avaliações da disciplina, avalia se o aluno está aprovado ou reprovado, bem como seu conceito.
Autor: GPV
Versão: 0.0.1
"""

print("Olá, aluno de Economia Computacional I! Utilize este programa para saber seu conceito e se está aprovado ou reprovado na disciplina.")
print("Primeiramente, é preciso também verificar sua presença nos encontros.")
presenca = int(input("Você compareceu a ao menos 75% dos encontros até o término do semestre? Digite 0 para Não e 1 para Sim. "))

if presenca == 0:
    print("Você foi reprovado com conceito FF.")

elif presenca == 1:
    print("Parabéns, sua presença foi suficiente! Agora, precisamos das suas notas para calcular o seu conceito e saber se você foi aprovado ou reprovado.")

    teste1 = float(input("Digite sua nota no Teste 1: "))
    teste2 = float(input("Digite sua nota no Teste 2: "))
    prova = float(input("Digite sua nota na Prova Final: "))

    media = 0.15*teste1 + 0.15*teste2 + 0.7*prova

    if media <= 10 and media >= 9:
        print("Parabéns! Você foi aprovado com conceito A.")
    elif media < 9 and media >= 7.5:
        print("Parabéns! Você foi aprovado com conceito B.")
    elif media < 7.5 and media >= 6:
        print("Parabéns! Você foi aprovado com conceito C.")
    elif media < 6 and media >= 0:
        recuperacao = float(input("Digite sua nota na Prova de Recuperação: "))
        nf = (3*recuperacao + 2*media)/5
        if nf >= 6 and nf < 8.4:
            print("Parabéns! Você foi aprovado com conceito C.")
        elif nf < 6 and nf >= 0:
            print("Você foi reprovado com conceito D.")
        else:
            print("Há um erro nas notas informadas. Por favor, repita o procedimento de informar as notas para o programa.")
    else:
        print("Há um erro nas notas informadas. Por favor, repita o procedimento de informar as notas para o programa.")

else:
    print("A frequência informada não é válida. Por favor, repita o procedimento e digite o valor 0 para frequências menores que 75% ou o valor 1 para frequências iguais a ou maiores que 75%.")







