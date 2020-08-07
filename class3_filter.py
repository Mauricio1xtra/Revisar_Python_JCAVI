## Função Filter - filtra valores passados em uma função ou na execução de saída

lista_mista = [1,"Mauricio",25,"Pedro",45]

def valida(x):
    return x == "Mauricio"

##utilizando lambda na saída
print(list(filter(lambda x : x == "Pedro", lista_mista)))

#ou 

print(list(filter(valida,lista_mista)))
