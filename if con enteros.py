import random
edad = random.randint(15, 20)
print('su edad es ', edad)
if (edad >= 18):
    print("Es mayor de edad")
    print("Puede Conducir")
if (edad < 18):
    print("Es menor de edad")
    print("No Puede Conducir")