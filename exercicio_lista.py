##Crie uma lista mista e conte o tamanho dessa lista

lista_mista = ["Café", "Pera", "Açucar", "Pão"]
print(len(lista_mista))

## Crie uma lista de dados do tipo string e adicione mais 2 valores nessa lista e printe o resultado

lista_cor = ["Vermelho", "Amarelo", "Preto", "Azul", "Rosa"]

lista_cor.append("Roxo")
lista_cor.append("Branco")
print(lista_cor)

## Percorra com o laço for a lista mista criada anteriormente
for i in lista_mista:
    print(i)

## Remover o último valor de dados da lista mista criada
del lista_mista[3]
print(lista_mista)

