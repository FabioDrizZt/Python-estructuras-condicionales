# Leer una variable N de tipo entero e informar si el número es positivo, negativo o cero y también si es par,
# impar o cero. El número cero no es ni positivo ni negativo ni par ni impar.

# CERO N==0
# PAR N % 2 == 0
# IMPAR N % 2 != 0
# POSITIVO N > 0
# NEGATIVO N < 0

N = int(input("Ingrese un N°: "))
if (N!=0):
    if (N%2==0):
        print(N, 'ES PAR')
    else:
        print(N, 'ES IMPAR')

    if (N>0):
        print(N, 'ES POSITIVO')
    else:
        print(N, 'ES NEGATIVO')
else:
    print(N, 'ES CERO')
    