# Exerício 1
# Escreva um programa que leia do teclado os valores da altura e do comprimento de um rectângulo e
# apresente no ecrã o seu perímetro e a sua área.

#Ler informação
comprimento = float(input('Comprimento: '))
altura = float(input('Altura: '))

#Processamento da informação
perimetro = 2 * (comprimento + altura)
area = comprimento * altura

#Apresentação da informação
print("Perimetro = %.2f" %perimetro)
print("Area = %.2f" %area)