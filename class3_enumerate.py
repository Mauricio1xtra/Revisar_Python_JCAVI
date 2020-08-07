## Função Enumerate

animais = ["Cachorro","Gato","Papagaio","Elevante"]

print(list(enumerate(animais)))

## Iterar uma lista com enumerate
for i, valor in enumerate(animais):
    print(i,valor)

## Iterador e Enumerate com condicionais (imprimir o indice maior que 1) temos 0 ate 3
for i, valor in enumerate(animais):
    if i > 1:
        break
    else:
        print(valor)



