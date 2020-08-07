##Função map

lista = [1,4,5,8]

def soma(x):
    return x + 2

## Executar o map
map(soma,lista)

## Retornar a saída em uma lista
print(list(map(soma,lista)))

## Importar a biblioteca matemática MATH
import math

print(list(map(math.sqrt,lista)))
