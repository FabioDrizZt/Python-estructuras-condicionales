#  Escribe un programa que solicite al usuario ingresar un valor. Usa isdigit() para verificar si el valor ingresado
# es un número. Si es un número, conviértelo a entero y determina si es par o impar. Si no es un número,
# imprime un mensaje indicando que la entrada no es válida

numero = input("Ingrese un número: ")

if  (numero.isdigit()):
    numero = int(numero)
    if (numero % 2 == 0):
        print(numero, "es par")
    else:
        print(numero, "es impar")
else:
    print("Ingrese un numero valido.")