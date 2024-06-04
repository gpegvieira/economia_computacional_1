# Exercício 3.15
cigarros_dia = int(input("Quantos cigarros você fuma por dia?"))
anos = int(input("Há quantos anos você fuma?"))

cigarros_total = cigarros_dia * anos * 365
tempo_perdido = cigarros_total * 10

print("Cada cigarro consumido subtrai 10 minutos da sua expectativa de vida, que já declinou %d minutos desde que você começou a fumar. Procure o serviço de saúde mais próximo para receber orientação médica sobre como parar de fumar." % tempo_perdido)