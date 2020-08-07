##Lista comprehensions é uma saída em lista onde
#declara uma lista com funções e ações na mesma
#linha de código

listaNumeros = [1,4,2,67,100]

lc1 = [multiplica * 2 for multiplica in listaNumeros]

print(lc1)

## Trás somente os pares de um range de números

listaPares = [p for p in range(20) if p % 2 == 0]

print(listaPares)

## Trabalhar com Strings

listaNomes = ["Mauricio", "Joao","Alberto","Afonso"]

lc2 = [troca.replace('a','@')for troca in listaNomes]

print(lc2)
