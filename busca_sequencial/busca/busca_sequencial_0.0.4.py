"""
Programa busca_sequencial.py
Descrição: Este programa busca um valor em uma base de dados.
Autor:
Versão: 0.0.4
Correções realizadas:
1. informação mais intuitiva ao usuário acerca da posição em que seu CPF foi encontrado
2. informação mais precisa de que o valor procurado é um CPF
3. esta versão do programa não informa mais a posição, porém é mais rápida
Data: 19/04/2024
"""

## Alocação de memória
lista = []
achou = False
cpf = 0

# Leitura da base de dados de CPF
base = [1,5,2,87,31]
lista = base

# Leitura (Entrada) de dados
cpf = int(input("Digite o CPF a procurar:"))

# Processamento de dados
for elem in lista:
    if elem == cpf:
        achou = True
        break
    
# Saída de dados
if achou:
    print(f'\nO CPF {cpf} foi achado.')
else:
    print(f'\nO CPF {cpf} não foi achado.')
