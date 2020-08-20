##Funções no Modulo

def soma(x,y):
    return x + y

def calculaMaximo(x,y,z):
    lista = [x,y,z]
    print(max(lista))

##Tudo daqui para baixo será executado apenas em modo iterativo
#Ou quando executado o script do módulo diretamente

if __name__ == "__main__":
    print(soma(2,3))
    print("Executei Sozinho")
    nome = "Mauricio"
