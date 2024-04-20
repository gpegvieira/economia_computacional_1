"""
Programa 1.10
Descrição: Este programa solicita o valor de um capital, o prazo de investimento e a taxa de juros e calcula e imprime na tela o valor capitalizado no regime de juros compostos.
Autor: GPV
Versão: 0.0.3
Correção realizada: alteração para o regime de juros compostos.
Data: 20/04/2024
"""

capital = float(input("Digite o capital: "))
prazo = float(input("Digite o prazo do investimento: "))
taxa = float(input("Digite a taxa de juros (em %): "))

montante = capital * (1 + taxa/100)**prazo
    
print(f"O valor capitalizado é de R$ {montante:.2f}.")