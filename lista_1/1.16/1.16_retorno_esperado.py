"""
Programa Retorno Esperado (1.16)
Descrição: Este programa calcula o retorno esperado de um ativo, dados pelo usuário o retorno do ativo sem risco, o retorno da carteira de mercado e o coeficiente de sensibilidade do retorno do ativo a variações no prêmio de risco de mercado.
Autor: GPV
Versão: 0.0.1
Data: 20/04/2024
"""

r_f = float(input("Informe o retorno do ativo sem risco (em %): "))
r_m = float(input("Informe o retorno da carteira de mercado (em %): "))
beta_i = float(input("Informe o coeficiente de sensibilidade do retorno do ativo a variações no prêmio de risco de mercado: "))

e = r_f + beta_i*(r_m - r_f)

print(f"O retorno esperado do ativo é de {e}%.")               