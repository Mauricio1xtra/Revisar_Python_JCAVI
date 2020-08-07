## Crie uma coleção de dados(lista,tupla,dicionário) e trabalhe com a função enumerate
# Aplicando condicionais.

listaMista = [1,"Chicago", 30, "Charlotte", 80, "Toronto"]

for i, valor in enumerate(listaMista):
    if i > 2:
        break
    else:
        print(valor)