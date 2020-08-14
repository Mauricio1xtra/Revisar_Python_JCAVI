
##Importar a biblioteca JSON
import json

##Transformar um JSON em dicionário

cadastro_pessoas = {
    "1": {
        "Nome": "Joao",
        "Idade": 35,
        "Sexo": "Masculino",
        "Data Nascimento": "29/12/1985"
    },
    "2": {
        "Nome": "Juca",
        "Idade": 34,
        "Sexo": "Masculino",
        "Data Nascimento": "12/12/1985"
    },
    "3": {
        "Nome": "Leandro",
        "Idade": 50,
        "Sexo": "Masculino",
        "Data Nascimento": "01/01/1970"
    },
    "4": {
        "Nome": "Rita",
        "Idade": 23,
        "Sexo": "Feminino",
        "Data Nascimento": "12/09/1997"
    }
}

##Iterar Dicionário
for c,v in cadastro_pessoas.items():
    print(c,v)

#Converter o dicionário em JSON com o médoto json.dump

dados = json.dumps(cadastro_pessoas,indent=4)
print(dados)

#Transformar a váriavel em JSON em um arquivo
with open("Files/cadastro_pessoas1.json","w+") as j:
    json.dump(cadastro_pessoas,j, indent=4)

##Converter um json em dicionário
with open ("Files/cadastro_pessoas1.json", "r") as f:
    le_json = json.load(f)
    #print(le_json)

##Iterar
for v in le_json.values():
    print(v)

##Importando um JSON da internet####

import urllib.request

#Ler os dados
url = "https://www.sba.gov/sites/default/files/data.json"

#Pegar o valor da url e vai ler e armazenar
pega_url = urllib.request.urlopen(url).read().decode()

#Converter os valores do Json em dicionário
dic_json = json.loads(pega_url)

##Iterar
for sba in dic_json.values():
    print(sba)

with open ("Files/sba.json","w+") as sba:
    json.dump(dic_json,sba, indent=4)
