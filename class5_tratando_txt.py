##Abrir o arquivo com o atributo open e read

arqu1 = open("Files/arquivo.txt",'r')

##Ler o arquivo

print(arqu1.read())

## Seek voltar o cursor
arqu1.seek(0,0)
print(arqu1.read())

## Fechar o arquivo

arqu1.close()

##Atrituto w+ permite gravar(substitui, criar o conteúdo e arquivo) e ler o arquivo

arqu2 = open("Files/arquivo.txt","w+")
arqu2.write("Gravei uma linha\n") #\n faz a quebra de linha
arqu2.write("Gravei segunda linha\n")


#Ler o arquivo
arqu2.seek(0,0)
print(arqu2.read())


#Alterar um arquivo existente e adicionar dados 
#Utilizar o modelo a+
arqu2 = open("Files/arquivo.txt","a+")
arqu2.write("Nova linha adicionada\n")


#Ler o arquivo
arqu2.seek(0,0)
print(arqu2.read())
arqu2.close()

##Gerenciando o Contexto do uso dos arquivos

with open("Files/arquivo.txt","w+") as f:
    f.read
    f.write("Grava primeira linha\n")
    f.write("Grava segunda linha\n")
    f.seek(0,0)

##Transformar o conteudo do arquivo em uma string (estrutura de dados)

gravar = str(f.read())

##Gravar conteudo de um arquivo em outro

with open("Files/arquivo2.txt","w+") as f2:
    f2.write(gravar)
    f2.seek(0,0)
    print(f2.read())