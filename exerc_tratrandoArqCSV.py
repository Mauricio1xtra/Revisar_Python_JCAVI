##Crie um arquivo em CSV com cabeçalho e lista de preço de produtos

import csv

with open ("Files/produtos.csv","w+", newline="") as fcsv:
    escrever = csv.writer(fcsv, delimiter = ',')
    escrever.writerow(("Produto","Preço"))
    escrever.writerow(("Arroz",14.50))
    escrever.writerow(("Feijão",7.90,))
    escrever.writerow(("Macarrão",9,90))

with open("Files/produtos.csv","r") as fcsv:
    ler_csv = csv.reader(fcsv)
    listaProdutos = list(ler_csv)

##Leia o arquivo CSV criado e itere os valores do mesmo com for e depois converta ele em uma lista
    for l in listaProdutos:
        print(l)


##Leia o arquivo disponibilizado chamado arquivo_ex.csv transforme o mesmo em uma lista
## e itere o valor da mesma

with open("Files/produtos.csv","r") as fcsv:
    ler_dic = csv.Dictreader(fcsv)
    listaProdutos = list(ler_csv)

##Após isso transforme o mesmo em um dicionário e itere os valores de chave chamado "SalesNumber

