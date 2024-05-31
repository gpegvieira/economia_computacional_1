"""
Programa soma
Descrição: Este é um modelo de programa escrito no paradigma sequencial no qual se calcula a soma de dois números lidos do teclado, convertendo o resultado da função input() em números inteiros. Além disso, o programa informa ao usuário a operação que foi realizada com os números digitados por ele.
Versão: 0.0.5
Data: 03/04/2024
"""



# Alocação de memória

numero_1: int = 0

numero_2: int = 0

soma: int = 0

# Entrada de dados

numero_1 = int(input("Digite a primeira parcela: "))

numero_2 = int(input("Digite a segunda parcela: "))

# Processamento de dados

soma = numero_1 + numero_2

# Saída de dados

print(f"O resultado da adição do número {numero_1} com o número {numero_2} é igual a {soma}.")
