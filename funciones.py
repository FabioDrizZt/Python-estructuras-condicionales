def multiplicar(a,b):
    if(type(a) != int or type(b) != int):
        print("Los valores ingresados deben ser enteros")
    else:
        resultado = (a) * (b)
        print(f"La multiplicación de {a} * {b} es: {resultado}" )

A = input("ingrese el valor de A: ")
B = input("ingrese el valor de B: ")

multiplicar(A,B)
multiplicar(3,4)
multiplicar(3,5)
multiplicar(3,7)
multiplicar(3,2.5)