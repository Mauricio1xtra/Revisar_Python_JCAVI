import urllib.request
import json

url = "https://data.townofcary.org/api/v2/catalog/datasets/rdu-weather-history"

captura_json = urllib.request.urlopen(url).read().decode()

#Converter em dicionário
dic_json = json.loads(captura_json)

#Iterando
for c in dic_json.values():
    print(c)

#Salvando o arquivo em json
with open("Files/exerc_json.json","w+") as exerc_json:
    json.dump(dic_json,exerc_json, indent=4)

