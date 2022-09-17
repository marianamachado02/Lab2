#Exercício 2
# al76381, Mariana Bessa Machado
# al77383, Pedro Miguel Silva Santos
# al76920, Pedro Manuel Sapage Madeira Guerra Duarte
# al76800, António Pedro Marques Trancoso

# 2. Crie e teste um módulo que permita implementar uma stack com as seguintes operações:

# a) isEmpty: devolve true se a pilha estiver vazia;

 def isEmpty(stack):
    if len(stack) == 0:
        return True

#b) push(): Adiciona um novo elemento;

def push(stack, elemento):
    stack = stack.append(elemento)
    return stack

# c) pop(): Retira o elemento adicionado por último;

def pop(stack):

    if (isEmpty(stack) == True):
        return "Erro"

    ultimo_elemento = stack[-1]
    stack[-1] = []

    # sugestão de função
    # stack=reverse(stack)
    #     stack=remove(stack)
    #         stack=reverse(stack)

    return ultimo_elemento

# d) peek(): Devolve o elemento no topo da pilha, sem o retirar;

def peek(stack):
    
    if (isEmpty(stack) == True):
        return "Erro"

    else: 
        return stack[-1]

# e) size(): Devolve o tamanho da pilha.

def size(stack):
    return len(stack)