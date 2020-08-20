##Importar arquivo CSV

import csv

##Criar o arquivo CSV
with open ("Files/nomes.csv","w+", newline="") as fcsv:
    escrever = csv.writer(fcsv, delimiter = ',')
    escrever.writerow(("Nome","Sobrenome","Idade"))
    escrever.writerow(("João","Ricardo",35))
    escrever.writerow(("Juca","Souza",23,))
    escrever.writerow(("Alberto","Cunha",54))

##Abrir o arquivo CSV

with open("Files/nomes.csv","r") as fcsv:
    ler = csv.reader(fcsv)

#Transformar em uma lista
    listacsv = list(ler)
    ##Extrair as informações de cabeçalho
    print(listacsv[1:])

##Iterar os valores do CSV com FOR
    for l in listacsv:
        print(l)

with open("Files/nomes.csv","r") as dicCsv:
    ler_dic = csv.DictReader(dicCsv)

##Iterar o dicionario transformado
    #for dic in ler_dic:
     #   print(dic)

    for dic in ler_dic:
        print(dic["Nome"])


##Lendo um arquivo CSV existente
with open("Files/arquivo1.csv","r") as arqu1:
    arqu1 = csv.reader(arqu1)
    
    for l in arqu1:
        print(l)