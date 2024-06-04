# Exercício 3.12
d = float(input("Digite a distância percorrida, em km:"))
v_m = float(input("Digite a velocidade média, em km/h, ao longo do percurso:"))

t = d/v_m

t_s = int(t * 3600)
t_h = int(t_s / 3600) # função parte inteira
t_s = int(t_s % 3600) # resto
t_m = int(t_s / 60) # função parte inteira
t_s = int(t_s % 60) # resto

print("O tempo decorrido do início ao término da viagem é de %d horas, %d minutos e %d segundos." % (t_h, t_m, t_s)