# Ingresar el nombre del estudiante y la nota del examen final (nota de tipo entero). Asignar la
# calificación de acuerdo a las notas de la siguiente tabla. Crear el algoritmo y ejecutar las pruebas.
import random
nombre = input("Ingrese el nombre del estudiante: ")
nota = random.randrange(-1,11)
print("nota: ",nota)
if 0 <= nota <= 10:
    if nota == 10:
        print("La calificación es Sobresaliente")
    elif nota >= 8:
        print("La calificación es Distinguido")
    elif nota >= 6:
        print("La calificación es Bueno")
    elif nota >= 4:
        print("La calificación es Suficiente")
    elif nota >= 1:
        print("La calificación es Insuficiente")
    else:
        print("La calificación es Reprobado")
else:
    print("Error: ingrese una nota valida")