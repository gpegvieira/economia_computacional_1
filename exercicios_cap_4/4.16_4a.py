# Exercício 4.16 (4ª ed.):
média = float(input("Digite sua média:"))

if média < 4:
    print("Infelizmente você reprovou")
elif média < 7:
    print("Você ficou de recuperação")
else: # Entenda-se que o aluno está aprovado com média >= 7, para abarcar o caso média = 7
    print("Você passou de ano")