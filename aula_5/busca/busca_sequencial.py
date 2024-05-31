"""
Programa busca_sequencial.py
Descrição: Este programa busca um valor em uma base de dados.
Autor:
Versão: 0.0.2
Correção realizada: informação mais intuitiva ao usuário acerca da posição em que seu CPF foi encontrado.
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
cpf = int(input("Digite o valor a procurar:"))
print(cpf) # debug com print

# Processamento de dados
while posicao < len(lista):
    if lista[posicao] == cpf:
        achou = True
        break
    posicao +=1 # o mesmo que posicao = posicao + 1
    
# Saída de dados
if achou:
    print(f'\nO valor {cpf} foi achado na posição {posicao + 1}.')
else:
    print(f'\nO valor {cpf} não foi achado.')