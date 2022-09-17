# Exercício 2
# Escreva um programa que leia valores de velocidades em Km/h e os converta para m/s.

# Leitura dos dados

velocidade= float(input('Velocidade:')) 

#Conversão dos dados
velocidademetro= velocidade/3.6

#Apresentação
print("A velocidade fica %.2f metros por segundo" %velocidademetro)