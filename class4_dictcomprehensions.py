##Dict Comprehensions

lista1 = [
    ('valor1', 10),
    ('valor2', 8),
    ('valor3', 30),
]

## Transformar os valores da lista em dicionário

d1 ={c:v for c,v in lista1}

print(d1)

d2 = {c:v*2 for c, v in lista1}
print(d2)

d3 = {c.upper():v for c,v in lista1}
print(d3)