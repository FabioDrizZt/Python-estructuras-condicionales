# 5. Escribe un programa que solicite al usuario ingresar una palabra. Usa strip() y lower() para normalizar la
# entrada y luego verifica si la palabra es "python". Imprime un mensaje confirmando si la palabra ingresada
# es "python" o no.

palabra = input("Ingrese una palabra: ")
palabra = palabra.strip().lower()
if palabra == "python":
    print("La palabra ingresada es python")
else:
    print("La palabra ingresada no es python")
