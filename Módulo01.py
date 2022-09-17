#Exercício 1
# al76381, Mariana Bessa Machado
# al77383, Pedro Miguel Silva Santos
# al76920, Pedro Manuel Sapage Madeira Guerra Duarte
# al76800, António Pedro Marques Trancoso

# 1. Crie e teste um módulo que permita efetuar o tratamento estatístico de uma lista de
# respostas a um questionário numa escala de 1 a 5 (1 – mau e 5 – excelente). Deverão ser
# criadas as seguintes funções:

# a) geração de uma lista de tamanho, passado como parâmetro, de valores aleatórios na
# escala definida;

#Criar a função
def listarandom ():
    #Importar a biblioteca para gerar números aleatórios
    import random

    #Pedir ao utilizador o tamanho da lista
    tamanholista = int(input("Introduza o tamanho da lista: "))

    #Ciclo com o número de elementos pedidos pelo utilizador
    lista = [random.randint(1,5) for i in range(tamanholista)]

    #Retornar a lista
    print("Lista: "+ str(lista))
    return lista

# b) cálculo da média;

#Criar a função
def media(lista):
   #Fazer a média dos elementos da lista
   media = sum(lista)/len(lista)

   #Retornar o valor da média
   return("A média da lista é de: "+ str(media))

# c) cálculo da moda;

#Criar a função
def moda(lista):
    #Importar a biblioteca
    import statistics

    #Saber qual é a moda dos valores da lista
    moda = statistics.mode(lista)

    #Retornar o valor da moda
    return(moda)


# d) cálculo do desvio padrão;

    #Primeiro criamos uma função para pôr a lista ao quadrado

    def square(lista):
        return [i ** 2 for i in list]

def desviopadrao(lista):

    # Primerio importamos a biblioteca math
    import math

    # Calculamos o desvio de padrão
    desvio = math.sqrt((square(lista))- (media(lista)^2))

    return desvio

# e) lista de frequências;

def lista_freq(lista):
    #Pedir ao utilizador o número
    x = int(input('Qual o número de que quer ver a frequencia: '))

    #Ver quantas vezes esse número aparece na lista
    for x in list: 
        if (x in list): 
            freq[list] += 1
        else: 
            freq[list] = 1

    #Retornar a frequencia desse valor
    return freq(list) 