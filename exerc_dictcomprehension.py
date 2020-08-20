## Crie uma dict comprehension através de uma lista strings

carros_Fabricas = [("Gol","Volks"),("Ranger","Ford")]

dic_strings = {c : v for c,v in carros_Fabricas}

print(dic_strings)


##Crie uma dict comprehension através de uma lista de inteiros executando uma operação matemática

listaNumeros2 = [(45,67),(12,77)]

dic_num = {c * 2 : v+10 for c,v }