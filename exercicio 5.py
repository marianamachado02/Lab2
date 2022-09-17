# Exercício 5

# Um aluno sujeita-se a um exame. Escreva um programa para apresentar no ecrã a classificação qualitativa
# dessa nota (valor inteiro) segundo os seguintes níveis:
# 0 <= nota < 8 : mau;
# 8 <= nota < 10 : insuficiente;
# 10 <= nota < 14 : suficiente;
# 14 <= nota < 18 : bom;
#  18 <= nota <= 20 : excelente.
# nota: o valor da nota do aluno deve ser introduzido através do teclado e pertencer ao intervalo [0,20].

#Leitura dos dados
nota = int(input('Nota:'))

#Processamento e apresentação da informação

if 0<=nota<=20:
    if 0 <= nota < 8:
        print("Mau")

    if 8 <= nota < 10:
        print("Insuficiente")

    if 10 <= nota < 14:
        print("Suficiente")

    if 14 <= nota < 18:
        print("Bom")

    if 18 <= nota <= 20:
        print("Excelente")
