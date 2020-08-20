##Criar um arquivo txt na pasta. Adicione algumas linhas no arquivo e faça
#um script python ler esse arquivo

file1 = open("Files/exercicio.txt","r")

print(file1.read())

file1.close()

##Abra o arquivo criado e sobrescreva o arquivo e adicione 2 linhas novas
file1 = open("Files/exercicio.txt","w+")
file1.write("Escrever um conteudo\n")
file1.write("Escrever dois conteudos\n")
file1.seek(0,0)
print(file1.read())
file1.close()

##No mesmo arquivo criado adicione uma nova linha sem sobrescrever o conteúdo do mesmo.
file1 = open("Files/exercicio.txt","a+")
file1.write("Adiciona mais uma linha")
file1.seek(0,0)
print(file1.read())
#file1.close()

##Copie o conteúdo do arquivo criado anteriormente para um novo arquivo.
#Utilize o gerenciador de contexto de arquivos para isso

outroFile = str(file1.read())

with open("Files/exercicio2.txt", "w+") as ftxt:
    ftxt.write(outroFile)
    ftxt.seek(0,0)
    print(ftxt.read())
    file1.close()

