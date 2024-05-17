"""
Programa Capital do Sul
Descrição: Lê um texto fornecido pelo usuário e avalia se ele é o nome de uma capital de uma das três UFs do Sul do Brasil
Autor: GPV
Versão: 0.0.1
"""

print("Este programa avalia se o texto a ser digitado por você corresponde ao nome de uma capital de um dos três Estados da Região Sul do Brasil.")
texto = input("Digite: ")

if texto == "Curitiba" or texto == "curitiba" or texto == "Florianópolis" or texto == "Florianopolis" or texto == "florianópolis" or texto == "florianopolis" or texto == "Porto Alegre" or texto == "porto alegre":
    print(f"{texto} é o nome da capital de um Estado localizado na Região Sul do Brasil.")
      
else:
    print(f"{texto} não corresponde ao nome da capital de qualquer Estado localizado na Região Sul do Brasil.")