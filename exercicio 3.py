# Exercicio 3
# Escreva um programa que leia valores de temperatura em °Fahrenheit e os converta para °Celsius.
# nota: °Celsius = (°Fahrenheit – 32) / 1,80

#Leitura dos dados
fahrenheit = float(input('Temperatura em Fahrenheit:'))

#Conversão dos dados
celcius = (fahrenheit-32)/1.8

#Apresentação dos dados
print("A temperatura em Celsius fica: %.2f graus" %celcius)