##Crie um dicionário com índices de chaves e valores e faça uma iteração na mesma com o for

frutas_iniciais = {"A": "Abacate", "M": "Melancia", "L": "Laranja", "P": "Pera"}

for dic in frutas_iniciais:
    print(dic + "-" + frutas_iniciais[dic])


## Imprima a saída de alguns valores e chaves em tela
print(frutas_iniciais["M"])

for dic in frutas_iniciais.values():
    print(dic)

for dic in frutas_iniciais.keys():
    print(dic)

##Crie um segundo dicionário e adicionar um dentro do outro
frutas_iniciais2 = {"B": "Bergamota"}

frutas_iniciais.update(frutas_iniciais2)
print(frutas_iniciais)