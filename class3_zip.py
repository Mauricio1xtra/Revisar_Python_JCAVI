## Função Zip retorna os valores de estruturas de dados em tuplas,
#porém, retorna os elementos sempre com base na estrutura de menor valor
#junta coleções de dados (listas, tuplas, dicionarios)

dicVerduras = {1:"Cebola", 2: "Alface", 3: "Repolho", 4: "Beterraba"}
dicFrutas = {1: "Maça", 2: "Laranja", 3: "Pera"}

junta = list(zip(dicVerduras,dicFrutas))

print(junta)

juntaValores = list(zip(dicVerduras.values(),dicFrutas.values()))

print(juntaValores)

## Iterar (trazer) o resultado do zip

for p in juntaValores:
    print(p)