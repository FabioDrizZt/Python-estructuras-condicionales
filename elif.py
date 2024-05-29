import random
edad = random.randint(14, 19)
print('su edad es ', edad)
if (edad >= 18):
    print("Es mayor de edad")
    print("Puede Conducir")
elif (edad >= 16):
    print("Puede Conducir")
    print("Acompañado de un adulto")
else:
    print("Es menor de edad")
    print("No puede Conducir")