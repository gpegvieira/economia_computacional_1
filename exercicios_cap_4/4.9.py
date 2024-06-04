# Exercício 4.9 (2ª ed.)/4.11 (4ª ed.):
casa = float(input("Qual é o valor da casa?"))
salario = float(input("Qual é o seu salário?"))
anos = int(input("Em quantos anos você pretende pagar?"))

prestacao = casa / (anos*12)

if prestacao <= (0.3*salario):
    print(f"Seu empréstimo foi aprovado! Suas prestações serão de R$ {prestacao:.2f} ao mês.")

else:
    print("Desculpe, você não está elegível para o empréstimo.")