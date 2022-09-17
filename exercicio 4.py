# Exercício 4

# Escreva um programa que leia valores de horas no formato horas:minutos:segundos e os converta para segundos.
# Exemplo:
# 11:22:14 → 40934 segundos

#Leitura dos dados
horas=int(input('Horas:'))
minutos=int(input('Minutos:'))
segundos=int(input('Segundos:'))

#Conversão dos valores
segundosconvertidos = horas*3600 + minutos*60 + segundos

#Apresentação do resultado
print("Convertido ficam %d segundos" %segundosconvertidos)