import modulo_prog

#Dentro do meu pacote importe o modulo prog1
from pacote.prog1 import var1,listaCarros,calculaPercentual

#Dentro do meu pacote importe o modulo prog2
from pacote.prog2 import listaPares 

##Execução da função do módulo_prog
modulo_prog.calculaMaximo(1,5,30)

#Executar a função soma do módulo_prog
print(modulo_prog.soma(4,6))

#Executar os códigos ou as estruturas de dados
print(var1)

print(listaCarros)

print(calculaPercentual(1000,10))

listaPares(60)