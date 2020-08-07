### Coleções de Dados ## Containers ou Iteraveis

## Lista

## Lista de Inteiros
lista_inteiros = [12,34,56,100]

## Lista de Strings

lista_frutas = ["Morango", "Uva", "Pera", "Laranja"]

lista_mista = ["Morango,",4.50, "Uva",10.30,"Pera",15.45]

print(lista_inteiros)
print(lista_frutas)
print(lista_mista)

## Posição de Dados de uma Lista
print(lista_mista[2])

# Tamanho de uma lista
print(len(lista_mista))

## Adicionar Valor a uma lista
lista_mista.append("Manga")
print(lista_mista)

# Excluir Valores de uma lista

del lista_mista[4:6]
print(lista_mista)

del lista_mista[:]
print(lista_mista)

## Iterador em uma  lista FOR (pecorrer a lista)
for f in lista_frutas:
    print(f)


### Coleções de Dados Imutaveis TUPLA

## Como definir uma TUPLA () ou, virgula ?aa
## Tupla sempre é definida por , virgula

tupla_numeros = (1,2,4,67,100)
print(type(tupla_numeros))
print(tupla_numeros)

tupla_teste = (4,)
print(type(tupla_teste))

## Tupla de Strings
tupla_carros = "Gol","Fusca","BMW","Mercedes"
print(type(tupla_carros))
print(tupla_carros)

## Tamanho da Tupla
print(len(tupla_carros))

print(tupla_numeros[2])

## Sobrescrevendo uma Tupla ## Uma tupla não posso alterar mas
## mas posso sobrescrever

tupla_numeros1 = 3,67,12,56

tupla_numeros = tupla_numeros + tupla_numeros1
print(tupla_numeros)

if (100 in tupla_numeros):
    print("Está na Tupla")
else:
    print("Não Está na Tupla")

## Iterar em uma Tupla

for i in tupla_numeros:
    print(i)

## Coleção de Dados Dicionários ##

## Possuem uma chave e um valor e são escritos por {}

dicionario = {"Chave": "Valor"}

estados_Siglas = {"SC": "Santa Catarina", "PR": "Paraná", "RS": "Rio Grande do Sul", "SP": "São Paulo"}
print(estados_Siglas)

# Trazendo o valor do dicionário atraves da chave
estados_Siglas = {"SC": "Santa Catarina", "PR": "Paraná", "RS": "Rio Grande do Sul", "SP": "São Paulo"}
print(estados_Siglas["SC"])

##Iterando os dicionários

for dic in estados_Siglas:
    print(dic + " - " + estados_Siglas[dic])

## Trazendo os valores do dicionário com função ITEMS
for dic in estados_Siglas.items():
    print(dic)

## Fazendo iteração apanas estruturas de chaves e valores
for dic in estados_Siglas.keys():
    print(dic)

for dic in estados_Siglas.values():
    print(dic)

## Adicionando Chaves e valores no dicionário
estados_Siglas["RJ"] = "Rio de Janeiro"
print(estados_Siglas)

#Removendo chaves e valores no dicionário

del estados_Siglas["SP"]
print(estados_Siglas)

# Adicionando segundo dicionário

estados_Siglas2 = {"MT": "Mato Grosso"}

estados_Siglas.update(estados_Siglas2)
print(estados_Siglas)