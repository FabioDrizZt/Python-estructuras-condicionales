def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def calcular(a,b,op):
    a = int(a)
    b = int(b)
    if op  == "suma":
        return suma(a,b)
    elif op=="resta":
        return resta(a,b)
    elif op=="multiplicacion":
        return multiplicar(a,b)
    elif op=="division":
        return dividir(a,b)
    else:
        return "operación invalida"

nro1 = input("ingrese el primer numero: ")
nro2 = input("ingrese el segundo numero: ")
op = input("que poeración desea realizar (suma, resta, multiplicacion, division)' ")

print(calcular(nro1,nro2,op))
