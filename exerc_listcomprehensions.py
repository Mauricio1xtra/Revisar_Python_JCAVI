##Crie uma list Comprehension executando algumas operações matemáticas.

listaNumeros = [2,40,60,100,120]

lc1 = [soma + 5 for soma in listaNumeros]
print(lc1)

##Crie um list comprehension listando valores  impares em um range de números

listaImpar = [lp for lp in range(50) if lp % 2 == 1]
print(listaImpar)

