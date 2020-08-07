##Iteravel

lista = ["Mauricio",1,"Juca",5,"Gustavo",90]

##Isso é o iterador
##Principal iterador em Python é o FOR
for l in lista:
    print(l)

##Checar se o objeto é iteravel vamos usar o __inter__

##Trazer atributo de um objeto hasattr

(print(hasattr(lista,'__iter__')))


String = "Florianópolis"

print(hasattr(String,'__iter__'))

##Transformando Iteraveis em Iteradores

nome = "João Ricardo"

listaIterador = iter(nome)

print(type(listaIterador))

## Método NEXT é a função ou método usado para iterar os valores o for utiliza essa


print(hasattr(listaIterador,'__next__'))

print(next(listaIterador))
print(next(listaIterador))
print(next(listaIterador))
print(next(listaIterador))

print("")

for n in listaIterador:
    print(n)

## Stop Iteration é a saída de Excessão que diz
#que não há mais objetivo para iterar..


import time

"""
def funcGerador():
    l = []
    for n in range(100):
        l.append(n)
        time.sleep(0.1)
    return l

#print(funcGerador())

gen = funcGerador()

for i in gen:
    print(i)


## Transformando em geradora, utiliza o yield (consome menos memoria)

def funcGeradora():
    for n in range(100):
        yield n
        time.sleep(0.1)

gen = funcGeradora()

#print(type(gen))

for i in gen:
    print(i)

## A saída de uma função geradora precisa ser iterada
#não vai em saída
"""
###########################
## Criar uma lista com list comprehension

lc1 = [l for l in range(100)]
print(lc1)

gen1 = (l for l in range(100))

## Para uma lista virar um gerador de forma prática
#coloque a mesma dentro de um list comprehension
# e depois transforme em um gerador

## Iterando o Gerador

print(next(gen1))
print(next(gen1))
print(next(gen1))

for l in gen1:
    print(l)



##Testar Memórias de listas e geradores
print("TERMINOU AQUI")
print("TAMANHO DE MEMORIA DOS OBJETOS")

import sys

print(sys.getsizeof(lc1))
print(sys.getsizeof(gen1))

#O Consumo de memória da lista sempre será maior que o Gerador