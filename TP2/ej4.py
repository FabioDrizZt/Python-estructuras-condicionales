# 4. Escribir un algoritmo que, al ingresar los lados de un triángulo,
# le diga al usuario si es isósceles, escaleno o  equilátero.
import random
A = random.randrange(1,10)
B = random.randrange(1,10)
C = random.randrange(1,10)

print(A,B,C)

if (A == B == C):
    print("Equilatero")
elif (A == B) or (A == C) or (B == C):
    print("Isosceles")
else: # elif  (A != B != C != A):
    print("Escaleno")