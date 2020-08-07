## Função REDUCE - reduz valores de uma coleção de dados
# a um unico valor final

#abaixo o reduce multiplicou todos os valores dentro da lista

from functools import reduce

lista = [2,7,10,3,78]

def mult(x,y):
    return x * y

print(reduce(mult,lista))

## Testar o maior valor com reduce

lista2 = [45,1,56,12,6]

testa_maior = lambda x,y : x if (x > y) else y

print(reduce(testa_maior,lista2))