"""
Programa busca_sequencial.py
Descrição: Este programa busca um valor em uma base de dados.
Autor:
Versão: 0.0.3
Correções realizadas:
1. informação mais intuitiva ao usuário acerca da posição em que seu CPF foi encontrado
2. informação mais precisa de que o valor procurado é um CPF
Data: 19/04/2024
"""

## Alocação de memória
lista = []
achou = False
posicao = 0
cpf = 0

# Leitura da base de dados de CPF
base = [1,5,2,87,31]
lista = base

# Leitura (Entrada) de dados
cpf = int(input("Digite o CPF a procurar:"))
print(cpf) # debug com print

# Processamento de dados
while posicao < len(lista):
    if lista[posicao] == cpf:
        achou = True
        break
    posicao +=1 # o mesmo que posicao = posicao + 1
    
# Saída de dados
if achou:
    print(f'\nO CPF {cpf} foi achado na posição {posicao + 1}.')
else:
    print(f'\nO CPF {cpf} não foi achado.')