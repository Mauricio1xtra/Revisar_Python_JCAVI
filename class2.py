## Funções em Python
"""
def oi():
    print("Olá estou dando oi")

#oi()

## Funções com argumentos ##

def soma(x,y):
    return x + y

print(soma(2,2))

# ou criando uma variável "s" e chamo ela no print
s = soma(2,2)

print(s)

## Funções com argumento de Strings # f strings para escrever saídas
# com string e argumentos variáveis

def identificacao(meu_nome,idade):
    print(f"Olá {meu_nome} Sua Idade é {idade}")
# ou
    print("Olá",meu_nome, "Sua idade é",idade)

identificacao("Mauricio", 36)

## funções de argumento ou parametros Nomeados

identificacao(36,"Mauricio")
# Ou condicionando os parametros assim não inverte a saída
identificacao(idade=36,meu_nome="Mauricio")

salario = float(input("Digite o Salário: "))

def salario_desconta_imposto(salario,imposto=27.0):
    print(salario - (salario * imposto * 0.01))

salario_desconta_imposto(salario)
#ou
salario_desconta_imposto(salario,imposto=10.0)

## Funções com Condicionais

def validausuario(nome_usuario,senha):
    if nome_usuario == "admin" and senha == "floripa":
        return("Usuário e Senha Correto. Bem Vindo!")
    elif nome_usuario == "admin":
        return ("Usuário está Correta!")
    elif senha == "floripa":
        return("Senha Correta!")
    else:
        return("Usuário e Senha Incorretos.")

print(validausuario("admin", "floripa"))

## função soma
def soma(x,y):
    return x + y

def calculo(num1,num2,funcao=soma):
    return funcao(num1,num2)

print(calculo(3,2))
#Função soma + subtracao juntas
def subtracao(num1,num2):
    return num1 - num2

print(calculo(2,2, subtracao))


## Argumentos *ARGS - retorna em tupla
def soma(*args):
    print(args)

soma(1,2,4,5,6,7,8)

def soma_total(*args):
    total = 0
    for numeros in args:
        total = numeros + total
    return total

print(soma_total(23,12,45,34,56,100))


## Argumentos **KWARGS - retorna em dicionário (chave e valor)

def saudacao(**kwargs):
    print(kwargs)

saudacao(manha="Bom dia",tarde="Boa tarde",noite="Boa noite")

def saudacao_dias(**kwargs):
    for hora,saudacao in kwargs.items():
        print(f"Durante a {hora} dizemos {saudacao} ")

saudacao_dias(manha="Bom dia",tarde="Boa tarde",noite="Boa noite")

### Funções decoradoras ###

def master(msg):
    def imprime():
        print("Essa é a Função Principal")
        msg() #apenas para declarar o argumento da função master
    return imprime

def chama_funcao():
    print("Essa chama a segunda Função")

chama_funcao()
"""
##Função Decoradora

# 1) opção - através de uma variável (chama_funcao)
#chama_funcao = master(chama_funcao)

#chama_funcao()

# 2) opção - através do decorador @ (FORMA MAIS UTILIZADA EM PYTHON)
@master
def chama_funcao():
    print("Está Chamando a função Verdadeira")

chama_funcao()

### Outros exemplos

def decoradora(valor): #vai varios argumentos pois vou fazer
    def imprime(*args):
        print("Multiplicação Efetuada")
        return valor(*args)
    return imprime

@decoradora
def multiplica(a,b):
    return a * b

print(multiplica(2,3))

## Exemplo 2

contador = 0

def contar_acessos(funcao_decorada):
    def nova_func(*args,**kwargs):
        global contador
        contador += 1
        return funcao_decorada(*args,**kwargs)
    return nova_func

@contar_acessos
def somar(a,b):
    return a + b

print(contador)
print(somar(2,2))
print(contador)
print(somar(2,3))
print(contador)
