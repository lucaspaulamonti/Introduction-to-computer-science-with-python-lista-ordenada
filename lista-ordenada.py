# Escreva a função ordenada(lista), que recebe uma lista com números inteiros como parâmetro e devolve o booleano True se a lista estiver ordenada e False se a lista não estiver ordenada.
def ordenada(lista):
    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]:
            return False      
    return True
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!